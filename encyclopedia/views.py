from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from django.contrib import messages

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

# Use functions given in util.py
# util.list_entries, util.save_entry, util.get_entry
def EditPage(title, content):
    gottenEntry = util.get_entry()
    SaveEntry = util.save_entry()
    #on SaveEntry:
    if gottenEntry == title:
        messages.warning(request, "This entry already exists!")
    
 
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

