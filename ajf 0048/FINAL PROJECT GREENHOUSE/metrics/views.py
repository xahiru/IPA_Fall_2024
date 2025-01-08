from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.db.models import Avg
from rest_framework import viewsets, permissions
from rest_framework.authentication import TokenAuthentication
from django_filters import rest_framework as filters
from .models import GreenHouseMetric
from .serializers import GreenHouseMetricSerializer
from django.core.mail import send_mail
import csv
from django.http import HttpResponse
from rest_framework.decorators import action
import logging

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'metrics/register.html', {'form': form})


logger = logging.getLogger(__name__)

# Function to send alerts based on metric values
def send_alert(metric):
    if metric.temperature > 30:
        send_mail(
            'High Temperature Alert',
            f'Temperature is {metric.temperature}°C',
            'from@example.com',  # Replace with your sender email
            ['to@example.com'],  # Replace with recipient email
            fail_silently=False,
        )
        logger.info(f'Alert sent for high temperature: {metric.temperature}°C')

# Registration view for new users using class-based view
class RegisterView(CreateView):
    form_class = UserCreationForm
    template_name = 'metrics/register.html'
    success_url = reverse_lazy('login')  # Redirect to login page after registration

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, f'Account created for {form.cleaned_data.get("username")}!')
        return response

# Dashboard view to display greenhouse metrics
def dashboard(request):
    metrics = GreenHouseMetric.objects.all()
    
    if not metrics.exists():
        return render(request, 'metrics/dashboard.html', {'error': 'No metrics available.'})

    latest = metrics.last()
    averages = metrics.aggregate(
        avg_temp=Avg('temperature'),
        avg_humidity=Avg('humidity'),
        avg_soil=Avg('soil_moisture')
    )

    context = {
        'metrics': metrics,
        'current_temp': latest.temperature if latest else 0,
        'current_humidity': latest.humidity if latest else 0,
        'current_soil': latest.soil_moisture if latest else 0,
        'avg_temp': round(averages['avg_temp'], 2) if averages['avg_temp'] else 0,
        'avg_humidity': round(averages['avg_humidity'], 2) if averages['avg_humidity'] else 0,
        'avg_soil': round(averages['avg_soil'], 2) if averages['avg_soil'] else 0,
    }
    
    return render(request, 'metrics/dashboard.html', context)

# Filter class for greenhouse metrics
class GreenHouseMetricFilter(filters.FilterSet):
    start_date = filters.DateTimeFilter(field_name="timestamp", lookup_expr="gte")
    end_date = filters.DateTimeFilter(field_name="timestamp", lookup_expr="lte")

    class Meta:
        model = GreenHouseMetric
        fields = ['start_date', 'end_date']

# ViewSet for GreenHouseMetric API
class GreenHouseMetricViewSet(viewsets.ModelViewSet):
    queryset = GreenHouseMetric.objects.all()
    serializer_class = GreenHouseMetricSerializer
    """
    Greenhouse Metrics API
    
    retrieve:
    Return a specific greenhouse measurement.

    list:
    Return a list of all greenhouse measurements.

    create:
    Create a new greenhouse measurement.

    delete:
    Remove an existing greenhouse measurement.

    update:
    Update an existing greenhouse measurement.

    partial_update:
    Update part of an existing greenhouse measurement.
    """
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    queryset = GreenHouseMetric.objects.all()
    serializer_class = GreenHouseMetricSerializer
    filterset_class = GreenHouseMetricFilter

@action(detail=False, methods=['get'])
def export_csv(self, request):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="metrics.csv"'
        
        writer = csv.writer(response)
        writer.writerow(['Timestamp', 'Temperature', 'Humidity', 'Soil Moisture', 'Light Level'])
        
        metrics = self.get_queryset()
        for metric in metrics:
            writer.writerow([
                metric.timestamp,
                metric.temperature,
                metric.humidity,
                metric.soil_moisture,
                metric.light_level
            ])
        
        return response
def dashboard(request):
    metrics = GreenHouseMetric.objects.all()
    
    # Get current and average values
    latest = metrics.last()
    averages = metrics.aggregate(
        avg_temp=Avg('temperature'),
        avg_humidity=Avg('humidity'),
        avg_soil=Avg('soil_moisture')
    )

    context = {
        'metrics': metrics,
        'temperatures': [metric.temperature for metric in metrics],
        'humidity': [metric.humidity for metric in metrics],
        'soil_moisture': [metric.soil_moisture for metric in metrics],
        'timestamps': [metric.timestamp.isoformat() for metric in metrics],
        'current_temp': latest.temperature if latest else 0,
        'current_humidity': latest.humidity if latest else 0,
        'current_soil': latest.soil_moisture if latest else 0,
        'avg_temp': round(averages['avg_temp'], 2) if averages['avg_temp'] else 0,
        'avg_humidity': round(averages['avg_humidity'], 2) if averages['avg_humidity'] else 0,
        'avg_soil': round(averages['avg_soil'], 2) if averages['avg_soil'] else 0,
    }
    
    return render(request, 'metrics/dashboard.html', context)

