#import Declarations
import datetime
from os import environ
from flask import Flask, render_template

app = Flask(__name__)

#HTML page routing

#Homepage Route-
@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'home.html',
        title='Home Page',
        year=datetime.datetime.now().year,
    )

#Contact Route-
@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.datetime.now().year,
        message='Send us a mail at'
    )

#About Route-   
@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.datetime.now().year,
        message='Your application description page.'
    )

#Products Route-
@app.route('/products')
def products():
    """Renders the product page."""
    return render_template(
        'Products.html',
        title='Products',
        year=datetime.datetime.now().year,
        message='Your products description page.'
    )

#Product1 Route-
@app.route('/prod1')
def prod1():
    """Renders the product page."""
    return render_template(
        'prod1.html',
        title='Solar Panel',
        year=datetime.datetime.now().year,
    )

#Product2 Route-
@app.route('/prod2')
def prod2():
    """Renders the product page."""
    return render_template(
        'prod2.html',
        title='Belts',
        year=datetime.datetime.now().year,
    )

#Product3 Route-
@app.route('/prod3')
def prod3():
    """Renders the product page."""
    return render_template(
        'prod3.html',
        title='ToothBrushes',
        year=datetime.datetime.now().year,
    )
#Product4 Route-
@app.route('/prod4')
def prod4():
    """Renders the product page."""
    return render_template(
        'prod4.html',
        title='Rugs',
        year=datetime.datetime.now().year,
    )

#Product5 Route-
@app.route('/prod5')
def prod5():
    """Renders the product page."""
    return render_template(
        'prod5.html',
        title='Lights',
        year=datetime.datetime.now().year,
    )

#Product6 Route-
@app.route('/prod6')
def prod6():
    """Renders the product page."""
    return render_template(
        'prod6.html',
        title='Phone cases',
        year=datetime.datetime.now().year,
    )
    
### Application runner ###
if __name__ == '__main__':
    HOST = environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
    app.run(HOST, PORT,debug=True)