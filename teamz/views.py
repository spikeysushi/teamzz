from django.shortcuts import render, redirect
from .models import Team, Member
from .forms import TeamForm, MemberForm

# Create your views here.

def team_list(request):
    context = {
        "teams" : Team.objects.all()
    }
    return render(request, "team.html", context)

def member_list(request):
    members = Member.objects.all()
    context={
        "members" : members
    }
    return render(request, "member.html", context)

def team_create(request):
    form = TeamForm()
    if request.method == 'POST':
        form = TeamForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('team')
    context = {
        "form" : form
    }
    return render(request, 'team_create.html', context)

def member_create(request):
    form = MemberForm()
    if request.method == 'POST':
        form = MemberForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('member')
    context = {
        "form" : form
    }
    return render(request, 'member_create.html', context)




