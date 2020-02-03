def validate_pin(pin):
    if (otp.isdecimal() and (len(otp) == 4 or len(otp) == 6 )):
        return True
    return False

