from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from bs4 import BeautifulSoup
import requests
from django.conf import settings
import json
from django.template.loader import render_to_string


def search(request):
    if request.method == 'POST':
        search_data = request.POST['name']
        name = '+'.join(search_data.split())
        endurl = 'http://content.guardianapis.com/search?api-key='+settings.API_KEY+'&q='+name+'&show-fields=thumbnail,headline'
        r = requests.get(endurl)
        r = r.json()
        totalResult = len(r['response']['results'])
        data = []
        for i in range(totalResult):
            x = {}
            x['webUrl'] = r['response']['results'][i]['webUrl']
            x['date'] = r['response']['results'][i]['webPublicationDate'][0:10]
            content = requests.get(x['webUrl']).content
            thumbnail = BeautifulSoup(content,'html.parser').find('img', {'class':'maxed responsive-img'})
            if thumbnail != None:
                x['thumbnail'] = thumbnail['src']
            else:
                x['thumbnail'] = None
            x['headline'] = BeautifulSoup(content,'html.parser').find('h1', {'class':"content__headline"}).get_text()
            data.append(x)
        return render(request, 'GuardianAPI/index.html', {'guardian_data':data,'search_data':search_data})
    if request.is_ajax():
        print(request.GET['search_text'])
        url = 'http://suggestqueries.google.com/complete/search'
        params = {
            'client': 'firefox',
            'q': request.GET['search_text'],
            'hl':'en'
            }
        r = requests.get(url, params=params)
        suggesions = r.json()[1]
        return HttpResponse(json.dumps({'suggesions':suggesions}), content_type='application/json')
    else:
        suggesions=[]
    return render(request, 'GuardianAPI/NewsLister.html', {'suggesions':suggesions})


