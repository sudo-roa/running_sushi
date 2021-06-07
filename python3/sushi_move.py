import time
import sushi_map

#SUSHIの移動
def Sushi_move(i,j,X,Y):
#    map = sushi_map.CleanMap(X,Y)
    map = sushi_map.Map(X,Y)
    map[i][j]="I"
    word =["H","S","U","S"]
    L = len(word)
    c = 0
    if(i==1):
        for n in range(1,L+1):
            if(j-n>0):
                map[i][j-n] = word.pop(0)
            elif(X-(L+1)>j):
                c += 1
                map[i+c][1] = word.pop(0)
    elif(j==X-2):
        for n in range(1,L+1):
            if(i-n>0):
                map[i-n][j] = word.pop(0)
            else:
                c+=1
                map[1][j-c] = word.pop(0)
    elif(i==Y-2):
        for n in range(1,L+1):
            if(X-1>j+n):
                map[i][j+n] = word.pop(0)
            else:
                c+=1
                map[i-c][X-2] = word.pop(0)
    elif(j==1):
        for n in range(1,L+1):
            if(Y-1>i+n):
                map[i+n][j] = word.pop(0)
            elif(i>L):
                c+=1
                map[Y-2][j+c] = word.pop(0)
#    print (map)
    return map
'''
X = 20
Y = 10
i = 1
j = 1 
Sushi_move(i,j,X,Y)
print(map)
'''