from django.shortcuts import render


def local(request):
    contexto = {
        'title' : 'Local'
    }

    return render(
        request,
        'local/local.html',
        contexto
    )




