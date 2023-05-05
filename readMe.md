# Django Ecommerce site
this site is an example of a real life e-commerce site. It allows users to browse through vehicles and orders. For this site, an open data source from `https://www.kaggle.com/datasets/farhanhossein/used-vehicles-for-sale` was used. 

After downloading the .csv file from the open source, it was place in our application `orders/fixtures/data/`. Run the command `python manage.py load_vehicle_data`, a custom built function, to convert the downloaded .csv file to a .json file

# Getting Started

## Dependencies used
- Django
- Faker
- Behave

## How the application was created.
created a directory named PythonWebsite and opened it in my vscode
- installed django using `pip install Django` command
- created a new Django project name ecommercesite using `django-admin startproject ecommercesite`
- next, created a new Django app within my project named `orders` with `python manage.py startapp orders`
- created another Django app within the project for all accounts and authentications called `accounts` using   `python manage.py startapp accounts`

## Development proccess
you now define your models within your `models.py` inside each of the apps(the accounts & orders app)


FOR ORDERS APP
Add `orders` to your INSTALLED_APPS in `settings.py`.

in the `models.py` inside the orders app, you define
- `vehicle`, `Details` and `Order` models. where `Vehicle` is joined to `Details` as a foreign key.

After defining models, you run `python manage.py makemigrations` and `python manage.py migrate` commands to create the tables in the database.

Run `python manage.py my_loaddata fixtures/vehicleData.json`, to load our data from the .json file into our sqlite database. 


Next to the `views.py` inside the orders app where we define our functions for our views.
We define `ProductListView` for displaying our vehicles, `OrderCreateView` that allows user to create orders, `OrderDetailView` for viewing details of order, `OrderHistoryView` allowing users to view history of orders and the `compare` function that allows users to be able to compare vehicles.

Now, we create a templates directory within our orders app and create templates for our views. We created `base.html`, `home.html`, `login.html`, `compare.html`, `order_details.html`, `order_form.html`, `order_history.html` and `product_list.html`.

Define our URLs: Finally, we to define our URLs. Open the `urls.py` file within your orders app and define URLs for the views.


FOR ACCOUNTS APP
Add 
`accounts`, 
`AUTH_USER_MODEL = 'accounts.User'`,
`LOGIN_URL = '/login/'`,
`LOGOUT_REDIRECT_URL = '/'`,
 to INSTALLED_APPS in `settings.py`.

In the `models.py` of the accounts app, you define
- `User` and and `UserManger` models.

After defining models, you run `python manage.py makemigrations` and `python manage.py migrate` commands to create the tables in the database.

## Starting the app
Run the `python manage.py runserver` to start app. View the site in your web browser.


## Getting users
For this app, we used Faker to generate some random users to help test some functionalities of the app.
Use `pip install Faker` to install the faker.

Run `python manage.py generate_users`, a custome functoin to generate some users for us.

List of users
jeremy16@example.org and password $xBK@BvdY4
tsimmons@example.com and password +2*CG@8ka7
delacruztanya@example.net and password p*5T!ZNkTV
castroalyssa@example.com and password vVK2FuBdb%
susanbush@example.net and password 6bMqMJzh#T
stokesrebecca@example.org and password _xBCrBGv29
lisastevens@example.org and password H*10PjmMdF
danielmarquez@example.net and password IE3nYJp3!o
jacqueline68@example.org and password a^sB2PVQMr
loriclay@example.com and password ^3U!CmvXN8
holly23@example.net and password &7Z&mBi_Xg
for admin
kristen66@example.net and password admin

For the admin, once you log in and you are an admin, you are redirected to `http://localhost:8000/admin/`, Django's inbuilt admin dashborad.

Next, in the `admin.py`, we define `OrderAdmin` model that allows the admin to see and manage all orders and `UserAdmin` to see and manage all users also.