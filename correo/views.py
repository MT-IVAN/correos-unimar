from django.shortcuts import render
from django.core.mail import EmailMessage
from django.core.mail import send_mail

from .forms import FormularioForm
# Create your views here.
def index(request):
	form = FormularioForm
	if request.method == "POST":
		form = FormularioForm
		correo = None
		nombre = request.POST.get('nombre')
		asunto = request.POST.get('asunto')
		correo = request.POST.get('correo')
		mensaje = request.POST.get('mensaje')

		send_mail(asunto, nombre + '. Correo de contacto '+ correo + '\n'+ mensaje , 'emuad316@gmail.com', ['emuand316@gmail.com'], fail_silently=False)
		correo = "Enviado"
	else:
		correo = None
	return render(request, 'index.html',{'form':form})

