from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy
from .models import Job, Application, ConversationMessage, Category
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import ApplicationForm, JobForm, EditForm



class HomeView(ListView):
    model = Job
    template_name = 'home.html'
    context_object_name = 'jobs'
    ordering = ['-posted']
    paginate_by = 5

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context

class MyApplicants(LoginRequiredMixin, ListView):
    model = Job
    template_name = 'my_applicants.html'
    context_object_name = 'jobs'
    paginate_by = 5

class JobDetailView(DetailView):
    model = Job
    template_name = 'job_details.html'


class JobCreateView(CreateView):
    model = Job
    form_class = JobForm
    template_name = 'Job-CRUD/create_job.html'
    

    def form_valid(self, form):
        form.instance.employer = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('home')

class JobUpdateView(UpdateView):
    model = Job
    form_class = EditForm
    template_name = 'Job-CRUD/update_job.html'
    

    def get_success_url(self):
        return reverse('home')

class JobDeleteView(DeleteView):
    model = Job
    template_name = 'Job-CRUD/delete_job.html'
    success_url = reverse_lazy('home')

class SearchResultsListView(ListView):
    model = Job
    context_object_name = 'job_list'
    template_name = 'job_search.html'

    def get_queryset(self):
        query = self.request.GET.get('q')

        return Job.objects.filter(
            Q(title__icontains=query) | Q(title__icontains=query)
        )

def CategoryView(request, cats):
    category_jobs = Job.objects.filter(category=cats) 
    

    return render(request, 'categories.html', {'cats':cats.title(), 'category_jobs':category_jobs})

@login_required
def apply_for_job(request, pk):
    job = Job.objects.get(pk=pk)

    if request.method == 'POST':
        form = ApplicationForm(request.POST)

        if form.is_valid():
            application = form.save(commit=False)
            application.job = job
            application.created_by = request.user
            application.save()

            return redirect('home')
    
    else:
        form = ApplicationForm()
    
    return render(request, 'apply_for_job.html', {'form': form, 'job': job})


class SearchApplicantsListView(ListView):
    model = Application
    context_object_name = 'applicants_list'
    template_name = 'applicants_search.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        return Application.objects.filter(
            Q(first_name__icontains=query) | Q(last_name__icontains=query) | Q(experience__icontains=query) | Q(email__icontains=query) | Q(phone__icontains=query)
            )

@login_required
def view_application(request, application_id):
    application = get_object_or_404(Application, pk=application_id, created_by=request.user)

    if request.user.is_employer:
        application = get_object_or_404(Application, pk=application_id, job__created_by=request.user)
    else:
        application = get_object_or_404(Application, pk=application_id, created_by=request.user)

    if request.method == 'POST':
        content = request.POST.get('content')

        if content:
            conversationmessage = ConversationMessage.objects.create(application=application, content=content, created_by=request.user)

            return redirect('view_application', application_id=application_id)
            

    return render(request, 'view_application.html', {'application': application})


@login_required
def view_applicant_job(request, job_id):
    job = get_object_or_404(Job, pk=job_id)

    return render(request, 'view_applicant_job.html', {'job': job})

@login_required
def dashboard(request):
    return render(request, 'dashboard.html', {'user': request.user})


def about(request):
    return render(request, 'about.html')
