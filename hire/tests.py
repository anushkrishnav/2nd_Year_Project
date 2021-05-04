from django.test import TestCase, LiveServerTestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from . models import Job 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class JobPostTests(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='testuser',
            first_name='Test',
            last_name='User',
            email='testuser@gmail.com',
            is_employer=True,
            password='secret'
        )

        self.job = Job.objects.create(
            title='Software development intern - Summer 2021',
            employer=self.user,
            description='A chance for college students to learn about industry techniques',
            requirement='Working on a bachelor degree in computer science or similar',
            workCondition='Attending college or higher education',
        )

    
    def test_string_representation(self):
        job = Job(title='Software development intern - Summer 2021', employer=self.user)
        self.assertEqual(str(job), job.title)
    
    def test_job_content(self):
        self.assertEqual(f'{self.job.title}', 'Software development intern - Summer 2021')
        self.assertEqual(f'{self.job.employer}', 'testuser')
        self.assertEqual(f'{self.job.description}', 'A chance for college students to learn about industry techniques')

    def test_job_list_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Software development intern')
        self.assertTemplateUsed(response, 'home.html')

    def test_job_detail_view(self):
        response = self.client.get('/jobs/1/')
        no_response = self.client.get('/jobs/10000/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, 'A chance for college students to learn')
        self.assertTemplateUsed(response, 'job_details.html')

class JobUpadteViewTest(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='testuser',
            first_name='Test',
            last_name='User',
            email='testuser@gmail.com',
            is_employer=True,
            password='secret'
        )

        self.job = Job.objects.create(
            title='Software development intern - Summer 2021',
            employer=self.user,
            description='A chance for college students to learn about industry techniques',
            requirement='Working on a bachelor degree in computer science or similar',
            workCondition='Attending college or higher education',
        )

        self.job.title = "New Title"
        self.job.description = "New Description"

    def test_string_representation(self):

        job = Job(title='Software development intern - Summer 2021', employer=self.user)
        job.title="New Title"
        self.assertEqual(str(job), job.title)
    
    def test_job_content(self):
        self.assertEqual(f'{self.job.title}', 'New Title')
        self.assertEqual(f'{self.job.employer}', 'testuser')
        self.assertEqual(f'{self.job.description}', 'New Description')

    def test_job_list_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Software development intern')
        self.assertTemplateUsed(response, 'home.html')

    # def test_job_detail_view(self):
    #     self.job.description = "New description"
    #     response = self.client.get('/jobs/1/')
    #     no_response = self.client.get('/jobs/10000/')
    #     self.assertEqual(response.status_code, 200)
    #     self.assertEqual(no_response.status_code, 404)
    #     self.assertContains(response, 'New description')
    #     self.assertTemplateUsed(response, 'job_details.html')