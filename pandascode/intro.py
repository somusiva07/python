import pandas as pd 

myDataSet = {
    'Car' : ['Maruti', 'Tata','Mahindra'],
    'Model': [1980,1990,1995]
}

myVar = pd.DataFrame(myDataSet)

print(myVar)