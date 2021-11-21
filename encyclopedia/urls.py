from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("EditPage", views.EditPage, name="EditPage"),
    path("not_found", views.not_found, name="title"),
    # path("<str:name>", views.greet1, name="greet"),
    ## After reading rest of code: Markdown to HTML Conversion
    #path("<str:title>", views.EntryPage, name="EntryPage"),
    #   path("brian", views.brian, name="brian"),
    #path("Search", views.Search, name="Search"),
    #   path("add", views.add, name="add"),
    #path("NewPage"), views.NewPage, name="NewPage"),
    #path("RandomPage", views.RandomPage, name="RandomPage")
]
