# advinterface/forms.py
from django import forms
from .models import CommunicationClass, MathematicsClass, SocialSciencesClass, ComponentAreaClass, CISClass, AdvancedCISElective, UserProfile

class UserProfileForm(forms.Form):
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    buff_id = forms.CharField(max_length=7, min_length=7)
    email = forms.EmailField()

    communication_classes = forms.ModelMultipleChoiceField(
        queryset=CommunicationClass.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
    )

    mathematics_class = forms.ModelChoiceField(
        queryset=MathematicsClass.objects.all(),
        widget=forms.RadioSelect,
        required=False,
    )

    social_sciences_class = forms.ModelChoiceField(
        queryset=SocialSciencesClass.objects.all(),
        widget=forms.RadioSelect,
        required=False,
    )

    component_area_classes = forms.ModelMultipleChoiceField(
        queryset=ComponentAreaClass.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
    )

    cis_classes = forms.ModelMultipleChoiceField(
        queryset=CISClass.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
    )

    advanced_cis_electives = forms.ModelMultipleChoiceField(
        queryset=AdvancedCISElective.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
    )
    
    transcript_upload = forms.FileField(
        label='Upload Previous Transcripts',
        required=False,
    )
    class Meta:
      model = UserProfile
      fields = ['first_name', 'last_name', 'buff_id', 'email', 'communication_classes', 'mathematics_class', 'social_sciences_class', 'component_area_classes', 'cis_classes', 'advanced_cis_electives', 'transcript_upload']
