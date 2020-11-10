from .serializers import JobSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from contact import bot


class JobList(APIView):

    def get(self, request, format=None):
        return Response({'detail': 'Method "GET" not allowed'},
                        status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def post(self, request, format=None):
        serializer = JobSerializer(data=request.data)

        if serializer.is_valid():
            msg = serializer.save()
            bot.send_as_attachment(msg)
            return Response(data=serializer.data,
                            status=status.HTTP_201_CREATED)

        return Response(data=serializer.errors,
                        status=status.HTTP_400_BAD_REQUEST)
