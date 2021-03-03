from ina219 import INA219
## sudo pip3 install pi-ina219
import time

## Messwiderstand, welcher momentan auf dem IN!219 verbaut ist
SHUNT_OHMS = 0.1 


def read():
    ina = INA219(SHUNT_OHMS)
    ina.configure()
    
##  print Current in mA
    print("Bus Current: %.3f mA" % ina.current())
    
##  print Power in mW
    print("Power: %.3f mW" % ina.power())
    print()
    
def main():
    while True:
        time.sleep(1)
        read()

if __name__=="__main__":
    main()
