# importing Flask and other modules
from flask import Flask, request, render_template 

# Flask constructor
app = Flask(__name__)   

# A decorator used to tell the application
# which URL is associated function
@app.route('/', methods =["GET"])
def main():

    template = "main_page.html"

    return render_template(template)

if __name__=='__main__':
   app.run()
