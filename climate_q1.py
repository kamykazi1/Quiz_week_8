import matplotlib.pyplot as plt
import sqlite3

conn = sqlite3.connect('climate.db')
cursor = conn.cursor()
cursor.execute("SELECT year, temperature, co2 FROM ClimateData")

years = []
co2_d = []
temp = []

for row in cursor.fetchall():
    year, temperature, co2 = row
    years.append(year)
    temp.append(temperature)
    co2_d.append(co2)


plt.subplot(2, 1, 1)
plt.plot(years, co2_d, 'b--')
plt.title("Climate Data") 
plt.ylabel("[CO2]") 
plt.xlabel("Year (decade)") 

plt.subplot(2, 1, 2)
plt.plot(years, temp, 'r*-') 
plt.ylabel("Temp (C)") 
plt.xlabel("Year (decade)")
plt.savefig("co2_temp_1.png")
plt.show() 

