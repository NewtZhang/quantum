from qiskit import *

# a try on the first quantum circuit
# print(QuantumCircuit(2, 2).draw('mpl', interactive = True))

# some qunatum and classical registers
qreg1 = QuantumRegister(size=2, name='qreg1')
qreg2 = QuantumRegister(1, 'qreg2')
creg = ClassicalRegister(1, 'oldschool')

qc = QuantumCircuit(qreg1, creg, qreg2)

print(qc.x(qreg1))
print(qc.x(0))
print(qc.x(1))