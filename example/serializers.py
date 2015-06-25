import rest_framework.serializers as sz
import ember_drf.serializers as ember

from example.models import *

class BigThingSerializer(sz.ModelSerializer):
    class Meta:
        model = BigThing
        fields = ('id', 'name')
        
class ChildThingSerializer(sz.ModelSerializer):
    class Meta:
        model = ChildThing
        fields = ('id', 'name', 'father')
        
class ChildThingSideloadSerializer(ember.SideloadSerializer):
    class Meta:
        base_serializer = ChildThingSerializer
        sideloads = [
            (BigThing, BigThingSerializer)
        ]