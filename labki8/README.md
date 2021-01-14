# Aplikacje- interneetowe-www-TomaszKonkel-185IC
# Autor: Tomasz Konkel grupa: 185IC_B1


#Laboratorium numer 8
Działanie WebSocketów w aplikacji z logowaniem się użytkowników i wyświetlania ich stanu połączenia 
OPIS PLIKÓW 
-------------------------------------ZAD1---------------------------------------------------

SETTINGS.py 

	- Dodane Channel_Layers w którym jest ustawiona domyślna współpraca BACKENDU redisa, hosta redisa i routingu
  
CONSUMER.py

	- Tutaj są napisane funkcje zapewniające podstawowe sprawdzanie połączenia między klientem a serwerem(Połączenie i rozłączenie), oraz wyświetlania tego na stronie
  
przy każdym zalogowaniu się, użytkownika będzie otrzymywał możliwość odbierania wiadomości on serwera(przyłączenie do grupy 'users'), przy wylogowaniuta możliwość będzie mu zabierana(usuwanie z grupy 'users')

ROUTING.py

	- Podłączanie funckji z CONSUMER.py do WebSocket, sposób zapisu podobny do Django URL
  
TEMPLATES

	- _base.html: Podstawowy wygląd HTML
  
	- user_list.html: rozszerzenie powyższego pliku o skrypt wyświetlający zalogowanych użytkowników
  
	- log_in.html: rozszerzenie wcześniejszego pliku _base.html, wyświetlający formularz do logowania, wszelkie  dane są przekazywane w JSON
  
	- sign_up.html: rozszerzenie wcześniejszego pliku _base.html, wyświetlajacy formularz rejestracji
  
VIEWS.py

	- W tym pliku mamy klasy wyświetlające nasze widoki do Templatsów, uwierzytelnianie w przypadku logowania i wszelkie gotowe w django formularze   
  
URLS.py

	- W tym pliku mamy odnosniki do adresów poszczególnych podstron(W projekcie do podstrony admin i pustej strony, a w aplikacji do każdej poszczególnej podstrony)
  
		- funkcja user_list wyświetla nam user_list.html, oraz informacje czu użytkownik jest zalogowany czy nie, aby wyświetlic ten widok trzeba być zalogowany
    
		- funkcja log_in, sprawdza logowanie użytkownika i wyświetla widok logowania
    
		- funkcja log_out wymaga aby byc zalogowany, oraz wyświetla widok po wylogowaniu
    
		- funkcja sign_up, wyświetla widok rejestracji i sprawdza poprawność wprowadzonych danych

MODELS.py

	- W tym pliku mamy zapisaną klase odpowiadającą za to czy użytkownik jest zalogowany czy nie

SIGNALS.py

	- W tym pliku mamy funkcje opowiedzialna za rozgłaszanie powiadomienia o tym czy uzytkownik jest zalogowany czy nie, wykorzystuje wbudowane rozszerzenia receiver(user_logged_in, user_logged_out) 
  
APP.py

	- W tym pliku zapewniamy, że sygnał działa w naszej aplikacji, tak samo w pliku __init__.py 
  

-------------------------------------------------------ZAD2---------------------------------------------------------

worker2.html

	- Kod w html w którym zawarty jest skrypt z WebWorkerem
  
	- WebWorker zapewnia nam wykonywania skryptów JS w tle, dzięki czemu rozbudowane skrypty nie blokują interfejsu użytkownika, bo są wykonywane w tle
  
	- Właściwość onmessage, jest wykonywana w momencie wystąpienia konkretnego zdarzenia(EventHandler). Zdarzenia są typu MessageEvent i są wywołane gdy zostanie otrzymana wiadomość
  
	- Właściwość postMessage służy do wysyłania wewnętrzego komunikatu między workerami. Za parametr może przyjąć dowolną wartość lub obiekt JS
  
	- Skrypt realizuje wyliczanie liczb pierwszy z uzyciem powyższyche metod
  
worker.html

	- Skrypt realizuje szukanie liczb pierwszych, zwrócenia ich ilości oraz czasu w jakim zostało to wykonane

1. Widok użytkowników z poziomu zalogowania użytkownika Tomasz 

![alt text](https://github.com/TomaszKonkel/aplikacje-internetowe-TomaszKonkel-185ic/blob/master/labki8/Zdjecia/1.PNG)	



2. Widok użytkowników z poziomu zalogowania użytkownika Admin

![alt text](https://github.com/TomaszKonkel/aplikacje-internetowe-TomaszKonkel-185ic/blob/master/labki8/Zdjecia/2.PNG)



2. Pierwszy program z WebWorkerem(Obliczanie liczb pierwszych)

![alt text](https://github.com/TomaszKonkel/aplikacje-internetowe-TomaszKonkel-185ic/blob/master/labki8/Zdjecia/3.PNG)


3. Drugi program z WebWorkerem(Szukanie liczb pierwszych i podawanie czasu szukania)

![alt text](https://github.com/TomaszKonkel/aplikacje-internetowe-TomaszKonkel-185ic/blob/master/labki8/Zdjecia/4.PNG)


3. Informacje w konsoli GitBash na temat WebSocketa

![alt text](https://github.com/TomaszKonkel/aplikacje-internetowe-TomaszKonkel-185ic/blob/master/labki8/Zdjecia/5.PNG)
