from qiskit.utils import algorithm_globals, QuantumInstance
from qiskit import Aer
from qiskit_algorithms.optimizers import COBYLA
from qiskit.opflow import Z
from qiskit_algorithms.minimum_eigensolvers import QAOA
from qiskit_ibm_provider import IBMProvider

H1 = Z^Z # Define Z_0Z_1
qaoa = QAOA()

seed = 1234
algorithm_globals.random_seed = seed
quantum_instance = QuantumInstance(Aer.get_backend("aer_simulator"),
seed_simulator=seed, seed_transpiler=seed,
shots = 10)
qaoa = QAOA(optimizer = COBYLA(), quantum_instance=quantum_instance)
result = qaoa.compute_minimum_eigenvalue(H1)
print(result)

My_token = 'c9f9e73ead2cd8e4a404105185a3abd681a91e9012bd5c77cfd4c07bcd265c32c7f7ff67d0d2a374ecdbf7c70a22f4482868ba92212d09900928adcaba224090' # Paste your token here

IBMProvider.save_account(My_token, overwrite=True)

provider = IBMProvider.load_account()
program_id = "qaoa"
H1 = Z^Z
opt = COBYLA()
reps = 1
shots = 1024
runtime_inputs = {
"operator": H1,
"reps": reps,
"optimizer": opt,
"initial_point": [0,0],
"use_swap_strategies": False
}
options = {"backend_name": "ibmq_belem"}
job = provider.runtime.run(program_id=program_id, options=options, inputs=runtime_inputs)
#job = provider.runtime.job(program_id)