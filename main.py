import machine
import time
import utilitats

class SensorHumitat():
    def __init__(self, sensor, led):
        """Inicialitza la classe SensorHumitat. Es defineixen paràmetres que seran constants durant tot el programa."""
        self.sensor_humitat = machine.ADC(machine.Pin(sensor)) # definim el pin del sensor com un input analògic
        self.led = machine.Pin(led, machine.Pin.OUT) # definim el pin del led com a output
        self.sensor_humitat.atten(machine.ADC.ATTN_11DB) #definim el màxim de 3.3 V
        self.humit = 1800 # definim el límit de la humitat, tot valor més petit serà humit
        self.sec = 2500 # definim el límit de la sequesa, tot valor més gran serà sec


    def llegir_sensor(self, sensor):
        """Retorna la lectura del sensor."""
        return sensor.read() # retorna la lectura del sensor
    

    def escriure_registre(self, valor):
        """Escriu en el fitxer 'registre.txt' els valor passat pels paràmetres."""
        with open("registre.txt", "a", encoding = "utf8") as registre: # obre el fitxer registre.txt
            registre.write(f"{valor}\n") # escriu al fitxer el valor


    def evaluar_valor(self, valor):
        """Evalua el valor obtingut i realitza les ordres corresponents en cada cas."""
        if valor < self.humit:
            self.led.value(0)
            utilitats.log(f"Valor: {valor}, HUMIT")

        elif valor > self.sec:
            self.led.value(1)
            utilitats.log(f"Valor: {valor}, SEC")

        else:
            self.led.value(0)
            utilitats.log(f"Valor: {valor}, INTERMIG")
            


    def main(self):
        while True:
            try:
                time.sleep(2) # esperem 2 segons entre crida i crida
                valor_sensor_humitat = self.llegir_sensor(self.sensor_humitat) # recollim el valor actual del sensor
                self.escriure_registre(valor_sensor_humitat) # escrivim al nostre registre aquest valor
                self.evaluar_valor(valor_sensor_humitat) # avaluem la situació i executem l'ordre que calgui

            except Exception as error:
                self.escriure_registre(f"{error}\n")
                utilitats.log(error)
                

pin_sensor_humitat = 32 # definim quin és el pin del sensor d'humitat
pin_led = 25 # definim quin és el pin del LED


sensor = SensorHumitat(pin_sensor_humitat, pin_led) # declarem l'objecte sensor
sensor.main() # cridem la funció principal de l'objecte sensor