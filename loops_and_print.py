def enumerate_list(list):
    lista=[]
    for i, elemento in enumerate(list):
        if elemento!="":
            lista.append(f'{len(lista)}. {elemento}')
    return lista




def enumerate_backwards(list):
    lista = []
    for i, elemento in enumerate(list):
        if elemento != "":
            lista.append(f'{len(lista)}. {elemento[::-1]}')
    return lista
