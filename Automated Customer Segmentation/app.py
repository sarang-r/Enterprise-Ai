from flask import *
from numpy.lib.function_base import select  
import pandas as pd
import numpy as np
from io import StringIO

from RFM import rfm
obj = rfm()
app = Flask(__name__)  

@app.route('/')  
def upload():  
    return render_template("file_upload_form.html")  
 
@app.route('/success', methods = ['POST'])  
def success(): 
    if request.method == 'POST':  
        f = request.files['file']  
        # f.save(f.filename)  
        # df = pd.read_csv(f.stream)
        # return render_template("success.html", name = f.filename)
        df = obj.dataframe(f.stream)
        return df.to_html()
    

@app.route('/dropdown', methods=['GET'])
def dropdown():
    df = obj.data()
    columns_list = df.columns.tolist()
    return render_template('test.html', colours=columns_list)

@app.route("/test" , methods=['GET', 'POST'])
def test():
    df = obj.data()
    select_1 = request.form.get('comp_select_1')
    select_2 = request.form.get('comp_select_2')
    select_3 = request.form.get('comp_select_3')
    select_4 = request.form.get('comp_select_4')
    
    
    df_RFM_1 = obj.rfm_features(df,str(select_1),str(select_2),str(select_3),str(select_4))
    df_RFM = df_RFM_1
    df_RFM = obj.automate_segmentation(df_RFM)
    df_RFM_SUM = obj.RFM_score(df_RFM,select_1)
    matrix = obj.Value_Matrix(df_RFM_SUM)
    
    matrix = matrix[2]
    # return df_RFM_1.to_html(), df_RFM.to_html(), df_RFM_SUM.to_html()
    # return df_RFM_SUM.to_html()
    return matrix.to_html()


if __name__ == '__main__':  
    app.run(debug = True)  