import numpy as np
import pickle 
import config


def get_prediction(cement, Blast_furnace_slag, Fly_Ash, water,
       Superplasticizer, Coarse_Aggregate, Fine_Aggregate,Age):
     
    

    with open(config.pickle_path , 'rb') as f:
        model=pickle.load(f)

    
    test_array=np.array([[cement, Blast_furnace_slag, Fly_Ash, water,
       Superplasticizer, Coarse_Aggregate, Fine_Aggregate, Age ]])
    
    result=model.predict(test_array)[0]

    return result