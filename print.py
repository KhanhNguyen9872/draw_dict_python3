#!/bin/python3
#Bạn có thể in ra 1 lúc nhiều dict nhưng những dict in ra phải cùng 1 độ dài
def main():
    global user_input
    size=1
    portrait=0
    landscape=999999
    for i in user_input:
        try:
            temp=eval(i)["p"]
            temp1=eval(i)["l"]
        except:
            print(f"dict {i} not found!")
            exit()
        if (int(temp) > portrait):
	        portrait=int(temp)
        if (int(temp1) < landscape):
	        landscape=int(temp1)
    del temp
    del temp1
    size_landscape=int(landscape)
    for i in range (1,portrait+1,1):
        for char in user_input:
            for i in range(size,size_landscape+1,1):
                if (i in eval(char)):
                    print(eval(char)[i],end="")
                else:
                    print(" ",end="")
                if (char == user_input[-1]):
                    size+=1
                    size_landscape+=1
            print(end="  ")
        print(end="\n")
        
if (__name__=="__main__"):
    with open("dict.txt", "r", encoding = 'utf-8') as f:
        file = f.readlines()
        for i in file:
            exec(i)
            try:
                exec(f"""global {i.split("=")[0]}""")
            except:
            	continue
    print("Nhập tên dict: ",end="")
    user_input=[x for x in input().upper().split(" ")]
    main()
        
