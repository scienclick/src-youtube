from rest_framework import generics
from myapp.models import myModel
from myapp.serializers import myModelSerializer


class myMoldeList(generics.ListCreateAPIView):
    queryset = myModel.objects.all()
    serializer_class = myModelSerializer
    name="myModel-list"

class myModelDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = myModel.objects.all()
    serializer_class = myModelSerializer
    name="myModel-detail"