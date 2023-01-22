import requests as rs
import os
URL = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vT1aGnC0w_8tdLizE5NTXX0NI5u-shqK4qikxTqh4omMzYkVup5fx9KedGn-J4AOOuT_n3EA18maMLd/pub?gid=0&single=true&output=csv'
try:
    res=rs.get(url=URL)
    if os.path.exists("questions.csv"):
        os.remove("questions.csv")
    open('questions.csv', 'wb').write(res.content)
    print("Dernière version des questions téléchargée!")
except:
    print("Téléchargement de la dernière version des questions échoué")