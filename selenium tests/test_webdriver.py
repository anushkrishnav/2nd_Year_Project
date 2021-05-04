import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest

class test_WebDriver(unittest.TestCase):

    def setUp(self):

        self.firefox_browser = webdriver.Firefox()
        
        self.website = 'http://127.0.0.1:8000/'

        self.firefox_browser.get(self.website)
        self.firefox_browser.maximize_window()

        # Applicant
        self.applicant_username = 'Wulfsige_Gumarich'
        self.applicant_email = 'WulfsigeGumarich@gmail.com'
        self.applicant_first_name = 'Wulfsige'
        self.applicant_last_name = 'Gumarich'
        self.applicant_password = 'wbZDU8PFpA'
        self.applicant_phone = '012 345 6789'
        self.applicant_experience = '15 Years of python'

        #Employer
        self.employer_username = 'Lynda_Moon'
        self.employer_email = 'LyndaMoon@gmail.com'
        self.employer_first_name = 'Lynda'
        self.employer_last_name = 'Moon'
        self.employer_password = 'hPJQ5uRU6W'

        # Profile 
        self.profile_image = 'C:\\Users\\karlo\\Downloads\\profile_picture.jpg'
        self.profile_description = 'Young self taught tech lover'
        self.profile_cv = 'C:\\Users\\karlo\\Downloads\\Student Declaration of Academic Integrity 2nd Yr Project.docx'

        # Application
        self.application_title = 'Trainee IT Support Engineer - No Experience Required'
        self.application_description = 'We are recruiting for companies who are looking to employ our IT Technician Traineeship graduates to keep up with their growth. The best part is you will not need any previous experience as full training will be provided. You will also have the reassurance of a job guarantee (18K- €30K) upon completion.'
        self.application_snippet = 'We are recruiting for companies who are looking to employ IT Technician Traineeship graduates '
        self.application_requirements = 'None'
        self.application_new_requirements = 'Will to learn new technologies'
        self.application_work_conditions = 'Salary: 18K- €30K'
        self.application_image = 'C:\\Users\\karlo\\Downloads\\job1.jpg'

    def tearDown(self):
        self.firefox_browser.close()
        self.firefox_browser.quit()

    def test_applicantUserSignup_SuccessfulSignup(self):

        signup = self.firefox_browser.find_element_by_link_text('Sign Up')
        signup.click()

        time.sleep(2)

        username_field = self.firefox_browser.find_element_by_id('id_username')
        email_field = self.firefox_browser.find_element_by_id('id_email')
        first_name_field = self.firefox_browser.find_element_by_id('id_first_name')
        last_name_field = self.firefox_browser.find_element_by_id('id_last_name')
        password_field = self.firefox_browser.find_element_by_id('id_password1')
        confirmation_password_field = self.firefox_browser.find_element_by_id('id_password2')
        signup_button = self.firefox_browser.find_element_by_xpath('/html/body/div[1]/form/button')


        if username_field.is_displayed():

            username_field.clear()
            username_field.send_keys(self.applicant_username)

        time.sleep(2)

        if email_field.is_displayed():

            email_field.clear()
            email_field.send_keys(self.applicant_email)

        time.sleep(1)

        if first_name_field.is_displayed():

            first_name_field.clear()
            first_name_field.send_keys(self.applicant_first_name) 
        
        time.sleep(1)

        if last_name_field.is_displayed():

            last_name_field.clear()
            last_name_field.send_keys(self.applicant_last_name)

        time.sleep(1)

        if password_field.is_displayed():

            password_field.clear()
            password_field.send_keys(self.applicant_password)

        time.sleep(1)

        if confirmation_password_field.is_displayed():

            confirmation_password_field.clear()
            confirmation_password_field.send_keys(self.applicant_password)

        time.sleep(1)

        signup_button.click()
        
        time.sleep(2)

    def test_applicantUserLogin_SuccessfulLogin(self):

        login_link = self.firefox_browser.find_element_by_link_text('Log In')
        login_link.click()

        # time.sleep(2)

        username_field = self.firefox_browser.find_element_by_id('id_username')
        password_field = self.firefox_browser.find_element_by_id('id_password')
        login_button = self.firefox_browser.find_element_by_xpath('/html/body/div[1]/form/button')

        if username_field.is_displayed():

            username_field.clear()
            username_field.send_keys(self.applicant_username)
        
        # time.sleep(1)
        
        if password_field.is_displayed():

            password_field.clear()
            password_field.send_keys(self.applicant_password)

        # time.sleep(1)

        login_button.click()
        time.sleep(1)

    def test_applyingForJob_SuccessfullyApplied(self):
        
        self.test_applicantUserLogin_SuccessfulLogin()

        job_post = self.firefox_browser.find_element_by_xpath('/html/body/div[1]/ul[1]/div/div/div[2]/div/h5/a')
        job_post.click()

        time.sleep(1)

        apply_button = self.firefox_browser.find_element_by_xpath('/html/body/div[1]/button[1]/a')
        apply_button.click()

        time.sleep(2)

        first_name_textarea = self.firefox_browser.find_element_by_id('id_first_name')
        last_name_textarea = self.firefox_browser.find_element_by_id('id_last_name')
        email_textarea = self.firefox_browser.find_element_by_id('id_email')
        phone_textarea = self.firefox_browser.find_element_by_id('id_phone')
        experience_textarea = self.firefox_browser.find_element_by_id('id_experience')

        first_name_textarea.send_keys(self.applicant_first_name)
        last_name_textarea.send_keys(self.applicant_last_name)
        email_textarea.send_keys(self.applicant_email)
        phone_textarea.send_keys(self.applicant_phone)
        experience_textarea.send_keys(self.applicant_experience)

        time.sleep(3)

        submit_button = self.firefox_browser.find_element_by_xpath('/html/body/div[1]/form/div[6]/div/input')
        submit_button.click()

        time.sleep(1)
        

    def test_employerUserSignup_SuccessfulSignup(self):

        signup = self.firefox_browser.find_element_by_link_text('Sign Up')
        signup.click()

        time.sleep(2)

        username_field = self.firefox_browser.find_element_by_id('id_username')
        email_field = self.firefox_browser.find_element_by_id('id_email')
        first_name_field = self.firefox_browser.find_element_by_id('id_first_name')
        last_name_field = self.firefox_browser.find_element_by_id('id_last_name')
        employer_field = self.firefox_browser.find_element_by_id('id_is_employer')
        password_field = self.firefox_browser.find_element_by_id('id_password1')
        confirmation_password_field = self.firefox_browser.find_element_by_id('id_password2')
        signup_button = self.firefox_browser.find_element_by_xpath('/html/body/div[1]/form/button')


        if username_field.is_displayed():

            username_field.clear()
            username_field.send_keys(self.employer_username)

        time.sleep(2)

        if email_field.is_displayed():

            email_field.clear()
            email_field.send_keys(self.employer_email)

        time.sleep(1)

        if first_name_field.is_displayed():

            first_name_field.clear()
            first_name_field.send_keys(self.employer_first_name) 
        
        time.sleep(1)


        if last_name_field.is_displayed():

            last_name_field.clear()
            last_name_field.send_keys(self.employer_last_name)

        time.sleep(1)

        if employer_field.is_displayed():

            employer_field.click()

        time.sleep(1)

        if password_field.is_displayed():

            password_field.clear()
            password_field.send_keys(self.employer_password)

        time.sleep(1)

        if confirmation_password_field.is_displayed():

            confirmation_password_field.clear()
            confirmation_password_field.send_keys(self.employer_password)

        time.sleep(1)

        signup_button.click()
        
        time.sleep(2)

    def test_employerUserLogin_SuccessfulLogin(self):

        login_link = self.firefox_browser.find_element_by_link_text('Log In')
        login_link.click()

        # time.sleep(2)

        username_field = self.firefox_browser.find_element_by_id('id_username')
        password_field = self.firefox_browser.find_element_by_id('id_password')
        login_button = self.firefox_browser.find_element_by_xpath('/html/body/div[1]/form/button')

        if username_field.is_displayed():

            username_field.clear()
            username_field.send_keys(self.employer_username)
        
        # time.sleep(1)
        
        if password_field.is_displayed():

            password_field.clear()
            password_field.send_keys(self.employer_password)

        # time.sleep(1)

        login_button.click()
        time.sleep(1)

    def test_employerCreateApplication_SuccessfulCreated(self):

        self.test_employerUserLogin_SuccessfulLogin()

        post_job = self.firefox_browser.find_element_by_id('postjob')
        post_job.click()

        time.sleep(1)

        title_textarea = self.firefox_browser.find_element_by_id('id_title')
        description_textarea = self.firefox_browser.find_element_by_id('id_description')
        snippet_textarea = self.firefox_browser.find_element_by_id('id_snippet')
        requirements_textarea = self.firefox_browser.find_element_by_id('id_requirement')
        work_conditions_textarea = self.firefox_browser.find_element_by_id('id_workCondition')
        header_image_button = self.firefox_browser.find_element_by_xpath('//*[@id="id_header_image"]')

        title_textarea.send_keys(self.application_title)
        description_textarea.send_keys(self.application_description)
        snippet_textarea.send_keys(self.application_snippet)
        requirements_textarea.send_keys(self.application_requirements)
        work_conditions_textarea.send_keys(self.application_work_conditions)
        header_image_button.send_keys(self.application_image)

        time.sleep(3)

        create_button = self.firefox_browser.find_element_by_xpath('/html/body/div[1]/div/form/input[2]')
        create_button.click()

        time.sleep(1)

    def test_updateApplication_SuccessfulUpdate(self):

        self.test_employerUserLogin_SuccessfulLogin()

        job_post = self.firefox_browser.find_element_by_link_text(self.application_title)
        job_post.click()

        time.sleep(2)

        update_job_button = self.firefox_browser.find_element_by_xpath('/html/body/div[1]/div/div/button[1]/a')
        update_job_button.click()

        time.sleep(0.5)

        requirement_textarea = self.firefox_browser.find_element_by_id('id_requirement')
        requirement_textarea.clear()

        time.sleep(0.5)

        requirement_textarea.send_keys(self.application_new_requirements)

        time.sleep(0.5)

        update_button = self.firefox_browser.find_element_by_xpath('/html/body/div[1]/form/input[2]')
        update_button.click()

        time.sleep(0.5)

    def test_deleteApplication_SuccessfulDeletion(self):
        
        self.test_employerUserLogin_SuccessfulLogin()

        job_post = self.firefox_browser.find_element_by_link_text(self.application_title)
        job_post.click()

        time.sleep(1)

        delete_button = self.firefox_browser.find_element_by_xpath('/html/body/div[1]/div/div/button[2]/a')
        delete_button.click()

        time.sleep(1)
        


    def test_applicantSignout_SuccessfulSignout(self):

        self.test_applicantUserLogin_SuccessfulLogin()

        time.sleep(1)

        user_link = self.firefox_browser.find_element_by_link_text(self.applicant_first_name + ' ' + self.applicant_last_name)
        user_link.click()

        logout_link = self.firefox_browser.find_element_by_link_text('Log Out')
        logout_link.click()

        time.sleep(1)

    def test_employerSignout_SuccessfulSignout(self):
        self.test_employerUserLogin_SuccessfulLogin()

        time.sleep(1)

        user_link = self.firefox_browser.find_element_by_link_text(self.employer_first_name + ' ' + self.employer_last_name)
        user_link.click()

        logout_link = self.firefox_browser.find_element_by_link_text('Log Out')
        logout_link.click()

        time.sleep(1)

    def test_userProfile(self):

        self.test_applicantUserLogin_SuccessfulLogin()
        time.sleep(1)

        user_link = self.firefox_browser.find_element_by_link_text(self.applicant_first_name + ' ' + self.applicant_last_name)
        user_link.click()
        profile_link = self.firefox_browser.find_element_by_link_text('Profile')
        profile_link.click()

        time.sleep(1)

    def test_updateProfile_updateProfileSuccess(self):

        self.test_userProfile()

        update_button = self.firefox_browser.find_element_by_link_text('Update Profile')
        update_button.click()

        time.sleep(1.5)

        image_button = self.firefox_browser.find_element_by_id('id_image')
        description_textarea = self.firefox_browser.find_element_by_id('id_description')
        cv_button = self.firefox_browser.find_element_by_id('id_cv')

        image_button.send_keys(self.profile_image)
        description_textarea.send_keys(self.profile_description)
        cv_button.send_keys(self.profile_cv)

        time.sleep(2)

        update_button = self.firefox_browser.find_element_by_xpath('/html/body/div[1]/form/input[2]')
        update_button.click()

        time.sleep(1)

