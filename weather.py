import os
import requests
import streamlit as st

st.set_page_config(page_title="SkySense AI")

st.title("SkySense AI")
st.write("Your smart weather assistant")

city = st.text_input(
    "Enter City Name",
    placeholder="Example: Chennai"
)

if st.button("Check Weather"):
    if city.strip():

        api_key = os.getenv("WEATHER_API_KEY")

        response = requests.get(
            "https://api.openweathermap.org/data/2.5/weather",
            params={
                "q": city,
                "appid": api_key,
                "units": "metric"
            }
        )

        if response.status_code == 200:
            data = response.json()

            st.success(f"Weather in {city.title()}")

            st.write(f"Temperature: {data['main']['temp']} °C")
            st.write(f"Feels Like: {data['main']['feels_like']} °C")
            st.write(f"Humidity: {data['main']['humidity']}%")
            st.write(f"Pressure: {data['main']['pressure']} hPa")
            st.write(
                f"Condition: {data['weather'][0]['description'].title()}"
            )

        else:
            st.error("Unable to fetch weather data.")

    else:
        st.warning("Please enter a city name.")