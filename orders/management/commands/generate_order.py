from accounts.models import User
from orders.models import Order, Vehicle, Details

# get an existing user from the database
user = User.objects.get(name='Joshua Mcgee')

# create an order for the user
order = Order.objects.create(
    name=user.name,
    email=user.email,
    address='123 Main St',
    product=Details.objects.get(id=1),
    user=user,
    quantity=1
)
print(f"completed")
