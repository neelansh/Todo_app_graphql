import graphene

import app.schema

from app.mutations import CreateTask
import graphql_social_auth

class Query(app.schema.Query, graphene.ObjectType):
    pass


class Mutation(graphene.ObjectType):
    create_task = CreateTask.Field()
    social_auth = graphql_social_auth.SocialAuth.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
