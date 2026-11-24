from django.shortcuts import render

def gst_bill(request):
    context = {
        "PresentCust": "",
        "initialCust": "",
        "has_result": False,
        "error": "",
    }

    if request.method == "POST":
        context["PresentCust"] = request.POST.get("PresentCust", "").strip()
        context["initialCust"] = request.POST.get("initialCust", "").strip()

        try:
            present_cust = int(context["PresentCust"])
            initial_cust = int(context["initialCust"])
        except ValueError:
            context["error"] = "Enter whole numbers for both customer counts."
        else:
            if present_cust < 0:
                context["error"] = "Present customers cannot be negative."
            elif initial_cust <= 0:
                context["error"] = "Initial customers must be greater than zero."
            else:
                bill = present_cust * 100 / initial_cust
                context["bill"] = bill
                context["has_result"] = True
                print("PresentCust =", present_cust, flush=True)
                print("initialCust =", initial_cust, flush=True)
                print("Churn Rate =", bill, flush=True)

    return render(request, "bharathapp/math.html", context)