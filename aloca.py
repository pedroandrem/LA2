"""

Implemente uma função que dado um dicionário com as preferências dos alunos
por projectos (para cada aluno uma lista de identificadores de projecto, 
por ordem de preferência), aloca esses alunos aos projectos. A alocação
é feita por ordem de número de aluno, e cada projecto só pode ser feito
por um aluno. A função deve devolver a lista com os alunos que não ficaram
alocados a nenhum projecto, ordenada por ordem de número de aluno.

"""
import collections

#100%
def aloca(prefs):
    distrib = {}
    novoPrefs = collections.OrderedDict(sorted(prefs.items()))
    listaPrefs = list(novoPrefs)
    listaNaoAlocados = []
    
    for i in novoPrefs: 
        for j in range(len(novoPrefs[i])): # range(len(prefs[i])) será a quantidade de valores atribuidos a uma so chave       
            if novoPrefs[i][j] not in distrib.values(): #Verifica se na pos j existe um valor atribuido e se esse valor existe no dicionario distrib
                distrib[i] = novoPrefs[i][j]
            else:
                continue
    
    listaDistrib = list(distrib)

    for i in listaPrefs:
        if i not in listaDistrib:
            listaNaoAlocados.append(i)
    print(listaNaoAlocados) 
        
            
    
    return listaNaoAlocados


def main():
    print("<h3>aloca</h3>")
    prefs = {10885:[1,5],40000:[5],10000:[1,2]}
    print("in:",prefs)
    print("out:",aloca(prefs))
    

import unittest


class alocaTest(unittest.TestCase):

    def test_aloca_1(self):
            prefs = {10885:[1,5],40000:[5],10000:[1,2]}
            self.assertEqual(aloca(prefs),[40000])
        
    def test_aloca_2(self):
            prefs = {30000:[1],20000:[2],10000:[3]}
            self.assertEqual(aloca(prefs),[])
            
if __name__ == '__main__':
    main()
    unittest.main()
