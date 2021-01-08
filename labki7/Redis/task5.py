from redis import Redis
##STRUMIENIE##

##Bardziej ustrukturyzowana metoda przekazywania danych ni� kana�a pub-sub##
redis_connection = Redis(decode_responses=True, db=0)
#Nazwa strumienia
stream_name ='testowy_strumien'
#Dodanie do strumienia s�ownika
redis_connection.xadd(stream_name,{'testowy_klucz': 'testowa_wartosc'})
#Odczytanie warto�ci strumienia o podan� ilo�� "count"
message = redis_connection.xread({stream_name: '0-0'}, block=None, count=1)
#Wypisanie wiadomo�ci, ka�dy element ma sw�j identyfiaktor(13liczb-1liczba(milisekundy,numer sekwencji))
print(message)