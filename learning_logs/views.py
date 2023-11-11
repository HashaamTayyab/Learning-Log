from django.shortcuts import render, redirect

from .models import Topic, Entry
from .forms import TopicForm, EntryForm
# Create your views here.
def index(request):
    return render(request, 'learning_logs/index.html')

def topics(request):
    """Shows all Topics in the database."""
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)

def topic(request, topic_id):
    """Show a single topic and all its entries."""
    topic = Topic.objects.get(pk = topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries' : entries}
    return render(request, 'learning_logs/topic.html', context)

def new_topic(request):
    if request.method != 'POST':
        # No data submitted just return the form.
        form = TopicForm()
    else:
        # POST request, processing data and storing it.
        form = TopicForm(data= request.POST)
        if form.is_valid():
            form.save()
            return redirect('learning_logs:topics')
    context = {'form': form}
    return render(request, 'learning_logs/new_topic.html', context)

def new_entry(request, topic_id):
    topic = Topic.objects.get(pk = topic_id)
    
    if request.method != 'POST':
        form = EntryForm()
    else:
        if form.is_valid():
            form = EntryForm(data= request.POST)
            new_entry = form.save(commit= False)
            new_entry.topic = topic
            new_entry.save()
            return redirect('learning_logs:topic', topic_id = topic.id)
    
    context = {'topic': topic, 'form' : form}
    return render(request, 'learning_logs/new_entry.html', context)

def edit_entry(request, entry_id):
    entry = Entry.objects.get(pk = entry_id)
    topic = entry.topic
    if request.method != 'POST':
        form = EntryForm(instance= entry)
    else:
        form = EntryForm(instance= entry, data= request.POST)
        if form.is_valid():
            form.save()
            return redirect('learning_logs:topic', topic_id = topic.id)
        
    context = {'entry': entry, 'form' : form, 'topic': topic}
    return render(request, 'learning_logs/edit_entry.html', context)