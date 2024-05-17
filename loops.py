def index_of(word, list):
    for i , elemento in enumerate(list):
        if elemento==word:
            return i
    return -1

def index_of_by_index(word, list, posicion_salida):
    for i in range(posicion_salida, len(list)): #hace el loop desde la salida hasta que encuentra la coincidencia
        if list[i]==word:
            return i
    return -1



def index_of_empty(lista):
    for i in range (len(lista)):
        if lista[i]=="":
            return i
    return -1



def put(word,list):
    for i in range (len(list)):
        if list[i]=="":
            list[i]=word
            return i
    return-1



def remove(word,list):
    borrados=0
    for i in range (len(list)):
        if list[i]==word:
            list[i]=""
            borrados = borrados + 1

    return borrados
