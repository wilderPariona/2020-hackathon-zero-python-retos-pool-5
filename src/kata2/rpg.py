#!/usr/bin/python

import random
import string

def RandomPasswordGenerator(passLen=10):
    #
    #
    txt_aleatorio = string.ascii_letters + string.digits + string.punctuation
    clave_generada = ""
    for i in range(passLen):
        clave_generada += str(random.choice(txt_aleatorio))
    #
    #
    return clave_generada

RandomPasswordGenerator()
