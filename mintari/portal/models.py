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
    ProductDimension = models.CharField(max_length=100)
    ProductPrice = models.FloatField()
    DetailedDescription = models.CharField(max_length=500)
    ProductBaseImage = models.ImageField(upload_to='stock_images/')
    ProductImageTopView = models.ImageField(upload_to='stock_images/', default='media/stock_images/chair1.jpg')
    ProductImageLeftView = models.ImageField(upload_to='stock_images/', default='media/stock_images/chair1.jpg')
    ProductImageFrontView = models.ImageField(upload_to='stock_images/', default='media/stock_images/chair1.jpg')

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


class WishList(models.Model):

    ProductCode = models.CharField(max_length=50)
    MintariUser = models.CharField(max_length=50)

    def __str__(self):
        return f"Product: {self.ProductCode} is in User {self.MintariUser} wishlist"


class Cart(models.Model):

    ProductCode = models.CharField(max_length=50)
    MintariUser = models.CharField(max_length=50)

    def __str__(self):
        return f"Product: {self.ProductCode} is in User {self.MintariUser} wishlist"


class Order(models.Model):
    OrderNumber = models.AutoField(primary_key=True, blank=False, null=False, unique=True)
    FirstName = models.CharField(max_length=50)
    LastName = models.CharField(max_length=50)
    Company = models.CharField(max_length=50)
    Country = models.CharField(max_length=50)
    BillingAddress1 = models.CharField(max_length=50, default="null address")
    BillingAddress2 = models.CharField(max_length=50, default="null address")
    City = models.CharField(max_length=50)
    PostCode = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    products = models.CharField(max_length=600)
    subtotal = models.FloatField()
    MintariUser = models.CharField(max_length=50)

    def __str__(self):
        return f"Product: {self.OrderNumber} for  {self.FirstName}"
