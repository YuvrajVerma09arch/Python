# 📘 The AI Project Cheat Sheet: From Factory to Server

## Part 1: The "Factory" (Building the Brain)
*File: `build_model.py`*

**1. Essential Imports**
```python
import pandas as pd                                # The Data Manager (reads CSVs)
from sklearn.neighbors import KNeighborsClassifier # The Brain Structure (Algorithm)
import joblib                                      # The Freezer (Save/Load models)
2. Loading Data

Python
# OPTION A: Toy Data (For learning)
from sklearn.datasets import load_iris
data = load_iris()

# OPTION B: Real Data (For production)
df = pd.read_csv('flowers.csv')     
3. Training & Saving

Python
# X = Questions (Features), y = Answers (Labels)
model.fit(X, y)                           
joblib.dump(model, 'flower_model.joblib') 


Part 2: The "Server" (The API)
File: app.py

1. Essential Methods

Flask(__name__): Creates the app object.

@app.route("/", methods=['GET']): Defines a URL for viewing (like the home page).

@app.route("/predict", methods=['POST']): Defines a URL for receiving data (submission).

app.run(debug=True): Starts the web server. debug=True allows auto-restart on code changes.

2. Loading the Brain
Python
model = joblib.load('flower_model.joblib')


3. Handling Inputs (The "Ears")

Python
val = request.form['input_name']  
val = request.json['input_name']

4. Making Predictions (The Logic)

Python
# Wrong: model.predict([1, 2, 3])
# Right: model.predict([[1, 2, 3]])
prediction_raw = model.predict([features])

result = int(prediction_raw[0])


5. Sending Responses (The "Mouth")

Python
# Return HTML Page with data inserted:
return render_template('index.html', answer=result)
Part 3: The Frontend (HTML & Jinja2)
File: templates/index.html

1. The Form

action="/predict": The URL where data goes when you click submit.

method="POST": The secure method for sending data.

name="var_name": The KEY Python uses to grab the value (must match request.form['var_name']).

2. Jinja2 Magic (Python Logic inside HTML)

HTML
<div class="result"> The result is: {{ result_variable }} </div>

{% if result_variable %}
   <div> Only show this box if we have a result! </div>
{% endif %}
