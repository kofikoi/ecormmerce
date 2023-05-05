# from accounts.models import User
# from faker import Faker

# fake = Faker()

# admin = User.objects.create_superuser(
#     name = fake.name(),
#     email=fake.email(),
#     password='admin'
# )

# print(f'Admin created. Username: {admin.email}, Password: admin')
from django.core.management.base import BaseCommand
from accounts.models import User
from faker import Faker

class Command(BaseCommand):
    help = 'Generate a superuser with fake data'

    def handle(self, *args, **options):
        fake = Faker()
        name = fake.user_name()
        email = fake.email()
        password = 'admin'
        admin = User.objects.create_superuser(name, email, password)
        self.stdout.write(self.style.SUCCESS(f"Admin created. Username: {name}, Password: {password}"))
