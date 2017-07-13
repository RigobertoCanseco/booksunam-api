from flask_mail import Mail, Message
from flask import render_template

from v1 import app

mail = Mail(app)


class Mailer:
    def __init__(self, sender):
        self.sender = sender

    def send_email(self, subject, sender, recipients, text_body, html_body):
        msg = Message(subject, sender=sender, recipients=recipients)
        msg.body = text_body
        msg.html = html_body
        mail.send(msg)

    def follower_notification(self, followed, follower):
        self.send_email("[microblog] %s is now following you!" % follower.nickname, self.sender, [followed.email],
                        render_template("follower_email.txt", user=followed, follower=follower),
                        render_template("follower_email.html", user=followed, follower=follower))
