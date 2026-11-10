import streamlit as st
import pandas as pd

# Page Configuration
st.set_page_config(
    page_title="Interior Design Studio",
    page_icon="🏠",
    layout="wide"
)

# App Header
st.title("🏠 Virtual Interior Design & Budget Studio")
st.markdown("Plan your dream space, explore curated design aesthetics, and estimate your room makeover budget instantly.")

# Sidebar Navigation
st.sidebar.header("Design Controls")
room_type = st.sidebar.selectbox("Select Room Type", ["Living Room", "Bedroom", "Kitchen", "Home Office", "Balcony"])
design_style = st.sidebar.selectbox("Choose Aesthetic Style", [
    "Minimalist Scandi", 
    "Vintage 90s Warmth", 
    "Modern Industrial", 
    "Bohemian Chic", 
    "Contemporary Luxury"
])

# Style Descriptions & Color Palettes
style_data = {
    "Minimalist Scandi": {
        "desc": "Clean lines, neutral tones, light wood finishes, and abundant natural light.",
        "colors": ["#F5F5F3", "#D3C5B4", "#4A4A4A", "#A3B18A"],
        "base_cost": 45000
    },
    "Vintage 90s Warmth": {
        "desc": "Rich wood tones, cozy textures, warm golden hour lighting, and nostalgic statement pieces.",
        "colors": ["#8C5830", "#D9AE7B", "#3D2314", "#F4E3C1"],
        "base_cost": 40000
    },
    "Modern Industrial": {
        "desc": "Exposed brick, matte black metal accents, leather textures, and raw utilitarian charm.",
        "colors": ["#2B2B2B", "#7F4F24", "#B08968", "#121212"],
        "base_cost": 55000
    },
    "Bohemian Chic": {
        "desc": "Eclectic mix of patterns, layered textiles, indoor plants, and handmade artisanal decor.",
        "colors": ["#C86D51", "#E9C46A", "#2A9D8F", "#F4A261"],
        "base_cost": 35000
    },
    "Contemporary Luxury": {
        "desc": "Sleek metallic finishes, plush velvet upholstery, marble textures, and sophisticated lighting.",
        "colors": ["#1D1E22", "#D4AF37", "#8D99AE", "#FFFFFF"],
        "base_cost": 75000
    }
}

current_style = style_data[design_style]

# Main Layout Tabs
tab1, tab2, tab3 = st.tabs(["✨ Style Guide & Palette", "🛋️ Room Elements Checklist", "💰 Budget Estimator"])

with tab1:
    st.subheader(f"{design_style} for your {room_type}")
    st.write(current_style["desc"])
    
    st.markdown("#### Curated Color Palette")
    cols = st.columns(len(current_style["colors"]))
    for i, color in enumerate(current_style["colors"]):
        with cols[i]:
            st.markdown(
                f"<div style='background-color: {color}; height: 80px; border-radius: 10px; border: 1px solid #ccc; display: flex; align-items: center; justify-content: center; color: #fff; font-weight: bold; text-shadow: 1px 1px 2px rgba(0,0,0,0.5);'>{color}</div>", 
                unsafe_allow_html=True
            )

with tab2:
    st.subheader("Recommended Furniture & Decor Pieces")
    
    # Dynamic checklist based on room
    items = {
        "Living Room": ["Sofa / Sectional", "Coffee Table", "Area Rug", "Floor Lamp", "Accent Chairs", "TV Unit"],
        "Bedroom": ["Queen/King Bed", "Bedside Tables", "Wardrobe", "Blackout Curtains", "Pendant Lighting"],
        "Kitchen": ["Modular Cabinets", "Countertop (Quartz/Granite)", "Bar Stools", "Backsplash Tiles"],
        "Home Office": ["Ergonomic Desk", "Task Chair", "Bookshelves", "Desk Lamp"],
        "Balcony": ["Outdoor Lounge Set", "Artificial Turf / Deck Tiles", "Hanging Planters", "String Lights"]
    }
    
    selected_room_items = items.get(room_type, ["General Decor", "Lighting", "Flooring"])
    
    st.markdown(f"Check off the elements you want to include in your **{room_type}**:")
    user_choices = {}
    for item in selected_room_items:
        user_choices[item] = st.checkbox(item, value=True)

with tab3:
    st.subheader("Interactive Cost Estimator")
    
    room_size_sqft = st.slider("Select Room Size (Square Feet)", min_value=100, max_value=800, value=250, step=25)
    
    # Cost calculation formula
    size_multiplier = room_size_sqft / 200
    estimated_total = int(current_style["base_cost"] * size_multiplier)
    
    col1, col2 = st.columns(2)
    with col1:
        st.metric(label="Estimated Makeover Cost", value=f"₹ {estimated_total:,}")
    with col2:
        st.info(f"Estimated breakdown for a {room_size_sqft} sq.ft. {room_type} styled in {design_style}.")
        
    st.markdown("---")
    if st.button("📥 Export Design Summary"):
        st.success("Design summary generated successfully! (Ready to integrate with PDF/CSV export plugins).")
