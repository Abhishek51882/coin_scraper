from django.shortcuts import render

import uuid
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import ScrapingTask
from .serializers import ScrapingTaskSerializer
from .tasks import scrape_coin_data

class StartScrapingView(APIView):
    def post(self, request):
        coins = request.data.get('coins', [])
        print('coins here:', coins)
        job_id = uuid.uuid4()
        tasks = []
        for coin in coins:
            task = ScrapingTask(job_id=job_id, coin=coin, status='pending')
            print(task)
            task.save()  # Ensure the task is saved to the database
            scrape_coin_data.delay(task.id)
            tasks.append(task)
        return Response({'job_id': job_id, 'tasks': ScrapingTaskSerializer(tasks, many=True).data}, status=status.HTTP_202_ACCEPTED)
class ScrapingStatusView(APIView):
    def get(self, request, job_id):
        tasks = ScrapingTask.objects.filter(job_id=job_id)
        return Response({'job_id': job_id, 'tasks': ScrapingTaskSerializer(tasks, many=True).data})

