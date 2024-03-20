"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.contrib.auth.decorators import user_passes_test
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from contactapp.views import *
from app1.views import *
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from productApp.views import create_products, update_product, CreateOrganization, get_product_details, products,delete_products


# Define a custom test for superuser check
'''def is_superuser(user):
    return user.is_authenticated and user.is_superuser'''
def is_user(user):
    return user.is_authenticated
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', products, name='product'),
    path('about-us/', AboutusPage, name='about-us'),  # Make sure to add a trailing slash for consistency

    path('signup/', SignupPage, name='signup'),  # Make sure to add a trailing slash for consistency
    path('login/', LoginPage, name='login'),    # Make sure to add a trailing slash for consistency
    path('logout/', LogoutPage, name='logout'),
    path('get-product-details/<int:product_id>/',get_product_details, name='get-product-details'),
    path('delete-product/<int:product_id>/',delete_products, name="delete-product"),

    path('contact-us/', CreateMessage, name='contact-us'),
    path('organization-form/', CreateOrganization, name='organization-form'),


    path('create-product/', create_products, name='create-product'),
    path('update-product/<id>/', user_passes_test(is_user)(update_product), name='update_product'),

    # Apply the user_passes_test decorator to restrict access to superusers only
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()