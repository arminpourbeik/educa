from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

from courses.views import CourseListView

urlpatterns = [
    path("", CourseListView.as_view(), name="course_list"),
    path("account/login/", auth_views.LoginView.as_view(), name="login"),
    path("account/logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("admin/", admin.site.urls),
    path("courses/", include("courses.urls")),
    path("students/", include("students.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
