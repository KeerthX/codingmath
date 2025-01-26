# Math Projects with Python

This repository contains Python implementations of various mathematical concepts, ranging from famous conjectures to infinite series, numerical methods, probability, statistics, and more. Each module explores a specific topic with step-by-step implementations, algorithms, and explanations.

## Structure of the Repository

The repository is organized into the following categories:

1. **Conjectures**: Famous unsolved and partially resolved conjectures, such as the Collatz Conjecture and Goldbach's Conjecture.
2. **Infinite Series**: Series like Fibonacci, Harmonic, and Taylor series, implemented to demonstrate computation and analysis.
3. **Numerical Methods**: Algorithms for solving equations, numerical integration, and optimization.
4. **Series Expansions**: Tools for approximating and expanding mathematical functions.
5. **Special Numbers**: Implementations of sequences such as Lucas numbers, triangular numbers, and perfect numbers.
6. **Functions**: Computational implementations of advanced functions like the gamma function and Bessel functions.
7. **Combinatorics and Graphs**: Topics including graph algorithms and combinatorial analysis.
8. **Probability and Statistics**: Simulation and computation of key statistical and probabilistic concepts.

---

## Python Libraries Used

The following Python libraries are utilized in this project:

1. **NumPy**
   - Used for numerical computation, vectorized operations, and handling large datasets.
   - [Documentation](https://numpy.org/doc/)

2. **SciPy**
   - For scientific and mathematical algorithms, including numerical integration, optimization, and advanced functions.
   - [Documentation](https://scipy.org/)

3. **SymPy**
   - For symbolic computation, simplifying algebraic expressions, and solving equations symbolically.
   - [Documentation](https://docs.sympy.org/)

4. **Matplotlib**
   - For data visualization, plotting functions, and graphs to understand mathematical relationships.
   - [Documentation](https://matplotlib.org/stable/contents.html)

5. **networkx**
   - For graph theory and network analysis, including graph algorithms like shortest paths and Eulerian cycles.
   - [Documentation](https://networkx.org/documentation/stable/)

6. **Pandas**
   - To handle and analyze datasets when working with statistical and combinatorial problems.
   - [Documentation](https://pandas.pydata.org/)

7. **Statsmodels**
   - For statistical modeling and hypothesis testing.
   - [Documentation](https://www.statsmodels.org/)

8. **Seaborn** (optional)
   - A high-level library for statistical data visualization based on Matplotlib.
   - [Documentation](https://seaborn.pydata.org/)

---

## Documents Contained in This Project

### Folder Breakdown:

#### **1. Conjectures**
- `collatz_conjecture.py`: Simulates sequences for the Collatz Conjecture.
- `goldbach_conjecture.py`: Tests partitions of even numbers into two primes.
- `riemann_hypothesis.py`: Explores approximations for the Riemann Zeta function.
- More files on related conjectures.

#### **2. Infinite Series**
- `fibonacci_series.py`: Iterative and recursive Fibonacci implementations.
- `harmonic_series.py`: Sum computations for harmonic series.
- `catalan_numbers.py`: Generates Catalan numbers using combinatorial logic.
- Additional series-related modules.

#### **3. Numerical Methods**
- `newton_raphson.py`: Solves nonlinear equations using derivatives.
- `simpsons_rule.py`: Implements Simpson's rule for numerical integration.
- `gradient_descent.py`: Optimizes functions using iterative gradient updates.

#### **4. Series Expansions**
- `taylor_series.py`: Expands functions into Taylor series.
- `fourier_series.py`: Decomposes periodic functions into sinusoidal components.

#### **5. Special Numbers**
- `lucas_numbers.py`: Recursive implementations of Lucas numbers.
- `triangular_numbers.py`: Calculates triangular numbers efficiently.

#### **6. Functions**
- `gamma_function.py`: Implements the gamma function for general \(n!\).
- `zeta_function.py`: Evaluates the Riemann zeta function.

#### **7. Combinatorics and Graphs**
- `graph_coloring.py`: Solves graph coloring problems.
- `eulerian_graphs.py`: Checks for Eulerian cycles and paths.

#### **8. Probability and Statistics**
- `central_limit_theorem.py`: Demonstrates the CLT through simulation.
- `markov_chains.py`: Implements and visualizes Markov chains.

---

## Additional Details

- **Wiki**: For theoretical explanations and advanced details, refer to the associated [Wikipedia articles](https://en.wikipedia.org).
- **How to Contribute**: Contributions are welcome! If you want to add more mathematical concepts or improve existing implementations, feel free to open a pull request.

---

## Getting Started

### Prerequisites
Ensure Python (version 3.8 or later) is installed on your system. Install the required libraries:

```bash
pip install -r requirements.txt
```

### Running Examples
Navigate to the respective folder and execute the `.py` files. For example:

```bash
python infinite_series/fibonacci_series.py
```

---

### Questions or Suggestions?
Feel free to reach out via GitHub issues if you have any questions, ideas, or suggestions. Enjoy exploring the beauty of mathematics with Python!

