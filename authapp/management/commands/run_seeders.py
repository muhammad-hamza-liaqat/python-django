from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

User = get_user_model()

class Command(BaseCommand):
    help = "Seeds the database with an initial admin user."

    def handle(self, *args, **options):
        email = "admin@gmail.com"

        if User.objects.filter(email=email).exists():
            self.stdout.write(self.style.WARNING("Admin user already exists."))
            return

        user = User.objects.create_superuser(
            email=email,
            name="admin",
            phone="090078601",
            gender="male",
            password="1234567a-"
        )
        user.is_admin = True  # set manually after creation
        user.save()

        self.stdout.write(self.style.SUCCESS("Admin user created successfully."))
