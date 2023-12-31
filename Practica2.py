import network
import urequests
import utime
from machine import Pin, I2C
import ssd1306

def conectar_wifi(ssid, password):
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print('Conectándose a la red WiFi...')
        sta_if.active(True)
        sta_if.connect(ssid, password)
        while not sta_if.isconnected():
            pass
    print('Conexión WiFi exitosa')
    print('Dirección IP:', sta_if.ifconfig()[0])

def obtener_hora():
    url = "http://worldtimeapi.org/api/ip"
    response = urequests.get(url)
    datos = response.json()
    return datos['datetime']

def configurar_oled():
    i2c = I2C(0, sda=Pin(0), scl=Pin(1))
    oled = ssd1306.SSD1306_I2C(128, 64, i2c)
    return oled

def mostrar_hora_en_oled(oled, hora):
    oled.fill(0)
    oled.text("Hora actual:", 0, 0)
    oled.text(hora, 0, 16)
    oled.show()

def main():
    ssid = "TecNM-ITT-Docentes"
    password = "tecnm2022!"

    conectar_wifi(ssid, password)
    oled = configurar_oled()

    while True:
        hora = obtener_hora()
        print("Hora:", hora)
        mostrar_hora_en_oled(oled, hora)
        utime.sleep(60) 

if __name__ == '__main__':
    main()
