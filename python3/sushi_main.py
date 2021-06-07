import time
import os
import sushi_move
import sushi_map

X = 20
Y = 10

if __name__ == '__main__':
    #初期位置
    i = 1
    j = 1
    #ループ
    while True:
        if (i==1 and X-2>j):
            j += 1
        elif(j==X-2 and Y-2>i):
            i += 1
        elif(i==Y-2 and j>1):
            j -= 1
        elif(j==1 and i>1):
            i -= 1
        map = sushi_move.Sushi_move(i,j,X,Y)
        
        for m in range(Y):
            for n in range(X):
                print(map[m][n],end="")
            print()
        time.sleep(0.05)
        print("\033[10A",end="")#10個上に戻る