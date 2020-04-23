import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','jobsproject.settings')

import django
django.setup()
from testapp.models import Hydjobs,Bengalorejobs,Delhijobs,punejobs
from faker import Faker
from random import *
fake=Faker()
def phonenumbergen():
    d1=randint(7,9)
    num=""+str(d1)
    for i in range(9):
        num=num+str(randint(0,9))
    return int(num)
def populate(n):
    for i in range(n):
        fname=fake.name()
        faddress=fake.address()
        feligibility=fake.random_element(elements=('b.tech','m.tech','MCA'))
        femail=fake.email()
        fphonenumber=phonenumbergen()
        hydjobs_record=Hydjobs.objects.get_or_create(name=fname,address=faddress,
                                             eligibility=feligibility, email=femail, phonenumber=fphonenumber )
        bengalorejobs_record =Bengalorejobs.objects.get_or_create(name=fname, address=faddress,
                                                       eligibility=feligibility, email=femail, phonenumber=fphonenumber)

        delhi_record = Delhijobs.objects.get_or_create(name=fname, address=faddress,
                                                       eligibility=feligibility, email=femail, phonenumber=fphonenumber)
        punejobs_record = punejobs.objects.get_or_create(name=fname, address=faddress,
                                                       eligibility=feligibility, email=femail, phonenumber=fphonenumber)

populate(10)


