'''from django.contrib import admin
from django.urls import path
from bharathapp import views

urlpatterns=[
    path('admin/', admin.site.urls),
    path('',views.calculate_area,name='churnrate'),
]

#Calculate Churn Rate
churn=(PresentCust/initialCust)*100'''

from django.contrib import admin
from django.urls import path
from bharathapp import views

urlpatterns = [path('', views.gst_bill, name='gst_bill'),]