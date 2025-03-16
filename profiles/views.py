from django.shortcuts import render
from django.views import View

# Create your views here.
class CreateProfileVieew(View):
    def get(self,request):
        return render(request,"profiles/create_profile.html")
    def post(self,request):
        pass
