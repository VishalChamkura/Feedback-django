from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from .forms import ReviewForm
from .models import Review
from django.views.decorators.csrf import csrf_protect
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic import ListView,DetailView
from django.views.generic.edit import FormView,CreateView

# Create your views here.
class ReviewView(CreateView):
    model = Review
    form_class = ReviewForm
    template_name = "reviews/review.html"
    success_url = "/thank-you"

    # def form_valid(self, form):
    #     form.save()
    #     return super().form_valid(form)
    

    # @csrf_protect
    # def get(self,request):
    #     form = ReviewForm()
    #     return render(request,"reviews/review.html",{
    #     "form":form
    # })

    # # @csrf_protect
    # def post(self,request):
    #     form = ReviewForm(request.POST)
    #     # entered_username = request.POST['username']

    #     if form.is_valid():
    #         # review = Review(
    #         #     user_name=form.cleaned_data['user_name'],
    #         #     review=form.cleaned_data['review_text'],
    #         #     rating=form.cleaned_data['rating'])
    #         form.save()    
    #         return HttpResponseRedirect("/thank-you")
    #     return render(request,"reviews/review.html",{
    #     "form":form
    #     })        






# def review(request):
#     if request.method == "POST":
#         form = ReviewForm(request.POST)
#         # entered_username = request.POST['username']

#         if form.is_valid():
#             # review = Review(
#             #     user_name=form.cleaned_data['user_name'],
#             #     review=form.cleaned_data['review_text'],
#             #     rating=form.cleaned_data['rating'])
#             review.save()    
#             return HttpResponseRedirect("/thank-you")
#     else:    
#         form = ReviewForm()    
#     return render(request,"reviews/review.html",{
#         "form":form
#     })








class ThankyouView(TemplateView):
    template_name = "reviews/thank_you.html"

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context["massage"] = "This works"
        return context
    
class ReviewsListView(ListView):
    template_name = "reviews/review_list.html"
    model = Review
    context_object_name = "reviews"

    # def get_queryset(self):
        # base_query = super().get_queryset()
        # data = base_query.filter(rating__gt=4)


    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     reviews = Review.objects.all()
    #     context['reviews'] = reviews
    #     return context
    

class SingleReviewView(DetailView):
    template_name = "reviews/single_review.html"    
    model = Review
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     review_id = kwargs["id"]
    #     selected_review = Review.objects.get(pk=review_id)
    #     context["review"] = selected_review
    #     return context