import pandas as pd
import streamlit as st
from weather import Weather


st.set_page_config(
        page_title='MAUSAM',
        initial_sidebar_state="auto",
        layout='wide'
    )

# Function to fetch current weather data
def fetch_weather_data(city):
    try:
        weather = Weather(city=city)
        current_weather_data = weather.current()
        return current_weather_data['data'][0]
    except Exception as e:
        st.error(f"Error fetching weather data: {e}")
        return None

def main():


    col1, col2, col3 = st.columns(3)
    with col1:
        st.empty()

    with col2:
        st.image(
            'static/images/logo.png',
            width=200
        )

        st.title("Welcome to :blue[MAUSAM]")
        st.caption("_For all your weather needs_")

        st.divider()

        city = st.text_input(
            label='Enter your city name.',
            value='Ex: New Delhi'
        )

        submit_button = st.button(
            label='Get Weather',
            type='primary'
        )

    

        if submit_button:
            if city:
                current_weather_data = fetch_weather_data(city)
                if current_weather_data:
                    relevant_keys = [
                        'city_name', 'country_code', 'ob_time',
                        'temp', 'app_temp', 'precip', 'rh',
                        'clouds', 'aqi', 'pres', 'wind_spd',
                        'wind_dir', 'wind_cdir_full', 'vis'
                    ]
                    relevant_current_weather_data = {
                        key: value for key, value in current_weather_data.items()
                        if key in relevant_keys
                    }

                    st.divider()
                    # st.write(relevant_current_weather_data)

                    df = pd.DataFrame(relevant_current_weather_data.items(), columns=['Weather Parameters', 'Value'])
                    # Rename the "Parameter" column
                    column_aliases = {
                        'city_name': 'City Name', 'country_code': 'Country Code', 'ob_time': 'Observation Time',
                        'temp': 'Temperature (Celsius)', 'app_temp': 'Apparent Temperature (Celsius)',
                        'precip': 'Precipitation Rate (mm/hr)', 'rh': 'Relative Humidity',
                        'clouds': 'Cloud Coverage (%)', 'aqi': 'Air Quality Index', 'vis': 'Visibility (km)',
                        'pres': 'Pressure (mb)', 'wind_spd': 'Wind Speed (m/s)', 'wind_dir': 'Wind Direction (degrees)', 'wind_cdir_full': 'Verbal Wind Direction'
                    }

                    df['Weather Parameters'] = df['Weather Parameters'].map(column_aliases)


                    parameter_order = [
                        'City Name', 'Country Code', 'Observation Time',
                        'Temperature (Celsius)', 'Apparent Temperature (Celsius)',
                        'Precipitation Rate (mm/hr)', 'Relative Humidity',
                        'Cloud Coverage (%)', 'Air Quality Index', 'Pressure (mb)',
                        'Wind Speed (m/s)', 'Wind Direction (degrees)',
                        'Verbal Wind Direction', 'Visibility (km)'
                    ]

                    df['Weather Parameters'] = pd.Categorical(df['Weather Parameters'], categories=parameter_order, ordered=True)
                    df = df.sort_values('Weather Parameters')

                    st.table(df)
            else:
                st.warning("Please enter a city name.")
            


    with col3:
        st.empty()

hide_streamlit_style = """
            <style>
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)


if __name__ == "__main__":
    main()







    





