'''
    This file holds all the views for the sessions api.
    
    Created on Jan 13, 2014

    @author: Andrew Oberlin, Jake Gregg
'''

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from rest.serializers import SessionSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import pycassa
from django.conf import settings
from rest.forms import SessionGetListForm, SessionPostForm, SessionPutForm, SessionGetSingleForm
from rest.exceptions import BadRequestException, NotImplementedException

class SessionsListView(APIView):
    '''
       Used for searching all sessions and creating new sessions
    '''
    
    def get(self, request):
        '''
            Used to search for a session
        '''
        # get the offset and limit query parameters
        form = UserGetListForm(request.QUERY_PARAMS)
        
        if form.is_valid():
            return Response(form.submit())
        else:
            raise BadRequestException()
            

    def post(self, request):
        '''
            Used to create a new user.
        '''
        form = UserPostForm(request.DATA)

        if form.is_valid():
            return Response(form.submit())
        else:
            raise BadRequestException()
        
class SessionsSingleView(APIView):
    '''
       Used for managing user properties, getting specific users and deleting users.
    '''
    
    def get(self, request, user_id):
        '''
            Used to get a user by id.
        '''
        # get the offset and limit query parameters
        form = UserGetSingleForm({ 'user_id' : user_id })
        
        if form.is_valid():
            return Response(form.submit())
        else:
            raise BadRequestException()
            
    
    def put(self, request, user_id):
        '''
            Used to update fields for a given user.
        '''
        data = { key : request.DATA[key] for key in request.DATA }
        data['user_id'] = user_id
        form = UserPutForm(data)

        if form.is_valid():
            return Response(form.submit())
        else:
            raise BadRequestException()
        
    def delete(self, request, user_id):
        '''
            Used to delete a user making it inactive.
        '''
        raise NotImplementedException()
