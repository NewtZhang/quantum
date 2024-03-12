# Applying a Quantum Approximate Optimization Algorithm and Grover's Algorithm to an Unweighted Max-Cut Problem

## Abstract

We apply a Quantum Approximate Optimization Algorithm (QAOA) and Grover's Algorithm to an unweighted Max-Cut problem with an input graph $G = (V, E)$ with $|V| = 6$ vertices and $|E| = 10$ edges. We develop a QAOA to solve the unweighted Max-Cut problem for $G$ utilizing Simultaneous Perturbation Stochastic Approximation (SPSA) as our classical optimizer. Given a number of cuts $x$ we utilize Grover's Algorithm to find the partitioning which yields $x$ cuts. We test both algorithms in ideal and noisy environments and discuss our findings.

## Report

See [`./report.pdf`](./report.pdf).

## Presentation

See [`./presentation.pdf`](./presentation.pdf).

## Code

Create a virtual environment, install dependencies, and view code in Jupyter Lab.

```
python3 -m venv .venv

source .venv/bin/activate

pip install -r requirements.txt

jupyter lab
```

Each code file has a "Settings" section that you may modify as needed.

### Quantum Approximate Optimization Algorithm

See [`./qaoa-spsa.ipynb`](./qaoa-spsa.ipynb).

### Grover's Algorithm

See [`./grovers.ipynb`](./grovers.ipynb).