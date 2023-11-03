import random

class PatientGen:
    def __init__(self, nome, idade, prioridade):
        self.nome = nome
        self.idade = idade
        self.prioridade = prioridade

def _genRandomName():
    vogais = 'aeiou'
    consoantes = 'bcdfghjklmnpqrstvwxyz'
    nome = random.choice(consoantes).capitalize() + random.choice(vogais) + random.choice(consoantes) + random.choice(vogais + consoantes)
    return nome

def genPatient():
    nome = _genRandomName()
    idade = random.randint(0, 90)
    prioridade = random.randint(1, 10)
    return PatientGen(nome, idade, prioridade)