
#x, w, bias
x = [[0,0], [0,1], [1,0], [1,1]]
w = [0, 0]
bias = 0

#현재 출력 리스트 초기화
y=[0,0,0,0]

#정답 리스트
d = [0,1,1,0]

#학습률
n=0.1

epoch=0
print("학습률 : ",n)
while True:
    
    #현재 출력이 정답과 같으면 break
    if y == d:
        break    
    
    else:
        
        print("==========================","epoch:",epoch + 1,"===========================")
        print("|x1 x2|  현재출력  |  정답  |  가중치1  |  가중치2  |  Bias  |")
        print("===============================================================")
        epoch = epoch + 1
        
        for i in range(0,4):

            #가중치 w와 입력값 x,bias와 내적
            yk = x[i][0]*w[0] + x[i][1]*w[1] + 1.0*bias

            #함수에 따라 현재 출력 결정
            if yk < 0:
                y[i] = 0 
            else:
                y[i] = 1
                
            #바이어스 계산
            if y[i] > d[i]:
                bias = bias - n
            elif y[i] == d[i]:
                pass
            else:
                bias = bias + n
                
            #가중치 결정
            w[0] = w[0] + n*(d[i]-y[i])*x[i][0]
            w[1] = w[1] + n*(d[i]-y[i])*x[i][1]
            
            
            print("|",x[i][0],x[i][1],"|    ",y[i],"     |  ",d[i],"   |   ",w[0],"   |   ",w[1],"   | ",round(bias,2)," |")
            

    print("")
    
