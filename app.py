from flask import Flask , request , jsonify , render_template
from utils import get_prediction



app=Flask(__name__)
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def concrete_strength():
    data=request.form

    cement=eval(data['cement'])
    Blast_furnace_slag=eval(data['blast_furnace_slag'])
    Fly_Ash=eval(data['fly_ash'])
    water=eval(data['water'])
    Superplasticizer=eval(data['superplasticizer'])
    Coarse_Aggregate=eval(data['coarse_aggregate'])
    Fine_Aggregate=eval(data['fine_aggregate'])
    Age=eval(data['age'])

    
    result=get_prediction(cement, Blast_furnace_slag, Fly_Ash, water,
                          Superplasticizer, Coarse_Aggregate, Fine_Aggregate,Age)
    
    return render_template('index.html',prediction_text=f'Concrete compressive strength is {result} Mpa')
        

    

if __name__ == '__main__' :
    app.run(port=1003,debug=False)
    


