from machine import I2C, Pin
import bme280
import utime

# I2Cインスタンスの作成
i2c = I2C(0, scl=Pin(1), sda=Pin(0))

# BME280センサーのインスタンス化
bme = bme280.BME280(i2c=i2c)

# 標高を計算する関数
def calculate_altitude(pressure):
    # 海面気圧
    sea_level_pressure = 1030
    return 44330 * (1.0 - (pressure / sea_level_pressure) ** 0.1903)

while True:
    # センサーから気圧を読み取る
    temp, pressure, humidity = bme.read_compensated_data()

    # hPa単位に変換
    pressure_hpa = pressure / 25600

    # 標高を計算
    altitude = calculate_altitude(pressure_hpa)

    # 気圧と標高のみを出力
    print("Pressure: {:.2f} hPa, Altitude: {:.2f} meters, Temperature: {:.2f} C, Humidity: {:.2f}".format(pressure_hpa, altitude, temp / 100, humidity / 1024))

    # 5秒待機（5000ミリ秒）
    utime.sleep_ms(5000)
