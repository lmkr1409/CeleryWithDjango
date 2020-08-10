from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from AppWithAsyncTask.tasks import async_model_task
from django.utils import timezone
from time import sleep

# Create your views here.

class SampleAPI(APIView):

    def get(self, request):
        requets_time = timezone.localtime()
        async_model_task.delay()
        return Response({"Request time": requets_time,"Response time": timezone.localtime()})

