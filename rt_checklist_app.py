import streamlit as st
from datetime import date

st.set_page_config(page_title="RT Team Checklist", layout="centered")
st.title("📋 RT Team Outstation Checklist")

# Section 1: Trip Info
st.header("1️⃣ Trip Information (2–3 Days)")

transport = st.text_input("🚛 Transportation Type & Plate No. (e.g. Lorry BDH 1234)")
overnight = st.radio("🛌 Overnight Stay?", ["Yes", "No"])

daily_info = []
for i in range(1, 4):
    with st.expander(f"📅 Day {i} Details"):
        trip_date = st.date_input(f"Date for Day {i}", key=f"date_{i}", value=date.today())
        site = st.text_input(f"Site Location (Day {i})", key=f"site_{i}")
        client = st.text_input(f"Client (Day {i})", key=f"client_{i}")
        request = st.radio(f"Request Sheet Received? (Day {i})", ["Yes", "No"], key=f"req_{i}")
        daily_info.append((trip_date, site, client, request))

# Section 2: X-Ray Equipment
st.header("2️⃣ X-Ray Equipment")

xray_type = st.radio("Select X-Ray Setup", ["Single Wall (Crawler)", "Double Wall"])

crawler = {}
kv_type = ""
double_wall = {}

if xray_type == "Single Wall (Crawler)":
    st.subheader("🧰 Crawler Equipment Checklist")
    crawler = {
        "Crawler": st.checkbox("Crawler"),
        "Battery Pack - Charged": st.checkbox("Battery Pack - Charged"),
        "Battery Pack - Not Charged": st.checkbox("Battery Pack - Not Charged"),
        "X-ray Tube (Crawler)": st.checkbox("X-ray Tube (Crawler)"),
        "Connector Pin": st.checkbox("Connector Pin"),
        "Caesium Detector": st.checkbox("Caesium Detector")
    }
elif xray_type == "Double Wall":
    kv_type = st.radio("Select Double Wall Power", ["200 kV", "300 kV"])
    st.subheader(f"⚙️ {kv_type} Equipment Checklist")
    double_wall = {
        "X-ray Tube": st.checkbox("X-ray Tube"),
        "Control Panel": st.checkbox("Control Panel"),
        "Cable": st.checkbox("Cable")
    }

# Section 3: Film Quantity
st.header("3️⃣ Film Quantity Used")

st.markdown("### 🎯 Single Wall Single Image (SWSI)")
swsi_lengths = ['2"', '4"', '6"', '8"', '12"', '16"']
swsi_film = {length: st.number_input(f"SWSI {length}", min_value=0, step=1) for length in swsi_lengths}

st.markdown("### 🎯 Double Wall Single Image (DWSI)")
dwsi_lengths = ['8"', '12"', '16"']
dwsi_film = {length: st.number_input(f"DWSI {length}", min_value=0, step=1) for length in dwsi_lengths}

# Section 4: Safety Equipment
st.header("4️⃣ Safety Equipment (Ticked on Space)")
safety_equipment = {
    "Safety vest": st.checkbox("Safety vest"),
    "Safety shoes": st.checkbox("Safety shoes"),
    "Rain boot": st.checkbox("Rain boot"),
    "Safety coverall": st.checkbox("Safety coverall"),
    "First aid kit": st.checkbox("First aid kit"),
    "Barricade": st.checkbox("Barricade"),
    "Warning sign": st.checkbox("Warning sign"),
    "Warning light": st.checkbox("Warning light"),
}

# Section 5: Processing Equipment
st.header("5️⃣ Processing Equipment")
st.markdown("**Chemical**")
chemical = {
    "Developer": st.checkbox("Developer"),
    "Fixer": st.checkbox("Fixer"),
    "Water": st.checkbox("Water"),
}
st.markdown("**Tools & Utensils**")
processing_tools = {
    "Basin": st.checkbox("Basin"),
    "Hanger/spiral": st.checkbox("Hanger/spiral"),
    "Clipper": st.checkbox("Clipper"),
    "Dryer": st.checkbox("Dryer"),
    "Film viewer": st.checkbox("Film viewer"),
}

# Section 6: Legality
st.header("6️⃣ Legality")
st.markdown("**Personal Documents**")
personal_legal = {
    "Radiography certificate": st.checkbox("Radiography certificate"),
    "Identity card": st.checkbox("Identity card"),
    "NIOSH card": st.checkbox("Niosh cards"),
    "Driving license": st.checkbox("Driving license"),
}
st.markdown("**Equipment**")
equipment_legal = {
    "License/calibrated cert": st.checkbox("License/calibrated cert"),
}
st.markdown("**Company**")
company_legal = {
    "Company license": st.checkbox("Company license"),
}


# Submit & Summary
if st.button("✅ Submit Checklist"):
    st.success("Checklist submitted. Here's your summary:")

    st.markdown("### 🚚 General Info")
    st.write("Transportation:", transport)
    st.write("Overnight Stay:", overnight)

    for i, info in enumerate(daily_info):
        st.markdown(f"**Day {i+1}:**")
        st.write(f"- Date: {info[0]}")
        st.write(f"- Site: {info[1]}")
        st.write(f"- Client: {info[2]}")
        st.write(f"- Request Sheet: {info[3]}")

    st.markdown("### 🛠️ X-Ray Setup")
    st.write("Machine Type:", xray_type)
    if xray_type == "Single Wall (Crawler)":
        st.write("Crawler Equipment:")
        for k, v in crawler.items():
            if v:
                st.write(f"- {k}")
    elif xray_type == "Double Wall":
        st.write("Power:", kv_type)
        for k, v in double_wall.items():
            if v:
                st.write(f"- {k}")

    st.markdown("### 🎥 Film Usage")
    st.write("**SWSI:**")
    for k, v in swsi_film.items():
        if v > 0:
            st.write(f"- {k}: {v} pieces")
    st.write("**DWSI:**")
    for k, v in dwsi_film.items():
        if v > 0:
            st.write(f"- {k}: {v} pieces")

    st.markdown("### 🦺 Safety Equipment")
    for item, checked in safety_equipment.items():
        if checked:
            st.write(f"- {item}")

    st.markdown("### 🧪 Processing Equipment")
    st.write("**Chemicals:**")
    for item, checked in chemical.items():
        if checked:
            st.write(f"- {item}")
    st.write("**Tools:**")
    for item, checked in processing_tools.items():
        if checked:
            st.write(f"- {item}")

    st.markdown("### 📜 Legality")
    st.write("**Personal Documents:**")
    for item, checked in personal_legal.items():
        if checked:
            st.write(f"- {item}")
    st.write("**Equipment:**")
    for item, checked in equipment_legal.items():
        if checked:
            st.write(f"- {item}")
    st.write("**Company:**")
    for item, checked in company_legal.items():
        if checked:
            st.write(f"- {item}")
