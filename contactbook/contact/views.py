from django.shortcuts import render
from django.contrib.auth.models import User
from .models import ContactDetail
from .serializers import ShowContactDetailSerializer, AddContactDetailSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics, status
from rest_framework.response import Response
from django.http import Http404


class ShowContacts(generics.ListCreateAPIView):
       queryset = ContactDetail.objects.all()
       serializer_class = ShowContactDetailSerializer
       permission_classes = (IsAuthenticated,)




class AddContacts(generics.RetrieveDestroyAPIView):
       queryset = ContactDetail.objects.all()
       serializer_class = AddContactDetailSerializer
       permission_classes = (IsAuthenticated,)


       def perfrom_created(self, serializer):
           serializer.save(user=self.request.user)



