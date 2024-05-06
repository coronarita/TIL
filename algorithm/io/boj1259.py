while 1 :
    n = input()
    m = n[::-1]    
    if n != '0' :
        if n == m :
            print("yes")
        else :
            print("no")
    else :
        break