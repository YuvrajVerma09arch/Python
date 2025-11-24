from flask import Flask,request,jsonify,render_template
import joblib
import pandas as pd
app=Flask(__name__)
model=joblib.load('flower_model.joblib')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/flower_predictor',methods=['POST'])
def predictor():
    try:
        features=[
            float(request.form['sepal_length']),
            float(request.form['sepal_width']),
            float(request.form['petal_length']),
            float(request.form['petal_width']),
            float(request.form['color_code']),
            float(request.form['has_thorns']),
        ]
        raw_data=model.predict([features])
        num_data=raw_data[0]
        variant={0:'rose',1:'sunflower',2:'marigold'}
        if num_data in variant:
            ans=variant[int(num_data)]
        else:
            ans='UNKNOWN flower type'
        return render_template('index.html', final_verdict=f"That is a {ans}")
    except Exception as e:
        return render_template('index.html', final_verdict=f"Error: {str(e)}")

if __name__=='__main__':
    app.run(debug=True)