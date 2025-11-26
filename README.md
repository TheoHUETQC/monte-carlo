# 🧲 Monte Carlo Methods

A small educational project exploring **Monte Carlo simulations** in Python, from simple random sampling to physical stochastic models.  
Designed as a foundation for later extensions to **quantum Monte Carlo** techniques.

In this project, I wanted to revisit what I learned in my Monte Carlo course during my first year of master's studies, particularly its use in simulating the Ising model.

---

## Overview

Monte Carlo methods are a class of algorithms that use **random sampling** to estimate numerical results.  
They are widely used in:
- Statistical physics
- Numerical integration
- Random processes and diffusion
- Bayesian inference and optimization

This repository provides a clear and commented implementation of several classical examples:
1. **Estimation of π**
2. **Numerical integration**
3. **Random walk simulation**
4. **Metropolis algorithm**
5. **simulation of a phase transition in the 2D Ising model**

---

## Theoretical Background

Monte Carlo methods rely on the **Law of Large Numbers**:  

When the number of random samples increases, the statistical average converges to the expected value.

The estimated error decreases as $` \frac{1}{\sqrt{N}} `$, making Monte Carlo particularly robust for high-dimensional problems.

---

## Phase Transition in the 2D Ising Model

In 2D, the Ising model got a phase transition in Tc.
I simulate this Phase transtion, this is my result, where we can see Tc in the magnetisation and susceptibility curve:

- magnetisation : ![magnetization curve](Ising2d_L20_magnetization_curve.png)
- susceptibility : ![susceptibility curve](Ising2d_L20_susceptibility_curve.png)

I aslo take model's config close to Tc, before and after the phase transition:

- T = 1.5 : ![magnetization curve](Ising2d_config_T1.5.png)
- T = 2.304 : ![magnetization curve](Ising2d_config_T2.304.png)
- T = 3.5 : ![magnetization curve](Ising2d_config_T3.5.png)

---

## Installation & Dependencies  

Ensure you have Python **3.7+** and install the required libraries:  

```bash
pip install numpy matplotlib
```

---

## Project Structure
```
📂 monte-carlo/
│
├── 📂 src/
│    ├── montecarlo_pi.py          # Estimate π by random sampling
│    ├── montecarlo_integral.py    # Integrate arbitrary functions
│    ├── random_walk.py            # Simulate Brownian motion
│    ├── metropolis_demo.py        # Simple Metropolis algorithm
│    └── ising_model.py            # phase transition on the 2D Ising Model
│
├── 📂 plots/
│    ├── 📂 ising_model/           # all graph. create in ising_model.py wich whow phase transition
│    │
│    ├── random_walk_1D.png           # graph from random_walk.py 
│    └── montecarlo_pi.png         # distibution's graph from montecarlo_pi.py 
│
└── 📜 README.md
```

---

## Contributions & Contact

Contributions are welcome! You can:

- Fork the repository and improve the simulations.

- Submit a pull request for enhancements or bug fixes.

- Open an issue for discussions or questions.

