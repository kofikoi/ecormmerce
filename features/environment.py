from behave import use_fixture
from behave_fixtures import django_test_runner, django_test_case
import os
from selenium import webdriver

os.environ["DJANGO_SETTINGS_MODULE"] = "ecommercesite.settings"


def before_scenario(context, scenario):
    context.browser = webdriver.Chrome()
    context.base_url = 'http://localhost:8000'



def before_all(context):
    use_fixture(django_test_runner, context)

def before_scenario(context, scenario):
    use_fixture(django_test_case, context)