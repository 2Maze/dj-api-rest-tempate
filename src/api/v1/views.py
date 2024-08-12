from rest_framework import viewsets
from rest_framework.response import Response
from api.models import *
from rest_framework.authentication import TokenAuthentication


class BaseApiView(viewsets.ViewSet):

    authentication_classes = [TokenAuthentication]

    def health(self, request, *args, **kwargs):
        """ Healthcheck """

        return Response({
            "status": "healthy",
        })

    # TODO Make write this function
    def balance(self, request, *args, **kwargs):
        """ Check out user balance """

        return Response({
            "balance": self.request.user.tokens,
        })

