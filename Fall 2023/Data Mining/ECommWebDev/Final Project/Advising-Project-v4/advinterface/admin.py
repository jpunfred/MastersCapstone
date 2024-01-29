# advinterface/admin.py
from django.contrib import admin
from .models import CommunicationClass, MathematicsClass, SocialSciencesClass, ComponentAreaClass, CISClass, AdvancedCISElective, UserProfile

class CourseAdmin(admin.ModelAdmin):
    list_display = ['code', 'name']
    search_fields = ['code', 'name']

@admin.register(CommunicationClass)
class CommunicationClassAdmin(CourseAdmin):
    pass

@admin.register(MathematicsClass)
class MathematicsClassAdmin(CourseAdmin):
    pass

@admin.register(SocialSciencesClass)
class SocialSciencesClassAdmin(CourseAdmin):
    pass

@admin.register(ComponentAreaClass)
class ComponentAreaClassAdmin(CourseAdmin):
    pass

@admin.register(CISClass)
class CISClassAdmin(CourseAdmin):
    pass

@admin.register(AdvancedCISElective)
class AdvancedCISElectiveAdmin(CourseAdmin):
    pass

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'buff_id', 'email']
    list_filter = ['communication_classes', 'mathematics_class', 'social_sciences_class', 'component_area_classes', 'cis_classes', 'advanced_cis_electives']
    search_fields = ['first_name', 'last_name', 'buff_id', 'email']

    fieldsets = [
        ('Personal Information', {'fields': ['first_name', 'last_name', 'buff_id', 'email']}),
        ('Communication Classes', {'fields': ['communication_classes']}),
        ('Mathematics Class', {'fields': ['mathematics_class']}),
        ('Social Sciences Class', {'fields': ['social_sciences_class']}),
        ('Component Area Classes', {'fields': ['component_area_classes']}),
        ('CIS Classes', {'fields': ['cis_classes']}),
        ('Advanced CIS Electives', {'fields': ['advanced_cis_electives']}),
        ('Transcript Upload', {'fields': ['transcript_upload']}),
    ]
    filter_horizontal = ['communication_classes', 'component_area_classes', 'cis_classes', 'advanced_cis_electives']
