from django import forms


class ContactForm(forms.Form):
    """
    A form for contact page
    """
    full_name = forms.CharField(label="Full name", required=True)
    from_email = forms.EmailField(label="Email", required=True)
    subject = forms.CharField(label="Subject line", required=True)
    message = forms.CharField(
        label="Your message", widget=forms.Textarea, required=True)

    class Meta:
        fields = ['full_name', 'from_email', 'subject', 'message']
