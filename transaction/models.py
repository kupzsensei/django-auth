from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=25)
    price = models.DecimalField(max_digits=10 , decimal_places=2)


    def __str__(self):
        return self.name

class Transaction(models.Model):
    buyer = models.CharField(max_length=20)
    items = models.ManyToManyField(Product , through='TransactionItem')

    def __str__(self):
        return self.buyer


class TransactionItem(models.Model):
    transaction = models.ForeignKey(Transaction , on_delete=models.CASCADE )
    product = models.ForeignKey(Product , on_delete=models.CASCADE )
    qty = models.IntegerField()

    def __str__(self):
        return f"{self.product} - {self.qty}"
