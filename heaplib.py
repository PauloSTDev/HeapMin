import heapq
import patient
class HeapMin:
    def __init__(self, fila_prioridade, fila_atendidos):
        self.fila_prioridade = fila_prioridade
        self.fila_atendidos = fila_atendidos

    def heapify(self, fila):
        heapq.heapify(fila)
    
    def generatePatients(self):
        self.fila_prioridade = [(patient.genPatient().prioridade, patient.genPatient().idade, patient.genPatient().nome) for _ in range(5)]
    
    def heappush(self, paciente):
        heapq.heappush(self.fila_atendidos, paciente)

    def pop(self):
        paciente = heapq.heappop(self.fila_prioridade)
        self.heappush(paciente)
        print(f"Atendido: Prioridade: {paciente[0]} (Idade: {paciente[1]}, Paciente: {paciente[2]})")

    def printNext(self):
        if (len(self.fila_prioridade) > 0):
            print(f"Prioridade {self.fila_prioridade[0][0]} (Idade: {self.fila_prioridade[0][1]}, Paciente: {self.fila_prioridade[0][2]})")
            
    def printPriority(self):
        self.heapify(self.fila_prioridade)
        for paciente in self.fila_prioridade:
            print(f"Prioridade {paciente[0]} (Idade: {paciente[1]}, Paciente: {paciente[2]})")
    
    def printServed(self, showJustFive = True):
        self.heapify(self.fila_atendidos)
        for paciente in self.fila_atendidos:
            print(f"Prioridade {paciente[0]} (Idade: {paciente[1]}, Paciente: {paciente[2]})")
            if showJustFive and len(self.fila_atendidos) > 5:
                if (paciente == self.fila_atendidos[4]):
                    break