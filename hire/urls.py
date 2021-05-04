from django.urls import path
from . views import (
    HomeView, 
    MyApplicants,
    JobDetailView,
    JobCreateView,
    JobUpdateView,
    JobDeleteView,
    SearchResultsListView,
    apply_for_job,
    SearchApplicantsListView,
    view_applicant_job, 
    dashboard, 
    view_application,
    CategoryView,
    about,
)

urlpatterns = [
path('', HomeView.as_view(), name="home"), 
path('jobs/applicants/', MyApplicants.as_view(), name='my_applicants'),
path('jobs/<int:pk>/', JobDetailView.as_view(), name="job-detail"),
path('jobs/new/', JobCreateView.as_view(), name='create_job'),
path('jobs/<int:pk>/update/', JobUpdateView.as_view(), name='update_job'),
path('jobs/<int:pk>/delete/', JobDeleteView.as_view(), name='delete_job'),
path('search/', SearchResultsListView.as_view(), name='search_results'),
path('jobs/<int:pk>/apply_for_job/', apply_for_job, name='apply_for_job'),
path('applicants_search/', SearchApplicantsListView.as_view(), name='search_applicants'), 
path('jobs/<int:job_id>', view_applicant_job, name='view_applicant_job'),
path('dashboard/', dashboard, name='dashboard'),
path('application/<int:application_id>/', view_application, name='view_application'),
path('category/<str:cats>/', CategoryView, name='category'),
path('about/', about, name='about'),
]