# Monte Carlo Physics Simulations

This repository gathers several numerical simulation projects applied to statistical and quantum physics, based on Monte Carlo methods. These implementations were carried out as part of my Master's degree in Physics.

## Academic Context

This repository compiles work from two years of study and two distinct courses:

* **Master 1 - Monte Carlo Methods (Prof. Torcini):**
    * **Grade:** 20 / 20
    * **Content:** Introductory scripts in the `basics/` folder and the study of the 2D Ising model phase transition (`02_ising_2d_phase_transition.ipynb`).
* **Master 2 - Quantum Monte Carlo (Prof. Honecker):**
    * **Grade:** [en attente de la note] / 20
    * **Content:** Advanced projects on the 1D Ising model (`01_ising_1d_metropolis.ipynb`), the Diffusion QMC method (`03_diffusion_qmc_ground_state.ipynb`), and the Stochastic Series Expansion method (`04_sse_heisenberg_chain.ipynb`).

---

## Projects and Key Results

Here is an overview of the four main projects. For each model, the physical theory is detailed in the corresponding notebook, and the Monte Carlo algorithms have been implemented in Python to extract fundamental thermodynamic and quantum observables.

### 1. 1D Ising Model: Metropolis Algorithm
**File:** `notebooks/01_ising_1d_metropolis.ipynb`

The goal of this project is to simulate the one-dimensional Ising model. Theory predicts the absence of a phase transition at finite temperature. The simulations allow us to visualize the behavior of energy, magnetization, magnetic susceptibility, and specific heat as a function of temperature, confirming a phase change only at $T=0$.

![1D Ising plots](/plot/ising_model/ising1d_plots.png)

### 2. 2D Ising Model: Phase Transition
**File:** `notebooks/02_ising_2d_phase_transition.ipynb`

Unlike the one-dimensional case, the 2D Ising model exhibits a ferromagnetic-paramagnetic phase transition. This notebook highlights this transition by observing the divergence of the susceptibility and specific heat, allowing us to identify the critical temperature $T_c$.

In 2D, the Ising model underwent a phase transition at Tc.I simulated this phase transition, and here are my results, where Tc can be seen in the magnetization and susceptibility curves:

- magnetisation : ![magnetization curve](/plot/ising_model/Ising2d_L20_magnetization_curve.png)
- susceptibility : ![susceptibility curve](/plot/ising_model/Ising2d_L20_susceptibility_curve.png)

I also take the configuration close to Tc, before and after the phase transition:

- T = 1.5 (Before): ![magnetization curve](/plot/ising_model/Ising2d_config_T1.5.png)
- T = 2.304 (close to Tc): ![magnetization curve](/plot/ising_model/Ising2d_config_T2.304.png)
- T = 3.5 (After): ![magnetization curve](/plot/ising_model/Ising2d_config_T3.5.png)

### 3. Diffusion Quantum Monte Carlo (DQMC)
**File:** `notebooks/03_diffusion_qmc_ground_state.ipynb`

This project explores the Diffusion QMC method to estimate the ground state energy. By diffusing "walkers" that represent the probability density, we reconstruct the ground state wave function for three distinct potentials: harmonic, cubic anharmonic, and quartic anharmonic. The ground state energies are accurately recovered using an imaginary time extrapolation ($\Delta \tau$).

- Harmonic potential case : ![harmonic potential density walker](/plot/diffusion_harmonic_walker_density.png)
- Extrapolation of the grounds states : ![Extrapolation of the grounds states](/plot/diffusion_extrapolation_gs.png)

### 4. Stochastic Series Expansion (SSE): Heisenberg Chain
**File:** `notebooks/04_sse_heisenberg_chain.ipynb`

This project uses the advanced Stochastic Series Expansion method to simulate a spin chain with the Heisenberg model (ferromagnetic and antiferromagnetic cases). The notebook details the calculation of magnetization, energy, susceptibility, and specific heat for various temperatures down to near absolute zero, thus recovering the ground state energy.

- Antiferromagnetic case result : ![Antiferromagnetic case](/plot/Heisenberg_antiferro_case.png)