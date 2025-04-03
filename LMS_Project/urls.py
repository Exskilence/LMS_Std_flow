"""LMS_Project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Student_Flow_App import views ,tests ,coding_validation as cv ,AppUsage,StudentProfile as profile
from Student_Flow_App import StudentDashBoard as dashboard ,StudentLiveSessions as live_session ,LearningModules as learning_modules
from Student_Flow_App import Student_Tickets as tickets , StudentRoadMap as roadmap , StudentTestDetails as test_details
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('api/clearcache/', AppUsage.clear_blob_ceche),
    # Login URLs
    path('api/login/<str:email>/', views.LogIn),
    path('api/logout/<str:student_id>/', views.LogOut),
    # Dashboard URLs
    path('api/studentdashboard/mycourses/<str:student_id>/',       dashboard.fetch_enrolled_subjects),
    path('api/studentdashboard/upcomming/sessions/<str:student_id>/',      dashboard.fetch_live_session),
    path('api/studentdashboard/upcomming/events/<str:Course_id>/',       dashboard.fetch_upcoming_events),
    path('api/studentdashboard/weeklyprogress/<str:student_id>/',       dashboard.get_weekly_progress),
    path('api/studentdashboard/hourspent/<str:student_id>/<str:week>/',       dashboard.fetch_study_hours),
    path('api/studentdashboard/summary/<str:student_id>/',       dashboard.fetch_student_summary),
    path('api/studentdashboard/event/calender/<str:student_id>/',       dashboard.fetch_calendar),
    
    # top navigation and roadmap URLs
    path('api/notifications/<str:student_id>/',       roadmap.fetch_top_navigation),
    path('api/roadmap/<str:student_id>/<str:course_id>/<str:subject_id>/',       roadmap.fetch_roadmap),

    # learning modules URLs
    path('api/student/learningmodules/<str:student_id>/<str:subject>/<str:day_number>/',       learning_modules.fetch_learning_modules),
    path('api/student/lessonoverview/<str:student_id>/<str:subject>/<str:day_number>/',       learning_modules.fetch_overview_modules),
    path('api/student/practice<str:type>/<str:student_id>/<str:subject>/<str:subject_id>/<str:day_number>/<str:week_number>/<str:subTopic>/',       learning_modules.fetch_questions),
    path('api/student/add/days/', learning_modules.add_days_to_student),
    path('api/student/practicemcq/submit/', learning_modules.submit_MCQ_Question),
    path('api/student/practicecoding/tables/', learning_modules.get_SQL_tables),
    
    # coding Validation URLs
    path('api/student/coding/py/',    cv.run_python),
    path('api/student/coding/ds/', cv.run_pythonDSA),
    path('api/student/coding/sql/', cv.sql_query),
    path('api/student/coding/', learning_modules.submition_coding_question),

    # Live Session URLs
    path('api/student/sessions/<str:student_id>/', live_session.fetch_all_live_session),

    # TEST Details URLs
    path('api/student/testdetails/<str:student_id>/', test_details.fetch_all_test_details),
    
    # Teckets URLs
    path('api/student/tickets/', tickets.submit_Tickets),
    path('api/student/tickets/<str:student_id>/', tickets.fetch_all_tickets),
    path('api/student/ticket/comments/', tickets.student_side_comments_for_tickets),

    # FAQ URLs
    path('api/student/faq/',views.fetch_FAQ),

    # Profile URLs
    path('api/student/profile/<str:student_id>/', profile.fetch_student_Profile),
    path('api/student/profile/', profile.update_profile),

    # TESTING URLS
    path('addstudent/',      tests.addStudent),
    path('addstudentactivity/<str:day>/<str:week>/',      tests.addStudetsActivity),
    path('addlivesession/',  tests.addLiveSession),
    path('addappusage/',     tests.addstudent_app_usages),
    path('addsubplan/',   tests.add_course_plane_details),
    path('addnotification/',   tests.add_notification),
    path('addstudentinfo/',   tests.update_student_info),
    path('addparticipants/',   tests.add_participants),
    path('addtestdetails/',   tests.add_test_sction),
    # path('ids/',   views.generate_ids),
]

