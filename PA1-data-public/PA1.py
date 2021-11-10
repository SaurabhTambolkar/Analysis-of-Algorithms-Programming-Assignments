import sys

t = []

def AddInt(x):
    x = x.split(' ')
    n = int(x[1])
    #print("n",n)
    if len(t) == 0:
        t.append(n)
        #print(t)
        return
    elif len(t) == 1:
        #print("gg", t[0])
        if t[0] < n:
            #print("gm")
            t.append(n)
            #print(t)
            return
        else:
            #print("gn")
            t.insert(0,n)
            #print(t)
            return
    s = 0
    e = len(t) - 1
    m = int((s + e) / 2)
    while 1:
        #print(s,m,e)
        if e - s == 1:
            if n < t[s]:
                t.insert(s,n)
                #print(t)
                return
            elif n > t[e]:
                t.insert(e+1,n)
                #print(t)
                return
            else:
                t.insert(e,n)
                #print(t)
                return
        if e - s == 0:
            if n < t[e]:
                t.insert(e,n)
                #print(t)
                return
            else:
                t.insert(e+1,n)
                #print(t)
                return
        if n < t[m]:
            s = s
            e = m
            m = int((s + e) / 2)
        elif n == t[m]:
            t.insert(m,n)
            #print(t)
            return
        else:
            s = m
            e = e
            m = int((s + e) / 2)
            
while True:
    try:
        x = sys.stdin.readline().strip()
        if not x:
            break
        if x == '':
            break
        if x[0] == 'A':
            AddInt(x)
        elif x[0] == 'E':
            if len(t) == 0:
                print('none')
            else:
                print(t[0])
                del t[0]
    except:
        break
