
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Project,Proposal 
from .models import Job
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from accounts.models import CustomUser


# Create your views here.

def index(request):
    if request.user.is_authenticated:
    
        if request.user.role == 'freelancer':
        
            all_projects = Project.objects.all().order_by('-created_at')[:10]
            context = {'projects': all_projects, 'page_title': 'Freelancer Dashboard'}
            return render(request, 'index.html', context)
        
        elif request.user.role == 'client':
         
            client_projects = Project.objects.filter(user=request.user).order_by('-created_at')
            context = {'client_projects': client_projects, 'page_title': 'Client Dashboard'}
            return render(request, 'index.html', context)
            
        else:
           
            return render(request, 'index.html', {'page_title': 'Welcome'})
    else:
        
        return render(request, 'index.html', {'page_title': 'Home'})


@login_required
def post_project(request):
    if request.user.role != 'freelancers':
        messages.warning(request, "Only freelancers can post projects.")
        return redirect('index')

    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        category = request.POST.get('category')
        skills = request.POST.get('skills')
        file = request.FILES.get('file')

        # Save project
        Project.objects.create(
            user=request.user,
            title=title,
            description=description,
            category=category,
            file=file,
            skills=skills
        )

        messages.success(request, "Your project has been posted successfully!")
        return redirect('index')

    context = {'page_title': 'Post a Project'}
    return render(request, 'post_project.html', context)


# @login_required
# def client_hire(request):
#     if request.user.role != 'client':
#         messages.warning(request, "Only clients can use the 'Hire a Freelancer' form.")
#         return redirect('index')

#     if request.method == 'POST':
#         form = ClientHireForm(request.POST)
#         if form.is_valid():
#             # Save the ClientHire request
#             form.save()
#             messages.success(request, "Your hiring request has been submitted! We'll be in touch.")
#             return redirect('index')
#         else:
#             messages.error(request, "Please correct the errors in the form.")
#     else:
#         form = ClientHireForm(initial={'full_name': f"{request.user.first_name} {request.user.last_name}"})
    
#     context = {'form': form, 'page_title': 'Client Hire Request'}
#     return render(request, 'client_hire.html', context)

# ... (rest of the views are fine, but add page_title for consistency) ...

def about_us(request):
    return render(request,'about_us.html', {'page_title': 'About Us'})

def freelancers_profile(request, user_id):
    user_profile = get_object_or_404(CustomUser, id=user_id)
   
    
    context = {
        'user_profile': user_profile,
        
        'page_title': f"{user_profile.first_name}'s Profile"
    }
    return render(request, 'freelancers_profile.html', context)

# def find_freelancers(request):
    # query = request.GET.get('q', '')
    
    # # Filter CustomUser objects where role is 'freelancer'
    # freelancers_queryset = CustomUser.objects.filter(role='freelancer', is_active=True)

    # if query:
    #     # Basic search on name or skills
    #     freelancers_queryset = freelancers_queryset.filter(
    #         Q(first_name__icontains=query) |
    #         Q(last_name__icontains=query) |
    #         Q(skills__icontains=query) |
    #         Q(bio__icontains=query)
    #     ).distinct()
    # context = {
    #     'freelancers_list': freelancers_queryset,
    #     'query': query,
    #     'page_title': 'Find Freelancers'
    # }
    # return render(request, 'find_freelancers.html', context)


def client_profile(request, user_id):
    
    client_user = get_object_or_404(CustomUser, id=user_id, role='client')

   
    projects_qs = Project.objects.filter(user=client_user).order_by('-created_at')

   
    total_projects_count = projects_qs.count()
   
    open_projects_count = projects_qs.filter(**{'status': 'open'}).count() if 'status' in [f.name for f in Project._meta.get_fields()] else total_projects_count

    return render(request, 'client_profile.html')

@login_required  
def post_job(request):
    if request.method == "POST":
        title = request.POST.get("title")
        description = request.POST.get("description")
        skills = request.POST.get("skills")
        budget = request.POST.get("budget")
        deadline = request.POST.get("deadline")

    
        # Job.objects.create(
        #     title=title,
        #     description=description,
        #     skills=skills,
        #     budget=budget,
        #     deadline=deadline,
        #     posted_by=request.user  
        # )

        
        # return redirect("job_list") 

    return render(request, "post-a-job.html")



def find_projects(request):
    query = request.GET.get('q', '')
    projects = Project.objects.all()

    if query:
        projects = projects.filter(title__icontains=query)

    context = {
        'projects': projects,
        'query': query,
    }
    return render(request, 'find_projects.html', context)


def project_detail(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    skills_list = project.skills.split(',') if project.skills else []

    # Check if freelancer already sent a proposal
    user_proposal = None
    if request.user.is_authenticated:
        user_proposal = Proposal.objects.filter(project=project, freelancer=request.user).first()

    context = {
        'project': project,
        'skills_list': skills_list,
        'user_proposal': user_proposal,
    }
    return render(request, 'project_detail.html', context)


@login_required
def send_proposal(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    if request.method == 'POST':
        message = request.POST.get('message')
        proposed_budget = request.POST.get('proposed_budget')
        Proposal.objects.create(
            freelancer=request.user,
            project=project,
            message=message,
            proposed_budget=proposed_budget
        )
        return redirect('project_detail', project_id=project.id)
    return redirect('project_detail', project_id=project.id)