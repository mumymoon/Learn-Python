spam=['a','b','c','d']
def dot(p):
    for i in range(len(p)):
        if i+1<len(p):
            p[i]=p[i]+", "
        else:
            p[i]="and "+p[i]
        
dot(spam)
print(spam)
        
