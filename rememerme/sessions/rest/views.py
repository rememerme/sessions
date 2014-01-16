'''
    This file holds all the views for the sessions api.
    
    Created on Jan 13, 2014

    @author: Andrew Oberlin, Jake Gregg
'''
from rest_framework.views import APIView
from rest_framework.response import Response
from rememerme.sessions.rest.forms import SessionPostForm, SessionPutForm, SessionDeleteForm
from rememerme.sessions.rest.exceptions import BadRequestException

class SessionsListView(APIView):
    '''
       Used for searching all sessions and creating new sessions
    '''
            
    def post(self, request):
        '''
            Used to create a new session.
        '''
        form = SessionPostForm(request.DATA)

        if form.is_valid():
            return Response(form.submit())
        else:
            raise BadRequestException()
        
class SessionsSingleView(APIView):
    '''
       Used for managing session properties, getting specific sessions and deleting sessions.
    '''
    
    def put(self, request, session_id):
        '''
            Used to update fields for a given session.
        '''
        data = { key : request.DATA[key] for key in request.DATA }
        data['session_id'] = session_id
        form = SessionPutForm(data)

        if form.is_valid():
            return Response(form.submit())
        else:
            raise BadRequestException()
        
    def delete(self, request, session_id):
        '''
            Used to delete a user making it inactive.
        '''
        form = SessionDeleteForm({'session_id':session_id})

        if form.is_valid():
            return Response(form.submit())
        else:
            raise BadRequestException()
