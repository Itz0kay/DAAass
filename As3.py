
class Item: 
    def __init__ (self, value, weight):
        self.value = value 
        self.weight = weight

        
def fractionalKnapsack(W, arr):
# Sorting Item on basis of ratio
    arr.sort(key=lambda x: (x.value/x.weight), reverse=True)#for decresing order
# Result(value in Knapsack)
    finalvalue = 0.0
    # Looping through all Items
    for item in arr: 
       if item.weight <= W: 
          W -= item.weight
          finalvalue += item.value# If we can't add current Item, add fractional part of it
       else:
         finalvalue += item.value * W / item.weight 
         break
    # Returning final value
    return finalvalue

# Driver Code
if __name__ == "__main__":
    W = 50
    arr = [Item(60, 10), Item(100, 20), Item(120, 30)]
# Function call
    max_val = fractionalKnapsack(W, arr)
    print(max_val)
    # -*- coding: utf-8 -*-






























'''
#my practice ..
class item:
    def __init__(self,value,weight):
        self.value=value
        self.weight=weight
def FracKnapsack(w,arr):
    arr.sort(key=lambda x:(x.value/x.weight),reverse=True)
    final=0.0
    for itm in arr:
        if itm.weight<=w:
            w-=itm.weight
            final+=itm.value
        else:
            final+=itm.value*w/itm.weight 
            break 
    return final
if __name__=="__main__":
    w=50
    arr=[item(60,10),item(100,20),item(120,30)]
    max=FracKnapsack(w,arr)
    print(max)
'''   













