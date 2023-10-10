import machine 
import ssd1306  

# Configura la comunicación I2C para la pantalla OLED
i2c = machine.I2C(0, sda=machine.Pin(0), scl=machine.Pin(1), freq=400000)  # Utiliza los pines GP0 (sda) y GP1 (scl)

# Inicializa la pantalla OLED
oled = ssd1306.SSD1306_I2C(128, 64, i2c)

oled.text("WELCOME!", 0, 0)
oled.text("This is a text", 0, 16)
oled.text("GOOD BYE", 0, 32)

# Actualiza la pantalla OLED
oled.show()
