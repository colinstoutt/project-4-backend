from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from ..models.recruit import Recruit
from ..serializers import RecruitSerializer

# Create your views here.
class RecruitClass(APIView):
    def get(self, request):
        """Index Request"""
        print(request.session)
        recruits = Recruit.objects.all()[:10]
        data = RecruitSerializer(recruits, many=True).data
        return Response(data)

    serializer_class = RecruitSerializer
    def post(self, request):
        """Post request"""
        print(request.data)
        recruit = RecruitSerializer(data=request.data)
        if recruit.is_valid():
            b = recruit.save()
            return Response(recruit.data, status=status.HTTP_201_CREATED)
        else:
            return Response(recruit.errors, status=status.HTTP_400_BAD_REQUEST)

class RecruitDetail(APIView):
    def get(self, request, pk):
        """Show request"""
        recruit = get_object_or_404(Recruit, pk=pk)
        data = RecruitSerializer(recruit).data
        return Response(data)

    def patch(self, request, pk):
        """Update Request"""
        recruit = get_object_or_404(Recruit, pk=pk)
        ms = RecruitSerializer(recruit, data=request.data)
        if ms.is_valid():
            ms.save()
            return Response(ms.data)
        return Response(ms.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        """Delete Request"""
        recruit = get_object_or_404(Recruit, pk=pk)
        recruit.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)