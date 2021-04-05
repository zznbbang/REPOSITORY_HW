import requests
from bs4 import BeautifulSoup
import csv

file = open('movie.csv', mode='w', newline='')
writer = csv.writer(file)
writer.writerow(["title","star","director","actor","date","img_src"])

MOVIE_URL = 'https://movie.naver.com/movie/running/current.nhn'
movie_html = requests.get(MOVIE_URL)
movie_soup = BeautifulSoup(movie_html.text,"html.parser")

movie_list_box = movie_soup.find("ul", {"class" : "lst_detail_t1"})
movie_list = movie_list_box.find_all('li')

final_result = []
for movie in movie_list:
    title = movie.find("dt", {"class" : "tit"}).find("a").text
    star = movie.find("dd",{"class":"star"}).find("div",{"class":"star_t1"}).find("a").find("span",{"class":"num"}).text
    detail = movie.find("dl",{"class":"info_txt1"})
    detail_list = detail.find_all('dd')
    director = detail_list[1].find("span",{"class":"link_txt"}).find("a").text
    date_source = detail_list[0].text
    date_replace = date_source.replace("\r",'').replace("\t",'').replace("\n",'')
    date_split = date_replace.split('|')
    date = date_split[2].replace(" 개봉",'')
    if(len(detail_list)==3):
        actor=detail_list[2].text.replace("\r",'').replace("\t",'').replace("\n",'')
    else:
        actor='None'
        img_src = movie.find("div", {"class" : "thumb"}).find("img")['src']
    movie_info = {
        'title' : title,
        'star' : star,
        'director' : director,
        'actor' : actor,
        'date' : date,
        'img_src' : img_src
        }
    final_result.append(movie_info)

for result in final_result:
    row = []
    row.append(result['title'])
    row.append(result['star'])
    row.append(result['director'])
    row.append(result['actor'])
    row.append(result['date'])
    row.append(result['img_src'])
    writer.writerow(row)
print(final_result)