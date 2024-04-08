#ČÁST 1
import requests
import json 

ico = []
ico = input("Zadej IČO subjektu: ")

def get_company_info(ico):
    url = f"https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty/{ico}"
    response = requests.get(url)
    data = response.json()
    obchodni_jmeno = data["obchodniJmeno"]
    adresa = data["sidlo"]["textovaAdresa"]

    print(obchodni_jmeno)
    print(adresa)

get_company_info(ico)


#ČÁST 2/1
headers = {
    "accept": "application/json",
    "Content-Type": "application/json",
}

name = input("Zadej název nebo část názvu objektu: ")

#BONUS
data = '{"kodCiselniku": "PravniForma", "zdrojCiselniku": "res"}'
res = requests.post("https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ciselniky-nazevniky/vyhledat", headers=headers, data=data)
ciselniky = res.json()     

novy_slovnik = {}
for polozka in ciselniky["ciselniky"][0]["polozkyCiselniku"]:
    novy_slovnik[polozka["kod"]] = polozka["nazev"][0]["nazev"]

#ČÁST 2/2
def company_name_info():
    data = '{"obchodniJmeno": "' + name + '"}'
    res = requests.post("https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty/vyhledat", headers=headers, data=data)
    vysledky = res.json()
    pocet_celkem = vysledky["pocetCelkem"]
    print(f"Nalezeno subjektů: {pocet_celkem}")
    for n in vysledky["ekonomickeSubjekty"]:
        pravni_forma = novy_slovnik.get(n["pravniForma"])
        print(f'{n["obchodniJmeno"]}, {n["ico"]}, {pravni_forma}')

company_name_info()



