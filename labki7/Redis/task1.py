#Sprawdzanie połączenia z serwerem redis
from redis import Redis #importowanie biblioteki z redisa
redis_connection = Redis(decode_responses=True) #zmienna sprawdzająca czy jest połączenie
print(redis_connection.ping(),"- Połączono") #wypisanie w konsoli, czy połaczono z redisem

##STRING##

#Dekleracja zmiennych
key ="some-key"
value ="some-val"
value1 = 55
#Przypisanie oraz wypisanie wartości key
redis_connection.set(key, value)
print("Wartość key to:",redis_connection.get(key))
#Do wartości key dodanie dowolnej frazy
redis_connection.append(key,"-dodana fraza")
print("Wartość key z dodaną frazą to:",redis_connection.get(key))
#Usuwanie wartości key
redis_connection.delete(key)
print("Wartość key po usunięciu to:",redis_connection.get(key))

#Przypisanie zmiennej key innej wartości(następuje nadpisanie)liczbowej
redis_connection.set(key, value1)
#Wypisanie liczbowej wartości key
print("Wartość key to:",redis_connection.get(key))
#Zwiększenie wartości key o 5
print("Wartość key + 5 to:",redis_connection.incr(key,5))
#Zmniejszenie wartości key o 20
print("Wartość key -20 to:",redis_connection.decr(key,20))