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
    obj.color_map()
    return render_template('som.html', url='/static/images/plot1.png')

@app.route('/your_flask_funtion2') 
def get_ses2(): 
    obj = class_som()
    obj.func_som()
    obj.color_map2()
    obj.color_map_combine()
    
    return render_template('som.html', url='/static/images/plot2.jpg')

@app.route('/your_flask_funtion3') 
def get_ses3(): 
    obj = class_som()
    obj.func_som()
    obj.color_map2()
    obj.color_map_combine()
    
    return render_template('som.html', url='/static/images/plot3.png')




    
if __name__ == '__main__':  
    app.run(debug = True)  
    
