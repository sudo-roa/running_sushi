import time

'''
#mapの初期配置に関する関数定義
def CleanMap(X,Y):
    map = [[" "] * X for i in range(Y)] #mapの初期化(配列[Y][X])
    return map
'''

def Map(X,Y):
#    map = CleanMap(X,Y)
    map = [[" "] * X for i in range(Y)] #mapの初期化(配列[Y][X])
    for i in range(Y):
        for j in range(X):
            #外側4辺
            map[0][j] = "-" #上辺
            map[i][0] = "|" #左辺
            map[i][X-1] = "|" #右辺
            map[Y-1][j] = "-" #下辺
            #内側4辺(何行になるかわからないので、内側は条件付きで置換) 
            if(i>1 and Y-2>i and j>1 and X-2>j):
                map[i][j] = " "
                #内側4辺
                map[2][j] = "-" #上辺
                map[i][2] = "|" #左辺
                map[i][X-3] = "|" #右辺
                map[Y-3][j] = "-" #下辺
    #外側4角(forループ不要)
    map[0][0] = "+" #左上角
    map[0][X-1] = "+" #右上角
    map[Y-1][0] = "+" #左下角
    map[Y-1][X-1] = "+" #右下角
    #内側4角(forループ不要)
    map[2][2] = "+" #左上角
    map[2][X-3] = "+" #右上角
    map[Y-3][2] = "+" #左下角
    map[Y-3][X-3] = "+" #右下角
    #初期マップ確認用
#    print (map)
    return map

'''
#関数の確認
Y = 20
X = 10
Map(X,Y)
'''