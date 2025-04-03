from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator

# Create quantum circuit with curvometric gates
qc = QuantumCircuit(2)
qc.ry(np.pi/2, 0)  # RY gate as curveton
qc.cx(0, 1)         # CNOT gate

# Simulate
simulator = AerSimulator()
compiled_circuit = transpile(qc, simulator)
result = simulator.run(compiled_circuit).result()
print(result.get_counts())
