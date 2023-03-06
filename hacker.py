"""
Um hacker teve acesso a um log de transações com cartões de
crédito. O log é uma lista de tuplos, cada um com os dados de uma transação,
nomedamente o cartão que foi usado, podendo alguns dos números estar
ocultados com um *, e o email do dono do cartão.

Pretende-se que implemente uma função que ajude o hacker a 
reconstruir os cartões de crédito, combinando os números que estão
visíveis em diferentes transações. Caso haja uma contradição nos números 
visíveis deve ser dada prioridade à transção mais recente, i.é, a que
aparece mais tarde no log.

A função deve devolver uma lista de tuplos, cada um com um cartão e um email,
dando prioridade aos cartões com mais digitos descobertos e, em caso de igualdade
neste critério, aos emails menores (em ordem lexicográfica).
"""

def tuploProcurado(lista, tuploP):
     for i in lista:
          if i[1] == tuploP[1]:
            return True
     return False 

def hacker(log):
    # O log é uma lista de tuplos, com os dados do cartao e o email
    novoLog = []
    novocc = ""
    for i in log:
         if tuploProcurado(novoLog, i) == False: #Verificaçao para os que sao iguais
              novoLog.append(i)
         elif tuploProcurado(novoLog, i) == True: #Se existir algum com o mail igual
              
              for cc,email in novoLog:
                   if email == i[1]:
                        for j in range(len(i[0])):
                             if i[0][j] != '*':
                                  novocc += i[0][j]
                             elif i[0][j] == '*' and cc[j] != '*':
                                  novocc += cc[j]
                             elif cc[j] == '*' and i[0][j] == '*':
                                  novocc += '*'
                        novoLog.remove((cc,email))
                        novoLog.append((novocc,email))
              
    novoLog1 = sorted(novoLog, key=lambda x: (x[0].count('*'), x[1]))
    

    return novoLog1

def main():
    print("<h3>hacker</h3>")
    log = [("****1234********","maria@mail.pt"),
           ("0000************","ze@gmail.com"),
           ("****1111****3333","ze@gmail.com")]
    print("in:",log)
    print("out:",hacker(log))

import unittest

class hackerTest(unittest.TestCase):
    
    def test_hacker_1(self):
            log = [("****1234********","maria@mail.pt"),
                   ("0000************","ze@gmail.com"),
                   ("****1111****3333","ze@gmail.com")]
            self.assertEqual(hacker(log),[("00001111****3333","ze@gmail.com"),("****1234********","maria@mail.pt")])       

    def test_hacker_2(self):
            log = [("0000************","ze@gmail.com"),
                   ("****1234********","maria@mail.pt")]
            self.assertEqual(hacker(log),[("****1234********","maria@mail.pt"),("0000************","ze@gmail.com")])  
            
            
if __name__ == '__main__':
    main()
    unittest.main()
