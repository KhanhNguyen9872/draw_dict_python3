#!/bin/python3
#Bạn có thể in ra 1 lúc nhiều dict bằng cách nhập tên các dict với các khoảng cách
#VD: a b android c yennhi
def main():
    global user_input, size
    variable=[]
    count=0
    portrait=0
    for i in user_input:
        try:
            temp=eval(i)["p"]
            temp1=eval(i)["l"]
        except:
            print(f"dict {i} not found!")
            exit()
        if (int(temp) > portrait):
	        portrait=int(temp)
        variable.append(f"dict{count}")
        exec(f"dict{count}=1")
        count+=1
    del temp1
    for i in range (1,portrait+1,1):
        temp=0
        for char in user_input:
            exec(f"global size; size=int({variable[temp]})")
            size_landscape=int(size+eval(char)["l"])
            for i in range(size,size_landscape,1):
                if (i in eval(char)):
                    print(eval(char)[i],end="")
                else:
                    print(end=" ")
            exec(f"{variable[temp]}={size_landscape}")
            temp+=1
            print(end=" ")
        print(end="\n")
        
if (__name__=="__main__"):
    from dict import *
    print("Nhập tên dict: ",end="")
    user_input=[x for x in input().upper().split(" ")]
    main()