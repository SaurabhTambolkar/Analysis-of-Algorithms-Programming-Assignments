import sys
t = []

#Method to rearrange Heap from Top to bottom
def rearrange(i):
    l ,r = 2*i + 1, 2*i + 2
    if l > len(t)-1:
        return
    z = i
    if l <= len(t) - 1 and r <= len(t) - 1:
        if t[l] < t[r]:
            z = l
        else:
            z = r
        if t[z] < t[i]:
            x = t[i]
            t[i] = t[z]
            t[z] = x
            rearrange(z)
    elif l <= len(t) - 1:
        z = l
        if t[z] < t[i]:
            x = t[i]
            t[i] = t[z]
            t[z] = x
            rearrange(z)
    

#Method to rearrange Heap from bottom to top            
def rearrange_from_bottom(i):
    if i == 0:
        return
    if i % 2 == 0:
        z = int(i/2) - 1
    else:
        z = int(i/2)
    if t[z] > t[i]:
        x = t[z]
        t[z] = t[i]
        t[i] = x
        rearrange_from_bottom(z)

#Method to Add Element in the Heap        
def Add_Element_Heap(x):
    t.append(x)
    rearrange_from_bottom(len(t)-1)

#Method to remove Element from the Heap    
def remove_Element_Heap():
    if len(t) == 0:
        return
    print(t[0])
    del t[0]
    if len(t) > 1:
        x = t[len(t) - 1]
        t.insert(0, x)
        del t[len(t) - 1]
        rearrange(0)


#Main Method to take inputs and pass to functions accordingly        
while True:
    try:
        x = sys.stdin.readline().strip()
        if not x:
            break
        if x == '':
            break
        if x[0] == 'A':
            z = x.split(' ')
            z = int(z[1])
            Add_Element_Heap(z)
        elif x[0] == 'E':
            if len(t) == 0:
                print('none')
            else:
                remove_Element_Heap()
    except:
        break

    