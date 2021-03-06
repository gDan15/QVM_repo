from pyquil import Program
from pyquil.gates import *
from pyquil import get_qc


p = Program()
# Declaration of a memory space where measurements will be read. The memory is equal to 1 bit in this case.
ro = p.declare('ro','BIT', 1)
# La porte quantique X est appliquée au qubit 0
p += X(0)
p += MEASURE(0, ro[0])
# La représentation du programme en Quil est affichée lorsque p est imprimé.
# print(p)

# qc = simulation of a quantic computer
qc = get_qc('1q-qvm')  # You can make any 'nq-qvm' this way for any reasonable 'n'
executable = qc.compile(p)
# L'instruction ci-dessous permet d'exécuter une instruction de la même manière que sur un QPU.
result = qc.run(executable)
print(result)

