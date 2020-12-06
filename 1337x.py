from bs4 import BeautifulSoup as bs4
import requests

names = []
pages = []
sizes = []
links = []
magnets = []
seeders = []
leachers = []
headers = {
    'User-Agent': 'Mozilla/5.0'
}
base_url = "https://1337x.to/"
pages_to_scrape = 1
movie_name = "ludo"


def linkSearch():
    for i in range(1, pages_to_scrape+1):
        url = (f"https://1337x.to/search/{movie_name}/{i}/")
        # url = ("https://1337x.to/search/{}/1/").format(movie_name)
        pages.append(url)

    for movies in pages:
        page = requests.get(movies, headers=headers)
        # print(page)
        soup = bs4(page.text, 'html.parser')
        # print(soup.prettify)
        # print("soup", soup.prettify())

        for i in soup.find_all('td', class_="coll-4 size mob-uploader"):
            size = i.getText()
            sizes.append(size)
            # print(sizes)

        for j in soup.find_all('td', class_="coll-1 name"):
            name = j.getText()
            names.append(name)
            # print(names)

        for k in soup.find_all('td', class_="coll-2 seeds"):
            seeds = k.getText()
            seeders.append(seeds)
            # print(seeders)

        for l in soup.find_all('td', class_="coll-3 leeches"):
            leach = l.getText()
            leachers.append(leach)
            # print(leachers)

        movielink = soup.find_all('td', class_="coll-1 name")
        for n in movielink:
            link_ = n.find_all('a')[1].get('href')
            # print(link_[0])
            # link_[0] = " "#string cannot be edited
            # therefore changing them into list and assigning to another variable
            new_link_list = list(link_)
            new_link_list[0] = ""
            new_links = "".join(new_link_list)
            # print(new_links)
            # print(new_link_list)

            # print(base_url+new_links)

            links.append(base_url+new_links)
            # print(links)


def magnet_link():
    i = 1
    url = links[i]
    # print(url)
    page = requests.get(url, headers=headers)
    # print(page)
    soup = bs4(page.text, 'html.parser')
    # print(soup.prettify)
    magnet_class_name = "l53b20aa549330b34fb66a8894db4504f7992437f lb3237c78b4503faf538f0bde79ffed2c2f6f7cb9 l133aa445b246c6a95cc7dc421d78c0b20a5cc611"
    magnet_class = soup.find_all(
        'a', class_=magnet_class_name)
    # print(magnet_class)
    for m in magnet_class:
        magnet1 = m.get('href')
        # magnet = m.getText()
        # print("1st::::::::::::::::::::::::  \n", magnet1)
        magnets.append(magnet1)
        # print(magnet)
        print(magnets)


linkSearch()
magnet_link()
