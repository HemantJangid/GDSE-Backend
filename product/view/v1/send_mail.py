from rest_framework.views import APIView
from middleware.response import success
from django.conf import settings
from django.core.mail import send_mail
from product.serializer.dao import SendEmailDao
from middleware.response import success, bad_request

import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail


class SendMailView(APIView):
    def post(self, request):
        attributes = SendEmailDao(data=request.data)
        if not attributes.is_valid():
            return bad_request(attributes.errors)

        message = Mail(
            from_email='contactus@gdsebike.com',
            to_emails=attributes.data['recipient_list'],
            subject=attributes.data['subject'],
            html_content=attributes.data['message'])

        try:
            sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
            response = sg.send(message)
            print(response.status_code)
            print(response.body)
            print(response.headers)

        except Exception as e:
            print("exception occured: ", e)

        return success({}, "email send successfully", True)
