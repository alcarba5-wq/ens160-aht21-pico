from machine import I2C, Pin
from ens160 import ENS160
from ahtx0 import AHT20
from ssd1306 import SSD1306_I2C


import time

i2c=I2C(0,scl=Pin(1),sda=Pin(0),freq=100000)
ens160 = ENS160(i2c)
aht21 = AHT20(i2c)

WIDTH =128 
HEIGHT= 64
i2c=I2C(0,scl=Pin(1),sda=Pin(0),freq=200000)
oled = SSD1306_I2C(WIDTH,HEIGHT,i2c)


print("ENS160 ID:", hex(ens160.get_id()))

while True:

    try:

        aqi, tvoc, eco2, eco2_rating, tvoc_rating = (
            ens160.read_air_quality()
        )

        temperatura = aht21.temperature
        humedad = aht21.relative_humidity

        print("-------------")
        print("AQI:", aqi)

        print("TVOC:", tvoc, "ppb")
        print("TVOC Rating:", tvoc_rating)

        print("eCO2:", eco2, "ppm")
        print("eCO2 Rating:", eco2_rating)

        print("Temp:", round(temperatura, 2), "°C")
        print("Hum :", round(humedad, 2), "%")
        
        oled.fill(0)
        oled.text(f"Temp: {temperatura:.1f} C", 0, 0)
        oled.text(f"Hum:  {humedad:.1f} %", 0, 9)
        oled.text(f"AQI:  {aqi}", 0, 18)
        oled.text(f"TVOC: {tvoc} ppb", 0, 27)
        oled.text(f"eCO2: {eco2} ppm", 0, 36)
        oled.text(f"Air:  {tvoc_rating}", 0, 45)  # Rating corto
        oled.text(f"CO2:  {eco2_rating.split('-')[0].strip()}", 0, 54)
        
        oled.show()
        

    except Exception as e:
        print("Error:", e)

    time.sleep(1)
