def inverte_string(string):
    nova_string = ""
    for i in range(len(string) - 1, -1, -1):
        nova_string += string[i]
    return nova_string

string = input("Informe uma string: ")
print("String original:", string)
print("String invertida:", inverte_string(string))
