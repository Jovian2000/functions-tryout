def fibonacci(nummer1,nummer2):    
    while True:
        uitkomst1 = nummer1 + nummer2    
        uitkomst2 = uitkomst1 + nummer2
        if uitkomst1 > 10000:
            return "stop"
        print(nummer1, nummer2, uitkomst1, fibonacci(uitkomst2, uitkomst1+uitkomst2))
        break
    return "^"     
    # nummer1, nummer2
    # uitkomst = nummer1 + nummer2
    # uitkomst2 = uitkomst + nummer2
    # for h in range(20):
    #     print(nummer1)            
    #     nummer1, nummer2 = nummer2, nummer1 + nummer2
        #  0, 1, 2
fibonacci(0,1)

# 0, 1, 1 , 
# 1, 1, 2

# 0, 1, 1, 2, 3, 5