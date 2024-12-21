#List Data type
cart_list = ['toys','fruits',9,45.50,True,[3.5,77,'veggies'],'python',45,'India'] #way1
counter_list = list(['praveen','py',99])  #way2 builtin mostly used in conversion
print(cart_list)
print(type(counter_list))
print(counter_list)
print(f"First element : {cart_list[0]}") #index starts at 0
print(f"first element : {cart_list[-6]}") # in reverse first index is -len(list)
last_ind = len(cart_list)-1     #n-1
print(f"Last element : {cart_list[last_ind]}")   #India
print(f"Last element : {cart_list[-1]}") # in reverse last index is -1
#Slicing [strt:stp:skp]  or [strt:stp]
print(cart_list[2:7]) # prints elements from 2 to 6 
print(cart_list[:-7]) # prints elements at index -9,-8
print(cart_list[5:]) #prints elements from 5 to last index
print(cart_list[-1:-5:-2]) #prints element at index -1,-3
print(cart_list[5:0:-2]) #prints elements at index 5,3,1
print(cart_list[-1:-8:-3]) # prints elements at index -1,-4,-7
print(cart_list[2:8:-3]) # prints empty list as start and stop is forward, skip is negative
print(cart_list[4:0]) # prints empty list as its backward flow
print(cart_list[4:0:-1]) # prints elements at index 4,3,2,1
print(cart_list[:]) #prints complete list
print(cart_list[::]) #prints complete list
print(cart_list[:-1]) #skips last elements prints rest all
print(cart_list[::-1]) # prints list in reverse
print(cart_list[2:2])# print empty as start and stop are at same
print(f"Element as 4 th index : {cart_list[4]}") #True
cart_list[4] = "Aki"
print(f"Element as 4 th index : {cart_list[4]}") #replaced with Aki
cric_team = [44,'Kohli','Rohit','Zaheer',63,'Kohli',44,7,44,'Rohit']
cric_team.append(['laxman','Dravid','kumble']) # appends as a sublist
print(cric_team)
cric_team.extend(['Irfi','Dhoni']) # extends the list by adding as elements
print(cric_team)
print(cric_team.count(44)) # returns the count of occurance in the list
print(cric_team.count('Kohli'))
print(cric_team.index('Irfi')) # returns the index of the element in list
print(cric_team.index('Rohit')) #returns the first occurance index when multiple elements exist 
print(f"length of the list : {len(cric_team)}")
india_team = cric_team  #copied with same location id
print(india_team)
print(f"memory location of india_team : {id(india_team)}")
print(f"memory location of cric_team : {id(cric_team)}")
print(india_team==cric_team)#comparing two lists
india_team.append("Sanju samson") # effects cric_team list too as it shares same location id
print(india_team)
print(cric_team)
print(india_team==cric_team)
cp_team_india = india_team.copy() # copied to a diff new id
print(f"memory location of india_team : {id(india_team)}")
print(f"memory location of cp_team_india : {id(cp_team_india)}")
cp_team_india.append("Venkatesh Iyer") # no effect on india_team list
cp_team_india.extend(["zampa","zara"])
print(cp_team_india)
print(india_team)
print(cp_team_india==india_team)
cart_list.clear() #clears elements from entire list
print(cart_list)
print(india_team)
india_team.pop()  # last element is popped out of the list
india_team.pop(10) # removes element at index 10
print(india_team)
india_team.insert(0,"Sanju samson") # inserts element at particular index
print(india_team)
india_team.remove(44) #removes first occurance of element in list
print(india_team)
cp_team_india.remove("zampa") #removes element from list
print(cp_team_india)
cp_team_india.reverse() #reverse the list
print(cp_team_india)
marks_list = [23,44,66,25,99,-1,-4]
marks_list.sort() # sorts an integer list in ascending
print(marks_list)
marks_list.sort(reverse=True) # sorts an integer list in descending order
print(marks_list)
#List Comprehension
wicket_list = ["good shot" if i>0 else "wicket down" for i in range(6)]   #shorthand if
print(wicket_list)

car_brands = ['tata','mahindra','hyundai','honda','aston martin','BMW']
req_cars = [x for x in car_brands if 'n' in x]  # filtering elements with 'n' 
print(req_cars)

start_year  = int(input("Enter start year : "))
end_year = int(input("Enter end year : "))
leap_list=[year for year in range(start_year,end_year+1) if year%4==0 and (year%100!=0 or year%400==0)]
print(leap_list)

year = int(input("Enter year : "))
print(f"{year} is leap year") if year%4==0 and (year%100!=0 or year%400==0) else print(f"{year} is not leap year")


num5_list = [1,5,5,4,7,5,3,8,99,5,89]
for i in num5_list:
    if i==5:
        num5_list.remove(5)
print(num5_list)