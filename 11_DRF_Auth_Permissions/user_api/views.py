from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['POST'])
def logout(request):
    return True
    if request.method == 'POST':
        request.user.auth_token.delete()
        return Response({"message":'Token Deleted'})