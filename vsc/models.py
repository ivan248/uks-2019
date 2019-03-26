# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.
class User(models.Model):
    email = models.CharField(max_length=100, unique=True, blank=False)
    password = models.CharField(max_length=30)

    def __str__(self):
        return self.email

class CurrentUser(models.Model):
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=30)

    def toUser(self):
        num_of_users = User.objects.filter(email = self.email).count()
        if num_of_users != 0 :
            return User.objects.filter(email=self.email).get()

        u = User(self.email, self.password)
        u.save()

        return User.objects.filter(email=self.email).get()

    def __str__(self):
        return self.email


class Project(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class ProjectMembership(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    def __str__(self):
        return "membership"


class Branch(models.Model):
    name = models.CharField(max_length=100)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Commit(models.Model):
    hash = models.CharField(max_length=50)
    message = models.CharField(max_length=3000)
    creation_date = models.DateTimeField('date published')
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.hash

class Issue(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class IssueAssignments(models.Model):
    issue = models.ForeignKey(Issue, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return "assignment"

class Label(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    color = models.CharField(max_length=7)

    def __str__(self):
        return self.name

class IssueLabels(models.Model):
    issue = models.ForeignKey(Issue, on_delete=models.CASCADE)
    label = models.ForeignKey(Label, on_delete=models.CASCADE)

    def __str__(self):
        return "label"

class Milestone(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    due_date = models.DateTimeField('due_date')
    issue = models.ForeignKey(Issue, on_delete=models.CASCADE)

    def __str__(self):
        return self.name