from django.db import models
from django.utils import timezone


# ORDERS TABLE
class StockCategories(models.Model):

    category_id = models.AutoField(primary_key=True, blank=False, null=False, unique=True)
    category = models.CharField(max_length=50, blank=False, null=False, unique=True)

    def __str__(self):
        return f"Category: {self.category}"


# stocK
class Stock(models.Model):

    ProductTitle = models.CharField(max_length=50)  # pot type eg: pot20, pot50
    ProductCode = models.CharField(max_length=50, primary_key=True)  # format pot20#1
    ProductCategory = models.CharField(max_length=50)  # filling, inplay, closed
    ProductWeight = models.FloatField()
    ProductDimension = models.CharField(max_length=50)
    ProductPrice = models.FloatField()
    ShortDescription = models.CharField(max_length=100)
    DetailedDescription = models.CharField(max_length=200)
    ProductBaseImage = models.ImageField()
    ProductImages = models.ImageField()

    def __str__(self):
        return f"{self.ProductTitle} @ [{self.ProductPrice}]"


# ORDERS TABLE
class RecordOrder(models.Model):

    OrderNumber = models.AutoField(primary_key=True, blank=False, null=False, unique=True)
    FirstName = models.CharField(max_length=50)  # pot type eg: pot20, pot50
    LastName = models.CharField(max_length=50)  # format pot20#1
    Email = models.CharField(max_length=100)  # filling, inplay, closed
    Phone = models.IntegerField()
    ProductTitle = models.CharField(max_length=50)
    DepositPaid = models.FloatField()

    def __str__(self):
        return f"Order: ORD_O{self.OrderNumber} from {self.FirstName} {self.LastName} with a desposit of Ksh {self.DepositPaid}"