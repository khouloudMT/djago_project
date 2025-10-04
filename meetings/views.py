from django.shortcuts import render

from meetings.models import Meeting

def meeting_list(request):
    meetings = Meeting.objects.all()
    return render(request, 'meetings.html', {'meetings': meetings})