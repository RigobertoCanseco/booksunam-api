# using SendGrid's Python Library
# https://github.com/sendgrid/sendgrid-python
import sendgrid
import os
from sendgrid.helpers.mail import *

sg = sendgrid.SendGridAPIClient(apikey='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')
from_email = Email("cansecorigoberto@gmail.com")
to_email = Email("cansecorigoberto@gmail.com")
subject = "Sending with SendGrid is Fun"
content = Content("text/plain", "and easy to do anywhere, even with Python")
mail = Mail(from_email, subject, to_email, content)
response = sg.client.mail.send.post(request_body=mail.get())
print(response.status_code)
print(response.body)
print(response.headers)