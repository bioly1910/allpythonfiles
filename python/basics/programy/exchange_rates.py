
import requests # import biblioteki requests niezbędnej do pobrania danych z serwera
# jeśli python nie widzi jakiejś biblioteki, trzeba ją zainstalować w terminalu:
# pip install requests

response = requests.get("http://api.nbp.pl/api/exchangerates/tables/a?format=json")

if response.ok == True: # sprawdzenie, czy serwer odpowiada poprawnie
    data = response.json()[0] # parsowanie danych z formatu teksowego na format do odczytu w python
    print(data) # wynik jest to lista która zawiera słownik. W tym słowniku mamy klucz "rates" którego wartość 
    # zawiera następną listę słowników, już z danymi nas interesującymi, czyli kursami walut

    table = data["table"]
    no = data["no"]
    effectiveDate= data["effectiveDate"]
    print("\nExchange rates: ", table, no, effectiveDate)

    rates = data["rates"]
    for rate in rates:
        currency = rate["currency"]
        code = rate["code"]
        mid = rate["mid"]
        print(currency, "code: ", code, "value: ", mid)



