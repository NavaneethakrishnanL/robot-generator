import streamlit as st
import subprocess
from pathlib import Path

TEMPLATE_PATH = Path("templates")

# ----------------------
# Load templates
# ----------------------
def load_template(name):
    f = TEMPLATE_PATH / name
    return f.read_text() if f.exists() else ""

# ----------------------
# LLM generator (Ollama)
# ----------------------
def generate_with_llm(prompt):
    full_prompt = f"""
You are an expert Robot Framework generator.
Output ONLY valid .robot syntax with no explanations.

User request:
{prompt}
"""
    result = subprocess.run(
        ["ollama", "run", "qwen2.5:7b"],
        input=full_prompt,
        text=True,
        capture_output=True
    )
    return result.stdout.strip()

# ----------------------
# Streamlit UI
# ----------------------
st.title("🤖 Robot Framework Script Generator (Open Source + Local)")

st.sidebar.header("Template Type")
template_type = st.sidebar.selectbox(
    "Choose a base template:",
    ["Web Test", "API Test", "Mobile Test", "Car HLK Test"]
)

template_file_map = {
    "Web Test": "web.robot",
    "API Test": "api.robot",
    "Mobile Test": "mobile.robot",
    "Car HLK Test": "car_hlk.robot"
}

base_template = load_template(template_file_map[template_type])
st.subheader("📄 Base Template")
st.code(base_template, language="robot")

st.subheader("📝 Describe the test you want")
user_prompt = st.text_area(
    "Example: 'Create a CAN heartbeat test and bootloader verification'",
    height=150
)

if st.button("Generate .robot File"):
    with st.spinner("Generating using local LLM..."):
        generated = generate_with_llm(user_prompt)

        st.subheader("✅ Generated Script")
        st.code(generated, language="robot")

        st.download_button(
            label="📥 Download .robot file",
            data=generated,
            file_name="generated_test.robot",
            mime="text/plain"
        )
