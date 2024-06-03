import requests

def hava_durumu_al(sehir, api_anahtari):
    url = f"http://api.weatherapi.com/v1/current.json?key={api_anahtari}&q={sehir}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print("Hava durumu verileri alinamadi. Lutfen gecerli bir sehir adi girin.")
        return None

def main():
    sehir = input("Lutfen hava durumunu ogrenmek istediginiz sehri girin: ")
    api_anahtari = "42ebdfc36b7642a39af182148240902"
    hava_durumu = hava_durumu_al(sehir, api_anahtari)
    if hava_durumu:
        print(f"{sehir} sehrinin hava durumu:")
        print("Sicaklik:", hava_durumu['current']['temp_c'], "°C")
        print("Hissedilen Sicakiık:", hava_durumu['current']['feelslike_c'], "°C")
        print("Durum:", hava_durumu['current']['condition']['text'])

if __name__ == "__main__":
    main()
