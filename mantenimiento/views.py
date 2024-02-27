from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from datetime import date
from .models import Area


@login_required
def mantenimiento(request):
    return render (request, 'mantenimiento/index.html', {})

@login_required
def area(request):
    return render(request, 'mantenimiento/area.html', {})

@login_required
def area_alerta_mantenimiento(request):
    if request.method == 'POST':
        area_id = request.POST.get('area_id')
        area = Area.objects.get(id=area_id)
        area.fecha_ultimo_mantenimiento = date.today()
        area.save()
        return redirect('area_alerta_mantenimiento')
    areas = Area.objects.filter(nombre__icontains=request.GET.get('search', ''))
    alertas = []
    for area in areas:
        dias_restantes = area.dias_restantes_mantenimiento()
        if dias_restantes <= 1000:
            alertas.append({
                'area': area,
                'dias_restantes': dias_restantes
            })
    alertas_ordenadas = sorted(alertas, key=lambda x: x['dias_restantes'])
    return render(request, 'mantenimiento/area_alerta_mantenimiento.html', {'alertas': alertas_ordenadas})

@login_required
def area_vista_mantenimiento(request):
    areas = Area.objects.filter(nombre__icontains=request.GET.get('search', ''))
    context = {
        'areas': areas
    }
    return render(request, 'mantenimiento/area_vista_mantenimiento.html', context)

#