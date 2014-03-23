# Create your views here.

from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404
from django.views.generic.base import View
from django.http import HttpResponseRedirect, HttpResponseForbidden
from django.core.urlresolvers import reverse

from communities.models import *

def list(request):
    communities = None
    if "loc" in request.GET:
        communities = Community.objects.filter(location=loc)
    else:
        communities = Community.objects.all()

    return render(request, "c_list.html", {"communities":communities})

class new(View):
    def get(self, request, invalid=False):
        if not request.user.is_authenticated():
            return HttpResponseForbidden()

        form = NewCommunityForm()
        return render(request, "c_new.html", {"form":form, "invalid": invalid})

    def post(self, request):
        if not request.user.is_authenticated():
            return HttpResponseForbidden()
            
        form = NewCommunityForm(request.POST)
        if form.is_valid():
            community           = Community()
            community.owner     = request.user
            community.title     = form.cleaned_data["title"]
            community.location  = form.cleaned_data["location"]
            community.slogan    = form.cleaned_data["slogan"]
            community.description= form.cleaned_data["description"]

            community.save()
            return HttpResponseRedirect(reverse("communities_details", args=(community.id,)))
        else:
            return get(request, invalid=True)

def details(request, id):
    community = get_object_or_404(Community, id=id)

    return render(request, "c_details.html", {"community":community})

class enroll(View):
    def get(self, request, id):
        if not request.user.is_authenticated():
            return HttpResponseForbidden()

        community = get_object_or_404(Community, id=id)
        return render(request, "c_enroll.html", {"community":community})

    def post(self, request, id):
        if not request.user.is_authenticated():
            return HttpResponseForbidden()

        community = get_object_or_404(Community, id=id)
        membership = Membership(community=community)
        membership.member = request.user

        if request.POST["enroll"] == True:
            membership.save()

        return HttpResponseRedirect(reverse("communities_details", args=(id,)))

def manage(request, id):
    
    community = get_object_or_404(Community, id=id)
    if request.method == 'GET':
        form = NewCommunityForm(instance=community)

        return render(request, "c_manage.html", {"community":community, "form":form, "invalid":False})
    else:
        form = NewCommunityForm(request.POST, instance=community)
        if form.is_valid():
            form.save()

            return HttpResponseRedirect(reverse("communities_details", args=(id,)))
        else:
            return render(request, "c_manage.html", {"community":community, "form":form, "invalid":True})

