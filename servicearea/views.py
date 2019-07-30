import json

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView
from rest_framework import viewsets, status
from rest_framework.response import Response

from servicearea.models import ServiceArea
from suppliers.models import Provider


class AddServiceAreaView(TemplateView):
    template_name = "servicearea/partials/add.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['providers'] = Provider.objects.all()
        return context


class ServiceAreaViewSet(viewsets.ViewSet):
    @csrf_exempt
    def create(self, request):
        # Should be done via validators/forms but doing it manually because of time crunch
        # Assuming all data is correct
        request_body = json.loads(request.body)
        service_area = ServiceArea()
        service_area.name = request_body.get("name")
        service_area.provider_id = request_body.get("provider")
        service_area.price = request_body.get("price")
        print(request_body.get("serviceAreaString"))
        polygon = request_body.get("serviceAreaString")
        polygon = polygon + ", " + polygon.split(',')[0]
        print(polygon)
        service_area.polygon = "POLYGON(({polygon}))".format(polygon=polygon)
        service_area.save()
        return Response({"status": "success"}, status=status.HTTP_201_CREATED)


def query(request):
    service_areas = ServiceArea.objects.filter(
        polygon__contains='POINT({longitude} {latitude})'.format(longitude=request.GET['lon'],
                                                                 latitude=request.GET['lat'])
    ).all()
    return HttpResponse(
        {
            'service_areas': service_areas
        }, content_type='application/json')
