import os
import requests
import urllib.request
from bs4  import BeautifulSoup

#absolute dir the script is in
script_dir = os.path.dirname(__file__)
opt_path = "./"
file_path = os.path.join(script_dir, opt_path)
#create folders
if not os.path.exists(file_path + "html"):
    os.makedirs(file_path       + "html")
if not os.path.exists(file_path + "opt"):
    os.makedirs(file_path       + "opt")

List_A     = []
url        = "https://www.twitch.tv/directory"
contents   = urllib.request.urlopen(url).read()
soup       = BeautifulSoup(contents, "html.parser")

#use not yet
Title      = soup.find_all('div', class_="")
List_A.append(Title)

#print out resaults
def output():
    with open(file_path + "./opt/output.json", "w") as f:
        for item in soup:
            f.write("%s\n" % item)

#okay.
output()
