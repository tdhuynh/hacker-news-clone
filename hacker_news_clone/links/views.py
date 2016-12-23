from django.shortcuts import render
from links.models import Link, Vote
from django.views.generic import ListView

class LinkListView(ListView):
    model = link
    queryset = link.with_votes.all()
    paginate_by = 3
