from django.contrib import admin
from .models import Project, Proposal



@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'client', 'company_name', 'category', 'budget_min', 'budget_max', 'deadline', 'created_at')
    list_filter = ('category', 'deadline', 'created_at')
    search_fields = ('title', 'description', 'skills', 'company_name', 'client__first_name', 'client__last_name')
    ordering = ('-created_at',)
  

# Admin for Proposal model (optional, also manageable independently)
@admin.register(Proposal)
class ProposalAdmin(admin.ModelAdmin):
    list_display = ('project', 'freelancer', 'proposed_budget', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('project__title', 'freelancer__first_name', 'freelancer__last_name')
    ordering = ('-created_at',)



