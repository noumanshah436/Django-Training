from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm

"""
we can access the current 
user's object with ->  request.user and 
its profile with ->   request.user.profile
"""


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to log in')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


"""
instance=request.user   :

to populate the fields of the form by pasing the instance of the object that it expects .

UserUpdateForm   -> pass the instance/object of the user
ProfileUpdateForm -> pass the instance of the profile
"""


@login_required
def profile(request):
    if request.method == 'POST':
        print("request.user :", request.user)
        print("request.user.profile :", request.user.profile)
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,  # to populate/get the updated post data into the fields
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'users/profile.html', context)

# messages.debug
# messages.success
# messages.info
# messages.warning
# messages.error
