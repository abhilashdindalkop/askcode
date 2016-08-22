from rest_framework import status
from rest_framework.response import Response
from django.http import Http404
from rest_framework.views import APIView


from questionapi.serializers import QuestionSerializer, AnswerSerializer
from models import (getAllQuestions, getCurrentUser, getAllAnswers, getTagid, 
        getQuestionId, add_tag_to_question, get_Tag_Names, 
        search_questions, vote_answer, getTotalVotes)

import json  

class QuestionList(APIView):
    """
    List all Questions, or post a new Question.
    """
    def get(self, request, format=None):
    	sessionid = request.META['HTTP_TOKEN']
        currentuser = getCurrentUser(sessionid)

        questions = getAllQuestions(currentuser.id)

        serializer = QuestionSerializer(questions, many=True)
        # Adding in object
        response_data = {}
        
        response_data['questions'] = serializer.data

        # Get tag names for all questionList
        i=0
        for que in questions:
            response_data['questions'][i]['tags'] = get_Tag_Names(que.id)
            i=i+1

        return Response(json.dumps(response_data), status.HTTP_201_CREATED, content_type="application/json")

    def post(self, request, format=None):
        sessionid = request.META['HTTP_TOKEN']
        currentuser = getCurrentUser(sessionid)

        question = request.data

        # Getting the tag list
        tagList = question['tagList']
    
        question['user_id'] = currentuser.id

        serializer = QuestionSerializer(data = question)
        if serializer.is_valid():
            serializer.save()
            # add tags to question
            qid = getQuestionId(serializer.data['id'])
            for tag in tagList:
                tagid = getTagid(tag['name'])                  #Check if tag is not present in db
                add_tag_to_question(qid,tagid)

            response_data = {}
            response_data['question'] = serializer.data
            response_data['question']['tags'] = get_Tag_Names(serializer.data['id'])

            return Response(json.dumps(response_data), status.HTTP_201_CREATED, content_type="application/json")
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AnswersList(APIView):
    """
    List all Answers for a question id, or post a Answer for a question id.
    """
    def get(self, request, qid, format=None):
        sessionid = request.META['HTTP_TOKEN']            
        owneruser = getCurrentUser(sessionid)
        
        answers = getAllAnswers(qid)   

        serializer = AnswerSerializer(answers, many=True)
        
        for ans in serializer.data:
            ans['votes'] = getTotalVotes(ans['id'])
        print (serializer.data)
        return Response(serializer.data)

    def post(self, request, format=None):
        sessionid = request.META['HTTP_TOKEN']            

        currentuser = getCurrentUser(sessionid)

        answer = request.data
        answer['owner_id'] = currentuser.id

        serializer = AnswerSerializer(data = answer)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Search(APIView):
    """
    Searching
    """
    def post(self, request, format=None):

        search_txt = request.data
        questions = search_questions(search_txt)

        serializer = QuestionSerializer(questions, many=True)
        
        return Response(serializer.data, status=status.HTTP_201_CREATED)



class AnswerVote(APIView):
    """
    Answer Vote
    """
    def post(self, request, format=None):
        
        sessionid = request.META['HTTP_TOKEN']           

        currentuser = getCurrentUser(sessionid)
        answer = request.data
        votetype = answer['vote']
        del answer['vote']
        
        vote_answer(answer['id'], currentuser, votetype)

        answer['vote'] = votetype
        response_data = {}
        response_data['answer'] = answer

        return Response(json.dumps(response_data), status.HTTP_201_CREATED, content_type="application/json")



