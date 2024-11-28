from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from .models import School
from .serializers import SchoolSerializer

class SchoolView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self, request):
        schools = School.objects.all()
        search = request.GET.get('search')
        if search :
            schools = School.objects.filter(name__contains=search)
        serializer = SchoolSerializer(schools, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = SchoolSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Enregistrement réussi'})
        else:
            return Response({'message': 'Données invalides'})
        
    def delete(self, request, id):
        try:
            school = get_object_or_404(School, id=id)
            school.delete()
            return Response({'message': 'Suppression réussie'})
        except Exception:
            return Response({'message': "L'objet n'existe pas"})
        
    def put(self, request, id):
        try:
            school = get_object_or_404(School, id=id)
            serializer = SchoolSerializer(school, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'message': 'Mise à jour réussie'})
            else:
                return Response(serializer.errors)
        except School.DoesNotExist:
            return Response({"message": "L'objet n'existe pas"})