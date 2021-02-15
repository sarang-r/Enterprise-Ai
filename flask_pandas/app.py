from flask import *
import pandas as pd
app = Flask(__name__)

@app.route("/tables")
def show_tables():
    data = pd.read_csv('data.csv')
    data.set_index(['Name'], inplace=True)
    data.index.name=None
    females = data.loc[data.Gender=='f']
    males = data.loc[data.Gender=='m']
    return render_template('view.html',tables=[females.to_html(classes='female'), males.to_html(classes='male')],
    titles = ['na', 'Female surfers', 'Male surfers'])

if __name__ == "__main__":
    app.run(debug=True)
# https://sarahleejane.github.io/learning/python/2015/08/09/simple-tables-in-webapps-using-flask-and-pandas-with-python.html