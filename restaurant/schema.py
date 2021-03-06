import graphene
from graphene_django.types import DjangoObjectType
from .models import RestaurantCategory, Restaurant, MenuCategory, Menu, Area, Review, PayMethod, \
    MenuItemAddCategory, MenuItemAdd
from django.contrib.auth.models import User


class AreaType(DjangoObjectType):
    class Meta:
        model = Area


class AreaInput(graphene.InputObjectType):
    name = graphene.String()


class PayMethodType(DjangoObjectType):
    class Meta:
        model = PayMethod


class RestaurantCategoryType(DjangoObjectType):
    class Meta:
        model = RestaurantCategory


class RestaurantType(DjangoObjectType):
    class Meta:
        model = Restaurant


class MenuCategoryType(DjangoObjectType):
    class Meta:
        model = MenuCategory


class MenuType(DjangoObjectType):
    class Meta:
        model = Menu


class ReviewType(DjangoObjectType):
    class Meta:
        model = Review


class MenuItemAddType(DjangoObjectType):
    class Meta:
        model = MenuItemAdd


class MenuItemAddCategoryType(DjangoObjectType):
    class Meta:
        model = MenuItemAddCategory


class Query(graphene.AbstractType):
    all_restaurantCategory = graphene.List(RestaurantCategoryType)
    restaurant = graphene.Field(RestaurantType,
                                id=graphene.Int(),
                                name=graphene.String())
    menu = graphene.Field(MenuType,
                          id=graphene.Int(),
                          restaurant=graphene.Int(),
                          category=graphene.Int(),
                          )
    all_restaurant = graphene.List(RestaurantType,
                                   name=graphene.String(),
                                   areaId=graphene.Int(),
                                   )
    all_menuCategory = graphene.List(MenuCategoryType,
                                     restaurant=graphene.Int())
    all_menu = graphene.List(MenuType,
                             name=graphene.String(),
                             id=graphene.Int(),
                             restaurant=graphene.Int(),
                             category=graphene.Int())
    all_area = graphene.List(AreaType)
    all_review = graphene.List(ReviewType,
                               restaurant=graphene.Int())

    all_menuItemAddCategory = graphene.List(MenuItemAddCategoryType,
                                            menu=graphene.Int()
                                            )
    all_menuItemAdd = graphene.List(MenuItemAddType,
                                    category=graphene.Int())

    def resolve_all_area(self, context, **kwargs):
        return Area.objects.all()

    def resolve_all_restaurantCategory(self, context, **kwargs):
        return RestaurantCategory.objects.all()

    def resolve_all_restaurant(self, context, **kwargs):
        name = kwargs.get('name')
        areaId = kwargs.get('areaId')
        if name is not None:
            return Restaurant.objects.filter(name=name)

        if areaId is not None:
            return Restaurant.objects.filter(area__id=areaId)

        return Restaurant.objects.all()

    def resolve_all_menuCategory(self, context, **kwargs):
        id = kwargs.get('restaurant')
        if id is not None:
            return MenuCategory.objects.filter(restaurant__id=id)
        return MenuCategory.objects.all()

    def resolve_all_menu(self, context, **kwargs):
        restaurant = kwargs.get('restaurant')
        category = kwargs.get('category')
        name = kwargs.get('name')
        if name is not None:
            return Menu.objects.filter(name=name)
        if restaurant is not None:
            return Menu.objects.filter(restaurant__id=restaurant)
        if category is not None:
            return Menu.objects.filter(category__id=category)

        return Menu.objects.all()

    def resolve_all_review(self, context, **kwargs):
        id = kwargs.get('restaurant')
        if id is not None:
            return Review.objects.filter(restaurant__id=id)
        return Review.objects.all()

    def resolve_restaurant(self, info, **kwargs):
        id = kwargs.get('id')
        name = kwargs.get('name')

        if id is not None:
            return Restaurant.objects.get(pk=id)

        if name is not None:
            return Restaurant.objects.get(name=name)
        return None

    def resolve_menu(self, info, **kwargs):
        id = kwargs.get('id')
        restaurant = kwargs.get('restaurant')
        category = kwargs.get('category')

        if id is not None:
            return Menu.objects.get(pk=id)
        if restaurant is not None:
            return Menu.objects.get(restaurant__id=restaurant)
        if category is not None:
            return Menu.objects.get(category__id=category)

        return None

    def resolve_menuItemAddCategory(self, info, **kwargs):
        menu = kwargs.get('menu')
        if menu is not None:
            return MenuItemAddCategory.objects.filter(menu=menu)

    def resolve_menuItemAdd(self, info, **kwargs):
        category = kwargs.get('category')
        if category is not None:
            return MenuItemAdd.objects.filter(category=category)


class Liked(graphene.Mutation):
    class Arguments:
        username = graphene.String()
        restaurantId = graphene.Int()

    liked = graphene.Field(RestaurantType)

    def mutate(self, info, username, restaurantId):
        user = User.objects.get(username=username)
        restaurant = Restaurant.objects.get(pk=restaurantId)

        if restaurant.likes.filter(id=user.id).exists():
            _liked = restaurant.likes.remove(user)
        else:
            _liked = restaurant.likes.add(user)

        return Liked(liked=_liked)


class Mutation(graphene.ObjectType):
    liked = Liked.Field()
