from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from mentorados.models import Mentorados, Navigators
from django.contrib import messages
from django.contrib.messages import constants

def mentorados(request):
    if not request.user.is_authenticated:
        return redirect ('login')
    if request.method == 'GET':
        navigators = Navigators.objects.filter(user = request.user)
        return render(request, 'mentorados.html', {'estagios': Mentorados.estagio_choice, 'navigators': navigators})
    elif request.method == 'POST':
        nome = request.POST.get('nome')
        foto = request.FILES.get('foto')
        estagio = request.POST.get("estagio")
        navigator = request.POST.get('navigator')

        mentorado = Mentorados(
            nome = nome,
            estagio = estagio,
            foto = foto,
            navigator_id = navigator,
            user = request.user
        )

        mentorado.save()

        messages.add_message(request, constants.SUCCESS, 'Mentorado, cadastrado com sucesso!')
        return redirect('mentorados')
