import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'firstproject.settings'

import django
django.setup()

import random
from firstapp.models import Topic, WebPage, Record
from faker import Faker

fakedata = Faker()
topics = ['Search', 'Social', 'Marketplace', 'News', 'Games']

def add_topic():
    t = Topic.objects.get_or_create(top_name=random.choice(topics))[0]
    t.save()
    return t

def add_data(n):
    for entry in range (n):

        # initiating fake data with faker
        fake_top = add_topic()
        fake_name = fakedata.company()
        fake_URL = fakedata.url()
        fake_date = fakedata.date()

        #assinging or crating value to WebPage model -------
        web_page = WebPage.objects.get_or_create(topic=fake_top, page_name=fake_name, url=fake_URL)[0]

        # assinging or crating value to Record model -------
        acc_record = Record.objects.get_or_create(name=web_page, date=fake_date)[0]


if __name__ == '__main__':
    print("entry ongoing")
    add_data(10)
    print("entry done")
