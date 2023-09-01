from rest_framework.exceptions import NotFound, ValidationError
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
import json


from .models import Listing
from .serializers import ListingSerializer


class ListingList(generics.ListAPIView):
    serializer_class = ListingSerializer
    queryset = Listing.objects.all()

    ##
    # def get(self, request, id):
    #    try:
    #        listing = Listing.objects.filter(id = id).values()
    #        return HttpResponse(json.dumps(listing.get()))
    #    except:
    #        return HttpResponse(json.dumps({'status':'error'}), status=404)
        

    def put(self, request, id):
        try:
            listing = self.serializer_class.Meta.model.objects.get(id = id)
            serializer = self.serializer_class(listing, request.data)
            if(serializer.is_valid()):
                serializer.save()
                return Response(serializer.data, status=200)
            else:
                raise ValidationError()
        except self.serializer_class.Meta.model.DoesNotExist:
            raise NotFound()
