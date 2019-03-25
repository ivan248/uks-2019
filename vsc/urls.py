from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.project_list, name='index'),
    url(r'^projects$', views.project_list, name='project_list'),
    url(r'^projects/(?P<project_id>[0-9]+)$', views.project_detail, name="project_detail"),
    url(r'^projects/create$', views.project_create, name="project_create"),
    url(r'^projects/(?P<project_id>[0-9]+)/update', views.project_update, name="project_update"),
    url(r'^projects/(?P<project_id>[0-9]+)/delete', views.project_delete, name="project_delete"),
    url(r'^projects/(?P<project_id>[0-9]+)/add_member', views.project_add_member, name="project_add_member"),
    url(r'^projects/(?P<project_id>[0-9]+)/branches/(?P<branch_id>[0-9]+)$', views.branch_detail, name="branch_detail"),
    url(r'^projects/(?P<project_id>[0-9]+)/branches$', views.branch_create, name="branch_create"),
    url(r'^projects/(?P<project_id>[0-9]+)/branches/(?P<branch_id>[0-9]+)/update', views.branch_update, name="branch_update"),
    url(r'^projects/(?P<project_id>[0-9]+)/branches/(?P<branch_id>[0-9]+)/delete', views.branch_delete, name="branch_delete"),
    url(r'^projects/(?P<project_id>[0-9]+)/branches/(?P<branch_id>[0-9]+)/commits/(?P<commit_id>[0-9]+)$', views.commit_detail, name="commit_detail"),
    url(r'^projects/(?P<project_id>[0-9]+)/branches/(?P<branch_id>[0-9]+)/commits$', views.commit_create, name="commit_create"),
    url(r'^projects/(?P<project_id>[0-9]+)/branches/(?P<branch_id>[0-9]+)/commits/(?P<commit_id>[0-9]+)/update$', views.commit_update, name="commit_update"),
    url(r'^projects/(?P<project_id>[0-9]+)/branches/(?P<branch_id>[0-9]+)/commits/(?P<commit_id>[0-9]+)/delete$', views.commit_delete, name="commit_delete"),
]
