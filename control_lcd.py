import time

def escriure_lcd(missatge, lcd, temps_espera = 5):
    if len(str(missatge)) <= 32:
        lcd.clear()
        lcd.putstr(str(missatge))
    
    else:
        num_maxim = 32
        llista_missatges = [missatge[i:i+num_maxim] for i in range(0, len(missatge), num_maxim)]
        for msg in llista_missatges:
            lcd.clear()
            lcd.putstr(str(msg))
            time.sleep(temps_espera)