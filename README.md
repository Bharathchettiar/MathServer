# Ex.03 Design a Website for Server Side Processing
## Date:21-11-2026

## AIM:
To create a web page to calculate Churn Rate using server-side scripts.

## FORMULA:
Churn Rate = (CustLost / InitCust) * 100
<br> InitCust --> Initial Customers Count
<br> CustLost --> Customers Lost Count

## DESIGN STEPS:

### Step 1:
Clone the repository from GitHub.

### Step 2:
Create Django Admin project.

### Step 3:
Create a New App under the Django Admin project.

### Step 4:
Create a HTML file to implement form based input and output.

### Step 5:
Create python programs for views and urls to perform server side processing.

### Step 6:
Receive input values from the form using request.POST.get().

### Step 7:
Calculate the Result using the given formula.

### Step 8:
Display the calculated result in the server console.

### Step 9:
Render the result to the HTML template.

### Step 10:
Publish the website in Localhost.

## PROGRAM:
```
views.py

from django.shortcuts import render
def gst_bill(request):
    v = float(request.POST.get('initial customers', '0'))
    s = float(request.POST.get('present customers', '0'))
    bill = v + (v * s / 100) if request.method == 'POST' else 0
    print("initial customers =",v)
    print("present customers =",s)
    print("churn rate =",bill)
    return render(request, 'bharathapp/gst.html',{'v': v, 's': s, 'bill': bill})

urls.py      

from django.contrib import admin
from django.urls import path
from bharathapp import views

urlpatterns = [path('', views.gst_bill, name='gst_bill'),]


<html>
    <head><title>calculator</title></head>
    <body>
        <h1 align="center"> Bharath (26000788)</h1>
        <form method="POST">
            {% csrf_token %}
            <label for="present-cust">Present customers</label>
            <input id="present-cust" type="number" name="PresentCust" min="0" step="1" value="{{ PresentCust }}" required><br><br>
            <label for="initial-cust">Initial customers</label>
            <input id="initial-cust" type="number" name="initialCust" min="1" step="1" value="{{ initialCust }}" required><br><br>
            <button type="submit">Calculate</button>
        </form>
    </body>
</html>
```

## OUTPUT - SERVER SIDE:
![alt text](<Screenshot 2026-11-24 071449.png>)

## OUTPUT - WEBPAGE:
![alt text](<Screenshot 2026-11-24 071434.png>)

## RESULT:
The the web page to calculate Churn Rate using server-side scripts is created successfully.
