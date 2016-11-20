# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class Ai(models.Model):
    tags = models.TextField(blank=True, null=True)
    questions = models.TextField()
    votes = models.TextField(blank=True, null=True)
    no_answers = models.TextField(blank=True, null=True)
    links = models.TextField()

    def __str__(self):
        return '%s %s %s %s %s' % (self.questions, self.links,self.votes,self.no_answers,self.tags)

    class Meta:
        managed = False
        db_table = 'AI'


class Askubuntu(models.Model):
    tags = models.TextField(blank=True, null=True)
    questions = models.TextField()
    votes = models.TextField(blank=True, null=True)
    no_answers = models.TextField(blank=True, null=True)
    links = models.TextField()

    def __str__(self):
        return '%s %s %s %s %s' % (self.questions, self.links,self.votes,self.no_answers,self.tags)

    class Meta:
        managed = False
        db_table = 'askUbuntu'


class Astronomy(models.Model):
    tags = models.TextField(blank=True, null=True)
    questions = models.TextField()
    votes = models.TextField(blank=True, null=True)
    no_answers = models.TextField(blank=True, null=True)
    links = models.TextField()

    def __str__(self):
        return '%s %s %s %s %s' % (self.questions, self.links,self.votes,self.no_answers,self.tags)

    class Meta:
        managed = False
        db_table = 'astronomy'
