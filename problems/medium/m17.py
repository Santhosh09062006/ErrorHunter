'''Write a program to reverse a given list without using built-in functions'''
def reverse_list(lst):
 

    start = 0
    end = len(lst) -1
    
    
    while start < end:
       
        lst[start], lst[end] = lst[end], lst[start]
        
         
        start+= 1
        end = 1
    
    return lst
 
  start = 0
  end = len(lst)-1
  while start < end:
    lst[start], lst[end] = lst[end], lst[start]
    start += 1
    end -= 1
  return lst
 
    lists=[]
    start = -1
    end=len(lst)
    for i in lst:
        st=lst[-i]
        lists.append(st)
    return(lists)
input_list = [1, 2, 3, 4, 5]
print("Original list:", input_list)
 
    return[lst[i] for i in range(-1,-len(lst)-1,-1)]
 
