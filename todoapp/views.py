from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Task
from .serializer import TaskSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated

class TaskListView(APIView):
    def get(self, request):
         tasks = Task.objects.all()
         serializer = TaskSerializer(tasks, many=True)
         return Response(serializer.data)
        

    def post(self, request):
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data['name']
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class TaskDetailView(APIView):

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
     
    def get(self, request, pk):
         tasks = Task.objects.get(pk=pk)
         serializer = TaskSerializer(tasks)
         return Response(serializer.data)
     
    def put(self, request, pk):
        task = Task.objects.get(pk=pk)
        serializer = TaskSerializer(task, data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        task = Task.objects.get(id=pk) 
        task.delete()
        # task.is_delete = True
        return Response({'success': True, 'message': 'Task deleted successfully'})