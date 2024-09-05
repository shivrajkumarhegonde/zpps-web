
from django.contrib import admin
from django.conf.urls import url
from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('i18n/', include('django.conf.urls.i18n')),
    path('', include('homescreen.urls')),
    path('about_school/', include('about_school.urls')),
    path('announcements/', include('announcements.urls')),
    path('contact_us/', include('contact_us.urls')),
    #path('zpps_faculty/', include('zpps_faculty.urls')),
    path('facilities/', include('facilities.urls')),
    path('activities/', include('activities.urls')),
    path('achievements/', include('achievements.urls')),
    path('student_database/', include('student_database.urls')),
    #path('blogs/', include('blogs.urls')),
    path('login/', include('login.urls')),
    path('faculty/', include('zpps_faculty.urls')),
    path('internal/', include('internal.urls')),
    path('users/', include('users.urls')),  # Include users app URLs
    #path('mdm/', include('mdm.urls')),
    path('mdm2/', include('mdm2.urls')),
]


# Serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Internationalized patterns
urlpatterns += i18n_patterns(
    path('', include('contact_us.urls')),  # Default language URL
    # Add other patterns here for internationalization
)



















# from django.contrib import admin
# from django.conf.urls.i18n import i18n_patterns
# from django.urls import path, include
#
# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('i18n/', include('django.conf.urls.i18n')),
#     path('', include('homescreen.urls')),
#     path('about_school/', include('about_school.urls')),
#     path('announcements/', include('announcements.urls')),
#     #path('about_us/about_us', include('about_us.urls')),
#     path('contact_us/', include('contact_us.urls')),
#     # path('faculty/', include('faculty.urls')),
#     path('zpps_faculty/', include('zpps_faculty.urls')),
#     path('facilities/', include('facilities.urls')),
#     path('activities/', include('activities.urls')),
#     path('achievements/', include('achievements.urls')),
#     path('student_database/', include('student_database.urls')),
#     path('blogs/', include('blogs.urls')),
# ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# ]
# urlpatterns += i18n_patterns(
#     path('', include('contact_us.urls')),
#     # Add other patterns here
# )