"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/
This file creates your application.
"""

import os
from app import app, db
from flask import render_template, request, redirect, url_for, flash, abort
from app.forms import PropertyForm
from app.models import Property
from werkzeug.utils import secure_filename


###
# Routing for your application.
###

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')


@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html', name="Rory Young")


@app.route('/property', methods=['POST', 'GET'])
def property():
    form = PropertyForm()

    # Validate profile info on submit
    if request.method == 'POST':
    
        # Get image data and save to upload folder
        image = request.files['photo']
        filename = secure_filename(image.filename)
        image.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        
        # Get the rest of the profile data
        Title = form.title.data
        details = form.details.data
        spaces = form.spaces.data
        bathroom = form.bathroom.data
        cost = form.cost.data
        located = form.located.data
        prop_type = form.prop_type.data

        # Save data to database
        newProperty = Property(Title=Title, details=details, spaces=spaces, bathroom=bathroom, cost=cost, located=located, ppty=prop_type, photo=filename )
        db.session.add(newProperty)
        db.session.commit()
        
        properties = Property.query.all()
        flash('Succcessfully Added')
        return redirect(url_for('properties', properties=properties))

    return render_template('property.html', form = form)


# @app.route('/property/<propertyid>')
# def property(propertyid):
#     properties = Property.query.id(id=propertyid)



@app.route('/properties', methods=['POST', 'GET'])
def properties():
    properties = Property.query.all()
    return render_template('properties.html',properties=properties)


def get_uploaded_images():
    rootdir = os.getcwd()
    list = []
    for subdir, dirs, files in os.walk(rootdir + '/app/static/uploads/'):
        for file in files:
            list.append(file)
        return list


###
# The functions below should be applicable to all Flask apps.
###

# Display Flask WTF errors as Flash messages
def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
            ), 'danger')

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also tell the browser not to cache the rendered page. If we wanted
    to we could change max-age to 600 seconds which would be 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port="8080")
