import pickle,json
import numpy as np

__dataColumns =None
__model = None
__locations = None

def getLocations():
    loadelements()
    return __locations

def predictPrice(location,sqft,bhk,bath):
    loadelements()
    try:
        loc_index = __dataColumns.index(location.lower())
    except:
        loc_index = -1
         
    x = np.zeros(len(__dataColumns))
    x[0] = sqft
    x[1] = bhk
    x[2] = bath
    
    if loc_index >= 0:
        x[loc_index] = 1
        
    return round(__model.predict([x])[0],2)


def loadelements():
    global __dataColumns
    global __model
    global __locations
    
    with open("documents\columns.json","r") as f:
        __dataColumns = json.load(f)["data_columns"]
        
        __locations = __dataColumns[3:]
        # print(__dataColumns)
        
        # print("locations loded succesfully..")
        
    with open('./documents/banglore_home_prices_model.pickle',"rb") as f:
        __model = pickle.load(f)
        # print("model lodded succesfully")
        
        
        
        
        
        

if __name__ == "__main__":
    loadelements()
    print(predictPrice("kenchenahalli",1200,2,1))
