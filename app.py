import streamlit as st
import plotly.graph_objects as go
import numpy as np

# -----------------------------------------------------------------------------
# 1. PAGE CONFIGURATION & CSS (HOLOGRAPHIC THEME)
# -----------------------------------------------------------------------------
st.set_page_config(
    page_title="HoloSpace Visualizer",
    page_icon="🌌",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS for the Futuristic Glass Look
st.markdown("""
    <style>
    /* 1. Background: Deep Space + Nebula Overlay */
    .stApp {
        background: radial-gradient(circle at 50% 50%, #1a2a3a 0%, #000000 90%);
        color: #e0e0e0;
    }

    /* 2. The Holographic Glass Container */
    .glass-card {
        background: rgba(10, 20, 30, 0.6);
        border: 1px solid rgba(0, 242, 255, 0.3);
        box-shadow: 0 0 20px rgba(0, 242, 255, 0.1), inset 0 0 50px rgba(0, 242, 255, 0.05);
        border-radius: 20px;
        padding: 20px;
        backdrop-filter: blur(10px);
        margin-top: 20px;
    }

    /* 3. Custom Sliders (Neon Cyan) */
    div.stSlider > div[data-baseweb="slider"] > div > div > div[role="slider"]{
        background-color: #00f2ff !important;
        box-shadow: 0 0 15px #00f2ff;
    }
    div.stSlider > div[data-baseweb="slider"] > div > div > div > div {
        background-color: #005f63 !important;
    }
    
    /* 4. Fonts and Headers */
    h1, h2, h3, .stMarkdown {
        font-family: 'Courier New', monospace; /* Tech/Code font */
        text-transform: uppercase;
        letter-spacing: 2px;
        color: #00f2ff;
        text-shadow: 0 0 8px rgba(0, 242, 255, 0.6);
    }
    
    /* Sidebar Styling */
    section[data-testid="stSidebar"] {
        background-color: #050505;
        border-right: 1px solid #333;
    }
    </style>
""", unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# 2. HELPER FUNCTIONS (GEOMETRY)
# -----------------------------------------------------------------------------

def generate_orbit_coords(a, e, points=100):
    """Generates 3D path coordinates for an elliptical orbit."""
    theta = np.linspace(0, 2 * np.pi, points)
    r = (a * (1 - e**2)) / (1 + e * np.cos(theta))
    x = r * np.cos(theta)
    y = r * np.sin(theta)
    z = np.zeros_like(x)
    return x, y, z

def create_holographic_sphere(cx, cy, cz, radius, color_hex, is_star=False):
    """
    Generates a 3D sphere.
    If is_star=True: Uses high ambient light (Yellow glow) + No Grid.
    If is_star=False: Uses wireframe contours (Grid look) + Standard lighting.
    """
    phi = np.linspace(0, np.pi, 20)
    theta = np.linspace(0, 2 * np.pi, 20)
    phi, theta = np.meshgrid(phi, theta)

    x = cx + radius * np.sin(phi) * np.cos(theta)
    y = cy + radius * np.sin(phi) * np.sin(theta)
    z = cz + radius * np.cos(phi)

    if is_star:
        # STAR CONFIG: High Ambient Light so it never looks black
        lighting = dict(ambient=1.0, diffuse=0.0, roughness=0.0, specular=0.0)
        contours = dict() # No grid for the star
        colorscale = [[0, color_hex], [1, color_hex]]
        surface_color = np.ones_like(z) # Uniform color matrix
    else:
        # PLANET CONFIG: Holographic Grid Look
        lighting = dict(ambient=0.4, diffuse=0.5, roughness=0.1, specular=0.5)
        # This adds the "Grid" lines seen in your reference image
        contours = dict(
            x=dict(show=True, color='rgba(0,242,255,0.3)', width=2),
            y=dict(show=True, color='rgba(0,242,255,0.3)', width=2),
            z=dict(show=False)
        )
        colorscale = [[0, color_hex], [1, color_hex]]
        surface_color = np.zeros_like(z)

    return go.Surface(
        x=x, y=y, z=z,
        surfacecolor=surface_color,
        colorscale=colorscale,
        showscale=False,
        lighting=lighting,
        contours=contours,
        opacity=0.9 if is_star else 0.7,
        hoverinfo='skip'
    )

# -----------------------------------------------------------------------------
# 3. SIDEBAR CONTROLS (HUD Style)
# -----------------------------------------------------------------------------

with st.sidebar:
    st.title("🛰️ SYSTEM PARAMETERS")
    st.markdown("---")
    
    st.markdown("### ☀️ STAR MASS")
    m_star_mass = st.slider("Radius (Solar R)", 2.0, 8.0, 5.0, key="m_star")
    
    st.markdown("---")
    st.markdown("### 🔵 ORBITER ALPHA")
    m1_dist = st.slider("Distance (AU)", 3.0, 10.0, 5.0, key="m1_d")
    m1_size = st.slider("Radius", 0.5, 3.0, 1.2, key="m1_m")

    st.markdown("---")
    st.markdown("### 🟢 ORBITER BETA")
    m2_dist = st.slider("Distance (AU)", 3.0, 12.0, 9.0, key="m2_d")
    m2_ecc = st.slider("Eccentricity", 0.0, 0.7, 0.4, key="m2_e")
    
    st.markdown("---")
    st.caption("v.3.0.1 // HOLOGRAPHIC RENDERER")

# -----------------------------------------------------------------------------
# 4. MAIN VISUALIZATION
# -----------------------------------------------------------------------------

# Calculate positions
theta_snap1 = np.pi / 3
r1 = m1_dist # Circular for simplicity on M1
p1_pos = [r1 * np.cos(theta_snap1), r1 * np.sin(theta_snap1), 0]

theta_snap2 = np.pi
r2 = (m2_dist * (1 - m2_ecc**2)) / (1 + m2_ecc * np.cos(theta_snap2))
p2_pos = [r2 * np.cos(theta_snap2), r2 * np.sin(theta_snap2), 0]

# Build Plot
fig = go.Figure()

# 1. ORBIT RINGS (Neon Lines)
x1, y1, z1 = generate_orbit_coords(m1_dist, 0) # Circular
fig.add_trace(go.Scatter3d(
    x=x1, y=y1, z=z1, mode='lines',
    line=dict(color='rgba(0, 123, 255, 0.5)', width=3), name='Orbit Alpha'
))

x2, y2, z2 = generate_orbit_coords(m2_dist, m2_ecc) # Elliptical
fig.add_trace(go.Scatter3d(
    x=x2, y=y2, z=z2, mode='lines',
    line=dict(color='rgba(0, 255, 136, 0.5)', width=3, dash='dash'), name='Orbit Beta'
))

# 2. 3D OBJECTS
# The Sun (Yellow, High Ambient, No Grid)
fig.add_trace(create_holographic_sphere(0, 0, 0, m_star_mass/3, '#FFD700', is_star=True))

# Planet 1 (Blue, Grid)
fig.add_trace(create_holographic_sphere(p1_pos[0], p1_pos[1], 0, m1_size/2, '#00ccff', is_star=False))

# Planet 2 (Green, Grid)
fig.add_trace(create_holographic_sphere(p2_pos[0], p2_pos[1], 0, 1.0, '#00ff99', is_star=False))

# 3. GLOW EFFECT (Using Scatter3d markers inside the sun to fake a glow)
fig.add_trace(go.Scatter3d(
    x=[0], y=[0], z=[0],
    mode='markers',
    marker=dict(size=m_star_mass*15, color='#FFD700', opacity=0.2, line=dict(width=0)),
    hoverinfo='none'
))

# 4. LAYOUT CONFIGURATION
fig.update_layout(
    scene=dict(
        xaxis=dict(visible=False, showgrid=False, showbackground=False),
        yaxis=dict(visible=False, showgrid=False, showbackground=False),
        zaxis=dict(visible=False, showgrid=False, showbackground=False),
        bgcolor='rgba(0,0,0,0)',
        aspectmode='data',
        camera=dict(eye=dict(x=1.2, y=1.2, z=0.6))
    ),
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    margin=dict(l=0, r=0, t=0, b=0),
    height=600,
    showlegend=False
)

# -----------------------------------------------------------------------------
# 5. RENDER UI
# -----------------------------------------------------------------------------

# Main Title Area
st.markdown("## 🔭 EXOPLANET SIMULATOR")

# The "Card" Wrapper
st.markdown('<div class="glass-card">', unsafe_allow_html=True)
st.plotly_chart(fig, use_container_width=True)
st.markdown('</div>', unsafe_allow_html=True)

# Fake holographic data output at bottom
c1, c2, c3 = st.columns(3)
c1.metric("GRAVITY WELL", f"{m_star_mass * 1.5} G")
c2.metric("ORBITAL FLUX", "STABLE", delta_color="normal")
c3.metric("SIMULATION TIME", "T-MINUS 00:00:00")