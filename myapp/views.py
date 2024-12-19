from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse
from django.http import JsonResponse
import json
from myapp.mixins import *


# Create your views here.
class CBV(View,HttpResponseMixin):
	def get(self,*args,**kwargs):
		json_data=json.dumps({'msg':'get method'})
		return self.render_to_http_response(json_data)
