---
hide:
  - navigation
---

# wanderwalk

![wanderwalk](assets/wanderwalk-logo.png){ .ww-hero }

Brownian motion on Riemannian 2-manifolds: the sphere, the torus, and the
hyperbolic plane. A small, tested NumPy library for simulating diffusion on
curved surfaces, plus an interactive Streamlit app for watching it happen.

```bash
pip install wanderwalk
```

```python
import numpy as np
import wanderwalk as ww

np.random.seed(0)
trajectory = ww.sphere_simulator(T=200, N=500, dt=0.01, noise_type="isotropic")
final_positions = trajectory[-1]        # (500, 3), every point on the sphere
```

## What this is about

Brownian motion is the random, erratic motion first observed in pollen grains
suspended in water and later given a rigorous mathematical treatment by
Einstein and Wiener. It underlies fields ranging from statistical physics to
quantitative finance, and, more recently, the diffusion models behind modern
generative AI.

The question this project explores is what happens to that random motion when
the space it lives in is curved. A particle wandering on the surface of a
sphere behaves differently from one wandering on a flat plane or on the
surface of a donut: the curvature of the space bends and constrains the
motion.

## The three surfaces

| Surface | Curvature | Behavior | Trajectory shape |
| --- | --- | --- | --- |
| Sphere `S^2` | Positive, constant | Recurrent; the particle distribution converges to uniform over the surface | `(T, N, 3)` |
| Torus `T^2` | Zero on average, non-trivial topology | Particles wrap around the surface  | `(T, N, 3)` |
| Poincare disk `H^2` | Negative, constant | Transient; paths converge to a random point on the boundary circle | `(T, N, 2)` |

The hyperbolic plane has no isometric embedding into three-dimensional space
(Hilbert's theorem), so wanderwalk represents it intrinsically as
2D vectors in the open unit disk. The
[hyperbolic plane tutorial](tutorials/03-hyperbolic.md) covers what follows
from that.

## Where to go next

<div class="grid cards" markdown>

-   __Start here__

    [Getting started](getting-started.md) walks through installation, the
    `ww` alias, and reading a trajectory array.

-   __Learn by surface__

    Six [tutorials](tutorials/01-sphere.md) covering each manifold, the
    lower-level stepping API, density estimation, and the heat kernel.

-   __Look things up__

    The [API reference](reference/index.md) is generated from the docstrings,
    so it always matches the installed version.

-   __Understand the maths__

    [Background](background.md) has the motivation and theory, and the
    [Poincare disk derivation](writeups/2-poincare-disk-derivation.md)
    derives the governing SDE from this project's own conventions.

</div>

## Installation

The library depends only on NumPy:

```bash
pip install wanderwalk
```

Three optional extras cover everything else:

```bash
pip install "wanderwalk[app]"        # Streamlit and Plotly, for the interactive app
pip install "wanderwalk[notebooks]"  # JupyterLab, matplotlib, SciPy
pip install "wanderwalk[docs]"       # MkDocs, for building this site locally
```

Requires Python 3.9 or newer.

## Authors

Jean-Jacques St. Leroux and Danielle Prilepskiy. Released under the
[MIT License](https://github.com/jeanjacquesstleroux/wanderwalk/blob/main/LICENSE).
