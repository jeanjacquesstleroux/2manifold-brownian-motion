import streamlit as st 
import numpy as np
import plotly.graph_objects as go
import math

import sys
sys.path.append("..")
from src.manifolds.sphere import Sphere
from src.simulation.simulator import simulator
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
    noise_type = st.selectbox(
        label="Noise Type", 
        options=["Isotropic", "Anisotropic"]
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
- Anisotropic noise restricts motion to only one tangent direction, producing structured trajectories.

Animation and visualizations are provided below, with these features:
- Red dot to display the initial position of particles on the sphere (from the latitude and longitude).
- Black trajectories showing sample paths of individual particles.
- Final particle distribution with black dots to display the final positions on the sphere.
- Heatmap visualizing occupation density (directly based on final particle distribution).

The heatmap is computed using a kernel distribution (von Mises-Fisher) over the sphere surface. The concentration parameter (k) controls how close points are in the kernel density estimation (KDE) heatmap.
Higher values of k produce more localized density peaks, whereas lower values create smoother, uniform distributions.

What users can adjust:
- Number of particles (N)
- Number of time steps (T)
- Size of time steps (dt)
- Concentration parameter (k)
- Noise type (isotropic vs anisotropic)
- Starting position on sphere (latitude, longitude)
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
    cols2[2].metric("Starting Point", f"({lat} degrees, {long} degrees)")
    # Run simulation on Sphere
    if manifold == "Sphere":
        sphere = Sphere()
        trajectory = simulator(T, N, dt, noise_type.lower(), starting_point=starting_point)
        surface, x_surface, y_surface, z_surface = sphere_creation()
        # Get first particle path
        path = trajectory[:, 0, :]
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
        # Plot the animation
        st.plotly_chart(animation_figure)
    else: # On torus
        # Add torus here
        pass

st.divider()

# Visualizations (plots)
st.subheader("Visualizations")
# Tabs
tab1, tab2 = st.tabs([
    "Final Particle Distribution",
    "KDE Heatmap"
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
    # Show KDE heatmap
    with tab2:
        # Get final positions
        final_positions = trajectory[-1]
        # Create heatmap
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
        