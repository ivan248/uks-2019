from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.shortcuts import get_object_or_404
from django.utils.crypto import get_random_string
import datetime

from .models import Project, ProjectMembership, Branch, Commit, User, CurrentUser


def index(request):
    template = loader.get_template('vsc/auth.html')
    context = {}
    return HttpResponse(template.render(context, request))

def register(request):
    email = request.POST.get('email_reg', "NO_USER_PROVIDED")
    password = request.POST.get('password_reg', "NO_PASSWORD_PROVIDED")
    if email == "NO_USER_PROVIDED" or password == "NO_PASSWORD_PROVIDED":
        return HttpResponse("You must enter both email and password")

    number_of_users = User.objects.filter(email=email).count()
    if number_of_users >= 1:
        return HttpResponse("User with that email already exists")

    u = User(email = email, password=password)
    u.save()

    number_of_current_users = CurrentUser.objects.all().count()
    if number_of_current_users != 0 :
        currentUser = CurrentUser.objects.all()[:1].get()
        currentUser.email = u.email
        currentUser.password = u.password
        currentUser.save()
        return HttpResponseRedirect(reverse('vsc:project_list'))

    currentUser = CurrentUser(email = u.email, password= u.password)
    currentUser.save()
    return HttpResponseRedirect(reverse('vsc:project_list'))


def login(request):
    user_name = request.POST.get('email', "NO_USER_PROVIDED")
    password = request.POST.get('password', "NO_PASSWORD_PROVIDED")
    user = get_object_or_404(User, email=user_name)
    if user.password != password:
        return HttpResponse("Password is incorrect")

    return HttpResponseRedirect(reverse('vsc:project_list'))

def project_list(request):
    projects = Project.objects.all()
    template = loader.get_template('vsc/project_list.html')
    context = {
        'projects': projects,
    }
    return HttpResponse(template.render(context, request))


def project_detail(request, project_id):
    project = Project.objects.get(id=project_id)
    template = loader.get_template('vsc/project_detail.html')
    branches = Branch.objects.filter(project=project)

    projectMemberships = ProjectMembership.objects.filter(project = project.id)
    members = []

    for membership in projectMemberships :
        members.append(membership.user.email)

    context = {
        'project': project,
        'branches': branches,
        'members': members
    }
    return HttpResponse(template.render(context, request))

def project_create(request):
    if request.method == 'POST':
        project_name = request.POST['project_name']
        project = Project(name=project_name)
        project.save()
        return HttpResponseRedirect(reverse('vsc:project_list'))

def project_update(request, project_id):

    if request.method == 'POST':
        project_name = request.POST['project_name']
        project = Project.objects.get(id=project_id)
        project.name = project_name
        project.save()
        return HttpResponseRedirect(reverse('vsc:project_list'))

def project_delete(request, project_id):

    if request.method == 'POST':
        Project.objects.filter(id=project_id).delete()
        return HttpResponseRedirect(reverse('vsc:project_list'))

def project_add_member(request, project_id):
    if request.method == 'POST':
        member_email = request.POST['member_email']
        project = get_object_or_404(Project, id=project_id)
        print(member_email)
        u = get_object_or_404(User, email=member_email)
        print("AAAAAAAAAAAAAAAAAA")

        found = ProjectMembership.objects.filter(project=project.id, user=u.id).count()
        if found != 0 :
            return HttpResponse("This member is already added")

        p = ProjectMembership(project=project, user=u)
        p.save()
        return HttpResponseRedirect(reverse('vsc:project_list'))

def branch_detail(request, project_id, branch_id):

    project = Project.objects.get(id=project_id)
    branch = Branch.objects.get(id=branch_id)
    template = loader.get_template('vsc/branch_detail.html')
    commits = Commit.objects.filter(branch=branch)
    context = {
        'project': project,
        'branch': branch,
        'commits': commits
    }
    return HttpResponse(template.render(context, request))

def branch_create(request, project_id):
    branch_name = request.POST['branch_name']
    p = get_object_or_404(Project, id=project_id)
    branch = Branch(name=branch_name, project=p)
    branch.save()
    return HttpResponseRedirect(reverse('vsc:project_detail', kwargs={'project_id':project_id}))

def branch_update(request, project_id, branch_id):
    if request.method == 'POST':
        branch_name = request.POST['branch_name']
        branch = Branch.objects.get(id=branch_id)
        branch.name = branch_name
        branch.save()
        return HttpResponseRedirect(
            reverse('vsc:project_detail', kwargs={'project_id':project_id})
        )

def branch_delete(request, project_id, branch_id):

    if request.method == 'POST':
        Branch.objects.filter(id=branch_id).delete()
        return HttpResponseRedirect(reverse('vsc:project_detail',kwargs={'project_id':project_id}))


def commit_detail(request, project_id, branch_id, commit_id):

    project = Project.objects.get(id=project_id)
    branch = Branch.objects.get(id=branch_id)
    commit = Commit.objects.get(id=commit_id)

    template = loader.get_template('vsc/commit_detail.html')
    context = {
        'project': project,
        'branch': branch,
        'commit': commit
    }
    return HttpResponse(template.render(context, request))

def commit_create(request, project_id, branch_id):
    commit_message = request.POST['commit_message']
    p = get_object_or_404(Project, id=project_id)
    b = get_object_or_404(Branch, id=branch_id)
    commit_hash = get_random_string(length=32)
    creation_date = datetime.datetime.now()
    currentUser = CurrentUser.objects.all()[:1].get()
    commit = Commit(
        message=commit_message,
        hash=commit_hash,
        creation_date=creation_date,
        branch=b,
        user= currentUser.toUser()
    )
    commit.save()
    return HttpResponseRedirect(
        reverse('vsc:branch_detail', kwargs={'project_id': project_id, 'branch_id': branch_id})
    )

def commit_update(request, project_id, branch_id, commit_id):

    if request.method == 'POST':
        commit_message = request.POST['commit_message']
        commit = Commit.objects.get(id=commit_id)
        commit.message = commit_message
        commit.save()
        return HttpResponseRedirect(
            reverse('vsc:branch_detail', kwargs={'project_id':project_id, 'branch_id': branch_id})
        )

def commit_delete(request, project_id, branch_id, commit_id):

    if request.method == 'POST':
        Commit.objects.filter(id=commit_id).delete()
        return HttpResponseRedirect(
            reverse('vsc:branch_detail',kwargs={'project_id':project_id, 'branch_id': branch_id})
        )