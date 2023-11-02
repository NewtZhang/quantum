from qiskit.opflow import Z,I
from qiskit.algorithms import QAOA

H1 = (Z^Z^I^I) + (I^Z^I^Z) + (Z^I^Z^I)# Define Z_0Z_1

# qaoa = QAOA()
# circuit = qaoa.construct_circuit([1,2],H1)[0]
# circuit.draw(output="mpl")
# circuit.decompose().decompose().draw(output="mpl")

qaoa = QAOA(reps = 5)
circuit = qaoa.construct_circuit([1,2,3,4,5,6,7,8,9,10],H1)[0]
circuit.decompose().decompose().draw(output="mpl")

from qiskit.utils import algorithm_globals, QuantumInstance
from qiskit import Aer
from qiskit.algorithms.optimizers import COBYLA
seed = 1024
algorithm_globals.random_seed = seed
quantum_instance = QuantumInstance(Aer.get_backend("aer_simulator"),
seed_simulator=seed, seed_transpiler=seed,shots = 10)
qaoa = QAOA(optimizer = COBYLA(), quantum_instance=quantum_instance)
result = qaoa.compute_minimum_eigenvalue(H1)
print(result)

