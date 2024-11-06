class Item:
    def __init__(self,value,weight):
        self.value=value
        self.weight=weight
    
    def get_ratio(self):
        return self.value/self.weight

def knapsack(items,capacity):
    items.sort(key=lambda x:x.get_ratio(),reverse=True)
    total_val=0.0
    for item in items:
        if capacity>0 and capacity>=item.weight:
            capacity-=item.weight
            total_val+=item.value
            print(item.weight)
            print(item.value)
        else:
            fraction=capacity/item.weight
            total_val+=fraction*item.value
            print(item.weight)
            print(item.value)
            break
    return total_val

items=[
    Item(100,20),
    Item(120,10),
    Item(90,30),
]
capacity=50
final_val=knapsack(items,capacity)
print(final_val)