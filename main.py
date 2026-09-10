from machine import I2C, Pin
from ens160 import ENS160
from ahtx0 import AHT20
import time

i2c = I2C(
    0,
    sda=Pin(0),
    scl=Pin(1),
    freq=100000
)

ens160 = ENS160(i2c)
aht21 = AHT20(i2c)

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

    except Exception as e:
        print("Error:", e)

    time.sleep(5)
