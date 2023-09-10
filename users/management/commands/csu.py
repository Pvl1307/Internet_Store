from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        user = User.objects.create(
            email='pvl@sky.pro',
            first_name='Pvl',
            last_name='Ivnv',
            is_staff=True,
            is_superuser=True
        )

        user.set_password('123123')
        user.save()
