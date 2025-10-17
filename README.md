# 🎲 Monte Carlo Methods

A small educational project exploring **Monte Carlo simulations** in Python — from simple random sampling to physical stochastic models.  
Designed as a foundation for later extensions to **quantum Monte Carlo** techniques.

---

## 📘 Overview

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
4. *(Optional)* Metropolis algorithm

---

## 🧠 Theoretical Background

Monte Carlo methods rely on the **Law of Large Numbers**:  
> When the number of random samples increases, the statistical average converges to the expected value.

The estimated error decreases as $ \frac{1}{\sqrt{N}} $, making Monte Carlo particularly robust for high-dimensional problems.

---

## 🛠 Installation & Dependencies  

Ensure you have Python **3.7+** and install the required libraries:  

```bash
pip install numpy matplotlib
```

---

## 📂 Project Structure
```
📂 monte-carlo/
│
├── 📂 src/
│    ├── montecarlo_pi.py          # Estimate π by random sampling
│    ├── montecarlo_integral.py    # Integrate arbitrary functions
│    ├── random_walk.py            # Simulate Brownian motion
│    └── metropolis_demo.py        # Simple Metropolis algorithm
│
├── 📂 plots/
│    └── (graphs and convergence plots)
│
└── 📜 README.md
```

---

## 🤝 Contributions & Contact

Contributions are welcome! You can:

- Fork the repository and improve the simulations.

- Submit a pull request for enhancements or bug fixes.

- Open an issue for discussions or questions.

📩 Feel free to reach out for any suggestions!

## “Randomness with purpose — that’s Monte Carlo.”
