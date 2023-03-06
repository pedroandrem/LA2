'''
Podemos usar um (multi) grafo para representar um mapa de uma cidade: 
cada nó representa um cruzamento e cada aresta uma rua.

Pretende-se que implemente uma função que lista os cruzamentos de uma cidade 
por ordem crescente de criticidade: um cruzamento é tão mais crítico quanto 
maior o número de ruas que interliga.

A entrada consistirá numa lista de nomes de ruas (podendo assumir que os nomes de ruas são únicos). 
Os identificadores dos cruzamentos correspondem a letras do alfabeto, e cada rua começa (e acaba) no cruzamento 
identificado pelo primeiro (e último) caracter do respectivo nome.

A função deverá retornar uma lista com os nomes dos cruzamentos por ordem crescente de criticidade, 
listando para cada cruzamento um tuplo com o respectivo identificador e o número de ruas que interliga.
Apenas deverão ser listados os cruzamentos que interliguem alguma rua, e os cruzamentos com o mesmo 
nível de criticidade deverão ser listados por ordem alfabética.
'''

def cruzamentos(ruas):
    dic = {}
    for i in ruas:
        if i[0] not in dic.keys():
            dic[i[0]] = 1
        else:
            dic[i[0]] += 1
        if i[-1] not in dic.keys():
            dic[i[-1]] = 1
        elif i[0] != i[-1]:
            dic[i[-1]] += 1
        
    lista = list(dic.items())
    lista.sort(key = lambda x: (x[1], x[0]) )
    return lista

def main():
    print("<h3>cruzamentos</h3>")
    ruas = ["raio","central","liberdade","chaos","saovictor","saovicente","saodomingos","souto","capelistas","anjo","taxa"]
    print("in:",ruas)
    print("out:",cruzamentos(ruas))


import unittest

class cruzamentosTest(unittest.TestCase):
    
    def test_cruzamentos_1(self):
            self.assertEqual(cruzamentos(["raio","central","liberdade","chaos","saovictor","saovicente","saodomingos","souto","capelistas","anjo","taxa"]),[('t',1),('a',2),('e',2),('l',2),('r',2),('c',3),('o',3),('s',6)])

    def test_cruzamentos_2(self):
            self.assertEqual(cruzamentos(["ab","bc","bd","cd"]),[('a',1),('c',2),('d',2),('b',3)])
            
if __name__ == '__main__':
    main()
    unittest.main()
