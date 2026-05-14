# Differential Geometry Curriculum — Master Checklist
### For: Brownian Motion on Manifolds Project
### Audience: Freshman with calculus, linear algebra, probability
### Structure: Five papers in dependency order

---

## How to Use This Document

Each section corresponds to one paper/set of notes. For every topic listed, your task is threefold:
1. **Understand it yourself** to the point you can derive the key results from scratch
2. **Write an explanation** that a calculus-fluent freshman can follow, using concrete examples before abstract definitions
3. **Ground it in the project**: every major concept has a direct connection to BM on manifolds — state it explicitly at the end of each section in your notes

The papers are in strict dependency order. Do not start Paper N+1 until you can answer the checkpoint questions at the end of Paper N from memory.

---

## Paper 1: Curves and Surfaces in ℝ³

**Goal:** Establish the geometric objects we are working with. By the end, your mentee can describe a sphere and torus as mathematical objects, compute tangent vectors, and understand what it means to measure length on a surface.

---

### Section 0: Prerequisites — Linear Algebra You Actually Need

Work through these before anything else. These are not review for completeness — each item reappears explicitly in the geometry.

**Inner Products and Projections**
- [x] Define the dot product on ℝⁿ as a bilinear, symmetric, positive definite form. State all three properties precisely.
- [x] Define the norm induced by the dot product: |v| = √(v · v)
- [x] Define the angle between two vectors via cos θ = (u · v)/(|u||v|). Derive this from the law of cosines.
- [x] State and prove: two vectors are orthogonal iff their dot product is zero
- [x] Define orthogonal projection of u onto v: proj_v(u) = (u·v / v·v) v
- [x] Define the component of u orthogonal to v: u_⊥ = u − proj_v(u)
- [x] **Key result**: Write the projection onto a subspace W with orthonormal basis {e_1, ..., e_k}: P_W(u) = Σ (u · e_i) e_i. Derive P_{W⊥}(u) = u − P_W(u). This is exactly the formula P_x v = v − (v·x)x used in the BM projection scheme when x is the unit normal.
- [x] Define orthogonal complement W⊥ and prove ℝⁿ = W ⊕ W⊥

**Matrices as Linear Maps**
- [x] State: every linear map T: ℝⁿ → ℝᵐ has a matrix representation [T] depending on the choice of basis
- [ ] Define symmetric matrix (A = Aᵀ) and state the spectral theorem: every symmetric matrix has real eigenvalues and an orthonormal basis of eigenvectors
- [ ] Define positive definite matrix: A is positive definite iff vᵀAv > 0 for all v ≠ 0. Equivalently, all eigenvalues are positive.
- [ ] Define a change-of-basis matrix P and how components of a vector transform: if v = Σ vⁱ eᵢ in basis {eᵢ} and {ẽⱼ} is a new basis, how do the components vⁱ change? (Contravariant transformation rule)
- [ ] State how matrix representations of linear maps change under change of basis: [T]_new = P⁻¹ [T]_old P. This is why eigenvalues are basis-independent.

**Quadratic Forms**
- [ ] Define a quadratic form Q(v) = vᵀAv for symmetric A
- [ ] Note: the first fundamental form (metric tensor) will be a quadratic form — it assigns a positive number to every tangent vector, measuring its squared length

---

### Section 1: Prerequisites — Multivariable Calculus You Actually Need

**Partial Derivatives and the Jacobian**
- [ ] Define partial derivative ∂f/∂xᵢ as the directional derivative along the standard basis vector eᵢ
- [ ] Define the gradient ∇f = (∂f/∂x₁, ..., ∂f/∂xⁿ) as the vector of all partial derivatives
- [ ] Define the directional derivative D_v f = lim_{t→0} [f(x + tv) − f(x)]/t. Prove D_v f = ∇f · v when f is differentiable. This is the chain rule in disguise.
- [ ] Define the Jacobian matrix Df|_x ∈ ℝᵐˣⁿ for a map f: ℝⁿ → ℝᵐ as the matrix of all partial derivatives: [Df]_{ij} = ∂fᵢ/∂xⱼ. Interpret: Df|_x is the best linear approximation to f near x.
- [ ] State the chain rule for compositions: if h = f ∘ g, then Dh|_x = Df|_{g(x)} · Dg|_x. Memorize this — it is used constantly.

**Change of Variables in Integrals**
- [ ] State the substitution formula for a change of variables φ: U ⊂ ℝ² → V ⊂ ℝ²: ∫∫_V f(x,y) dx dy = ∫∫_U f(φ(u,v)) |det Dφ(u,v)| du dv
- [ ] Compute this explicitly for polar coordinates: φ(r,θ) = (r cos θ, r sin θ). Show |det Dφ| = r. Verify the formula for the area of a disk.
- [ ] **Note for later**: the area element on a surface will look like |φ_u × φ_v| du dv, which is a generalization of this determinant formula.

**Second Derivatives**
- [ ] Define the Hessian Hf as the matrix of second partial derivatives: [Hf]_{ij} = ∂²f/∂xᵢ∂xⱼ
- [ ] State Clairaut's theorem: mixed partials commute if f is C², i.e., ∂²f/∂xᵢ∂xⱼ = ∂²f/∂xⱼ∂xᵢ, so Hf is symmetric
- [ ] Write the second-order Taylor expansion: f(x+h) ≈ f(x) + ∇f·h + ½ hᵀ Hf h + O(|h|³)
- [ ] Define the Laplacian Δf = ∇²f = Σᵢ ∂²f/∂xᵢ² = trace(Hf). Compute Δf for f(x,y) = x² + y², f(x,y,z) = 1/|x|.

---

### Section 2: Parametric Curves in ℝ³

The goal here is to build intuition for how calculus interacts with geometry. Surfaces are parametrized analogously to curves, and every concept here has a direct surface analog.

**Parametrization and Velocity**
- [ ] Define a parametric curve γ: I ⊂ ℝ → ℝ³ as a smooth map. The image γ(I) ⊂ ℝ³ is the curve; t is just a label.
- [ ] Define the velocity vector γ'(t) = dγ/dt. Interpret geometrically: it is the tangent direction to the curve at γ(t). Its magnitude |γ'(t)| is the speed.
- [ ] Define a regular curve: γ'(t) ≠ 0 for all t. Explain why this is needed (without it, the parametrization can have cusps or the tangent direction is undefined).
- [ ] Define arc length: L(γ) = ∫_a^b |γ'(t)| dt. Show this is independent of reparametrization (compute for γ(t) and γ(φ(s)) where φ is a reparametrization).
- [ ] Define arc-length parametrization (unit speed): |γ'(t)| = 1 for all t. Show every regular curve can be reparametrized by arc length.

**Curvature of a Curve**
- [ ] Define the unit tangent vector T(t) = γ'(t)/|γ'(t)|
- [ ] Define curvature κ = |dT/ds| where s is arc length. Interpret: how fast does the tangent direction turn per unit length traveled?
- [ ] Compute curvature for a circle of radius R: show κ = 1/R (larger circle → smaller curvature → "flatter"). This is the prototype intuition for surface curvature.
- [ ] Define the principal normal vector N = (dT/ds)/κ. It points toward the center of curvature.
- [ ] State the Frenet-Serret formula: dT/ds = κN. This is a preview of the covariant derivative.
- [ ] **Project connection**: A Brownian path on a surface is a curve. The curvature of the surface will constrain how such paths can behave. On S², every geodesic (straightest possible path) is a great circle with the same curvature as a circle of radius R.

---

### Section 3: Regular Surfaces in ℝ³

**Parametrized Surfaces**
- [ ] Define a parametrized surface patch: φ: U ⊂ ℝ² → ℝ³, a smooth map. U is the parameter domain.
- [ ] Define the partial derivatives (tangent vectors): φ_u = ∂φ/∂u, φ_v = ∂φ/∂v. These are vectors in ℝ³.
- [ ] Interpret φ_u and φ_v: they span the tangent plane at φ(u,v).
- [ ] Define a regular point: a point where φ_u × φ_v ≠ 0. The cross product being nonzero means the tangent vectors are linearly independent, so the tangent plane is well-defined.
- [ ] Define a regular surface: a surface that can be covered by patches that are all regular everywhere.

**Concrete Computations: Sphere S²**
- [ ] Parametrize S² = {(x,y,z) ∈ ℝ³ : x² + y² + z² = 1} using spherical coordinates: φ(θ,φ) = (sin θ cos φ, sin θ sin φ, cos θ) for θ ∈ (0,π), φ ∈ (0,2π)
- [ ] Compute φ_θ and φ_φ explicitly
- [ ] Compute φ_θ × φ_φ. Show it is nonzero for θ ∈ (0,π) (i.e., away from poles). Conclude S² is a regular surface.
- [ ] Note: two patches are needed to cover the sphere (the poles require separate treatment). This is a topological subtlety — do not paper over it.

**Concrete Computations: Torus T²**
- [ ] Parametrize T² with parameters (u,v), u ∈ [0,2π), v ∈ [0,2π), with R = major radius (distance from z-axis to tube center), r = minor radius (tube radius): φ(u,v) = ((R + r cos v) cos u, (R + r cos v) sin u, r sin v)
- [ ] Compute φ_u and φ_v explicitly (work this out by hand)
- [ ] Compute φ_u × φ_v. Show its magnitude is r(R + r cos v). Note: this is NOT constant. The outer equator (v=0) has magnitude r(R+r), the inner equator (v=π) has magnitude r(R-r). **This is the origin of the non-uniform invariant measure.**
- [ ] Show T² is a regular surface (assuming R > r).

**The Tangent Plane**
- [ ] Define the tangent plane at a point p = φ(u₀, v₀): T_p S = span{φ_u(u₀,v₀), φ_v(u₀,v₀)} ⊂ ℝ³
- [ ] Note: the tangent plane is a 2D linear subspace of ℝ³ (technically an affine subspace of ℝ³, centered at p)
- [ ] Define the unit normal N = (φ_u × φ_v)/|φ_u × φ_v|. Show N is perpendicular to both tangent vectors.
- [ ] Define the tangent space T_p S = {v ∈ ℝ³ : v · N(p) = 0}. This is the set of all vectors tangent to the surface at p. It is a 2-dimensional subspace of ℝ³.
- [ ] **Project connection**: The projection formula P_x v = v − (v · N(x)) N(x) is exactly the orthogonal projection from ℝ³ onto T_x S. For S², N(x) = x, recovering P_x v = v − (v·x)x.

**Checkpoint: Before proceeding, you should be able to answer these without notes**
- [ ] Write the parametrization of S² and T². Compute φ_u, φ_v for each.
- [ ] Compute the unit normal N(x) for the sphere at an arbitrary point. Verify N(x) = x.
- [ ] Write the projection formula T_x S² → T_x S² and explain in words what it does geometrically.
- [ ] Why is the tangent plane only defined at regular points?

---

## Paper 2: The First Fundamental Form — Measuring Geometry on a Surface

**Goal:** Understand how to measure lengths, angles, and areas intrinsically on a surface. This is the metric. By the end, you should be able to write down the metric tensor for S² and T², compute areas, and understand what "Riemannian geometry" means at an intuitive level.

---

### Section 4: The First Fundamental Form

**Definition and Motivation**
- [ ] Motivate: on a surface, how do we measure the length of a curve γ(t) = φ(u(t), v(t))? Compute γ'(t) = φ_u u' + φ_v v'. Then |γ'|² = (φ_u u' + φ_v v') · (φ_u u' + φ_v v') = (φ_u · φ_u)(u')² + 2(φ_u · φ_v) u'v' + (φ_v · φ_v)(v')²
- [ ] Define the coefficients of the first fundamental form: E = φ_u · φ_u, F = φ_u · φ_v, G = φ_v · φ_v
- [ ] Write the metric tensor as a 2×2 matrix: g = [[E, F], [F, G]]. State: g is symmetric and positive definite (since the surface is regular).
- [ ] Rewrite arc length: L = ∫ √(E u'² + 2F u'v' + G v'²) dt. This is the arc length formula in terms of surface parameters.
- [ ] Define the area element: dA = |φ_u × φ_v| du dv = √(EG − F²) du dv. (Derive this: |φ_u × φ_v|² = |φ_u|²|φ_v|² − (φ_u · φ_v)² = EG − F².)
- [ ] State: all of these measurements — length, angle, area — depend only on the functions E, F, G, not on the ambient ℝ³. This is the beginning of intrinsic geometry.

**Concrete Computations: S²**
- [ ] With spherical parametrization φ(θ,φ): compute E, F, G
  - E = φ_θ · φ_θ = 1
  - F = φ_θ · φ_φ = 0
  - G = φ_φ · φ_φ = sin²θ
- [ ] Write the metric: ds² = dθ² + sin²θ dφ². This is the standard round metric on S².
- [ ] Compute the area element: dA = sin θ dθ dφ. Verify: ∫∫ dA = 4π (total area of unit sphere).
- [ ] Compute arc length of a great circle: parametrize as θ ↦ (θ, 0), length = ∫₀^π dθ = π. Correct.

**Concrete Computations: T²**
- [ ] With torus parametrization φ(u,v): compute E, F, G
  - E = φ_u · φ_u = (R + r cos v)²
  - F = φ_u · φ_v = 0
  - G = φ_v · φ_v = r²
- [ ] Write the metric: ds² = (R + r cos v)² du² + r² dv²
- [ ] Compute the area element: dA = r(R + r cos v) du dv. **This is the same expression that appears in the invariant measure calculation.** Make this connection explicit in your notes.
- [ ] Compute the total area of T²: ∫₀^{2π}∫₀^{2π} r(R + r cos v) du dv = 4π²Rr

**The Metric Tensor in Index Notation**
- [ ] Introduce Einstein summation convention: repeated upper and lower indices are summed. Write g_{ij} for the metric tensor components (i,j ∈ {1,2}).
- [ ] Define the inverse metric g^{ij}: the matrix inverse of g_{ij}. For the diagonal cases (F=0): g^{uu} = 1/E, g^{vv} = 1/G.
- [ ] State: the metric g_{ij} allows us to lower indices (convert vectors to covectors). The inverse g^{ij} raises indices. This will be needed for the Laplace-Beltrami formula.
- [ ] **Why this notation matters**: the Laplace-Beltrami operator is written Δ_g f = (1/√|g|) ∂_i(√|g| g^{ij} ∂_j f). Every symbol in this formula is something you have now defined.

**Isometries**
- [ ] Define an isometry between surfaces S and S̃: a diffeomorphism f: S → S̃ that preserves the first fundamental form (lengths and angles).
- [ ] State: the flat torus ℝ²/ℤ² is isometric to itself, but NOT isometric to the embedded torus T² in ℝ³. They have the same topology but different geometries. **This is why "converges to uniform" is wrong for the embedded torus — the geometry is different.**
- [ ] Concrete example: show that unrolling a cylinder onto a flat strip is an isometry (the metric on the cylinder is ds² = dz² + dθ², same as the flat metric in Cartesian coordinates after unrolling). The cylinder and the plane are locally isometric but globally different.

---

### Section 5: The Second Fundamental Form and Curvature

**Motivation**
- [ ] State the question: the first fundamental form measures intrinsic geometry (lengths, angles). But how "curved" is the surface? A cylinder has E=G=1, F=0 just like the plane — they are locally isometric — yet a cylinder is clearly curved in ℝ³. The second fundamental form captures this extrinsic curvature.

**Definition**
- [ ] Define the second derivatives of φ: φ_{uu}, φ_{uv}, φ_{vv} (compute these for practice on S² and T²)
- [ ] Note: φ_{uu} is not necessarily tangent to the surface. Decompose it: φ_{uu} = (tangential component) + (normal component). The normal component is L N where L = φ_{uu} · N.
- [ ] Define the coefficients of the second fundamental form: L = φ_{uu} · N, M = φ_{uv} · N, N_coeff = φ_{vv} · N (note: overloaded notation — use e, f, g or L, M, N carefully in your notes)
- [ ] Write the second fundamental form matrix: II = [[L, M], [M, N_coeff]]

**Principal Curvatures**
- [ ] Define the shape operator (Weingarten map) W: T_pS → T_pS by W = g⁻¹ · II (matrix product of inverse metric with second fundamental form). It measures how the normal N changes as you move along the surface.
- [ ] Define principal curvatures k₁, k₂: the eigenvalues of W. The corresponding eigenvectors are the principal directions.
- [ ] Define Gaussian curvature K = k₁ k₂ = det(II)/det(g). This is the product of the two principal curvatures.
- [ ] Define mean curvature H = (k₁ + k₂)/2 = trace(W)/2. This is the average of the two principal curvatures.

**Concrete Computations: S²**
- [ ] Compute II for S²: show L = 1, M = 0, N_coeff = sin²θ (using the computed normal N = −φ, the inward normal for the unit sphere)
- [ ] Compute k₁ = k₂ = 1. S² is a sphere with both principal curvatures equal to 1/R (for unit sphere, R=1).
- [ ] K = 1, H = 1. S² has constant positive Gaussian curvature.

**Concrete Computations: T²**
- [ ] Compute N (the unit normal) for the torus: N(u,v) = (cos v cos u, cos v sin u, sin v). Show this directly from the cross product calculation.
- [ ] Compute L, M, N_coeff for the torus
- [ ] Compute the principal curvatures: k₁ = cos v / (R + r cos v), k₂ = 1/r
- [ ] Compute Gaussian curvature: K = cos v / (r(R + r cos v))
- [ ] **Key observation**: K > 0 when cos v > 0 (outer half of the torus), K = 0 on the top/bottom circles (v = π/2, 3π/2), K < 0 when cos v < 0 (inner half). The torus has regions of all three signs of curvature. Draw this.
- [ ] Compute mean curvature: H = (R + 2r cos v)/(2r(R + r cos v))

**Theorema Egregium (Statement Only)**
- [ ] State Gauss's Theorema Egregium: the Gaussian curvature K is an intrinsic invariant — it can be computed from the first fundamental form alone, without reference to the ambient ℝ³. This is non-obvious: K = k₁k₂ is defined extrinsically via the shape operator, but Gauss showed it depends only on g_{ij}.
- [ ] State the formula (Brioschi formula): K = [expression in E, F, G and their derivatives — look this up in Pressley]. You do not need to derive it, but you should state it.
- [ ] Corollary: a flat map of the sphere cannot preserve distances (any map from S² to ℝ² must distort lengths). This is why no world map is perfectly accurate.
- [ ] **Project connection**: Gaussian curvature will appear in the Gauss-Bonnet theorem and influences the spectral theory of the Laplace-Beltrami operator.

**Checkpoint: Before proceeding, you should be able to answer these without notes**
- [ ] State the first and second fundamental forms for S² and T². What do their components measure?
- [ ] State the Gaussian curvature of S². Explain in words: what does K=1 mean geometrically?
- [ ] For the torus, identify the regions of positive, zero, and negative curvature. Draw it.
- [ ] Explain in one sentence why the cylinder and the plane are locally isometric but S² and the plane are not.

---

## Paper 3: Geodesics and the Covariant Derivative

**Goal:** Understand geodesics (the "straight lines" on a surface) and the covariant derivative (the "correct" notion of differentiation on a surface). These two concepts together are the geometric foundation of BM on manifolds. The covariant derivative is the hardest concept in the series.

---

### Section 6: Geodesics

**Motivation and Definition**
- [ ] State the question: on ℝⁿ, straight lines minimize length between two points. On a surface, what plays the role of a straight line? Two equivalent answers: (1) curves that locally minimize length, (2) curves whose acceleration is always normal to the surface (no tangential acceleration).
- [ ] Define geodesic via the second characterization: γ is a geodesic if γ''(t) is perpendicular to T_{γ(t)}S at every point, i.e., the tangential component of γ'' is zero.
- [ ] Derive the geodesic equations in terms of surface parameters (u(t), v(t)):
  - u'' + Γ^u_{uu}(u')² + 2Γ^u_{uv}u'v' + Γ^u_{vv}(v')² = 0
  - v'' + Γ^v_{uu}(u')² + 2Γ^v_{uv}u'v' + Γ^v_{vv}(v')² = 0
- [ ] The symbols Γ^k_{ij} are called Christoffel symbols — define them (see next section). For now, note that geodesics depend on the first fundamental form alone.

**Christoffel Symbols**
- [ ] Define the Christoffel symbols of the first kind: [ij, k] = ½(∂_i g_{jk} + ∂_j g_{ik} − ∂_k g_{ij})
- [ ] Define the Christoffel symbols of the second kind: Γ^k_{ij} = g^{kl} [ij, l] (raise the last index with the inverse metric)
- [ ] Physical interpretation: Γ^k_{ij} measures how much the basis vector ∂_j "tilts" in the eₖ direction as you move in the eᵢ direction. They encode all the information about how the coordinate system curves.
- [ ] Compute Christoffel symbols for S² (spherical coordinates): 
  - The nonzero ones are Γ^θ_{φφ} = −sin θ cos θ and Γ^φ_{θφ} = Γ^φ_{φθ} = cos θ / sin θ
  - Verify this computation step by step
- [ ] Compute Christoffel symbols for T² (write out all nonzero ones):
  - Γ^u_{uv} = Γ^u_{vu} = −r sin v / (R + r cos v), Γ^v_{uu} = sin v (R + r cos v) / r

**Geodesics on Specific Surfaces**
- [ ] Geodesics on S²: show that great circles satisfy the geodesic equations. Parametrize a great circle and verify.
- [ ] Geodesics on T²: the geodesics of the embedded torus are complicated. State that they exist (by the existence theorem for ODEs applied to the geodesic equations) but do not have simple closed-form expressions in general.
- [ ] Geodesics on ℝ²: show that Christoffel symbols vanish in Cartesian coordinates, and the geodesic equations reduce to u'' = v'' = 0, so geodesics are straight lines. Verify this is consistent with the definition.

**The Exponential Map**
- [ ] Define exp_p: T_pS → S by exp_p(v) = γ(1) where γ is the geodesic starting at p with velocity v
- [ ] State: exp_p is defined on a neighborhood of 0 in T_pS and is a local diffeomorphism near 0 (by the inverse function theorem + ODE existence/uniqueness)
- [ ] Interpret geometrically: exp_p(v) is the point you reach if you walk in direction v for |v| units of arc length along the geodesic
- [ ] **Project connection**: the "correct" formulation of Euler-Maruyama on a manifold uses the exponential map: X_{n+1} = exp_{X_n}(√Δt · Z_n) where Z_n is a tangent vector at X_n. The projection scheme we use is an approximation to this that works well for small Δt.

---

### Section 7: The Covariant Derivative

This is the conceptually hardest section. Take more time here than anywhere else.

**The Problem with Ordinary Differentiation**
- [ ] State the problem: if V(t) is a vector field along a curve γ(t) on a surface, and we want to differentiate V, the naive derivative V'(t) = dV/dt is a vector in ℝ³ that may point off the surface. We need a notion of derivative that stays tangential.
- [ ] Concrete example: take γ(t) to be a meridian on S² (a great circle at fixed φ). The tangent field V(t) = γ'(t) is always tangent to S². Compute V'(t) in ℝ³ — it points toward the center of the sphere, i.e., normal to S². So V'(t) is not a tangent vector. The "intrinsic" rate of change of V along γ is zero (V is a geodesic, so it parallel transports its own tangent vector), but the ambient derivative is nonzero.
- [ ] Define the covariant derivative: ∇_{γ'(t)} V = (V'(t))_T = V'(t) − (V'(t) · N) N, the projection of V'(t) onto the tangent plane. This is the tangential component of V'(t).

**Parallel Transport**
- [ ] Define: a vector field V(t) along γ(t) is parallel if ∇_{γ'(t)} V = 0, i.e., the covariant derivative is identically zero along the curve. The vector is "not rotating" intrinsically as you move along γ.
- [ ] Give the key example: transport a tangent vector on S² along a spherical triangle (1/8 of the sphere). When you return to the start, the vector has rotated by π/2. This is holonomy — a direct consequence of curvature. Draw this.
- [ ] State: parallel transport preserves the inner product between vectors. If V, W are both parallel along γ, then d/dt (V · W) = 0.
- [ ] Connect to Christoffel symbols: the parallel transport equation in coordinates is dVᵏ/dt + Γᵏ_{ij} (dxⁱ/dt) Vʲ = 0. The Christoffel symbols measure the "correction" needed to keep a vector parallel.

**The Covariant Derivative for Vector Fields (not just along curves)**
- [ ] Define the Levi-Civita connection ∇_X Y for vector fields X, Y on S: it is the unique connection that (1) is compatible with the metric (preserves inner products under parallel transport), and (2) is torsion-free (∇_X Y − ∇_Y X = [X,Y]).
- [ ] State: uniqueness of the Levi-Civita connection is Theorem 7.1 in Pressley. Do not prove it, but state it precisely: these two conditions uniquely determine all the Christoffel symbols Γᵏ_{ij}.
- [ ] In coordinates: ∇_∂ᵢ ∂ⱼ = Σₖ Γᵏ_{ij} ∂ₖ. The Christoffel symbols are exactly the components of the covariant derivative of basis vectors.
- [ ] **Project connection**: The covariant derivative is why BM on a manifold requires the Stratonovich formulation. The Itô formula with ordinary derivatives does not respect the geometric structure (it does not transform correctly under isometries). The Stratonovich formula uses the Levi-Civita connection implicitly, and it does transform correctly.

**The Riemann Curvature Tensor (Conceptual Only)**
- [ ] Define: the Riemann curvature tensor R(X,Y)Z = ∇_X ∇_Y Z − ∇_Y ∇_X Z − ∇_{[X,Y]} Z. It measures the failure of covariant derivatives to commute.
- [ ] State: for surfaces in ℝ³, R is determined entirely by the Gaussian curvature K.
- [ ] Intuition: on a flat plane, parallel transport around any closed loop returns the vector unchanged (R=0). On a curved surface, parallel transport around a loop rotates the vector — the rotation angle equals K times the enclosed area (Gauss-Bonnet). This is why holonomy measures curvature.
- [ ] You do not need to compute R explicitly for this project, but you must know what it measures.

**Checkpoint: Before proceeding, you should be able to answer these without notes**
- [ ] Define the covariant derivative ∇_{γ'} V in words and in formula
- [ ] Explain the parallel transport example on S² (spherical triangle). Why does the vector rotate?
- [ ] Write the geodesic equation using covariant derivatives: ∇_{γ'} γ' = 0 (the acceleration is zero intrinsically)
- [ ] What are Christoffel symbols measuring? Write the formula for Γᵏ_{ij} in terms of the metric.
- [ ] Why does the covariant derivative matter for stochastic processes on manifolds?

---

## Paper 4: Abstract Manifolds, the Laplace-Beltrami Operator

**Goal:** Generalize from surfaces in ℝ³ to abstract Riemannian manifolds. Define the Laplace-Beltrami operator and compute it explicitly on S² and T². This is the differential operator that generates Brownian motion.

---

### Section 8: Smooth Manifolds (Lightweight Treatment)

**Why Abstract Manifolds?**
- [ ] Motivate: the Poincaré hyperbolic disk H² is not naturally a surface in ℝ³ with an induced metric. It is defined abstractly as a set with a Riemannian metric imposed on it. To handle H², we need the abstract framework.
- [ ] For S² and T², the abstract framework produces the same results as the embedded framework — so mastering the embedded case first is the right approach.

**Definitions (State Precisely, Do Not Derive)**
- [ ] Define a topological manifold of dimension n: a Hausdorff topological space M such that every point has a neighborhood homeomorphic to ℝⁿ
- [ ] Define a chart (U, φ): an open set U ⊂ M and a homeomorphism φ: U → ℝⁿ. The functions φ give local coordinates.
- [ ] Define a smooth atlas: a collection of charts {(U_α, φ_α)} that cover M, such that all transition maps φ_β ∘ φ_α⁻¹ are smooth
- [ ] Define a smooth manifold: a topological manifold with a smooth atlas
- [ ] Define the tangent space T_pM at p ∈ M: the set of equivalence classes of curves through p, where two curves are equivalent if they have the same velocity in local coordinates. This is the abstract version of the tangent plane.
- [ ] State: T_pM is an n-dimensional real vector space. The tangent bundle TM = ∪_p T_pM is the collection of all tangent spaces.

**Riemannian Metric (Abstract)**
- [ ] Define a Riemannian metric g: an assignment of an inner product g_p: T_pM × T_pM → ℝ to each tangent space T_pM, varying smoothly in p
- [ ] State: in local coordinates (x¹,...,xⁿ), g is a smooth matrix-valued function g_{ij}(x) that is symmetric and positive definite at every point
- [ ] Define a Riemannian manifold: a smooth manifold with a Riemannian metric
- [ ] Connect: for a surface S ⊂ ℝ³ with parametrization φ, the first fundamental form g_{ij} = ∂ᵢφ · ∂ⱼφ is exactly a Riemannian metric in the abstract sense. The abstract framework recovers everything we have done.

**The Poincaré Disk H²**
- [ ] Define H² = {(x,y) ∈ ℝ² : x² + y² < 1} (the open unit disk) with metric: g_{ij} = (4/(1−r²)²) δ_{ij} where r² = x² + y²
- [ ] This means ds² = 4(dx² + dy²)/(1−r²)² — the metric is the Euclidean metric scaled by a position-dependent conformal factor
- [ ] Note: as r → 1 (approaching the boundary), the conformal factor blows up — distances near the boundary are much larger than they appear in the disk. This is why "equal" triangles near the boundary look smaller.
- [ ] Compute the area element: dA = 4 dx dy / (1−r²)². Show the total area of H² is infinite.
- [ ] State the Gaussian curvature of H²: K = −1 everywhere. H² is the unique (up to scaling) simply connected surface of constant negative curvature.
- [ ] **Project connection**: BM on H² does NOT converge to a uniform distribution — H² has infinite volume. Instead, BM paths converge to the boundary circle almost surely (the Martin boundary). This is the striking visual in the stretch goal.

---

### Section 9: The Laplace-Beltrami Operator

**Motivation**
- [ ] Recall: on ℝⁿ, the Laplacian Δf = Σ ∂²f/∂xᵢ² generates Brownian motion. If we run BM in ℝⁿ and test it with a smooth function f, the expected rate of change of f along the path is ½ Δf. We need the analog of this for a Riemannian manifold.

**Definition**
- [ ] Recall: the gradient in ℝⁿ satisfies ∇f · v = D_v f (directional derivative). On a manifold, define the Riemannian gradient grad f as the unique tangent vector satisfying g(grad f, v) = df(v) for all tangent vectors v.
- [ ] In coordinates: (grad f)ⁱ = g^{ij} ∂_j f. The inverse metric raises the index.
- [ ] Define the divergence of a vector field X: div X = (1/√|g|) ∂_i(√|g| Xⁱ). This is the generalization of ∇ · X that accounts for the volume distortion of the metric.
- [ ] Define the Laplace-Beltrami operator: Δ_g f = div(grad f) = (1/√|g|) ∂_i(√|g| g^{ij} ∂_j f)
- [ ] Show this reduces to the ordinary Laplacian in Cartesian coordinates on ℝⁿ: g_{ij} = δ_{ij}, √|g| = 1, so Δ_g f = ∂_i(∂ⁱf) = Σ ∂²f/∂xᵢ².

**Concrete Computations: S²**
- [ ] With metric g_{θθ} = 1, g_{φφ} = sin²θ, F=0: compute √|g| = sin θ
- [ ] Compute grad f: (grad f)^θ = ∂f/∂θ, (grad f)^φ = (1/sin²θ) ∂f/∂φ
- [ ] Compute Δ_{S²} f = (1/sin θ) [∂/∂θ(sin θ ∂f/∂θ) + (1/sin θ) ∂²f/∂φ²]
- [ ] Verify: for f(θ,φ) = cos θ (which is z restricted to S²), compute Δ_{S²} f = −2 cos θ = −2f. Conclude that f = cos θ is an eigenfunction of Δ_{S²} with eigenvalue −2 = −l(l+1) for l=1.
- [ ] State (without full derivation): the eigenfunctions of −Δ_{S²} are the spherical harmonics Y^m_l with eigenvalues l(l+1). They form a complete orthonormal basis for L²(S²). This is the spectral theory of the sphere.

**Concrete Computations: T²**
- [ ] With metric g_{uu} = (R + r cos v)², g_{vv} = r², F=0: compute √|g| = r(R + r cos v)
- [ ] Compute Δ_{T²} f = [1/(r(R + r cos v))] { ∂/∂u[(r/(R + r cos v)) ∂f/∂u] + ∂/∂v[((R + r cos v)/r) ∂f/∂v] }
- [ ] Simplify for u-direction: since ∂/∂u[(1/(R+r cos v)) ∂f/∂u] = (1/(R+r cos v)) ∂²f/∂u²
- [ ] Simplify for v-direction: this involves a derivative of (R + r cos v) which produces a sin v term
- [ ] Write the full expression. Note it is not separable (the v-coefficient of ∂²f/∂v² depends on v), confirming that the embedded torus does not have a clean eigenfunction decomposition.

**The Invariant Measure Connection**
- [ ] State: the Laplace-Beltrami operator is self-adjoint with respect to the Riemannian volume measure dμ_g = √|g| du dv. This means ∫ f Δ_g h dμ_g = ∫ (Δ_g f) h dμ_g for smooth f, h.
- [ ] State and derive: the Riemannian volume measure dμ_g is the invariant measure of BM. That is, if X₀ has distribution dμ_g (normalized), then X_t has the same distribution for all t. This follows from the self-adjointness of Δ_g.
- [ ] **For T²**: dμ_g = r(R + r cos v) du dv. This is not uniform. Write out the normalized version: the probability density is p(u,v) = r(R + r cos v) / (4π²Rr) = (R + r cos v)/(4π²R). **This is the theoretical target distribution your simulation must match.**
- [ ] **For S²**: dμ_g = sin θ dθ dφ. Normalized: p(θ,φ) = sin θ / (4π). Uniform in φ, biased toward the equator (where sin θ is larger). In Cartesian coordinates this is just uniform on the sphere.

**Checkpoint: Before proceeding, you should be able to answer these without notes**
- [ ] Write the formula for Δ_g f from memory. Define every symbol in it.
- [ ] Compute Δ_{S²}(cos θ) and confirm it equals −2 cos θ
- [ ] What is the invariant measure for BM on the embedded T²? Why is it not uniform in (u,v)?
- [ ] State the relationship between Δ_g and the generator of BM on a manifold

---

## Paper 5: Stochastic Processes on Riemannian Manifolds

**Goal:** Connect everything above to the actual simulation. Understand why the projection scheme works, why Stratonovich is required, and what "Brownian motion on a manifold" means precisely. This paper assumes working knowledge of Itô calculus (which JJ already has).

---

### Section 10: Itô vs. Stratonovich — The Coordinate Problem

**Review of Itô Calculus on ℝⁿ**
- [ ] State Itô's formula: for X_t satisfying dX = b dt + σ dW and f smooth: df(X_t) = ∂f/∂xᵢ dXⁱ + ½ σσᵀ_{ij} ∂²f/∂xᵢ∂xⱼ dt. The second-order term is the Itô correction.
- [ ] State Stratonovich's formula: for the same X_t, with ∘ denoting Stratonovich integral: df(X_t) = ∂f/∂xᵢ ∘ dXⁱ. No second-order correction. The chain rule holds in its classical form.
- [ ] State the conversion formula: X ∘ dW = X dW + ½ d[X, W]_t where [X, W]_t is the quadratic covariation. For σ(X_t): Stratonovich drift = Itô drift + ½ σ(X) σ'(X).

**Why Itô Fails on Manifolds**
- [ ] State the problem: suppose X_t ∈ S and we change coordinates y = φ(x) (a diffeomorphism). The Itô formula for y(X_t) gives: dy = Dφ(X) dX + ½ trace(D²φ(X) σσᵀ) dt. The second term is NOT intrinsic — it depends on the coordinate change φ, not just the geometry of S.
- [ ] Consequence: if you write an Itô SDE in one coordinate chart and transform it to another chart, you get a different SDE with extra drift terms. This means Itô SDEs are NOT coordinate-invariant — two observers using different parametrizations would disagree about what process is running.
- [ ] State: the Stratonovich SDE transforms correctly: dy = Dφ(X) ∘ dX, with no extra drift terms. Stratonovich SDEs are coordinate-invariant.
- [ ] **Conclusion**: the intrinsic Brownian motion on a manifold must be defined via a Stratonovich SDE. Any Itô representation will have extra drift terms (the Itô-Stratonovich correction) involving the Christoffel symbols.

**The Itô-Stratonovich Correction on S²**
- [ ] State the Itô form of BM on S² (unit sphere in ℝ³): dXⁱ = (Pᵢⱼ(X)/1) dWʲ − ½(n−1) Xⁱ dt where P_{ij}(x) = δ_{ij} − xᵢxⱼ is the projection matrix and n=3
- [ ] Interpret: the drift term −Xⁱ dt points inward (toward the origin). In the Itô representation, BM on S² needs a drift to stay on the sphere.
- [ ] The Stratonovich form: dXⁱ = Pᵢⱼ(X) ∘ dWʲ. No drift term. The projection handles everything.
- [ ] Verify the two are equivalent by computing the Itô correction: for σᵢⱼ = Pᵢⱼ(X), ½ Σⱼ (∂σᵢⱼ/∂xₖ) σₖⱼ = −Xⁱ. So Stratonovich = Itô form + drift −Xⁱ dt. The Itô-to-Stratonovich correction exactly cancels the inward drift.

**Why the Projection Scheme Implements Stratonovich**
- [ ] The Euler-Maruyama scheme for the Stratonovich SDE dX = σ(X) ∘ dW: X_{n+1} = X_n + σ(X_n) ΔW_n + ½ Σⱼ (∂σᵢⱼ/∂xₖ σₖⱼ)(X_n) Δt + O(Δt^{3/2})
- [ ] The projection scheme: X̃_{n+1} = X_n + √Δt · P_{X_n}(Z_n), then X_{n+1} = X̃_{n+1}/|X̃_{n+1}| (for sphere)
- [ ] Show: to first order in Δt, X_{n+1} = X_n + P_{X_n}(√Δt Z_n) − ½ (X_n · (√Δt Z_n)²) X_n + O(Δt^{3/2}). The second term contributes an O(Δt) drift. Compute its expectation: E[½ (X_n · √Δt Z_n)² X_n] = ½ Δt · E[Z^T P_X Z] X_n = ½ Δt (n-1) X_n dt where n-1 = 2 for S² ⊂ ℝ³. This is exactly the Itô-Stratonovich correction, so the scheme is consistent with the Stratonovich formulation.
- [ ] **Conclusion to write in notes**: the re-normalization after each step automatically incorporates the Itô correction, so the projection scheme implements Stratonovich EM without any extra drift term needing to be computed explicitly.

---

### Section 11: Brownian Motion on a Manifold

**Definition**
- [ ] Define Brownian motion on a Riemannian manifold (M, g): a continuous stochastic process X_t on M with generator ½ Δ_g. Equivalently, for every smooth f: M → ℝ, f(X_t) − f(X_0) − ½ ∫₀ᵗ Δ_g f(X_s) ds is a martingale.
- [ ] State (without proof): BM on M can be constructed as the solution to the Stratonovich SDE on M corresponding to choosing σ to be the "square root" of the metric g. For S² and T², the projection scheme implements this.
- [ ] State: BM on M is the diffusion whose transition density p_t(x, y) solves the heat equation ∂_t p = ½ Δ_g p with initial condition p_0(x, ·) = δ_x.

**The Heat Kernel**
- [ ] Define the heat kernel p_t(x, y): the fundamental solution to ∂_t u = ½ Δ_g u. It is simultaneously (1) the transition density of BM (P_x(X_t ∈ dy) = p_t(x,y) dμ_g(y)), and (2) the Green's function for the heat equation.
- [ ] State properties: p_t(x,y) > 0, ∫ p_t(x,y) dμ_g(y) = 1, p_{s+t}(x,y) = ∫ p_s(x,z) p_t(z,y) dμ_g(z) (Chapman-Kolmogorov)
- [ ] Heat kernel on S²: via spectral expansion. If φ_l are eigenfunctions of Δ_g with eigenvalues −λ_l: p_t(x,y) = Σ_l e^{−λ_l t/2} Σ_m φ_{lm}(x) φ_{lm}(y). For S², λ_l = l(l+1), eigenfunctions are spherical harmonics Y^m_l, and: p_t(x,y) = Σ_{l=0}^∞ [(2l+1)/(4π)] e^{−l(l+1)t/2} P_l(cos d(x,y)) where d(x,y) is geodesic distance and P_l is the Legendre polynomial.
- [ ] Verify: as t → ∞, all terms except l=0 vanish, leaving p_∞(x,y) = 1/(4π) = uniform density on S². This is the correct long-time behavior on S².
- [ ] For T²: the spectral expansion does not simplify cleanly (see Paper 4, Section 9 notes). The long-time limit is p_∞(u,v) = (R + r cos v)/(4π²R), which is the normalized invariant measure.

**Euler-Maruyama Convergence**
- [ ] State the strong convergence theorem for EM: under Lipschitz conditions on σ and b, the EM scheme converges with strong order ½ (i.e., E[|X_T − X̃_T|²] = O(Δt)).
- [ ] State the weak convergence theorem: for smooth test functions f, |E[f(X_T)] − E[f(X̃_T)]| = O(Δt). Weak order 1.
- [ ] State: the geometric projection introduces an O(Δt) error per step from the constraint manifold (points are pushed slightly off the surface before renormalization). This does not degrade the order of convergence but affects the constant.
- [ ] **Practical implication**: use Δt ≤ 0.01 for S² and T² simulations. At Δt = 0.1, the approximation error is large enough to see visually in the distribution plots.

**Checkpoint: All Papers Complete**
- [ ] Write the Stratonovich SDE for BM on S² without notes
- [ ] Explain in words why Itô fails on manifolds (coordinate non-invariance argument)
- [ ] Derive the Itô form of BM on S² and identify the inward drift term
- [ ] Explain why the projection + renormalize scheme implements Stratonovich, not Itô
- [ ] Write the heat kernel formula for S²; identify the eigenvalues, eigenfunctions, and long-time limit
- [ ] State the invariant measures for S² and embedded T² and explain where they come from

---

## Master Reading Schedule

Aligned with the weekly timeline, 2 hrs/week minimum:

| Weeks | Read | Purpose |
|---|---|---|
| Pre-work | Pressley Ch. 1–3 | Curves, basic surface definitions |
| Week 1 | Pressley Ch. 4–5 | First fundamental form, S² and T² metric |
| Week 2 | Pressley Ch. 6–7, Øksendal Ch. 8 §8.1 | Curvature, Stratonovich argument |
| Week 3 | Pressley Ch. 8 | Geodesics |
| Week 4 | Grigor'yan §1–3 | Laplace-Beltrami, generator |
| Week 5 | Grigor'yan §4–6 | Heat kernel, spectral expansion |
| Stretch (H²) | do Carmo DG Ch. 4, hyperbolic section | Poincaré disk geometry |

---

## Notes on Writing Style for Your Documentation

Since these notes are for a calculus-fluent freshman:
- Every definition must be followed by a concrete example on S² or T² before any abstract discussion
- Figures are mandatory for: tangent plane, parallel transport holonomy example, curvature sign regions on T², heat kernel spreading
- Every "this will matter because..." statement should link to a specific line of code in the project
- State theorems first, proofs second (or omit proofs for Theorema Egregium, Levi-Civita uniqueness). The freshman should know what is true before seeing why.
- Do not introduce index notation without first writing the formula in expanded form for n=2
