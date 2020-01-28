def get_number(otp):
    if (otp.isdecimal() and (len(otp) == 4 or len(otp) == 6 )):
        return True
    return False
    
otp = input("here:")
print(get_number(otp))