
# create random number
import random



def tebak():
    x = random.randint(1, 10)
    y = random.randint(1, 10)
    if x > y:
        print('x lebih besar dari y dimana ', x, '>', y)
    elif x < y:
        print('x lebih kecil dari y dimana ', x, '<', y)
    else:
        print('x sama dengan y dimana ', x, '=', y)

