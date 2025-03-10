from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from .forms import ReviewForm
from .models import Review
from django.views.decorators.csrf import csrf_protect

# Create your views here.
@csrf_protect
def review(request):
    if request.method == "POST":
        form = ReviewForm(request.POST)
        # entered_username = request.POST['username']

        if form.is_valid():
            review = Review(
                user_name=form.cleaned_data['user_name'],
                review=form.cleaned_data['review_text'],
                rating=form.cleaned_data['rating'])
            review.save()    
            return HttpResponseRedirect("/thank-you")
    else:    
        form = ReviewForm()    
    return render(request,"reviews/review.html",{
        "form":form
    })

def thank_you(request):
    return render(request,"reviews/thank_you.html")