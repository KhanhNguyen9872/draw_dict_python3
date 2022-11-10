#!/bin/python3
def clear():
    if (os.name == 'nt'):
        os.system("cls")
    else:
        os.system("clear")
def main():
	global name, limit, num
	print(f"Tên dict: {name}\nNhập dấu * [Độ dài: {limit}]\n Gõ [cmd save] để hoàn tất!\n Gõ [cmd clear] để xóa toàn bộ dòng\n Gõ [cmd del] để xóa 1 dòng trước đó\n Gõ [cmd undo] để khôi phục lại dòng trước đó\n Gõ [cmd exit] để thoát\n\n{num}")
def draw(name,limit,num,count):
    user_input=""""""
    show=""""""
    lines=0
    undo_text=""""""
    clear()
    main()
    while True:
        inp=str(input())
        if (inp == "cmd save"):
            break
        elif (inp == "cmd clear"):
            if (user_input != ""):
                for _ in range(0,int(len(user_input) / limit),1):
                    undo_text+=user_input[-limit:]
                    user_input=user_input[:-limit]
                user_input=""""""
                show=""""""
                lines=0
        elif (inp == "cmd del"):
            if (user_input != ""):
                undo_text+=user_input[-limit:]
                user_input=user_input[:-limit]
                show=show[:-(limit+1)]
                lines-=1
        elif (inp == "cmd undo"):
            if (undo_text != ""):
                user_input+=undo_text[-limit:]
                show+=undo_text[-limit:] + "\n"
                undo_text=undo_text[:-limit]
                lines+=1
        elif (inp == "cmd exit"):
        	print("Exiting")
        	exit()
        else:
            if (len(inp)>limit):
                inp=inp[:limit]
            elif (len(inp)<limit):
                for _ in range(0,int(limit - len(inp)),1):
                	inp+=" "
            user_input+=inp
            show+=f"{inp}\n"
            lines+=1
        clear()
        main()
        print(show,end="")
    convert_to_dict(user_input,limit,lines)
def convert_to_dict(user_input,limit,lines):
    dict={}
    count=1
    for line in user_input:
        if (line != " "):
            dict[count]=str(line)
        count+=1
    dict["l"]=limit
    dict["p"]=lines
    save(name,dict)
def save(name,dict):
    with open("dict.py", "a", encoding = 'utf-8') as f:
        f.write(f"\n{name}={dict}")
        print("Saved to dict.py file!")
    exit()

if (__name__ == "__main__"):
    import os
    num=""
    count=1
    name=""
    clear()
    while (name==""):
        name=str(input("Đặt tên dict: ")).upper()
        try:
            int(name)==0
            name=""
            print("Vui lòng nhập có chữ")
            continue
        except:
        	break
    limit=int(input("Nhập độ dài: "))
    if (limit > 100) or (limit < 1):
	    print("Sai giới hạn [1-100]")
	    exit()
    for _ in range(0,limit,1):
        num+=str(count)
        count+=1
        if (count==10):
            count=0
    draw(name,limit,num,count)
