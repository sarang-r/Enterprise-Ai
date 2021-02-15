from flask import *
from som import class_som


app = Flask(__name__)  


obj = class_som()

# @app.route('/')  
# def upload():  
#     return render_template("file_upload_form.html")  
 
@app.route('/')  
def home():  
    return render_template("som.html")  
 
@app.route('/success', methods = ['POST'])  
def success(): 
    if request.method == 'POST':  
        f = request.files['file']  
        # f.save(f.filename)  
        # df = pd.read_csv(f.stream)
        # return render_template("success.html", name = f.filename)
        df = obj.dataframe(f.stream)
        
        return str("str")
    
@app.route('/your_flask_funtion') 
def get_ses(): 
    obj = class_som()
    obj.func_som()
    
    return render_template('plot.html', url='/static/images/plot.png')

@app.route('/your_flask_funtion2') 
def get_ses2(): 
    obj = class_som()
    obj.func_som()
    
    return render_template('plot.html', url='/static/images/plot2.png')


    
if __name__ == '__main__':  
    app.run(debug = True)  
    
