from rest_framework.exceptions import NotFound, ValidationError
from rest_framework import generics
from rest_framework.response import Response
import json


from .models import Assignment
from .serializers import AssignmentSerializer


class AssignmentList(generics.ListAPIView):
    serializer_class = AssignmentSerializer
    queryset = Assignment.objects.all()

    ##
    # def get(self, request, id):
        

    def post(self, request):
        try:
            serializer = self.serializer_class(data=request.data)
            if serializer.is_valid() :
                serializer.save()
                return Response(serializer.data, status=200)
            else:
                raise ValidationError()
        except self.serializer_class.Meta.model.DoesNotExist:
            raise NotFound()


