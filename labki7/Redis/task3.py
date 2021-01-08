from redis import Redis

redis_connection = Redis(decode_responses=True)

##ZBIORY##


#Dodanie do zmiennej key ró¿nych wartoœci
redis_connection.sadd("key","val1")
redis_connection.sadd("key","val2")
redis_connection.sadd("key","val3")
#Wyœwietlenie wartoœci key losowo
print(redis_connection.smembers("key"))

##POSORTOWANE_ZBIORY##


#Dodanie do zmiennej sorted_set_key ró¿nych wartoœci
redis_connection.zadd("sorted_set_key",{"key1": 11})
redis_connection.zadd("sorted_set_key",{"key2": 2})
redis_connection.zadd("sorted_set_key",{"key3": 33})
redis_connection.zadd("sorted_set_key",{"key4": 8})
#Wyœwietlenie wartoœci sorted_set_key od najmniejszej do najwiekszej
#W przypadku przypisania tych samych wartoœci liczbowych wyœwietlane alfabetycznie wed³ug nazw
print(redis_connection.zrange("sorted_set_key",0, -1))

##HASHE##

#Zainicjalizowanie hasha
hash_key ='test_hash'
redis_connection.hset(hash_key,'key','value')