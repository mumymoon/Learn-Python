import pprint
message = 'when you are old and gray and full of sleep,and nodding by the fire, take down this book, ' \
          'and slowly read, and dream of the soft look, your eyes had once, and of their shadows deep;'
count={}
for i in message:
    count.setdefault(i,0)
    count[i]=count[i]+1
pprint.pprint(count)