# Brownian Motion on Manifolds
## A Computational Project in Stochastic Geometry

---
This document serves as a gentle introduction to the project, giving motivation, intuition, and some detailed explainations.
---

## 1. Motivation

In 1827, the botanist Robert Brown looked through a microscope at pollen grains suspended in water and noticed they moved in an erratic manner, for the water molecules were constantly colliding with them from all directions. Each collision was too small and too fast to track, but their collective, random effect produced a visible wandering motion. This phenomenon, now called *Brownian motion*, became a remarkable development throughout 20th-century mathematics. Albert Einstein used it to estimate the size of atoms, and Norbert Wiener gave it a rigorous mathematical foundation. Today it is the basis of the mathematics behind topics from financial modeling and machine learning to heat flow and the geometry of curved spaces.

The central question this project asks is what happens when the space itself is curved?

If a particle wanders randomly on the surface of a sphere, constrained always to stay on that surface and being unable to leave it, its behavior differs from, say, wandering in a flat plane. The sphere's curvature bends and redirects the motion. On a flat plane, a particle that starts at the origin will, on average, move farther and farther away and never return. On a sphere, there is no notion of "far away" in the same sense. The sphere closes back on itself, and over a long time the particle will spread out and fill the surface uniformly. On the hyperbolic plane, a surface with negative curvature, the particle drifts toward the boundary and essentially doesn't return to where it started.

Brownian motion on curved spaces is the foundation of the mathematics underlying:

- **Modern generative AI.** Diffusion models, the technology behind image generators, are reverse-time diffusion processes, and understanding why they work requires the same mathematics used to study diffusion on manifolds.
- **Geometric analysis.** The heat equation on a Riemannian manifold, whose solutions are the probability densities of Brownian motion, encodes information about the manifold's shape. Spectral geometers study the manifold by studying how heat spreads across it.
- **Statistical physics.** Diffusion processes model how particles, energy, and information propagate through physical systems with complex geometries.

This project is a laboratory for exploring these principles, culminating with interactive visualizations that let you watch the diffusion process unfold in real time.

---

## 2. Background

### Brownian Motion in Flat Space

The simplest version of Brownian motion starts with a random walk. Imagine standing at the origin of a number line. At each step, you flip a coin: heads means you move one unit to the right, and tails means one unit to the left. After many steps, your position is the sum of the independent coin flips. The Central Limit Theorem says that this sum converges to a Gaussian (bell-curve) distribution when scaled properly. Brownian motion is the continuous-time limit of this process as the step size shrinks to zero and the steps become infinitely frequent.

A few properties of Brownian motion in flat space are worth noting:

- Brownian paths are continuous but they are nowhere differentiable.
- Where the particle goes next depends only on where it is now, not on how it got there.
- (*Connection to the heat equation*) If you were to release a cloud of particles at a single point and allowed them all to diffuse independently, their probability density at a later time satisfies the heat equation. Brownian motion is, in this sense, a probabilistic model of heat flow.

### What Is a Manifold?

A manifold is a space that looks flat when you zoom in close enough, even if it were to be globally curved. The surface of the Earth is a typical example. Stand anywhere on the Earth's surface and look at a small patch around you; it looks like a flat plane. But the Earth as a whole is a sphere, and a map of the entire surface cannot be drawn on flat paper without distorting it somewhere, which is exactly why every world map lies to you about something (whether it's area, shape, or distance, some countries appear much smaller/larger than they are!).

The manifolds that appear in this project are:

- **The sphere, S².** The set of all points in three-dimensional space at distance exactly 1 from the origin. This is merely the surface of a ball, not the entire ball itself. It's a two-dimensional surface embedded in three-dimensional space. Its geometry is positively curved everywhere.
- **The torus, T².** The surface of a donut shape. Topologically it's equivalent to a square with opposite edges identified —- wrap the left edge around to meet the right edge, then the top to meet the bottom (try it with a napkin!). Unlike the sphere, the torus has zero average curvature (it is locally flat almost everywhere), however its global topology is still non-trivial.
- **The hyperbolic plane, H².** A surface of constant *negative* curvature that cannot be embedded in three-dimensional space without distortion. It is represented in this project using the Poincaré disk, which is a unit disk in the plane where distances near the boundary are much larger than they appear. This is a stretch goal for the project, and we may need a V2 to cover it.

Despite manifolds' global complexity, every point has a tangent space, or a flat plane that best approximates the surface at that point. The tangent plane to a sphere at any point is an ordinary flat plane touching the sphere at that point. This local flatness is what allows one to use the familiar tools of linear algebra and calculus.

### Brownian Motion on a Manifold

Brownian motion on a manifold is defined very similarly to the manifold definition itself, where it is the continuous random process that, if you were to zoom in to any small region, looks exactly like "flat" Brownian motion. Specifically, it is the diffusion process whose generator (or the operator describing how expected values of smooth functions evolve with time) is one-half of the Laplace-Beltrami operator of the manifold.

The Laplace-Beltrami operator is the manifold's equivalent of the Laplacian (the sum of second derivatives). On a flat plane, the Laplacian of a function at a point measures how much the function's value at that point differs from its average over a small disk around the point. The Laplace-Beltrami operator does the same thing but uses the intrinsic geometry of the manifold. On the sphere, this operator has a well-known spectrum as its eigenfunctions are the spherical harmonics. This spectrum encodes information about the sphere in the same way that, say, the frequencies of a drum encode information about the drum's shape.

The heat kernel, written `p(t, x, y)`, describes the probability density of finding a Brownian particle at location `y` at time `t`, given that it started at location `x` at time zero. It satisfies the heat equation with respect to the Laplace-Beltrami operator in both the `x` and `y` variables. On a flat plane, the heat kernel is the Gaussian distribution with variance `t`. On the sphere, it's an infinite series involving spherical harmonics, but its qualitative behavior is easy to describe: at short times, it models the flat Gaussian, while at long times, it spreads out and converges to the uniform distribution on the sphere (meaning the particle is equally likely to be anywhere).

### Stochastic Differential Equations on Manifolds

A stochastic differential equation (SDE) describes how a random process evolves over infinitesimally small increments in time. In flat space, Brownian motion satisfies the simplest possible SDE, which means the change in position over a small time interval is a small Gaussian random variable. On a manifold, we need to specify that each small random step lives in the tangent space at the current point. The particle can only move along the surface, not through it or away from it.

Stochastic integrals can be defined in two ways, the Itô convention and the Stratonovich convention. In flat space the difference is minor, but on a manifold the Itô convention produces correction terms (called "Itô-Stratonovich corrections") dependent on how you specify local coordinates. This means that an Itô SDE written in one coordinate system looks different from the same process written in another coordinate system, which can be a problem if you want to define something on the manifold instead of a coordinate chart. The Stratonovich convention transforms calculus under coordinate changes, defining a coordinate-free object. For this reason, Brownian motion on a Riemannian manifold is most naturally expressed as a Stratonovich SDE and hence is the formulation used in this project.

### The Projection Method

We use a technique called the projection method. The idea has three steps:

1. **Propose a step.** Generate a small random vector in the ambient space (ordinary three-dimensional Euclidean space) that lies in the tangent plane at the current point. For the sphere, this means generating a random (Gaussian) vector and subtracting its component in the radial direction, leaving only the component tangent to the surface.

2. **Take the step.** Add the tangent vector scaled by the square root of the time step to the current position. This is the Euler-Maruyama update (the discrete-time approximation to the SDE).

3. **Project back to the surface.** The resulting point will not lie exactly on the manifold (it will be slightly off the surface due to curvature). Project it back. For the sphere, this is normalization: divide the new point by its Euclidean norm. For the torus, this is finding the nearest point on the torus surface.

The error introduced in step 3 is the distance we had to travel to return to the surface. It is proportional to the square of the step size. Since we are taking steps of size proportional to the square root of the time increment, this error is proportional to the time increment itself, which is the same order of error as the Euler-Maruyama approximation. 

### The Heat Kernel

A particularly compelling visualization in this project comes from empirically estimating the heat kernel. The procedure is the following: fix a starting point `x` on the manifold (say, the north pole of the sphere). Run a large number of independent simulated paths all starting at `x`. At several fixed times `t`, record the positions of all particles. Estimate the probability density of those positions using kernel density estimation. This empirical density is an approximation to the heat kernel `p(t, x, ·)`. The visualization shows the density spreading from the starting point, thinning as it expands, and eventually reflecting off the "back" of the sphere and filling it uniformly. On the torus, the density wraps around the edges and interferes with itself. On the hyperbolic plane, it spreads and concentrates toward the boundary without ever returning. 

---

## 4. The Three Surfaces in Detail

### The Sphere

The sphere is the natural first surface because its geometry is familiar and its curvature is
uniform; every point on the sphere looks like every other point. The behavior of Brownian motion on the sphere is well-understood theoretically: it is recurrent (the particle returns arbitrarily close to its starting point infinitely often), and the heat kernel converges to the uniform distribution at a rate governed by the first nontrivial eigenvalue of the Laplace-Beltrami operator.

The sphere also provides the clearest opportunity for validation: the exact heat kernel on the
sphere is known, expressed as a series involving Legendre polynomials. Comparing the empirical
density from simulation to the exact formula at several times gives a concrete accuracy check.

### The Torus

The torus introduces a new geometric feature: it is flat (its Gaussian curvature is zero almost
everywhere), but its global topology is non-trivial. Brownian motion on a flat torus behaves
locally exactly like Brownian motion on a flat plane — but the torus wraps around, so the
particle cannot escape. The invariant distribution is again uniform. The heat kernel on the
torus has a particularly elegant form — it is a sum of flat Gaussians placed at the images of
the starting point under the torus's translation symmetry — which connects the simulation
directly to the theory of theta functions and Fourier analysis on groups.

The torus is also computationally instructive because periodic boundary conditions are a staple technique in physics simulations. Implementing them correctly requires careful modular arithmetic.

### The Hyperbolic Plane (Our Stretch Goal)

The hyperbolic plane is the most striking surface in the project. Its constant
negative curvature has a counterintuitive consequence: there is so much room in the hyperbolic plane that a random walker is transient. The particle drifts to infinity and never returns.
In the Poincaré disk representation, where the entire infinite hyperbolic plane is mapped to the interior of a unit disk, this means the particle's path converges to a point on the boundary circle, chosen at random. This boundary behavior is called the Poisson boundary of the hyperbolic plane.

Unlike the sphere and torus, where the particle cloud eventually fills the space uniformly, the cloud on the hyperbolic plane concentrates toward the boundary circle and never equilibrates.

---

## 5. Implementation Strategy

The project is organized as a Python library with a testable structure. The manifold geometry (how points are represented, how tangent vectors are computed, how the projection step works) is separate from the simulation process (which only knows that it needs a "step" and a "project" operation), which is separate from the visualization layer. Thus, adding a new surface requires implementing only the geometry module for that surface, with no changes to the simulator or the visualizer. It also makes the code testable since each module has clear inputs and outputs that can be verified
independently.

### Performance

The inner loop of a stochastic simulation — stepping thousands of particles forward one time increment at a time — is intensive if written naively in Python. The solution to this vectorization. Instead of iterating over particles one by one, we represent all particle positions as one NumPy array and perform operations simultaneously. NumPy's array operations compile to optimized machine code and can be thousands of times faster than an equivalent Python loop. 

### The App

The Streamlit application provides:

- A surface selector (sphere, torus, or hyperbolic plane).
- A time slider that advances the simulation and re-renders the particle distribution.
- A temperature or diffusivity parameter that controls the step size.
- A starting-point selector for the heat kernel visualization.
- An animated mode that renders the diffusion so the viewer can watch the process occur in real time.

The goal of making an app is to make the mathematics tangible. A viewer who hasn't heard of a Laplace-Beltrami operator can nevertheless gain an accurate intuition for what diffusion on curved space means.

---

## 9. Deliverables

- **A Python library** with implementations of Brownian motion on the sphere and torus, a vectorized Euler-Maruyama simulator, and an empirical heat kernel estimator, all with full docstrings, unit tests, and a one-command setup.
- **Jupyter notebooks** exported to HTML for easy viewing without running any code. Each notebook is designed to be readable as a document.
- **A Streamlit application** with a live animated visualization of the diffusion process unfolding step by step across the selected surface, a heat kernel panel, and interactive controls for all simulation parameters.
- **Technical blog posts** written accessibly for a reader with one year of college mathematics, with the key visualizations embedded inline. These cover mathematical foundations, the geometry of each surface, the Stratonovich SDE formulation, the projection method with error analysis, the Laplace-Beltrami operator, and the heat kernel. Find the blog posts here [link inserted when done]
- **A LinkedIn post, presentation, and demo** of the Streamlit application showing the diffusion process in real time. Find Danielle and JJ's links here [link inserted when done]

---

## 10. Broader Significance

The project also positions naturally as a computational foundation for future work. A follow-on project could study diffusion processes with drift (stochastic gradient flows on a manifold), or the spectral geometry of the Laplace-Beltrami operator, or the connection to sampling algorithms in high-dimensional statistics.

### Connection to Machine Learning

A diffusion model (DDPM, score-based generative model) defines a forward process that gradually adds Gaussian noise to data until the data distribution becomes a standard Gaussian, and then learns to reverse this process. The forward process is a stochastic differential equation, specifically an Ornstein-Uhlenbeck process, and the reversal of that process is Anderson's time-reversal theorem for diffusions, a result in stochastic analysis. The score function the neural network learns to approximate is the logarithmic derivative of the heat kernel with respect to the spatial variable. Every concept in this project -- the heat kernel, the generator, the forward SDE -- appears  in the theory of score-based generative models. Understanding the geometry of diffusion processes significantly helps one understand why these models work.

### Connection to Quantitative Finance

Geometric Brownian motion, the standard model for asset prices in quantitative finance, is the simplest stochastic differential equation in flat space. The mathematical tools developed in this project, including Stratonovich calculus, the diffusion generator, and numerical SDE integration, are just generalized versions of the same tools. A student who has built an SDE simulator on a Riemannian manifold has, implicitly, built and understood the majority of what is needed to work with stochastic volatility models, interest rate models, and the numerical methods used to price exotics.
