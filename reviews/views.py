from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from .forms import ReviewForm

# Create your views here.
def review(request):
    if request.method == "POST":
        form = ReviewForm(request.POST)
        # entered_username = request.POST['username']

        if form.is_valid():
            print(form.cleaned_data)
            return redirect("thank-you")
    else:    
        form = ReviewForm()    
    return render(request,"reviews/review.html",{
        "form":form
    })

def thank_you(request):
    return render(request,"reviews/thank_you.html")