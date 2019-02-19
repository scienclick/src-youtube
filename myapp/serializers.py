from rest_framework import serializers
from myapp.models import myModel

class myModelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=myModel

        fields=(
            'description',
            'image',
        )
