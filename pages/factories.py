import factory
from .models import Product
from .models import Comment

class ProductFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Product
    name = factory.Faker('company')
    price = factory.Faker('random_int', min=200, max=9000)

class ProductFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Comment
    description = factory.Faker('company')
    product_id = factory.Faker('random_int', min=200, max=9000)