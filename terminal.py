def terminal():
    while True:
        userinput = input(">")
        if userinput[0] == "#" :
            continue
        elif userinput[0:5] == "code?" :
            print(terminal)
        elif userinput == "?" :
            print("this is a terminal mock created by s.s.r.w")
        elif userinput == "exit" :
            print("Bye!")
            break
        else :
            print(userinput)
terminal()
print("done")