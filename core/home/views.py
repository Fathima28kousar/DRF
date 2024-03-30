from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializers import *
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework import generics



class StudentGeneric(generics.ListAPIView, generics.CreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class StudentGeneric1(generics.UpdateAPIView,generics.DestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    lookup_field = 'id'



# @api_view(['GET'])
# def get_book(request):
#     book_objs = Book.objects.all()
#     serializer = BookSerializer(book_objs, many=True)
#     return Response({'status':200, 'payload':serializer.data})


# from rest_framework_simplejwt.tokens import RefreshToken


# class RegisterUser(APIView):
#     def post(self,request):
#         serializer = UserSerializer(data = request.data)
        

#         if not serializer.is_valid():
#             return Response({'status' : 403, 'errors': serializer.errors, 'message': 'Something went wrong'})
        
#         serializer.save()
#         user = User.objects.get(username = serializer.data['username']) 
#         refresh = RefreshToken.for_user(user)  #manual simple.jwt token
#         # token_obj , _  = Token.objects.get_or_create(user = user)            #manual token
#         return Response({'status':200,'payload':serializer.data,'message':'Your data is saved',  'refresh': str(refresh),
#         'access': str(refresh.access_token),})

# from rest_framework.authentication import TokenAuthentication
# from rest_framework.permissions import IsAuthenticated
# from rest_framework_simplejwt.authentication import JWTAuthentication

# class StudentAPI(APIView):
#     authentication_classes = [JWTAuthentication]
#     permission_classes = [IsAuthenticated]
#     def get(self, request):
#         student_objs = Student.objects.all()
#         serializer = StudentSerializer(student_objs, many=True)
#         return Response({'status' : 200, 'message' : serializer.data})
#     def post(self, request):
#         data = request.data
#         serializer = StudentSerializer(data = request.data)
#         # if request.data['age'] < 18:
#         #     return Response({'status':403, 'message':'age must be > 18'})
#         if not serializer.is_valid():
#             print(serializer.errors)
#             return Response({'status' : 403, 'errors': serializer.errors, 'message': 'Something went wrong'})
#         serializer.save()
#         return Response({'status':200,'payload':data,'message':'Your data is saved'})
    

#     def patch(self, request):
#         try:
#             student_obj = Student.objects.get(id = request.data['id'])
#             serializer = StudentSerializer(student_obj, data=request.data, partial=True)
#             if not serializer.is_valid():
#                 print(serializer.errors)
#                 return Response({'status':403, 'errors': serializer.errors, 'message':'Something went wrong'})
#             serializer.save()
#             return Response({'status': 200, 'payload':serializer.data, 'message':'data is updated'})
    
#         except Exception as e:
#             print(e)
#             return Response({'status':403, 'message':'invalid id'})
        

#     def put(self, request):
#         try:
#             student_obj = Student.objects.get(id = request.data['id'])
#             serializer = StudentSerializer(student_obj, data=request.data, partial=False)
#             if not serializer.is_valid():
#                 print(serializer.errors)
#                 return Response({'status':403, 'errors': serializer.errors, 'message':'Something went wrong'})
#             serializer.save()
#             return Response({'status': 200, 'payload':serializer.data, 'message':'data is updated'})
    
#         except Exception as e:
#             print(e)
#             return Response({'status':403, 'message':'invalid id'})

#     def delete(self, request):
#         try:
#             student_id = request.data.get('id')
#             student_obj = Student.objects.get(id = student_id )
#             student_obj.delete()
#             return Response({'status':200,'message':'deleted'})
#         except Exception as e:
#             print(e)
#             return Response({'status':403,'message':'invalid id'})










# @api_view(['GET'])
# def home(request):
#     student_objs = Student.objects.all()
#     serializer = StudentSerializer(student_objs, many=True)
#     return Response({'status' : 200, 'message' : serializer.data})

# @api_view(['POST'])
# def post_student(request):
#     data = request.data
#     serializer = StudentSerializer(data = request.data)

#     # if request.data['age'] < 18:
#     #     return Response({'status':403, 'message':'age must be > 18'})

#     if not serializer.is_valid():
#         print(serializer.errors)
#         return Response({'status' : 403, 'errors': serializer.errors, 'message': 'Something went wrong'})
    
#     serializer.save()
#     return Response({'status':200,'payload':data,'message':'Your data is saved'})

# @api_view(['PUT'])
# def update_student(request,id):

#     try:
#         student_obj = Student.objects.get(id = id)
#         serializer = StudentSerializer(student_obj, data=request.data, partial=True)
#         if not serializer.is_valid():
#             print(serializer.errors)
#             return Response({'status':403, 'errors': serializer.errors, 'message':'Something went wrong'})
#         serializer.save()
#         return Response({'status': 200, 'payload':serializer.data, 'message':'data si saved'})
    
#     except Exception as e:
#         print(e)
#         return Response({'status':403, 'message':'invalid id'})
    
# @api_view(['DELETE'])
# def delet_student(request,id):
#     try:
#         student_obj = Student.objects.get(id = id)
#         student_obj.delete()
#         return Response({'status':200,'message':'deleted'})
#     except Exception as e:
#         print(e)
#         return Response({'status':403,'message':'invalid id'})