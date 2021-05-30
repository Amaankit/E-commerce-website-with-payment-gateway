from django.db import models
from django.contrib.auth.models import User

# Create your models here.
STATE_CHOICES = (
   ("AN","Andaman and Nicobar Islands"),
   ("AP","Andhra Pradesh"),
   ("AR","Arunachal Pradesh"),
   ("AS","Assam"),
   ("BR","Bihar"),
   ("CG","Chhattisgarh"),
   ("CH","Chandigarh"),
   ("DN","Dadra and Nagar Haveli"),
   ("DD","Daman and Diu"),
   ("DL","Delhi"),
   ("GA","Goa"),
   ("GJ","Gujarat"),
   ("HR","Haryana"),
   ("HP","Himachal Pradesh"),
   ("JK","Jammu and Kashmir"),
   ("JH","Jharkhand"),
   ("KA","Karnataka"),
   ("KL","Kerala"),
   ("LA","Ladakh"),
   ("LD","Lakshadweep"),
   ("MP","Madhya Pradesh"),
   ("MH","Maharashtra"),
   ("MN","Manipur"),
   ("ML","Meghalaya"),
   ("MZ","Mizoram"),
   ("NL","Nagaland"),
   ("OD","Odisha"),
   ("PB","Punjab"),
   ("PY","Pondicherry"),
   ("RJ","Rajasthan"),
   ("SK","Sikkim"),
   ("TN","Tamil Nadu"),
   ("TS","Telangana"),
   ("TR","Tripura"),
   ("UP","Uttar Pradesh"),
   ("UK","Uttarakhand"),
   ("WB","West Bengal")
)

      
CATEGORY_CHIOCES=(
    ('M',('Mobile')),
    ('L',('Laptop')),
    ('BW',(
        ('BWMENS', 'Menswear'),
            ('BWWOMENS', 'Womenswear'),
    )
    ),
    ('TW',(
        ('TWMENS', 'Menswear'),
            ('TWWOMENS', 'Womenswear'),
    )
    
    )
)
class Product(models.Model):
    title=models.CharField(max_length=100)
    selling_price=models.FloatField()
    discounted_price=models.FloatField()
    discription=models.TextField()
    brand= models.CharField(max_length=100)
    category= models.CharField(choices=CATEGORY_CHIOCES,max_length=10)
    product_image= models.ImageField(upload_to='product_img' )
    def __str__(self):
        return str(self.id)

class Cart(models.Model):
    user=models.ForeignKey( User,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField(default=1)
    def __str__(self):
        return str(self.id)
    @property
    def totalCost(self):
        return (self.quantity * self.product.discounted_price)

STATUS_CHOICES=(
    ('Accepted','Accepted'),
    ('Packed','Packed'),
    ('On The Way','On The Way'),
    ('Delivered','Delivered'),
    ('Cancel','Cancel')
)

class UserProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    landmark = models.CharField(max_length=100)
    locality = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    zipcode=models.PositiveIntegerField()
    state=models.CharField(choices=STATE_CHOICES, max_length=60)

class OrderPlaced(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    userprofile=models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField(default=1)
    ordered_date=models.DateField(auto_now_add=True)
    status= models.CharField(choices=STATUS_CHOICES,max_length=100)
    def __str__(self):
        return str(self.id)
    @property
    def totalCost(self):
        return (self.quantity * self.product.discounted_price)




