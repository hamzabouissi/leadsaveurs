from django.urls import path

from leadsaveurs.searcher.views import HomeSearchView


app_name = "searcher"

urlpatterns = [
    path("homesearch",HomeSearchView.as_view(), name="homesearch")
]
