from django.urls import path
from . import views

urlpatterns = [
    path("",views.ReviewView.as_view()),
    path("thank-you",views.ThankyouView.as_view(),name="review_name"),
    path("reviews",views.ReviewsListView.as_view()),
    path("reviews/favorite",views.AddFavoriteView.as_view()),
    path("reviews/<int:pk>",views.SingleReviewView.as_view())
]