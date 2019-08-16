import json
import requests
import datetime
import os
import csv


def fix_delimiters(filename):
        lines = []
        with open(filename, 'r', encoding="utf8") as file:
            lines = file.readlines()
        lines[0] = lines[0].replace(',', ';')
        print(lines[0])
        open(filename, 'w', encoding="utf8").writelines(lines)

def convert_to_json(filename):
        with open(filename, encoding="utf8") as csvfile:
            reader = csv.DictReader(csvfile, delimiter=';', dialect='excel')
            j = json.dumps([row for row in reader])
            open(filename.replace('.csv', '.json'), 'w').write(j)

def fetch_and_convert():
    komunestyrevalg = 'https://valg.no/globalassets/dokumenter-2019/valglister-og-kandidater-2019/uttrekk/eksport_kandidater2019_komunestyrevalg.csv'
    fylkestingsvalg = 'https://valg.no/globalassets/dokumenter-2019/valglister-og-kandidater-2019/uttrekk/eksport_kandidater2019_fylkestingsvalg.csv'
    valg_bydelsutvalg_oslo = 'https://valg.no/globalassets/dokumenter-2019/valglister-og-kandidater-2019/uttrekk/eksport_kandidater2019_valg_bydelsutvalg_oslo.csv'

    datestring = datetime.datetime.now().strftime('%Y-%m-%d-kl%H%M')

    r = requests.get(komunestyrevalg)
    open('komunestyrevalg.csv', 'wb').write(r.content)
    fix_delimiters('komunestyrevalg.csv')
    convert_to_json('komunestyrevalg.csv')

    r = requests.get(fylkestingsvalg)
    open('fylkestingsvalg.csv', 'wb').write(r.content)
    fix_delimiters('fylkestingsvalg.csv')
    convert_to_json('fylkestingsvalg.csv')

    r = requests.get(valg_bydelsutvalg_oslo)
    open('valg_bydelsutvalg_oslo.csv', 'wb').write(r.content)
    fix_delimiters('valg_bydelsutvalg_oslo.csv')
    convert_to_json('valg_bydelsutvalg_oslo.csv')



