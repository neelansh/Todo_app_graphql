import graphene

from graphene_django.types import DjangoObjectType

from graphql import GraphQLError

from .models import *
from django.contrib.auth.models import User

class user(DjangoObjectType):
    class Meta:
        model = User

class task(DjangoObjectType):
    class Meta:
        model = Task


class Query(object):
    all_tasks = graphene.List(task)
    profile = graphene.NonNull(user)

    def resolve_all_tasks(self, info, **kwargs):
        if(not info.context.user.is_authenticated):
            raise GraphQLError('Please log in')
        return Task.objects.filter(user=info.context.user)

    def resolve_profile(self, info, **kwargs):
        if(not info.context.user.is_authenticated):
            raise GraphQLError('Please log in')
        return info.context.user

    # def resolve_all_users(self, info, **kwargs):
    #     return User.objects.all()
