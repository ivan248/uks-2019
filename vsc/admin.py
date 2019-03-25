# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Project, Branch, Commit
from .models import ProjectMembership
# Register your models here.

admin.site.register(Project)
admin.site.register(ProjectMembership)
admin.site.register(Branch)
admin.site.register(Commit)