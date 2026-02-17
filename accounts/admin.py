from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from .models import Freelancer, Skill

# Register your models here.


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    model = CustomUser

   
    list_display = ('email', 'first_name', 'last_name', 'role', 'is_active', 'is_staff', 'date_joined')

    
    fieldsets = (
        ('Login Credentials', {'fields': ('email', 'password')}),
        ('Personal Information', {'fields': ('first_name', 'last_name', 'contact_number', 'role')}),
        ('Freelancer Details', {
            'fields': ('profile_picture', 'bio', 'skills', 'years_of_experience', 'portfolio_link'),
            'classes': ('collapse',), 
        }),
        ('Permissions', {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')
        }),
        ('Important Dates', {'fields': ('last_login', 'date_joined')}),
    )

    
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'email',
                'first_name',
                'last_name',
                'contact_number',
                'role',
                'password1',
                'password2',
                'is_staff',
                'is_active'
            ),
        }),
    )

    ordering = ('email',)


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Freelancer)
class FreelancerAdmin(admin.ModelAdmin):
    list_display = ('name', 'title', 'rating', 'hourly_rate', 'location', 'experience_years')
    list_filter = ('location', 'skills')
    search_fields = ('name', 'title', 'bio')