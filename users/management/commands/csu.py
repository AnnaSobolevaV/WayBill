import os

from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):
        user = User.objects.create(
            email=os.getenv("SU_EMAIL"),
            first_name="Admin",
            last_name="curs_work",
            is_staff=True,
            is_active=True,
            is_superuser=True,
        )

        user.set_password(os.getenv("SU_PASS"))
        user.save()
