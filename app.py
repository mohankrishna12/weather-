import streamlit as st
from agents.weather_agent import weather_agent
from agents.content_agent import content_agent
from agents.pdf_agent import pdf_agent

st.set_page_config(page_title="AI Weather Report", layout="centered")

st.title("🌦️ AI Weather Report Generator")
st.write("Multi-agent system using Python + LLaMA (Ollama)")

city = st.text_input("Enter city name")

if st.button("Generate Weather Report"):
    if city.strip() == "":
        st.warning("Please enter a city name.")
    else:
        with st.spinner("Fetching weather data..."):
            weather_data = weather_agent(city)

        with st.spinner("Generating AI summary..."):
            summary = content_agent(weather_data)

        with st.spinner("Creating PDF..."):
            pdf_file = pdf_agent(summary)

        st.subheader("Weather Summary")
        st.write(summary)

        with open(pdf_file, "rb") as f:
            st.download_button(
                "📄 Download PDF Report",
                f,
                file_name=pdf_file
            )
