from rest_framework. decorators import api_view
from rest_framework.response import Response
from rest_framework.exceptions import ParseError
from .models import *
from .serializer import *

@api_view(['GET'])
def get_todo(request):
    response= {'status':200}
    todo_objs = Todo.objects.all()
    serializer = TodoSerializer (todo_objs , many = True)
    response ['data'] = serializer.data
    return Response (response)

@api_view(['POST'])
def post_todo(request):
    try:
        data = request.data
        serializer = TodoSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            response = {'status': 200, 'data': serializer.data}
            return Response(response)
        else:
            return Response(serializer.errors, status=400)
    except ParseError as e:
        return Response({'detail': str(e)}, status=400)

@api_view (['PATCH'])
def patch_todo(request):
    response = {'status': 200}
    data = request.data
    try: 
        obj = Todo.objects.get(id = data.get('id'))
        serializers = TodoSerializer(obj , data = data , partial=True)
        if serializers.is_valid():
            serializers.save()
            response['data'] = serializers.data
            return Response(response)
        
        return Response(serializers.errors)
    
    except Exception as e:
        print(e)

    return Response({
        'status': 400,
        'message' : "invalid id"
        })
    
@api_view (['DELETE'])
def delete_todo(request):
    response = {'status' : 200}
    data = request.data
    try:
        obj = Todo.objects.get(id = data.get('id'))
        obj.delete()
        return Response({'status': 200 , 'message' : 'deleted id'})
    
    except Exception as e:
        print (e)

    return Response ({'status':400 , 'message' : 'invalid id'})
        
    

