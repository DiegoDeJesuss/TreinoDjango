from django.shortcuts import render

def horarios(request):
    contexto = {
        'title': 'Horários'
    }

    return render(
        request,
        'horarios/horarios.html',
        contexto
    )

# Create your views here.
