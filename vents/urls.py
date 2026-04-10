from django.urls import path
from . import views
app_name = 'vents'

urlpatterns = [
    path('submit_vent', view=views.submit_vent, name='submit_vent'),
]
