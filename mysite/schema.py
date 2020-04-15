from restaurant.schema import Query as RestaurantQuery
from restaurant.schema import Mutation as RestaurantMutation
from accounts.schema import Query as UserQuery
from accounts.schema import Mutation as UserMutation

import graphene
import graphql_jwt


class Query(RestaurantQuery, UserQuery, graphene.ObjectType):
    pass


class Mutation(UserMutation, RestaurantMutation, graphene.ObjectType,):
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)