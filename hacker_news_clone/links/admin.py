from django.contrib import admin
from links.models import Link, Vote

admin.site.register(Link, Vote)
