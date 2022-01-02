from django.shortcuts import redirect, render
from .scraper.Scrape import Scrape
from .build_wordcloud.build_wc import Build_WC
from .models import Headline, Search
from datetime import datetime
from .forms import SearchForm
from django.contrib.auth.decorators import login_required
from dotenv import load_dotenv
import os
load_dotenv(os.path.join(os.path.dirname(__file__), '..', 'aggrenews_project', '.env'))

# Create your views here.

@login_required(login_url="account/login/")
def scrape_view(request):

    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = SearchForm(request.POST)
        # check whether it's valid
        if form.is_valid():
            wc_text = []
            search_indonesian = form.cleaned_data['search_indonesian']
            search_english = form.cleaned_data['search_english']
            result = Scrape.scrape(search_indonesian)
            Headline.objects.filter(requestor=request.user.id).delete()
            print(request.user.username)
            for media in result.keys():
                for index, article_title in enumerate(result[media]['title']):            
                            
                    if (result[media]['date'][index] != ""):                        
                        date_time_obj = datetime.strptime(result[media]['date'][index], '%Y-%m-%d')
                    else:                        
                        date_time_obj = datetime.strptime('1970-01-01', '%Y-%m-%d')
                    
                    Headline.objects.create(
                        title = article_title,
                        media_name = result[media]['name'][index],
                        date = date_time_obj,
                        image = result[media]['imgSrc'][index],
                        link = result[media]['link'][index],
                        bodytext = result[media]['body'][index],     
                        requestor = request.user                   
                    )
                         
            return redirect('/result/' + str(request.user.id))

    elif request.method == 'GET':
        print('here is called')
        form = SearchForm()
        return render(request, 'home/home.html', {'form': form})

def news_list(request, id):
    headlines = Headline.objects.filter(requestor=id).order_by('-date')
    cloudinary_params = {
        'CLOUDINARY_NAME': os.getenv('CLOUDINARY_NAME'),
        'CLOUDINARY_API_KEY':  os.getenv('CLOUDINARY_API_KEY'),
        'CLOUDINARY_API_SECRET':  os.getenv('CLOUDINARY_API_SECRET')
    }
    
    wc_text = []
    for headline in headlines:
        wc_text.append(headline.bodytext)
    result_url = Build_WC.build_wc(wc_text, cloudinary_params)       
    context = {
        'object_list': headlines,
        'url': result_url
    }
    return render(request, 'result/result.html', context)