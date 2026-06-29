import streamlit as st
import pandas as pd
import pickle

# 🔹 Load model
with open("best_model.pkl", "rb") as f:
    model = pickle.load(f)

# 🔹 Page config
st.set_page_config(page_title="Laptop Price Predictor", layout="wide")

st.markdown("<h1 style='text-align: center; color: #4CAF50;'>💻 Laptop Price Predictor</h1>", unsafe_allow_html=True)
st.markdown("---")

# 🔹 Dictionaries
company_dict = {
    "Dell": 1, "HP": 2, "Lenovo": 3, "Apple": 4,
    "Asus": 5, "Acer": 6, "MSI": 7
}

type_dict = {
    "Notebook": 1, "Ultrabook": 2, "Gaming": 3,
    "2 in 1 Convertible": 4, "Workstation": 5
}

opsys_dict = {
    "Windows": 0, "Mac": 1, "Linux": 2, "Other": 3
}

cpu_dict = {
    "Intel i3": 1, "Intel i5": 2, "Intel i7": 3, "AMD": 4
}

gpu_dict = {
    "Intel": 0, "Nvidia": 1, "AMD": 2, "Other": 3
}

# 🔹 Sidebar Inputs
st.sidebar.header("⚙️ Select Laptop Features")

company = st.sidebar.selectbox("Company", list(company_dict.keys()))
type_name = st.sidebar.selectbox("Type", list(type_dict.keys()))
ram = st.sidebar.selectbox("RAM (GB)", [4, 8, 16, 32, 64])
op_sys = st.sidebar.selectbox("Operating System", list(opsys_dict.keys()))
cpu_name = st.sidebar.selectbox("CPU", list(cpu_dict.keys()))
gpu_brand = st.sidebar.selectbox("GPU Brand", list(gpu_dict.keys()))

# 🔹 Main Area Inputs (Columns)
col1, col2 = st.columns(2)

with col1:
    weight = st.number_input("⚖️ Weight (kg)", value=1.5)
    ppi = st.number_input("🖥️ PPI", value=141.0)
    hdd = st.selectbox("💾 HDD (GB)", [0, 256, 512, 1000])

with col2:
    touchscreen = st.selectbox("📱 TouchScreen", ["No", "Yes"])
    ips = st.selectbox("🌈 IPS Display", ["No", "Yes"])
    ssd = st.selectbox("🚀 SSD (GB)", [0, 128, 256, 512])

st.markdown("---")

# 🔹 Convert to DataFrame
input_data = pd.DataFrame([{
    'Company': company_dict[company],
    'TypeName': type_dict[type_name],
    'Ram': ram,
    'OpSys': opsys_dict[op_sys],
    'Weight': weight,
    'TouchScreen': 1 if touchscreen == "Yes" else 0,
    'IPS': 1 if ips == "Yes" else 0,
    'PPI': ppi,
    'CPU_name': cpu_dict[cpu_name],
    'HDD': hdd,
    'SSD': ssd,
    'Gpu brand': gpu_dict[gpu_brand]
}])

# 🔹 Center button
col_btn1, col_btn2, col_btn3 = st.columns([1,2,1])

with col_btn2:
    if st.button("🎯 Predict Price", use_container_width=True):
        prediction = model.predict(input_data)

        st.markdown(
            f"""
            <div style='text-align: center; padding: 20px; border-radius: 10px; background-color: #e8f5e9;'>
                <h2 style='color: green;'>💰 Predicted Price</h2>
                <h1 style='color: #2e7d32;'>₹ {round(prediction[0], 2)}</h1>
            </div>
            """,
            unsafe_allow_html=True
        )