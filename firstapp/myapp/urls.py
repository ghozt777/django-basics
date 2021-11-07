from django.urls import path
from . import views


urlpatterns = [
    path('myapp/' , views.index) # domain/com/myapp : Don't invoke the function just point it django will call it 

]   