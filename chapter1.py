nums = [12,15,16,17,18,19,20]


for i in nums:
    if i % 2 == 0 and i %3 ==0:
        print(f'{i} is divided by 3 and 2 ')
    elif i % 2 == 0:
        print(f'{i} is divied by 2 ')        
    elif i % 3 == 0:
        print(f'{i} is divied by 3 ')
    else:
        print(f" {i} not divided by any thing")        

