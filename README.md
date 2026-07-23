# Brownian Motion on Manifolds

This project simulates Brownian motion on curved surfaces (Riemannian manifolds) instead of the flat plane most people first learn it on. It pairs a small, testable Python library for running these simulations with an interactive Streamlit app for watching the diffusion unfold in real time.

## What This Project Is About

Brownian motion is the random, erratic motion first observed in pollen grains suspended in water and later given a rigorous mathematical treatment by Einstein and Wiener. It underlies fields ranging from statistical physics to quantitative finance, and, more recently, the diffusion models behind modern generative AI.

The question this project explores is what happens to that random motion when the space it lives in is curved. A particle wandering on the surface of a sphere behaves differently from one wandering on a flat plane or on the surface of a donut (a torus): the curvature of the space bends and constrains the motion. This project builds simulations of that behavior and visualizes it directly.

For the full motivation, mathematical background, and the theory connecting this project to diffusion models and quantitative finance, see [ONBOARDING.md](ONBOARDING.md). For the differential geometry curriculum used to build the mathematical foundations (fundamental forms, curvature, the Laplace-Beltrami operator, Ito versus Stratonovich calculus), see [docs/writeups/1-curriculum-checklist.md](docs/writeups/1-curriculum-checklist.md).

## Surfaces Implemented

- **Sphere (S²)**: positively curved, particle paths are recurrent, and the particle distribution converges to uniform over the surface.
- **Torus (T²)**: zero average curvature but non-trivial global topology; particles wrap around the surface rather than escaping it.
- **Hyperbolic plane (H²)**: a stretch goal, not yet implemented. Its negative curvature makes random paths transient, drifting toward a boundary rather than equilibrating.

## How the Simulation Works

Each manifold is represented by a small class (`src/manifolds/sphere.py`, `src/manifolds/torus.py`) implementing a shared interface (`src/manifolds/base.py`):

- `sample_tangent_noise`: generates a random vector constrained to the tangent plane at a point, so a step never points off the surface.
- `euler_maruyama_step`: advances a point one time step using the Euler-Maruyama method, the standard numerical scheme for stochastic differential equations.
- `project_to_manifold`: pulls a point back onto the surface after a step, correcting for the small numerical drift introduced by moving in a straight line through the ambient space.

This is the projection method: propose a step in the tangent plane, take it, then project back onto the surface. Running this update for many particles at once (vectorized with NumPy) is handled by `src/simulation/simulator.py`, and the resulting particle distributions are visualized with a kernel density estimate over the sphere surface in `src/visualization/kde.py`.

The geometry, the simulation loop, and the visualization are kept in separate modules, so adding a new surface only requires implementing its geometry, with no changes needed to the simulator or the app.

## Project Layout

```
app/                   Streamlit application
src/manifolds/         Sphere and torus geometry (tangent projection, noise, stepping)
src/simulation/        Vectorized Euler-Maruyama simulators
src/visualization/     Kernel density estimation for particle distributions
notebooks/             Jupyter notebooks (also exported to HTML for viewing without running code)
docs/writeups/         Mathematical background and the differential geometry curriculum
ONBOARDING.md          Motivation, theory, and project background
```

## Requirements

- Python 3.x
- Dependencies listed in `requirements.txt`, most notably `numpy`, `streamlit`, and `plotly`

## Starting the App

From the project root (`2manifold-brownian-motion/`):

```bash
pip install -r requirements.txt
streamlit run app/app.py
```

This opens the app in your browser. From the sidebar you can:

- Choose the manifold (sphere or torus).
- Set the number of particles, number of time steps, and the size of each time step.
- Choose isotropic noise (motion in all tangent directions) or, for the sphere only, anisotropic noise (motion constrained to a single tangent direction).
- Set the starting point (latitude and longitude for the sphere, or the toroidal and poloidal angles for the torus) and, for the torus, its major and minor radius.

Click "Run Simulation" to generate an animated trajectory, the final particle distribution, and a density heatmap of where the particles ended up.

## Notebooks

The `notebooks/` directory contains the exploratory work behind the library, each one also exported to HTML in the same folder so it can be read without running any code.
