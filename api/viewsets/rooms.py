from api.models.rooms import Room
from api.viewsets.chat import ChatSerializer
from rest_framework import serializers, viewsets


class RoomSerializer(serializers.ModelSerializer):
    chat = ChatSerializer(many=True, read_only=True)

    class Meta:
        model = Room
        fields = (
            'code',
            'url',
            'description',
            'admin',
            'chat',
            'created',
            'expires',
            'name',
        )

        
class RoomViewSet(viewsets.ModelViewSet):
    """
    Django Rest Framework Room ViewSet
    """
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
