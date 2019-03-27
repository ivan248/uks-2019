from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login$', views.login, name='login'),
    url(r'^register$', views.register, name='register'),
    #PROJECT
    url(r'^projects$', views.project_list, name='project_list'),
    url(r'^projects/(?P<project_id>[0-9]+)$', views.project_detail, name="project_detail"),
    url(r'^projects/create$', views.project_create, name="project_create"),
    url(r'^projects/(?P<project_id>[0-9]+)/update', views.project_update, name="project_update"),
    url(r'^projects/(?P<project_id>[0-9]+)/delete', views.project_delete, name="project_delete"),
    url(r'^projects/(?P<project_id>[0-9]+)/add_member', views.project_add_member, name="project_add_member"),
    #BRANCH
    url(r'^projects/(?P<project_id>[0-9]+)/branches/(?P<branch_id>[0-9]+)$', views.branch_detail, name="branch_detail"),
    url(r'^projects/(?P<project_id>[0-9]+)/branches$', views.branch_create, name="branch_create"),
    url(r'^projects/(?P<project_id>[0-9]+)/branches/(?P<branch_id>[0-9]+)/update', views.branch_update, name="branch_update"),
    url(r'^projects/(?P<project_id>[0-9]+)/branches/(?P<branch_id>[0-9]+)/delete', views.branch_delete, name="branch_delete"),
    #COMMIT
    url(r'^projects/(?P<project_id>[0-9]+)/branches/(?P<branch_id>[0-9]+)/commits/(?P<commit_id>[0-9]+)$', views.commit_detail, name="commit_detail"),
    url(r'^projects/(?P<project_id>[0-9]+)/branches/(?P<branch_id>[0-9]+)/commits$', views.commit_create, name="commit_create"),
    url(r'^projects/(?P<project_id>[0-9]+)/branches/(?P<branch_id>[0-9]+)/commits/(?P<commit_id>[0-9]+)/update$', views.commit_update, name="commit_update"),
    url(r'^projects/(?P<project_id>[0-9]+)/branches/(?P<branch_id>[0-9]+)/commits/(?P<commit_id>[0-9]+)/delete$', views.commit_delete, name="commit_delete"),
    #ISSUE
    url(r'^projects/(?P<project_id>[0-9]+)/issues$', views.issue_create, name="issue_create"),
    url(r'^projects/(?P<project_id>[0-9]+)/issues/(?P<issue_id>[0-9]+)$', views.issue_detail, name="issue_detail"),
    url(r'^projects/(?P<project_id>[0-9]+)/issues/(?P<issue_id>[0-9]+)/update$', views.issue_update, name="issue_update"),
    url(r'^projects/(?P<project_id>[0-9]+)/issues/(?P<issue_id>[0-9]+)/delete$', views.issue_delete, name="issue_delete"),
    url(r'^projects/(?P<project_id>[0-9]+)/issues/(?P<issue_id>[0-9]+)/add_label', views.issue_add_label, name="issue_add_label"),
    url(r'^projects/(?P<project_id>[0-9]+)/issues/(?P<issue_id>[0-9]+)/add_assignee', views.issue_add_assignee, name="issue_add_assignee"),
    #MILESTONE
    url(r'^projects/(?P<project_id>[0-9]+)/issues/(?P<issue_id>[0-9]+)/milestones$', views.milestone_create, name="milestone_create"),
    url(r'^projects/(?P<project_id>[0-9]+)/issues/(?P<issue_id>[0-9]+)/milestones/(?P<milestone_id>[0-9]+)$', views.milestone_detail, name="milestone_detail"),
    url(r'^projects/(?P<project_id>[0-9]+)/issues/(?P<issue_id>[0-9]+)/milestones/(?P<milestone_id>[0-9]+)/update$', views.milestone_update, name="milestone_update"),
    url(r'^projects/(?P<project_id>[0-9]+)/issues/(?P<issue_id>[0-9]+)/milestones/(?P<milestone_id>[0-9]+)/delete$', views.milestone_delete, name="milestone_delete"),
    #LABEL
    url(r'^labels/create$', views.label_create, name="label_create"),
    url(r'^labels$', views.label_list, name="label_list"),
    url(r'^labels/(?P<label_id>[0-9]+)$', views.label_detail, name="label_detail"),
    url(r'^labels/(?P<label_id>[0-9]+)/update$', views.label_update, name="label_update"),
    url(r'^labels/(?P<label_id>[0-9]+)/delete$', views.label_delete, name="label_delete"),

]
