from guardian.shortcuts import assign_perm
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from permissions.services import APIPermissionClassFactory
from events.models import Event
from events.serializers import EventSerializer

def evaluate(user, obj, request):
    return user.username == obj.baby.parent.name

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = (
        APIPermissionClassFactory(
            name='EventPermission',
            permission_configuration={
                'base': {
                    'create': True,
                    'list': True,
                },
                'instance': {
                    'retrieve': 'events.view_event',
                    'destroy': evaluate,
                    'update': evaluate,
                    'partial_update': 'events.change_event',
                }
            }
        ),
    )

    def perform_create(self, serializer):

        parent_baby=serializer.validated_data["baby"]

        user = self.request.user


        nameUser=str(user.username)
        
        nameFather=str(parent_baby)

        if (nameUser!=nameFather):
            print ("No tiene lo permisos para acceder.")
        elif(nameUser==nameFather):
            event = serializer.save()
            print ("Se guardo exitosamente.")
            assign_perm('events.change_event', user, event)
            assign_perm('events.view_event', user, event)
            return Response(serializer.data)
