import requests
import re
from bs4 import BeautifulSoup
import csv


def get(url):
    try:
        r = requests.get(url)
        status = r.status_code
        if status is 200:
            soup = BeautifulSoup(r.text, 'html.parser')
            return soup
        else:
            print('Error code: {}; URL: {}'.format(status, url))
    except:
        print('Error with URL: {}'.format(url))

def parser(soup, url):
    try:
        regex = re.compile("(Subject: ){1}(.)*[\n\r]+")
        header = soup.find('header', id='header')
        out = str(re.search(regex,str(header)).group(0)[9:])
        if out == "": return
        else: return out
    except:
        print("failed " + url)

def listAllSubjects(fileName, outFile):
    flaggedSubjects = open(outFile, 'w')
    file = open(fileName)
    links = csv.reader(file)
    subjects = []
    for link in links:
        print("processing " + link[0])
        try:
            subject = parser(get(link[0]), link[0])
            subjects.append(subject)
            flaggedSubjects.write(subject)
            flaggedSubjects.flush()
        except:
            print("error in IO " + link)
    file.close()
    flaggedSubjects.close()
    return subjects.sort()

listAllSubjects("links.csv", "flaggedSubjects.csv")
