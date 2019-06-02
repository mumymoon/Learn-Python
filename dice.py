def dice(number):
    if number==1:
        return('wish dishes')
    elif number==2:
        return('laundry cloth')
    elif number==3:
        return('clean house')
    elif number==4:
        return('massage each other')
    elif number==5:
        return('dry cloth')
    else:
        return('get water for feet')
import random
print(dice(random.randint(1,7)))
