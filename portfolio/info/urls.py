from django.urls import path
from .views import (SkillAddView,SkillView,skillEditView,deleteSkill,
                    EducationAddView,EducationView,educationEditView,deleteEducation,
                    ExperienceAddView,ExperienceView,experienceEditView,deleteExperience,
)
urlpatterns = [
    path('skill/create/', SkillAddView.as_view(), name='add_skill'),
    path('skill/edit/<int:id>', skillEditView, name='edit_skill'),
    path('skill/', SkillView.as_view(), name='skill'),
    path('delete/<int:id>', deleteSkill, name='delete_skill'),
    # education_urls
    path('education/create/', EducationAddView.as_view(), name='add_education'),
    path('education/edit/<int:id>', educationEditView, name='edit_education'),
    path('education/', EducationView.as_view(), name='education'),
    path('delete/<int:id>', deleteEducation, name='delete_education'),
    # experience_urls
    path('experience/create/', ExperienceAddView.as_view(), name='add_experience'),
    path('experience/edit/<int:id>', experienceEditView, name='edit_experience'),
    path('experience/', ExperienceView.as_view(), name='experience'),
    path('delete/<int:id>', deleteExperience, name='delete_experience'),
]