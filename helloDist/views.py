from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.template import RequestContext

from django.core.context_processors import csrf

def homeView(request):
	if request.method == "GET":
		return render_to_response('index.html')