from redis import Redis
##LUA##

#Lua to skryptowy j�zyk programowania 
redis_connection = Redis(decode_responses=True, db=0)

#Wypisanie skryptu w zmiennej, kt�ry zwraca liste z podanymi argumentami
script ="""
return {KEYS[1],KEYS[2],ARGV[1],ARGV[2]}
"""
#Dwa pierwsze elementy w liscie keys, a kolejne w tabeli ARGV
print(redis_connection.eval(script,2,1,2,'first','second'))