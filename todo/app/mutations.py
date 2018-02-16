import graphene
from graphene import relay

from .models import Task

class CreateTask(relay.ClientIDMutation):
    class Input:
        task_name = graphene.String(required=True)
        task_description = graphene.String(required=True)
        completed = graphene.Boolean(required=True)

    success = graphene.Boolean()
    errors = graphene.List(graphene.String)

    @classmethod
    def mutate_and_get_payload(cls, root, info, **input):
        
        task_name = input.get('task_name')
        task_desc = input.get('task_description')
        done = input.get('completed')

        if(info.context.user.is_authenticated):
            task = Task.objects.create(
                task_name=task_name,
                task_desc=task_desc,
                completed=done,
                user=info.context.user
            )
            
            return CreateTask(success=bool(task.id))
        errors = ["Please Log In."]
        return CreateTask(success=False, errors=errors)
