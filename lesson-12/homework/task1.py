from bs4 import BeautifulSoup

with open("weather.html", "r", encoding="utf-8") as file:
    soup = BeautifulSoup(file, "html.parser")

rows = soup.find("table").find("tbody").find_all("tr")

weather_data = []
temperatures = []

for row in rows:
    cols = row.find_all("td")
    day = cols[0].text.strip()
    temp = int(cols[1].text.strip().replace("°C", ""))
    condition = cols[2].text.strip()
    weather_data.append({"day": day, "temperature": temp, "condition": condition})
    temperatures.append(temp)

print("5-Day Weather Forecast:")
for entry in weather_data:
    print(f"{entry['day']}: {entry['temperature']}°C, {entry['condition']}")

max_temp = max(temperatures)
hottest_days = [entry["day"] for entry in weather_data if entry["temperature"] == max_temp]
print(f"\nHottest day(s): {', '.join(hottest_days)} with {max_temp}°C")

sunny_days = [entry["day"] for entry in weather_data if entry["condition"].lower() == "sunny"]
print(f"Sunny day(s): {', '.join(sunny_days)}")

avg_temp = sum(temperatures) / len(temperatures)
print(f"\nAverage temperature for the week: {avg_temp:.2f}°C")
