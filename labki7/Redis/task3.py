from redis import Redis

redis_connection = Redis(decode_responses=True)

##ZBIORY##


#Dodanie do zmiennej key r�nych warto�ci
redis_connection.sadd("key","val1")
redis_connection.sadd("key","val2")
redis_connection.sadd("key","val3")
#Wy�wietlenie warto�ci key losowo
print(redis_connection.smembers("key"))

##POSORTOWANE_ZBIORY##


#Dodanie do zmiennej sorted_set_key r�nych warto�ci
redis_connection.zadd("sorted_set_key",{"key1": 11})
redis_connection.zadd("sorted_set_key",{"key2": 2})
redis_connection.zadd("sorted_set_key",{"key3": 33})
redis_connection.zadd("sorted_set_key",{"key4": 8})
#Wy�wietlenie warto�ci sorted_set_key od najmniejszej do najwiekszej
#W przypadku przypisania tych samych warto�ci liczbowych wy�wietlane alfabetycznie wed�ug nazw
print(redis_connection.zrange("sorted_set_key",0, -1))

##HASHE##

#Zainicjalizowanie hasha
hash_key ='test_hash'
redis_connection.hset(hash_key,'key','value')