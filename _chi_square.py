#defining the mean value                                          
def mean(x):
    x=[1,2,3,4]
    val=sum(x)
    val_one=len(x)
    mean=val/val_one
    return mean
 #defining chi square
def kai_square(x,y):
    for i in range(0,len(y)):
        kai_sqaure = y[0]+ mean(x) / mean(x)
        return kai_square
    print(sum(kai_square))
 
dataset = list()
value =list()
number = input("Enter the number of elements you want:")
for i in range(int(number)):
    val = input("Enter the value")
    data = input("Enter the data")
    value.append(int(val))
    dataset.append(int(data))

print ('Observation',value)
print('Data',dataset)

test = kai_sqaure(dataset,value)
