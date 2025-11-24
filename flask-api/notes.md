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
df = pd.read_csv('flowers.csv')           # Reads your custom Excel/CSV file
3. Training & Saving

Python
# X = Questions (Features), y = Answers (Labels)
model.fit(X, y)                           # The "Study" command. Model learns patterns.
joblib.dump(model, 'flower_model.joblib') # Saves the trained model to a file.
Part 2: The "Server" (The API)
File: app.py

1. Essential Methods

Flask(__name__): Creates the app object.

@app.route("/", methods=['GET']): Defines a URL for viewing (like the home page).

@app.route("/predict", methods=['POST']): Defines a URL for receiving data (submission).

app.run(debug=True): Starts the web server. debug=True allows auto-restart on code changes.

2. Loading the Brain

Python
# Load this AT THE TOP (Global Scope), so it only loads once.
model = joblib.load('flower_model.joblib')
3. Handling Inputs (The "Ears")

Python
# If data comes from HTML Form:
val = request.form['input_name']          # Use Square Brackets []

# If data comes from Curl/Code (JSON):
val = request.json['input_name']
4. Making Predictions (The Logic)

Python
# ⚠️ CRITICAL: The model needs a "Batch" (List of Lists)
# Wrong: model.predict([1, 2, 3])
# Right: model.predict([[1, 2, 3]])
prediction_raw = model.predict([features])

# Fix the NumPy Error (Convert math number to Python number)
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
⚡ Quick Troubleshooting Guide
Error Message	Likely Cause	Solution
"Method Not Allowed"	You tried to visit a POST URL (like /predict) directly in the browser.	Go to the Home URL (/) first, then submit the form.
"ImmutableDict not callable"	You used parentheses () to get data.	Use square brackets: request.form['key'].
"Unhashable type: numpy.ndarray"	You used the raw model output as a dictionary key.	Wrap it in int(): species_map[int(prediction[0])].
"Expected 2D array"	You passed a flat list to .predict.	Wrap features in extra brackets: model.predict([[f1, f2, ...]]).