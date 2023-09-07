from flask.views import MethodView
from wtforms import Form, StringField, SubmitField
from flask import Flask, render_template, request
from temperature import Temperature
from calorie import Calorie

# Instantiate the flask class
app = Flask(__name__)

class Homepage(MethodView):

    def get(self):
        return render_template('index.html')
    
class CaloriesFormPage(MethodView):

    def get(self):
        # Initialize the calories form 
        calories_form = CaloriesForm()
        return render_template('calories_form_page.html', caloriesform = calories_form)
    
    def post(self):
        
        # Initialize the calories form 
        caloriesform = CaloriesForm(request.form)

        # extract the data that user inputs
        user_weight = float(caloriesform.weight.data)
        user_height = float(caloriesform.height.data)
        user_age = float(caloriesform.age.data)

        user_city = caloriesform.city.data
        user_country = caloriesform.country.data        

        # initialize the Temperature object
        temperature = Temperature(country=user_country,city=user_city).get()              
        
        if temperature is None:
            # Display an error message if the temperature is None
            error_message = f"Could not get the temperature for {user_city}, {user_country}"
            return render_template('calories_form_page.html',
                                result=True,
                                caloriesform=caloriesform,
                                error_message=error_message)
        else:
            cal = Calorie(user_weight, user_height, user_age, temperature)
            calories = cal.calculate()

            return render_template('calories_form_page.html',                                
                                caloriesform=caloriesform,
                                calories = calories,
                                result=True)      


class CaloriesForm(Form):
    # to create the label and textbox, we need to use StringField class
    weight = StringField("Weight: ", default=72)
    height = StringField("Height: ", default=178)
    age = StringField("Age: ", default=33)
    city = StringField("City: ", default="Pleasanton")
    country = StringField("Country: ", default="USA")

    button = SubmitField("Calculate")

app.add_url_rule('/', view_func=Homepage.as_view('home_page'))
app.add_url_rule('/calories_form', view_func=CaloriesFormPage.as_view('calories_form_page'))

app.run(debug=True)