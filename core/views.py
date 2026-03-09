from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import json
from .models import Event
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def create_event(request):
    if request.method == "POST":
        data = json.loads(request.body)
        event = Event.objects.create(
            name=data.get("name"),
            description=data.get("description"),
            location=data.get("location"),
            start_date=data.get("start_date"),
            end_date=data.get("end_date"),
            created_at=data.get("created_at"),
            updated_at=data.get("updated_at")
        )
        return JsonResponse({"message": "Event created successfully", 
                             "id": event.id
                             }, status=201)
    else:
        return HttpResponse("Method not allowed",status=405)

def update_event():
    pass

def get_all_events(request):
    if request.method == "GET":
        events = Event.objects.all()
        event_list=[]
        for event in events:
            event_list.append({
                "id": event.id,
                "name": event.name,
                "description": event.description,
                "location": event.location,
                "start_date": event.start_date,
                "end_date": event.end_date,
                "created_at": event.created_at,
                "updated_at": event.updated_at
            })
        return JsonResponse(event_list,safe=False)
    else:
        return HttpResponse("Method not allowed",status=405)

def get_event():
    pass

def delete_event():
    pass

def homepage(request):
    return HttpResponse("Welcome to the Homepage!")

def about(request):
    return HttpResponse("Welcome to the about page!")