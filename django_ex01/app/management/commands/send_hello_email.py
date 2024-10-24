from typing import List

from django.conf import settings
from django.core.exceptions import ValidationError
from django.core.mail import send_mail
from django.core.management import BaseCommand, CommandError
from django.core.validators import validate_email
from django.template.loader import render_to_string


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument("receiver", nargs="+", type=str, help="이메일 수신자 주소")

    def handle(self, *args, **options):
        # subject = (
        #     "장고를 활용한 이메일 발송"  # TODO: 템플릿 시스템을 통해 문자열 완성하기
        # )
        # content = "메세지 내용입니다."  # TODO: 템플릿 시스템을 통해 문자열 완성하기
        subject = render_to_string("app/hello_email_subject.txt")
        content = render_to_string(
            "app/hello_email_content.txt", {"event_name": "장고 연습장"}
        )
        sender_email = settings.DEFAULT_FROM_EMAIL
        receiver_email_list: List[str] = options["receiver"]

        try:
            for email in receiver_email_list:
                validate_email(email)
        except ValidationError as e:
            raise CommandError(e.message)

        # send_mail(
        #     subject,
        #     content,
        #     sender_email,
        #     receiver_email_list,
        #     fail_silently=False,
        # )
