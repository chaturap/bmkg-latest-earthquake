import requests
from bs4 import BeautifulSoup


def ekstrasi_data():
    """
tanggal : 26 April 2023,
waktu : 09:56:27 WIB
Magnitudo :     4.7
Kedalaman : 61 km
Lokasi :  4.77 LU - 95.56 BT
Pusat gempa : Pusat gempa berada di darat 15 km BaratLaut Calang
Dirasakan : Dirasakan (Skala MMI): II Aceh Besar, II Banda Aceh
    :return:
    """

    try:
        content = requests.get('https://www.bmkg.go.id')
    except Exception:
        return None


    print(content)
    print(content.status_code)
    if content.status_code == 200:
        #print(content.text)

        soup = BeautifulSoup(content.text, 'html.parser')
        result = soup.find('div', {'class': 'col-md-6 col-xs-6 gempabumi-detail no-padding'})
        result = result.findChildren('li')
        print(result)

        magnitudo = None
        kedalaman = None
        koordinat = None
        lintang = None
        bujur = None
        lokasi = None
        tsunami = None


        i = 0
        for res in result:
            print(i, res)
            if i == 1 :
                magnitudo = res.text
            elif i== 2 :
                kedalaman = res.text
            elif i== 3 :
                koordinat = res.text
                koordinat_split = res.text.split('- ')
                lintang = koordinat_split[0]
                bujur = koordinat_split[1]
            elif i== 4 :
                lokasi = res.text
            elif i == 5:
                tsunami = res.text
            i = i + 1

        title = soup.find('title')
        tanggal = soup.find('span', {'class': 'waktu'})
        waktu = tanggal.text.split(', ')[1]
        tanggal = tanggal.text.split(', ')[0]

        print(title.string)
        #print(soup.prettify())

        hasil = dict()
        hasil['tanggal'] = tanggal
        hasil['waktu'] = waktu
        hasil['magnitudo'] = magnitudo
        hasil['kedalaman'] = kedalaman
        hasil['koordinat'] = koordinat
        hasil['lintang'] = lintang
        hasil['bujur'] = bujur
        hasil['lokasi'] = lokasi
        hasil['tsunami'] = tsunami
    else:
        return None
    return hasil


def tampilkan_data(result):
    if result is None:
        print("tidak bisa menemukan data gempa terkini")
        return
    print('gempa terakhir berdasarkan BMKG')
    print(f"Tanggal : {result['tanggal']}")
    print(f"Waktu : {result['waktu']}")
    print(f"Magnitudo : {result['magnitudo']}")
    print(f"Kedalaman : {result['kedalaman']}")
    print(f"Koordinat : {result['koordinat']}")
    print(f"Lintang : {result['lintang']}")
    print(f"Bujur : {result['bujur']}")
    print(f"Lokasi : {result['lokasi']}")
    print(f"Potensi Tsunami : {result['tsunami']}")
