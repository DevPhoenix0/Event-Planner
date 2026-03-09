from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import json
from .models import Event
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def create_event(request):
    if request.method == "POST":
        events = json.loads(request.body)
        event = Event.objects.create(
            name=events.get("name"),
            description=events.get("description"),
            location=events.get("location"),
            start_date=events.get("start_date"),
            end_date=events.get("end_date"),
            created_at=events.get("created_at"),
            updated_at=events.get("updated_at")
        )
        return JsonResponse({"message": "Event created successfully", 
                             "id": event.id
                             }, status=201)
    else:
        return HttpResponse("Method not allowed",status=405)

def update_event(request,id):
    if request.method == "PATCH":
        events = Event.objects.get(id=id)
        events.name = request.data.get("name", events.name)
        events.description = request.data.get("description", events.description)
        events.location = request.data.get("location", events.location)
        events.start_date = request.data.get("start_date", events.start_date)
        events.end_date = request.data.get("end_date", events.end_date)
        events.created_at = request.data.get("created_at", events.created_at)
        events.updated_at = request.data.get("updated_at", events.updated_at)
        events.save()
        return JsonResponse({"message": "Event updated successfully"}, status=200)
    else:
        return HttpResponse("Method not allowed",status=405)

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

def get_event(request,id):
    if request.method == "GET":
        events = Event.objects.get(id=id)
        return JsonResponse({
                    "id": events.id,
                    "name": events.name,
                    "description": events.description,
                    "location": events.location,
                    "start_date": events.start_date,
                    "end_date": events.end_date,
                    "created_at": events.created_at,
                    "updated_at": events.updated_at
                })

def delete_event(request,id):
    if request.method == "DELETE":
        events = Event.objects.get(pk=id)
        events.delete()
        return JsonResponse({"message": "Event deleted successfully"}, status=200)
    else:
        return HttpResponse("Method not allowed",status=405)

def homepage(request):
    return HttpResponse("Welcome to the Homepage!")

def about(request):
    return HttpResponse("Welcome to the about page!")