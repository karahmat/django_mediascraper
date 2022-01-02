from django.urls import path
from aggregrator.views import scrape_view, news_list

app_name = "aggregrator"

urlpatterns = [  
#   path('scrape/', scrape_result, name="scrape"),  
  path('', scrape_view, name="search"),
  path('result/<int:id>', news_list, name="result")

]