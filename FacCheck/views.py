from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User

# from tweet.models import Tweet


def home(request):
    # context = {
    #     'tweets': Tweet.objects.all().order_by('-when_created')
    # }
    return render(request, 'homepage.html')


# def profile(request, username):
#     user = get_object_or_404(User, username=username)
#     context = {
#         'user': user,
#         'tweets': user.tweets.all().order_by('-when_created')
#     }
#     return render(request, 'profile.html', context=context)
