from rest_framework import serializers
from . models import mymodel


class mymodelserializers(serializers.ModelSerializer):
    class Meta:
           model=mymodel
           fields="__all__"