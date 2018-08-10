#collatz
def collatz(number):
    while True:
        if int(number)%2==0:
            number= int(number)//2
        elif int(number)%2==1 and int(number)!=1:
            number= 3*int(number)+1
        else:
            return int(1)
        print(number)
                
try:
    mun=input()
    collatz(mun)
except ValueError:
    print('please enter an int')
    
