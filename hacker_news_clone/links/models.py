from django.db import models
from django.db.models import Count
from django.dispatch import receiver
from django.db.models.signals import post_save

class LinkVoteCountManager(models.Manager):
    def get_query_set(self):
        return super(LinkVoteCountManager, self).get_query_set().annotate(votes=count('vote')).order_by('-votes')


class Link(models.Model):
    title = models.CharField("Headline", max_length=100)
    submitter = models.ForeignKey('auth.User')
    submitted_on = models.DateTimeField(auto_now_add=True)
    rank_score = models.FloatField(default=0.0)
    url = models.URLField("URL", max_length=250, blank=True)
    description = models.TextField(blank=True)
    with_votes = LinkVoteCountManager()
    objects = models.Manager()

    def __unicode__(self):
        return self.title


class Vote(models.Model):
    voter = models.ForeignKey('auth.User')
    link = models.ForeignKey(Link)

    def __unicode__(self):
        return "%s voted %s" % (self.voter.username, self.link.title)


class UserProfile(models.Model):
    user = models.OneToOneField('auth.User', unique=True)
    bio = models.TextField(null=True)

    def __unicode__(self):
        return "%s's profile" % self.user

@receiver(post_save, sender='auth.User')
def create_user_profile(**kwargs):
    created = kwargs.get('created')
    instance = kwargs.get('instance')
    if created:
        Profile.objects.create(user=instance)

    
