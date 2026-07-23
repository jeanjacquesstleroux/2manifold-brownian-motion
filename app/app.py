import streamlit as st
import numpy as np
import plotly.graph_objects as go
import math

import sys
sys.path.append("..")
from src.manifolds.sphere import Sphere
from src.manifolds.torus import Torus
from src.simulation.simulator import simulator, torus_simulator
from src.visualization.kde import sphere_kde

# Helper function for creating a sphere surface
def sphere_creation():
    # Create sphere surface
    # Get angle arrays
    theta = np.linspace(0, 2*math.pi, num=100)
    phi = np.linspace(0, math.pi, num=100)
    # Turn theta and phi angles into a 2D grid
    theta_grid, phi_grid = np.meshgrid(theta, phi)
    # Apply sphere formulas for each axis of the surface
    x_surface = np.sin(phi_grid) * np.cos(theta_grid)
    y_surface = np.sin(phi_grid) * np.sin(theta_grid)
    z_surface = np.cos(phi_grid)
    # Create surface of sphere
    surface = go.Surface(
        x=x_surface,
        y=y_surface,
        z=z_surface,
        opacity=0.5,
        showscale=False
    )
    return surface, x_surface, y_surface, z_surface

# Helper function for creating a torus surface
def torus_creation(R, r):
    # Get angle arrays
    u = np.linspace(0, 2*math.pi, num=100)
    v = np.linspace(0, 2*math.pi, num=100)
    # Turn u and v angles into a 2D grid
    u_grid, v_grid = np.meshgrid(u, v)
    # Apply torus formulas for each axis of the surface
    x_surface = (R + r*np.cos(v_grid)) * np.cos(u_grid)
    y_surface = (R + r*np.cos(v_grid)) * np.sin(u_grid)
    z_surface = r*np.sin(v_grid)
    # Create surface of torus
    surface = go.Surface(
        x=x_surface,
        y=y_surface,
        z=z_surface,
        opacity=0.5,
        showscale=False
    )
    return surface, x_surface, y_surface, z_surface

# Helper function for building the animated trajectory figure, shared by
# both manifolds
def build_animation_figure(surface, path, starting_point):
    # Create frames for animation
    frames = []
    for i in range(1, len(path), 10):
        frames.append(
            go.Frame(
                data=[go.Scatter3d(
                    x=path[:i, 0],
                    y=path[:i, 1],
                    z=path[:i, 2],
                    mode="lines",
                    line=dict(color="black")
                )
            ],
            traces=[1],
            name=str(i)
            )
        )
    # Starting point
    starting_marker = go.Scatter3d(
        x=[starting_point[0]],
        y=[starting_point[1]],
        z=[starting_point[2]],
        mode="markers",
        marker=dict(size=5, color="red"),
        showlegend=False
    )
    # Starting trace
    animated_trace = go.Scatter3d(
        x=path[:1, 0],
        y=path[:1, 1],
        z=path[:1, 2],
        mode="lines",
        line=dict(color="black"),
        showlegend=False
    )
    # Animation figure
    animation_figure = go.Figure(
        data=[surface, animated_trace, starting_marker],
        frames=frames
    )
    animation_figure.update_layout(
        updatemenus=[
            dict(
                type="buttons",
                buttons=[
                    dict(
                        label="Play",
                        method="animate",
                        args=[
                            None,
                            {
                                "frame": {"duration": 50, "redraw": True},
                                "fromcurrent": True
                            }
                        ]
                    )
                ]
            )
        ],
        showlegend=False
    )
    return animation_figure, starting_marker

# Set up browser tab title and layout
st.set_page_config(page_title="Brownian Motion Simulation", layout="wide")

# Sidebar layout
with st.sidebar:
    st.header("Settings")
    st.write("Edit the parameters here")

    manifold = st.selectbox(
        "Select the manifold:",
        options=["Sphere", "Torus"]
    )

    N = st.slider(
        label="Number of Particles (N)",
        min_value=1, max_value=1000,
        value=500
    )
    T = st.slider(
        label="Number of Steps (T)",
        min_value=10,
        max_value=5000,
        value=1000
    )
    dt = st.slider(
        label="Time Step (dt)",
        min_value=0.001,
        max_value=0.1,
        value=0.01
    )
    k = st.slider(
        label="Concentration Parameter (k)",
        min_value=1,
        max_value=100,
        value=20
    )
    # Anisotropic noise is only implemented for the Sphere manifold so far
    noise_options = ["Isotropic", "Anisotropic"] if manifold == "Sphere" else ["Isotropic"]
    noise_type = st.selectbox(
        label="Noise Type",
        options=noise_options
    )

    if manifold == "Sphere":
        lat = st.slider(
            label="Starting latitude",
            min_value=-90,
            max_value=90,
            value=0
        )
        long = st.slider(
            label="Starting longitude",
            min_value=-180,
            max_value=180,
            value=0
        )
        # Convert degrees to radians
        lat_rad = np.radians(lat)
        long_rad = np.radians(long)
        # Compute the starting point on the sphere from radians
        starting_point = np.array([
            np.cos(lat_rad) * np.cos(long_rad),
            np.cos(lat_rad) * np.sin(long_rad),
            np.sin(lat_rad)
        ])
        start_label = f"({lat} degrees, {long} degrees)"
    else: # Torus
        R = st.slider(
            label="Major radius (R)",
            min_value=1.0,
            max_value=10.0,
            value=3.0,
            step=0.5
        )
        r = st.slider(
            label="Minor radius (r)",
            min_value=0.1,
            max_value=R - 0.1,
            value=min(1.0, R - 0.1),
            step=0.1
        )
        start_u = st.slider(
            label="Starting toroidal angle (u)",
            min_value=0,
            max_value=360,
            value=0
        )
        start_v = st.slider(
            label="Starting poloidal angle (v)",
            min_value=0,
            max_value=360,
            value=0
        )
        # Convert degrees to radians
        u_rad = np.radians(start_u)
        v_rad = np.radians(start_v)
        # Compute the starting point on the torus from radians
        starting_point = Torus(R, r).parametrize(u_rad, v_rad)
        start_label = f"(u={start_u} degrees, v={start_v} degrees)"

    # Run simulation button
    run_clicked = st.button(
        "Run Simulation",
        type="primary",
        use_container_width=True
    )

# Title
st.title("Brownian Motion Simulation")
st.caption("On Sphere and Torus Manifolds")

# Project description
st.markdown("""
### Project Description
This project simulates Brownian motion on a Riemannian manifold.
Brownian motion is the random evolution of particles over time. It is simulated using the Euler-Maruyama method for stochastic differential equations.
Two types of noise are supported:
- Isotropic noise allows motion in all tangent directions, uniformly.
- Anisotropic noise restricts motion to only one tangent direction, producing structured trajectories (currently only implemented for the sphere).

Animation and visualizations are provided below, with these features:
- Red dot to display the initial position of particles on the manifold.
- Black trajectories showing sample paths of individual particles.
- Final particle distribution with black dots to display the final positions on the manifold.
- A density heatmap of the final particle distribution (a von Mises-Fisher KDE over the sphere surface, or an occupation histogram in (u, v) coordinates for the torus).

What users can adjust:
- Number of particles (N)
- Number of time steps (T)
- Size of time steps (dt)
- Concentration parameter (k), used by the sphere's KDE heatmap
- Noise type (isotropic vs anisotropic)
- Starting position on the manifold
- Major/minor radius (R, r), for the torus
""")

st.divider()

# Simulation shown
st.subheader("Simulation")
# Display user's selected parameters after they click Run Simulation
if run_clicked == True:
    st.subheader("Selected Parameters")
    cols1 = st.columns(3)
    cols2 = st.columns(3)
    cols1[0].metric("Manifold", manifold)
    cols1[1].metric("Particles", N)
    cols1[2].metric("Steps", T)
    cols2[0].metric("dt", dt)
    cols2[1].metric("Noise Type", noise_type)
    cols2[2].metric("Starting Point", start_label)
    # Run simulation on the selected manifold
    if manifold == "Sphere":
        trajectory = simulator(T, N, dt, noise_type.lower(), starting_point=starting_point)
        surface, x_surface, y_surface, z_surface = sphere_creation()
    else: # Torus
        trajectory = torus_simulator(T, N, dt, R, r, starting_point=starting_point)
        surface, x_surface, y_surface, z_surface = torus_creation(R, r)
    # Get first particle path
    path = trajectory[:, 0, :]
    # Build the shared animated trajectory figure
    animation_figure, starting_marker = build_animation_figure(surface, path, starting_point)
    # Plot the animation
    st.plotly_chart(animation_figure)

st.divider()

# Visualizations (plots)
st.subheader("Visualizations")
# Tabs
tab1, tab2 = st.tabs([
    "Final Particle Distribution",
    "Density Heatmap"
])
# Run simulation to display plots
if run_clicked == True:
    # Show final positions of all particles
    with tab1:
        final_positions = trajectory[-1]
        # Coordinates
        x_coor = final_positions[:, 0]
        y_coor = final_positions[:, 1]
        z_coor = final_positions[:, 2]
        # Particle trace
        particle_trace = go.Scatter3d(
            x=x_coor,
            y=y_coor,
            z=z_coor,
            mode="markers",
            marker=dict(size=2, color="black"),
            showlegend=False
        )
        # Plot figure
        figure = go.Figure(
            data=[surface, particle_trace, starting_marker]
        )
        st.plotly_chart(figure)
    # Show density heatmap
    with tab2:
        # Get final positions
        final_positions = trajectory[-1]
        if manifold == "Sphere":
            # Create heatmap using a von Mises-Fisher KDE over the sphere surface
            density = sphere_kde(
                final_positions,
                x_surface,
                y_surface,
                z_surface,
                k,
                N
            )
            density_surface = go.Surface(
                x=x_surface,
                y=y_surface,
                z=z_surface,
                surfacecolor=density,
                colorscale="Viridis",
                showscale=True
            )
            figure = go.Figure(data=[density_surface, starting_marker])
            st.plotly_chart(figure)
        else: # Torus
            # The invariant measure on the embedded torus is not uniform in
            # (u, v), so we visualize the empirical occupation density
            # directly in parameter space rather than reusing the sphere's
            # ambient-space KDE.
            x_coor = final_positions[:, 0]
            y_coor = final_positions[:, 1]
            z_coor = final_positions[:, 2]
            rho = np.sqrt(x_coor**2 + y_coor**2)
            u_values = np.arctan2(y_coor, x_coor) % (2 * np.pi)
            v_values = np.arctan2(z_coor, rho - R) % (2 * np.pi)
            histogram, u_edges, v_edges = np.histogram2d(
                u_values, v_values, bins=30, range=[[0, 2 * np.pi], [0, 2 * np.pi]]
            )
            max_count = histogram.max()
            density = histogram / max_count if max_count > 0 else histogram
            heatmap = go.Heatmap(
                z=density.T,
                x=(u_edges[:-1] + u_edges[1:]) / 2,
                y=(v_edges[:-1] + v_edges[1:]) / 2,
                colorscale="Viridis"
            )
            figure = go.Figure(data=[heatmap])
            figure.update_layout(
                xaxis_title="u (toroidal angle)",
                yaxis_title="v (poloidal angle)"
            )
            st.plotly_chart(figure)
            st.caption(
                "Theoretical invariant density is p(u, v) = (R + r cos v) / (4π²R) "
                "— not uniform in v, since the embedded torus has non-constant curvature."
            )
