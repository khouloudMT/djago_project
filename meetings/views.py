from django.shortcuts import get_object_or_404, render

from meetings.models import Meeting

def meeting_list(request):
    meetings = Meeting.objects.all()
    return render(request, 'meetings.html', {'meetings': meetings})

def detail(request, id):
    meeting = get_object_or_404(Meeting, id=id)
    return render(request, 'detail.html', {'meeting': meeting})