birthdays={'dad':'lunar 1024','mom':'lunar 0102','grandma':'lunar 1108','auntie':'lunar 1123','little sister':'lunar 1016','qing':'lunar 0317'
           ,'gongling':'lunar 321','yancai':'gregorian 0823','passby':'lunar 0213','xiaohouzi':'lunar0101','luowei':'lunar0304','Linda':'lunar0320','Rose':'gregorian0420'}
while True:
    name=input()
    if name=='':
        break
    if name in birthdays:
        print(birthdays[name]+ ' is the brithday of '+name)
    else:
        print('I do not know his birthday')
        newbirthday=input()
        birthdays[name]=newbirthday
        print('birthday datebase updated')
    
