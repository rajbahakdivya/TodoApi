from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Task
from .serializer import TaskSerializer

class TaskListView(APIView):
    def get(self, request):
         tasks = Task.objects.all()
         serializer = TaskSerializer(tasks, many=True)
         return Response(serializer.data)
        #     msg = {
        #         "message" : "",
        #         "data" : serializer.data

        #     }
            
        #     return Response(msg, status= status.HTTP_200_OK)
        # except Exception as e:
        #     print(e)
        #     msg={
        #         'status' : 400,
        #         "message" : "invalid data"
        #     }
        #     return Response(msg, status= status.HTTP_400_BAD_REQUEST)

    def post(self, request):
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data['name']
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class TaskDetailView(APIView):
    
    # def get(self, request, pk):
    #     task = Task.get_object.filter(pk=pk)
    #     if not task.exists():
    #         data = {"error": "Task does not exist."}
    #         return Response(data=data, status=status.HTTP_400_BAD_REQUEST)
    #     serializer = TaskSerializer(task)
    #     return Response(serializer.data)  
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