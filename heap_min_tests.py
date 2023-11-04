import unittest
import patient
from heaplib import HeapMin

class PatientTests(unittest.TestCase):
    def setUp(self):
        self.patient = patient.PatientGen("Luciano", 20, 10)

    def test_genRandomName(self):
        self.patient = patient._genRandomName()
        self.assertIsInstance(self.patient, str)
        self.assertEqual(len(self.patient), 4)

    def test_genPatient(self):
        self.patient = patient.genPatient()
        self.assertEqual(len(self.patient.nome), 4)        
        self.assertIn(self.patient.prioridade, [1,2,3,4,5,6,7,8,9,10])        
        self.assertIn(self.patient.idade, list(range(91)))

class HeapLibTests(unittest.TestCase):
    def setUp(self):
        self.fila_prioridade = []
        self.fila_atendidos = []
        self.heap = HeapMin(self.fila_prioridade, self.fila_atendidos)

    def test_heapify(self):
        
        self.heap.fila_prioridade = [(6, 6, 'Clara'), (2, 2, 'Maria'), (1, 1, 'Ana'), (3, 10, 'Pedro'), (1, 4, 'Ana'), (5, 5, 'Lucas')]
        self.heap.heapify(self.heap.fila_prioridade)
        self.assertEqual(len(self.heap.fila_prioridade), 6)
        # self.assertEqual(self.heap.fila_prioridade, [(1, 1, 'Ana'), (1, 4, 'Ana'), (2, 2, 'Maria'), (3, 10, 'Pedro'), (5, 5, 'Lucas'), (6, 6, 'Clara')])

    def test_generatePatients(self):
        self.heap.generatePatients()
        self.assertEqual(len(self.heap.fila_prioridade), 5)

    def test_heappush(self):
        self.heap.heappush((3, 5, 'Paulo tester'))
        self.heap.heappush((5, 5, 'Guilherme tester'))
        self.assertEqual(self.heap.fila_atendidos, [(3, 5, 'Paulo tester'), (5, 5, 'Guilherme tester')])

    def test_pop(self):
        self.heap.fila_prioridade = [(1, 1, 'Ana'), (1, 4, 'Ana'), (2, 2, 'Maria')]
        self.heap.pop()
        self.assertEqual(self.heap.fila_prioridade, [(1, 4, 'Ana'), (2, 2, 'Maria')])
        self.assertEqual(self.heap.fila_atendidos, [(1, 1, 'Ana')])

    def test_printNext(self):
        self.heap.fila_atendidos = [(2, 2, 'Maria')]
        self.heap.printNext()

        # Apenas verificando se a estrutura continua a mesma
        self.assertEqual(self.heap.fila_atendidos, [(2, 2, 'Maria')])
        self.assertEqual(len(self.heap.fila_atendidos), 1)
        self.assertEqual(len(self.heap.fila_prioridade), 0)

    def test_printPriority(self):
        self.heap.fila_atendidos = [(1, 4, 'Ana'), (2, 2, 'Maria')]
        self.heap.printPriority()

        # Apenas verificando se a estrutura continua a mesma
        self.assertEqual(self.heap.fila_atendidos, [(1, 4, 'Ana'), (2, 2, 'Maria')])
        self.assertEqual(len(self.heap.fila_atendidos), 2)
        self.assertEqual(len(self.heap.fila_prioridade), 0)

    def test_printServed(self):
        # Deve retornar None caso a fila_atendidos esteja vazia
        self.assertIsNone(self.heap.printServed())

        self.heap.fila_atendidos = [(1, 4, 'Ana'), (2, 2, 'Maria')]
        self.heap.printServed()

        # Apenas verificando se a estrutura continua a mesma
        self.assertEqual(self.heap.fila_atendidos, [(1, 4, 'Ana'), (2, 2, 'Maria')])
        self.assertEqual(len(self.heap.fila_atendidos), 2)
        self.assertEqual(len(self.heap.fila_prioridade), 0)

        self.heap.heappush((3, 5, 'Paulo tester'))
        self.heap.heappush((3, 6, 'Paulo tester 2'))
        self.heap.heappush((5, 5, 'Guilherme tester'))
        self.heap.heappush((7, 5, 'Guilherme tester 2'))

        # Deve printar todos por mais que tenha mais que 5 pacientes
        self.heap.printServed(showJustFive = False)

        # Apenas verificando se a estrutura continua a mesma
        self.assertEqual(self.heap.fila_atendidos, [(1, 4, 'Ana'), (2, 2, 'Maria'), (3, 5, 'Paulo tester'), (3, 6, 'Paulo tester 2'), (5, 5, 'Guilherme tester'), (7, 5, 'Guilherme tester 2')])
        self.assertEqual(len(self.heap.fila_atendidos), 6)
        self.assertEqual(len(self.heap.fila_prioridade), 0)
        

if __name__ == "__main__":
    unittest.main()
