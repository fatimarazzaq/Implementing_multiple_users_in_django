from django.db import models
from users.models import User

# Create your models here.

class Buyer(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    buyer_name=models.CharField(max_length=200)
    buyer_email=models.CharField(max_length=200)

    def __str__(self):
        return self.buyer_name


class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    # parent = models.ForeignKey('self',blank=True, null=True,related_name='children', on_delete=models.CASCADE)


    def __str__(self):     
        return self.name

    class Meta:
        verbose_name = ("Category")
        verbose_name_plural = ("Categories")


class Product(models.Model):
    id=models.AutoField(primary_key=True)
    title=models.CharField(max_length=255)
    description=models.TextField(null=True,blank=True)
    price=models.IntegerField()
    slug = models.SlugField(max_length=255)
    date_posted = models.DateTimeField(auto_now_add=True)
    date_updated= models.DateTimeField(auto_now=True)
    image = models.ImageField(default='default.jpg',upload_to='product_pics')
    category=models.ForeignKey(Category,on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    @staticmethod
    def filter_product_by_category_id(categor_id):
        if categor_id:
            product_filter=Product.objects.filter(category=categor_id)
            return product_filter
        else:
            return Product.objects.all()

        

class Order(models.Model):      #Cart
    buyer=models.ForeignKey(Buyer,on_delete=models.SET_NULL,blank=True,null=True)
    date_ordered=models.DateTimeField(auto_now_add=True)
    complete=models.BooleanField(default=False,null=True,blank=False)
    transaction_id=models.CharField(max_length=200,null=True)


    def __str__(self):
        return str(self.id)

    @property
    def order_item_total(self):
        items=self.orderitem_set.all()
        sum=0
        for i in items:
            sum+=int(i.product_total)
        return sum
    
    @property
    def order_item_quantity(self):
        items=self.orderitem_set.all()
        sum=0
        for i in items:
            sum+=int(i.quantity)
        return sum
    

class OrderItem(models.Model):  #Product in Cart
    product=models.ForeignKey(Product,on_delete=models.SET_NULL,null=True,blank=True)
    order=models.ForeignKey(Order,on_delete=models.SET_NULL,null=True,blank=True)
    quantity=models.PositiveIntegerField(default=0,null=True,blank=True)
    date_added=models.DateTimeField(auto_now_add=True)

    @property
    def product_total(self):
        return int(self.product.price)*self.quantity


    def __str__(self):
        return self.product.title

    
class ShippingAddress(models.Model):
    buyer=models.ForeignKey(Buyer,on_delete=models.SET_NULL,null=True,blank=True)
    order=models.ForeignKey(Order,on_delete=models.SET_NULL,null=True,blank=True)
    address=models.CharField(max_length=200,null=False)
    city=models.CharField(max_length=200,null=False)
    state=models.CharField(max_length=200,null=False)
    zipcode=models.CharField(max_length=200,null=False)
    date_added=models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.address




