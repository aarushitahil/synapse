n = int(input('Enter number of customers: '))
print('Enter arrival time and order prep time (as space seperated integers with each customer on a new line)')
l = [list(map(int, input().split())) for _ in range(n)]

wait_time = 0   #we will add sum of all waiting times to this variable
current_time = l[0][0]  #assigning arrival time of first customer as current time 

for i in l:     
    if current_time > i[0]:     #if customer arrived before prev order being completed
        wait_time += current_time - i[0] + i[1]  #diff between time rn and time customer arrived + order prep time
        current_time += i[1]  
    else:                       #if there is buffer time between two customers
        wait_time += i[1]
        current_time = i[0] + i[1]

print(f'Average time is {wait_time/n}')  


# sample input:
# Enter number of customers: 4
# Enter arrival time and order prep time (as space seperated integers with each customer on a new line)
# 5 2
# 5 4
# 10 3
# 20 1
# sample output:
# Average time is 3.25