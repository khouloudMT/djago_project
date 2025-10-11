from django.shortcuts import get_object_or_404, redirect, render

from meetings.forms import MeetingForm
from meetings.models import Meeting

def meeting_list(request):
    meetings = Meeting.objects.all()
    return render(request, 'meetings.html', {'meetings': meetings})

def detail(request, id):
    meeting = get_object_or_404(Meeting, id=id)
    return render(request, 'detail.html', {'meeting': meeting})

def deletemeeting(request, id):
    meeting = get_object_or_404(Meeting, id=id)
    if request.method == 'POST':
        meeting.delete()
        return redirect('meetings')
    return render(request, 'confirm_delete.html', {'meeting': meeting})

def addmeeting(request):
    if request.method == 'POST':
        form = MeetingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('meetings')
    else:
        form = MeetingForm()
    return render(request, 'add_meeting.html', {'form': form})
