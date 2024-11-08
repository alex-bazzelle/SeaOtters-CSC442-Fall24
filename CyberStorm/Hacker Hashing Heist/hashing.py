def pass_hash(password):
    length = len(password)
    
    while len(password) < 12:
        password = '\xbb' + password
    
    return "".join([chr(pow(0x1d, ord(c[1]) + c[0] - length, 0xfb))  for c in enumerate(password)])