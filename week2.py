def validate_pin(pin):
    pin = str(pin)
    if (pin.isdigit() and (len(pin) == 4 or len(pin) == 6 )):
        return True
    return False
    
