from qiskit.opflow import Z,I
from qiskit.algorithms import QAOA

H1 = (Z^I^Z^I^I^I) + (Z^I^I^I^Z^I) + (Z^I^I^I^I^Z) + (I^Z^I^I^Z^I) + (I^Z^I^I^I^Z) + (I^I^Z^Z^I^I) + (I^I^Z^I^Z^I) + (I^I^I^I^Z^Z)# Define Z_0Z_1

qaoa = QAOA(reps = 6)
circuit = qaoa.construct_circuit([1,2,3,4,5,6,7,8,9,10,11,12],H1)[0]
circuit.decompose().decompose().draw(output="mpl")

from qiskit.utils import algorithm_globals, QuantumInstance
from qiskit import Aer
from qiskit.algorithms.optimizers import COBYLA
seed = 4096*16
algorithm_globals.random_seed = seed
quantum_instance = QuantumInstance(Aer.get_backend("aer_simulator"),
seed_simulator=seed, seed_transpiler=seed,shots = 500000)
qaoa = QAOA(optimizer = COBYLA(), quantum_instance=quantum_instance)
result = qaoa.compute_minimum_eigenvalue(H1)
print(result)