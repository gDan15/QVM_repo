from pyquil import Program
from pyquil.gates import *
from pyquil import get_qc

p = Program()

# Declaration of a memory space where measurements will be read. The memory is equal to 1 bit in this case.
ro = p.declare('ro','BIT', 2)

## Create superposition state for 2 qubits.
p += H(0)
p += H(1)

## Hide queen at 4th position.
p += H(0)
# 1 is control and 0 is the target
p += CNOT(1, 0)
p += H(0)

## Turn queen on one try
p += H(0)
p += H(1)
p += X(0)
p += X(1)
p += H(0)
p += CNOT(1, 0)
p += H(0)
p += X(0)
p += X(1)
p += H(0)
p += H(1)

## Measurement
p += MEASURE(0, ro[0])
p += MEASURE(1, ro[1])

qc = get_qc('2q-qvm')
executable = qc.compile(p)
result = qc.run(executable)
print(result)

## Quil representation
# print(p)


