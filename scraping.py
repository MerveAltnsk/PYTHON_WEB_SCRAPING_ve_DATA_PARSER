import requests
from bs4 import BeautifulSoup

url = 'https://www.nationalgeographic.com/'
response = requests.get(url)

# response.text kullanarak HTML içeriğini al
soup = BeautifulSoup(response.text, 'html.parser')

# Sayfa başlığını yazdır
print(soup.title.string)

# Belirli bir etiketle eşleşen tüm öğeleri bul ve yazdır
# Örneğin, tüm <h1> etiketlerini bul
for headline in soup.find_all('h1'):
    print(headline.text)
    

################################################################

# Belirli bir sınıfa sahip <p> etiketini bul
copyrights = soup.find('p', attrs={'class': 'copyrights'})

# Eğer öğe bulunursa içeriğini yazdır
if copyrights:
    print(copyrights.text)
else:
    print("Öğe bulunamadı.") 
    

################################################################


# Belirli bir id'ye sahip <div> etiketini bul
example_div = soup.find('div', attrs={'id': 'example'})

# Eğer öğe bulunursa içeriğini yazdır
if example_div:
    print(example_div.text)
else:
    print("Öğe bulunamadı.")