from django.shortcuts import render, redirect
from .forms import RegistrForm
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
 
def register(request):
	if request.method == "POST":
		form = RegistrForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			email = form.cleaned_data.get('email')
			messages.success(request, f'You are registered now, {username}!')
			send_mail(
				'You have successfully registered on Steam. <no-reply>',
				f'Hi, {username}.\nThank you for register on Steam. \n\nWe remind you, that you have chosen username {username}. You can edit any information in your own profile.\n\nSee ya.',
				settings.EMAIL_HOST_USER,
				[f'{email}'],
				fail_silently=False,
			)
			return redirect('/')
	else:
		form = RegistrForm()
	return render(request, 'users/register.html', {'form': form})