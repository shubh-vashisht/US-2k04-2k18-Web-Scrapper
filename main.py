import requests
from bs4 import BeautifulSoup
import re


# url = "https://www.census.gov/construction/bps/msaannual.html"
def getAllData():
    f = open("data.txt", "w")
    f.close()
    f = open("data.txt", "a")
    for i in range(2004, 2019):
        url = f'https://www.census.gov/construction/bps/txt/tb3u{i}.txt'
        htmlData = requests.get(url).content.decode('UTF-8')
        f.write(htmlData)
    f.close()
    f = open("data.txt", "r")
    print(f.read())


def getAll(place):
    f = open("data.txt", "r")
    Lines = f.readlines()
    t = open("temp.txt", "w")
    count = 2004
    for l in Lines:
        if place in l:
            print(f"{count}:  {l}")
            t.write(f"{count}: {l}")
            count = count + 1
    f.close()
    t.close()

def getSpecific(place, year):
    f = open("data.txt", "r")
    Lines = f.readlines()
    t = open("temp.txt", "w")
    count = year - 2004
    i = 0
    header = False
    for l in Lines:
        if "CSA" in l:
            if header == False:
                print(l)
                t.write(l)
                header = True
        if place in l:
            if i == count:
                print(f"{year}:  {l}")
                t.write(f"{year}: {l}")
                break
            i = i + 1
    f.close()
    t.close()

