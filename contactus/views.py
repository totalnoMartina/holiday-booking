from django.http import HttpResponse
from django.views import generic
import smtplib
from django.core.mail import send_mail, BadHeaderError
from django.shortcuts import render
from .forms import ContactForm
from bookingproject import settings

# server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
# server.starttls()
def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = request.POST.get('full_name')
            from_email = request.POST.get('email')
            message = request.POST.get('contacting')
            print(name, subject, message)

            send_mail(
                from_email,
                subject,
                message,
                ['martina01061987@gmail.com'],
                fail_silently=False,
                )
            # subject = f'Message from {form.cleaned_data["full_name"]}'
            # message = form.cleaned_data["contacting"]
            # sender = form.cleaned_data["email"]
            # recipients = ['martina01061987@gmail.com']
            try:
                sendmail(sender, recipients, message)
                print('Mail sent!')
            except BadHeaderError:
                return HttpResponse('Invalid header found')
            return HttpResponse('Success...Your email has been sent')
        return render(request, 'contactus/success.html')
    # form = ContactForm()
    # context = {'form': form}
    return render(request, 'contactus/contact.html', context)
