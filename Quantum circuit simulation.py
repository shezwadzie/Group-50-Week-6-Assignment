# Objective: Code a basic quantum circuit and explain its AI relevance.

from qiskit import QuantumCircuit, Aer, execute

# Create a quantum circuit with 1 qubit
qc = QuantumCircuit(1, 1)
qc.h(0)  # Apply Hadamard gate to create superposition
qc.measure(0, 0)

# Simulate
simulator = Aer.get_backend('qasm_simulator')
result = execute(qc, backend=simulator, shots=1000).result()
counts = result.get_counts()

print("Quantum Output:", counts)


# Explanation of AI Relevance
# This simple circuit demonstrates quantum superposition, a foundational principle for quantum-enhanced AI. In drug discovery, AI algorithms require evaluating vast chemical combinations. Classical systems struggle due to exponential complexity, but quantum circuits like this can evaluate multiple paths simultaneously, making optimization tasks faster and more efficient. This positions quantum AI as a powerful ally in accelerating precision medicine and molecular research.