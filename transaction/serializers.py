from rest_framework import serializers
from .models import Product , Transaction , TransactionItem

class ProductSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Product
        fields = '__all__'


class TransactionItemSerializer(serializers.ModelSerializer):
    # transaction = serializers.PrimaryKeyRelatedField(read_only=True)
    product = ProductSerializer(read_only=True)
    class Meta:
        model = TransactionItem
        fields = ['id'  , 'product', 'qty']

class TransactionSerializer(serializers.ModelSerializer):
    items = serializers.SerializerMethodField()
    class Meta:
        model = Transaction
        fields = ['id' , 'buyer' , 'items']
        # depth = 1

    def get_items(self , obj):
        transaction_items = TransactionItem.objects.filter(transaction=obj)
        return TransactionItemSerializer(transaction_items, many=True).data
    
class TransactionPostSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Transaction
        fields = ['buyer' , 'items']

    def create(self, validated_data):
        transaction_items = validated_data.pop('items')
        transaction = Transaction.objects.create(buyer=validated_data['buyer'])
        # for item in transaction_items:
        #     print(item)
        #     new_item = TransactionItem.objects.create(transaction=transaction , **item)
        #     new_item.save()
        
        return super().create(validated_data)
