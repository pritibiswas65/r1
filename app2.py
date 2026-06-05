import streamlit as st

# Page configuration
st.set_page_config(
    page_title="Glazed Donut Recipe",
    page_icon="🍩",
    layout="centered"
)

# Header
st.title("🍩 Hello World!")
st.subheader("Welcome to the Glazed Donut Recipe Landing Page")

st.image(
    "https://images.unsplash.com/photo-1551024506-0bccd828d307",
    caption="Fresh Glazed Donuts",
    use_container_width=True
)

st.markdown("---")

# Description
st.write("""
Glazed donuts are soft, fluffy, deep-fried treats coated with a sweet vanilla glaze.
This classic recipe makes delicious homemade donuts perfect for breakfast or dessert.
""")

# Ingredients
st.header("📝 Ingredients")

ingredients = [
    "2¼ tsp active dry yeast",
    "¾ cup warm milk",
    "¼ cup granulated sugar",
    "2 eggs",
    "¼ cup melted butter",
    "3 cups all-purpose flour",
    "½ tsp salt",
    "Vegetable oil for frying"
]

for item in ingredients:
    st.checkbox(item, key=item)

# Glaze
st.subheader("✨ Glaze")
st.write("""
- 2 cups powdered sugar
- ¼ cup milk
- 1 tsp vanilla extract
""")

# Instructions
st.header("👨‍🍳 Instructions")

steps = [
    "Dissolve yeast in warm milk and let sit for 5 minutes.",
    "Mix sugar, eggs, butter, flour, and salt into the yeast mixture.",
    "Knead until smooth and let rise for 1 hour.",
    "Roll out dough and cut donut shapes.",
    "Let donuts rise again for 30 minutes.",
    "Heat oil to 350°F (175°C) and fry until golden brown.",
    "Mix glaze ingredients together.",
    "Dip warm donuts into the glaze and allow to set.",
    "Serve and enjoy!"
]

for i, step in enumerate(steps, start=1):
    st.write(f"**Step {i}:** {step}")

st.markdown("---")

# Footer
st.success("🎉 Congratulations! You now have a simple Streamlit landing page for glazed donuts.")

st.button("Order a Donut 🍩")