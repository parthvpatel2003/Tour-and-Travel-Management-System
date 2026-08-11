from django.db import models

class Customer(models.Model):
    name = models.CharField(max_length=100)

class TravelAgency(models.Model):
    name = models.CharField(max_length=100)

class Resort(models.Model):
    name = models.CharField(max_length=100)

class Order(models.Model):
    name = models.CharField(max_length=100)

class HelpTicket(models.Model):
    message = models.CharField()

class Feedback(models.Model):
    message = models.CharField()

class PackageType(models.Model):

    DESTINATION_CHOICES = [
        ('India', 'India'),
        ('Australia', 'Australia'),
        ('Bali', 'Bali'),
        ('Disneyland', 'Disneyland'),
        ('Dubai', 'Dubai'),
        ('Greece', 'Greece'),
        ('Maldives', 'Maldives'),
        ('Paris', 'Paris'),
        ('Phuket', 'Phuket'),
    ]

    destination = models.CharField(max_length=20, choices=DESTINATION_CHOICES)
    package_type = models.CharField(max_length=100)
    plan_management = models.CharField(max_length=100)

    def __str__(self):
        return self.package_type

class PlanManagement(models.Model):
    plan_name = models.CharField(max_length=100)
    duration = models.CharField(max_length=50)
    nights_days = models.CharField(max_length=50)
    status = models.CharField(max_length=20,)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.plan_name

class Destination(models.Model):
    destination = models.CharField(max_length=100)
    description = models.TextField()
    displaylogo = models.ImageField(upload_to='logos/', blank=True, null=True)
    displaybanner = models.ImageField(upload_to='banners/', blank=True, null=True)

    def __str__(self):
        return self.destination

class UserDetails(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    mobile = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    fromcity = models.CharField(max_length=100)
    fromstate = models.CharField(max_length=100)
    fromcountry = models.CharField(max_length=100)
    tocity = models.CharField(max_length=100)
    tostate = models.CharField(max_length=100)
    tocountry = models.CharField(max_length=100)
    startdate = models.CharField(max_length=100)
    enddate = models.CharField(max_length=100)


    def __str__(self):
        return self.userdetail

class InquiryDetails(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    contactno = models.CharField(max_length=100, default="0000000000")
    message = models.CharField(max_length=100)

    def __str__(self):
        return self.inquirydetail

class Role_Master(models.Model):
    rolename = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.rolename