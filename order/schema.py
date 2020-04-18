import graphene
from graphene_django.types import DjangoObjectType
from .models import Order
from django.contrib.auth.models import User
import sys
sys.path.append('..')
from restaurant.models import Restaurant, PayMethod


class OrderType(DjangoObjectType):
    class Meta:
        model = Order


class CreateOrder(graphene.Mutation):

    class Arguments:
        user = graphene.Int()
        restaurant = graphene.Int()
        pay_method = graphene.Int()
        sum_price = graphene.String()
        menus = graphene.String()

    order = graphene.Field(OrderType)

    def mutate(self, info, user, restaurant, sum_price, menus, pay_method):
        _order = Order.objects.create(user=User.objects.get(id=user), restaurant=Restaurant.objects.get(id=restaurant),
                                      sum_price=sum_price, menus=menus, pay_method=PayMethod.objects.get(id=pay_method))

        return CreateOrder(order=_order)


class Query(graphene.AbstractType):
    all_order = graphene.List(OrderType)

    def resolve_all_order(self, context, **kwargs):
        return Order.objects.all()


class Mutation(graphene.ObjectType):
    create_order = CreateOrder.Field()
