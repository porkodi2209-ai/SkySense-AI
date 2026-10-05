# SkySense AI – Weather Assistant

## Project Overview

SkySense AI is a simple weather assistant developed using Python and Streamlit. It uses the OpenWeatherMap weather service through the PyOWM Python library to retrieve current weather information for a city entered by the user.

The application provides important weather details such as temperature, feels-like temperature, humidity, atmospheric pressure, and current weather condition through an interactive Streamlit interface.

The Weather API key is securely accessed through a terminal environment variable instead of being stored directly in the source code.

## Features

* Enter any city name to check its current weather.
* Fetch real-time weather information using a Weather API.
* Display current temperature in Celsius.
* Display feels-like temperature.
* Display humidity percentage.
* Display atmospheric pressure.
* Display current weather condition.
* Secure API key handling using an environment variable.
* Interactive web interface using Streamlit.
* Simple and user-friendly design.

## Technologies Used

* Python
* Streamlit
* PyOWM
* OpenWeatherMap API

## How It Works

1. The user enters a city name in the Streamlit application.
2. The application reads the Weather API key from the environment variable.
3. PyOWM connects to the weather service and retrieves the weather information.
4. The received weather data is processed using Python.
5. The application displays the weather details in the Streamlit interface.

## Example

Enter:

```text
Chennai
```
<img width="1920" height="1080" alt="Screenshot (132)" src="https://github.com/user-attachments/assets/9f9d39d9-de5d-4767-b130-73028d8b770b" />


The application displays:

```text
- Temperature
- Feels Like
- Humidity
- Pressure
- Condition
```

## Conclusion

SkySense AI demonstrates how Python and Streamlit can be used to build an interactive weather assistant. By integrating a weather service through the PyOWM library and securely managing the API key through an environment variable, the project provides a practical example of API integration and secure application development.
