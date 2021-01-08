from redis import Redis
from time import sleep
from datetime import datetime

##LISTY##

redis_connection = Redis(decode_responses=True)
#Deklaracja zmiennej
list_key ="example-list"
#"Wrzucenie" do zmiennej wartoœci 1,2,3,4,5
redis_connection.rpush(list_key,1,2,3,4,5)
#Wypisanie wszystkich elementów zmiennej 
print("Wszystkie elementy tablicy to:",redis_connection.lrange(list_key,0, -1))
#Wypisanie elementów od 1 do 3, numerowane wed³ug tablicy
print("Elementy od 1 do 3 tablicy to:",redis_connection.lrange(list_key,1,3))


##SELECTY##


redis_connection.set("key","value")
redis_connection_1 = Redis(decode_responses=True, db=1)
#Wypisanie wartoœci key dla redis_connection_1
print(redis_connection_1.get("key"))
#Wypisanie wartoœci key dla redis_connection
print(redis_connection.get("key"))
#Ustawiona wartoœæ dla klucza z czasem wygaœniecia 30 sekund
redis_connection.setex("key",30,"value")


##TTL##


#Wyœwietlanei aktualnego czasu z opóŸnieniem
print(datetime.now().time(),"Aktualny czas")
sleep(10)
print(datetime.now().time(),"10sekund opoznienia")
sleep(30)
print(datetime.now().time(),"30sekund opoznienia")

