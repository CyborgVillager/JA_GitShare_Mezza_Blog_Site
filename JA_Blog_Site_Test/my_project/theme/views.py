from django.shortcuts import render
# Redirection
from django.shortcuts import redirect


# Create your views here.
def blog_post_redirect(request):
    return redirect('/', permanent=True)
