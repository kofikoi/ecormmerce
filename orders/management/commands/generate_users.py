from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand
from faker import Faker

fake = Faker()
User = get_user_model()

class Command(BaseCommand):
    help = 'Generate fake users'

    def handle(self, *args, **options):
        for _ in range(11): # generate 11 users
            email = fake.email()
            password = fake.password()
            name = fake.name()

            user = User.objects.create_user(email=email, password=password, name=name)
            print(f"Created user with email {email} and password {password}")
