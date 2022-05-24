from rest_framework.decorators import api_view
from rest_framework.response import Response

# every view function should take in a request 

@api_view(['GET'])
def cars_list(request):

    return Response('ok')