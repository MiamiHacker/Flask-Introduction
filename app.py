'''
SETUP: Virtual Environments

python3 -m venv venv

. venv/bin/activate

pip install Flask

python3 app.py 

Use any browser for: http://127.0.0.1:5000 
'''

from flask import Flask, render_template

app = Flask(__name__)

class GalileanMoons:
    def __init__(self, first, second, third, fourth):
        self.first = first,
        self.second = second,
        self.third = third,
        self.fourth = fourth


@app.route('/')
def index():
    return render_template(
        "jinja_intro.html", name="MiamiHacker", template_name = "Jinja2"
        )


@app.route("/expressions/")
def expressions():

    #interpolation
    color = "brown"
    animal_one = "fox"
    animal_two = "dog"
    
    #addition and subtractioen
    orange_amount = 10
    apple_amount = 20
    donate_amount = 15

    #string concatenation
    first_name = "Miami"
    last_name = "Hacker"

    kwargs = {
        "color": color,
        "animal_one": animal_one,
        "animal_two": animal_two,
        "orange_amount": orange_amount,
        "apple_amount": apple_amount,
        "donate_amount": donate_amount,
        "first_name": first_name,
        "last_name": last_name
    }

    return render_template(
        "expressions.html", **kwargs
    )


@app.route('/data_structures/')
def data_structures():

    movies = [
        "Lord of the Things", 
        "It's just me",
        "Iron Fist"
    ]

    car = {
        "brand": "Audi",
        "model": "R8",
        "year": "2022"
    }

    moons = GalileanMoons("Io", "Europa", "Ganymede", "Callisto")

    return render_template(
        "data_structures.html", movies=movies, car=car, moons=moons
        )


@app.route('/conditionals-basics/')
def render_conditionals():
    company = "Apple"
    return render_template("conditionals_basics.html", company=company)


@app.route('/for-loop/')
def render_for_loop():
    planets = [
        "Mercury",
        "Venus",
        "Earth", 
        "Mars",
        "Jupiter",
        "Saturn",
        "Uranus",
        "Neptune"
    ]
    return render_template("for-loop.html", planets=planets)


@app.route('/for-loop/conditionals/')
def render_for_loop_conditionals():
    user_os = {
        "MiamiHacker": "Kali",
        "Angela": "MacOs",
        "Bob": "Windows",
        "Britt": "Linux"
    }
    return render_template("loops_and_conditionals.html", user_os=user_os)


if __name__ == "__main__":
    app.run(debug=True)