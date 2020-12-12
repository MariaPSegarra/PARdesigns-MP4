from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import ContactForm
from django.conf import settings
from profiles.models import UserProfile


def contact(request):
    """
    A view to return contact page allowing the user to contact
    the admin site
    """

    if request.method == 'GET':
        contact_form = ContactForm()
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            subject = contact_form.cleaned_data['subject']
            full_name = contact_form.cleaned_data['full_name']
            from_email = contact_form.cleaned_data['from_email']
            message = contact_form.cleaned_data['message']
            try:
                send_mail(
                    full_name, from_email, subject,
                    message, [settings.DEFAULT_FROM_EMAIL])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('contact_success')
    else:
        if request.user.is_authenticated:
            profile = UserProfile.objects.get(user=request.user)
            user_email = profile.user.email
            contact_form = ContactForm(initial={
                'full_name': profile.profile_full_name,
                'from_email': user_email,
                })
        else:
            contact_form = ContactForm()

    context = {
        'contact_form': contact_form,
    }

    return render(request, 'contact/contact.html', context)


def contact_success(request):
    """
    A view to return page with confirmation of a successful
    contact with admin site.
    """

    return render(request, 'contact/contact_success.html')
