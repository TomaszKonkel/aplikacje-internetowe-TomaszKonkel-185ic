import requests
from bs4 import BeautifulSoup
import csv

print("PRZYKŁAD1")
odpowiedz = requests.get("https://www.google.pl")
print("odpowiedź = \n", odpowiedz)
print(odpowiedz.status_code)
html_text: str = odpowiedz.text


html_doc = """<html>
<head>
    <title>Moja pierwsza strona!</title>
</head>
<body>
<p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec posuere elit at malesuada tempor. Donec eget ligula in ante auctor luctus. Phasellus iaculis porttitor gravida. Donec eget sem lorem. Morbi a libero imperdiet, viverra tellus ac, consequat tortor. Suspendisse nibh massa, accumsan non neque a, vestibulum commodo dui.</p>
<p>Phasellus vestibulum ut <br>erat sit amet ullamcorper. Nam at elit feugiat, dapibus ante vitae, ullamcorper dui. Nunc rutrum at nibh tincidunt mattis. In finibus sed ante vel mollis. Donec at semper metus. Aenean quis consectetur risus. Sed suscipit felis sed ex pretium euismod. In fermentum mi a odio porttitor, dapibus aliquet leo accumsan. Suspendisse pretium augue et faucibus euismod. Quisque risus metus, ultricies nec tortor at, efficitur convallis nunc.</p>
<ul>
    <li>Pierwszy punkt</li>
    <li>Drugi punkt</li>
    <li>Trzeci punkt</li>
</ul>
<ol>
    <li>Pierwszy punkt</li>
    <li>Drugi punkt</li>
    <li>Trzeci punkt</li>
</ol>
<table border="3" bgcolor="#ff00ff" class="tabela blog">
    <tr><th>Naglowek 1</th><th>Naglowek 2</th></tr>
    <tr><td>komorka 11</td><td>komorka 12</td></tr>
    <tr><td>komorka 21</td><td>komorka 22</td></tr>
</table>
<a href="http://google.pl">Arcyciekawa strona</a>
</body>
</html>"""


soup = BeautifulSoup(html_doc, "html.parser")

print("\n")

print("Pojemnik title, oraz jego zawartość")
print(soup.title)
print(soup.title.text)

print("\n")


print("Lista li, oraz jej zawartość")
print(soup.li)
print(soup.li.text)
print("\n")



print("Pojemnik table jej zawartość, oraz jej atrybuty")
print(soup.table)
print(soup.table.attrs)
print("\n")



print("Wyszukiwanie podanych elementów strony")
print(soup.find_all("a"))

print("\n")

print("/////////////////////////////////////////////////////////")
print("PRZYKŁAD2")
page = requests.get("https://codedamn-classrooms.github.io/webscraper-python-codedamn-classroom-website/")
soup = BeautifulSoup(page.content, "html.parser")


tabelaTagow = []


for element in soup.select("h1"):
    tabelaTagow.append(element.text)


paragraf = soup.select("a")[3].text
print("Wyświetlenie wartości wszystkich znaczników h1, oraz wartość 3 paragrafu")
print(tabelaTagow, paragraf)

print("/////////////////////////////////////////////////////////")
print("PRZYKŁAD3")
page = requests.get(
    "https://codedamn-classrooms.github.io/webscraper-python-codedamn-classroom-website/"
)
soup = BeautifulSoup(page.content, "html.parser")


image_data = []


images = soup.select("img")
print("Zliczenie ilości danych elementów na stronie")
print("Liczba obrazków =", len(images))


print("/////////////////////////////////////////////////////////")
print("PRZYKŁAD4")

page = requests.get(
    "https://codedamn-classrooms.github.io/webscraper-python-codedamn-classroom-website/")
soup = BeautifulSoup(page.content, 'html.parser')


all_products = []


products = soup.select('div.thumbnail')
for product in products:
    name = product.select('h4 > a')[0].text.strip()
    price = product.select('h4.price')[0].text.strip()
    all_products.append({
        "name": name,
        
        "price": price,
        
    })

keys = all_products[0].keys()
print("keys = ", keys)
print("Wyodrębnienie elementów ze strony i wyeksportowanie ich do plików")
with open('products.csv', 'w', newline='') as output_file:
    dict_writer = csv.DictWriter(output_file, keys)
    dict_writer.writeheader()
    dict_writer.writerows(all_products)

print("/////////////////////////////////////////////////////////")
print("PRZYKŁAD5")


page = requests.get(
    "https://codedamn-classrooms.github.io/webscraper-python-codedamn-classroom-website/"
)
soup = BeautifulSoup(page.content, "html.parser")


all_links = []


links = soup.select("a")
print("Liczba linków = ", len(links))
for ahref in links:
    text = ahref.text
    text = text.strip() if text is not None else ""

    href = ahref.get("href")
    href = href.strip() if href is not None else ""
    all_links.append({"href": href, "text": text})

    
print(all_links[8])
print("Zliczenie liczby elementów na stronie, oraz wyświetlenie wartości tego o podanym indeksie")