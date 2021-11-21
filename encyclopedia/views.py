from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.contrib import messages
import markdown

from . import util

def entry():
    pass

def new_entry():
    pass

def edit_entry():
    pass

def overview_entries(request):
    entries = util.list_entries()
    return render(request, 'encyclopedia/entries.html', { 'entries': entries})
    # pass
    
def view_entry(request, entry_name):
    if not entry_name in util.list_entries():
        # Maybe run this in custom 404 page later? or not_found
        return HttpResponseNotFound("Could not find an entry for that")    
        
    entry_content = util.get_entry(entry_name)    
    html_content = markdown.markdown(entry_content)    
    return render(request, "encyclopedia/entry.html", {'name': entry_name, 'content': html_content })

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

# Use functions given in util.py
# util.list_entries, util.save_entry, util.get_entry
# all fucntions get request argument (Not title, content)
def CreateNew(request):
    gottenEntry = util.get_entry()
    SaveEntry = util.save_entry()
    #on SaveEntry:
    if gottenEntry == title:
        messages.warning(request, "This entry already exists!")
    #else
    # SaveEntry
    
    
 # 404
 # view function to display a single post
 # def post_detail example(request, primary key)
# def not_found(request, pk):
def not_found(title):
    try:
        #You could pk=model2_id if you want to join sql in django?
        # post = Post.objects.get(pk=pk)
        util.get_entry(title)
    #except Post.DoesNotExist:
    except title.DoesNotExist:    
    # This part of the code I need as is.
        return HttpResponseNotFound("Entry not found")
    #return render(request, 'blog/post_detail.html', {'post': post}) 
    # is this the correct indendation? Check in /src
    return render(title, '/wiki/not_found.html', {'title':"title"})

