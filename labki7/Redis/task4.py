from redis import Redis
##KANA�Y_KOMUNIKACYJNE##


redis_connection = Redis(decode_responses=True)
#Po��czenie z kana�em 
pubsub = redis_connection.pubsub()
#Wy�wietlenie wiadomo�ci subskrybentowi
pubsub.subscribe("testowa_kanal_komunikacyjny")
#Po wy�wietleniu wiadomo�ci kana� si� blokuje w oczekiwaniu na odpowiedz 
for message in pubsub.listen():
    print(message)