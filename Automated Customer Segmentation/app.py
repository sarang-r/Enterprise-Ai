from flask import *
from numpy.lib.function_base import select  
import pandas as pd
import numpy as np
from io import StringIO

from RFM import rfm
obj = rfm()
app = Flask(__name__)  

# @app.route('/')  
# def upload():  
#     return render_template("file_upload_form.html")  
 
@app.route('/')  
def home():  
    return render_template("index.html")  
 
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
    rfm_score = ['RFM features','Segment Customer','RFM Score']
    matrix_types = ['Monetary Matrix','Number of Customer','Recency Matrix']
    return render_template('test.html', colours=columns_list, rfm_score = rfm_score,matrix_ = matrix_types)


@app.route("/test" , methods=['GET', 'POST'])
def test():
    df = obj.data()
    
    select_1 = request.form.get('comp_select_1')
    select_2 = request.form.get('comp_select_2')
    
    select_3 = request.form.get('comp_select_3')
    select_4 = request.form.get('comp_select_4')
    
    global df_RFM_1
    df_RFM_1 = obj.rfm_features(df,str(select_1),str(select_2),str(select_3),str(select_4))
    
    df_RFM_sam = df_RFM_1
    global df_RFM
    df_RFM = obj.automate_segmentation(df_RFM_sam)
    
    global df_RFM_SUM
    df_RFM_SUM = obj.RFM_score(df_RFM,select_1)
    global matrix
    matrix = obj.Value_Matrix(df_RFM_SUM)
    # return df_RFM_1.to_html(), df_RFM.to_html(), df_RFM_SUM.to_html()
    # # return df_RFM_SUM.to_html()
    # rfm_score = request.form.get('score')

    return df_RFM.to_html()


@app.route("/test2" , methods=['GET', 'POST'])
def test2():
    select_1 = request.form.get('score')
    if select_1 == 'RFM Features':
        return df_RFM_1.to_html()
    elif select_1 == 'Segment Customer':
        return df_RFM.to_html()
    elif select_1 == 'RFM Score':
        return df_RFM_SUM.to_html()
    
    else:
        return df_RFM_1.to_html()
    


@app.route("/test3" , methods=['GET', 'POST'])
def test3():
    selected = request.form.get('matrix_type')
    if selected == 'Monetary Matrix':
        print(selected)
        return matrix[0].to_html()
    elif selected == 'Number of Customer':
        return matrix[1].to_html()
    elif selected == 'Recency Matrix':
        return matrix[2].to_html()
    else:
        return str("Don't lose")
    
    
    
    
if __name__ == '__main__':  
    app.run(debug = True)  