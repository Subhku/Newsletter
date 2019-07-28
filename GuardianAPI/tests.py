# # from django.test import TestCase
import requests, sys, bs4
# #
# # r = requests.get('http://content.guardianapis.com/search?api-key=test&q=modi&show-%20fields=thumbnail,headline')
# #
# # r = r.json()
# # print(r['response']['results'][0]['id'])
#
# from bs4 import BeautifulSoup
# import requests
# #url = 'https://www.theguardian.com/world/2019/jul/23/india-denies-asking-for-donald-trumps-mediation-in-kashmir'
# url = 'https://google.com/search?q='+''+'modi'
#
# r = requests.get(url)
#
# #soup = BeautifulSoup(r.content,'html.parser')
# # print(soup.prettify())
# #image = soup.find('img', {'class':'maxed responsive-img'})
# #headline = soup.find('h1', {'class':"content__headline"})
# #print(image['src'])
# #print(headline.get_text())
#
# soup= bs4.BeautifulSoup(r.text, "html.parser")
# print(soup.prettify)
url = 'http://suggestqueries.google.com/complete/search'
params = {
    'client': 'firefox',
    'q': 'ind',
    'hl': 'en'
}
r = requests.get(url, params=params)
suggesions = r.json()
print(suggesions)
print(type(suggesions))