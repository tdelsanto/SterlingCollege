import requests


def fetch_weather_data():
    try:
        # Conecta ao  API
        response = requests.get(f"https://api.open-meteo.com/v1/forecast?latitude={49.2846}&longitude={-122.7822}&hourly=relativehumidity_2m,pressure_msl,temperature_2m")

        # Verifique requisição (bem-sucedida = código 200)
        if response.status_code == 200:
            # Obtenha resposta JSON
            weather_data = response.json()

            # Obtenha os valores de umidade, pressão e temperatura
            humidity = weather_data['hourly']['relativehumidity_2m'][0]
            pressure = weather_data['hourly']['pressure_msl'][0]
            temperature = weather_data['hourly']['temperature_2m'][0]

            return humidity, pressure, temperature
        else:
            print(f"Erro. Código de status: {response.status_code}")
            return None
    except Exception as e:
        print(f"Erro: {e}")
        return None

# Obtem os dados do clima
weather_data = fetch_weather_data()


# Imprimi os dados
if weather_data is not None:
    humidity, pressure, temp = weather_data
    print(f"Umidade: {humidity}%")
    print(f"Pressão: {pressure} hPa")
    print(f"Temperatura: {temp}°C")
else:
    print("Não conectou.")


