from flask import Flask, render_template, request 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import cgi
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
import os
PEOPLE_FOLDER = os.path.join('static', 'images')

form = cgi.FieldStorage()
app = Flask(__name__)
app.config['UPLOAD_FOLDER']= PEOPLE_FOLDER
@app.route('/')
@app.route('/homepage')
def homepage():
    return render_template('reg_webapp.html')

@app.route('/getting', methods=['GET', 'POST'])
def getting():
    db_file = request.form['csv_file']
    data = pd.read_csv(db_file)
    if len(list(data))!= 2:
        exit

    x = data.iloc[:, 0:1].values
    x = np.array(x)
    x.reshape(-1, 1)
    y = data.iloc[:, -1].values
    y = np.array(y)
    y.reshape(-1, 1)
    polyi_x = PolynomialFeatures(degree = 8)
    poly_x = polyi_x.fit_transform(x)
    model = LinearRegression()
    model.fit(poly_x, y)
    y_predict = model.predict(poly_x)
    fig, ax = plt.subplots()
    ax.plot(x, y, color="red")
    ax.plot(x, y_predict, color="blue")
    fig.savefig(os.path.join(app.config['UPLOAD_FOLDER'],'polyreg_web_app.png'))
    fn = os.path.join(app.config['UPLOAD_FOLDER'],'polyreg_web_app.png')
    return render_template('show_img.html', url = fn)
#    img = fig.savefig('polyreg_web_app.png')
    

if __name__ == "__main__":
    app.run(debug=True,port=3000)
    

    #dependent_var = form.getvalue('dependent')
    #db_file = form.getvalue('csv_file')
    #image = resultpage(db_file)


"""
#@app.route('/resultpage')
def resultpage(db_file):
    #dep_list = []
    #indep_list = []
    #for i in list(dependent_var):
    #    if i == " ":
    #        continue
    #    else:
    #        dep_list.append((int)(i))
    #for j in list(independent_var):
    #    if j == " ":
    #        continue
    #    else:
    #       indep_list.append((int)(j))

    #polyi_indep = PolynomialFeatures(degree = 8)
    #poly_indep = polyi_indep.fit_transform(indep_list)

"""


"""x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2) 
    model = LinearRegression()
    model.fit(x_train, y_train)
    y_predict = model.predict(x_test)
"""