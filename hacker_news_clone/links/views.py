from django.shortcuts import render
from links.models import Link, Vote, UserProfile
from django.views.generic import ListView, DetailView
from djanog.contrib.auth import get_user_model


class LinkListView(ListView):
    model = Link
    queryset = Link.with_votes.all()
    paginate_by = 3


class UserProfileDetailView(DetailView):
    model = get_user_model()
    slug_field = "username"
    template = "user_detail.html"

    def get_object(self, queryset=None):
        user = super(UserProfileDetailView, self).get_object(queryset)
        UserProfile.objects.get_or_create(user=user)
        return user
