from redis import Redis
##KANA£Y_KOMUNIKACYJNE##


redis_connection = Redis(decode_responses=True)
#Po³¹czenie z kana³em 
pubsub = redis_connection.pubsub()
#Wyœwietlenie wiadomoœci subskrybentowi
pubsub.subscribe("testowa_kanal_komunikacyjny")
#Po wyœwietleniu wiadomoœci kana³ siê blokuje w oczekiwaniu na odpowiedz 
for message in pubsub.listen():
    print(message)