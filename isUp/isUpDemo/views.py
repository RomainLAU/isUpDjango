# from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.serializers import HyperlinkedModelSerializer
from rest_framework.viewsets import ModelViewSet
from isUpDemo.models import Domain


@api_view(["GET"])
def index(request):
    return Response({"Hello": "world."})


class DomainSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Domain
        fields = ["domain", "is_up", "checks_url", "url"]


class DomainViewSet(ModelViewSet):
    queryset = Domain.objects.all()
    serializer_class = DomainSerializer
    # permission_classes = [IsOwner]
