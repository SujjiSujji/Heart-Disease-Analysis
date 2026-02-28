
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Tableau Public embed URLs
VISUALIZATIONS = [
    {
        "id": 1,
        "title": "Gender vs Heart Disease",
        "url": "https://public.tableau.com/views/HeartDisease_17721871709100/GendervsHeartdisease?:embed=y&:display_count=yes&:showVizHome=no"
    },
    {
        "id": 2,
        "title": "Age vs Heart Disease",
        "url": "https://public.tableau.com/views/HeartDisease_17721871709100/AgevsHeartdisease?:embed=y&:display_count=yes&:showVizHome=no"
    },
    {
        "id": 3,
        "title": "Diabetic vs Stroke",
        "url": "https://public.tableau.com/views/HeartDisease_17721871709100/DiabeticvsStroke?:embed=y&:display_count=yes&:showVizHome=no"
    },
    {
        "id": 4,
        "title": "Impact of Smoking and Alcohol",
        "url": "https://public.tableau.com/views/HeartDisease_17721871709100/ImpactofsmokingandalcoholonHeartdisease?:embed=y&:display_count=yes&:showVizHome=no"
    },
    {
        "id": 5,
        "title": "Other Heart Disease vs Stroke",
        "url": "https://public.tableau.com/views/HeartDisease_17721871709100/StrokevsOtherDisease?:embed=y&:display_count=yes&:showVizHome=no"
    },
    {
        "id": 6,
        "title": "Race wise Heart Disease",
        "url": "https://public.tableau.com/views/HeartDisease_17721871709100/RacewiseHeartDisease?:embed=y&:display_count=yes&:showVizHome=no"
    },
    {
        "id": 7,
        "title": "Physical Activity vs Heart Disease",
        "url": "https://public.tableau.com/views/HeartDisease_17721871709100/PhysicalActivityvsHeartDisease?:embed=y&:display_count=yes&:showVizHome=no"
    },
    {
        "id": 8,
        "title": "Age vs BMI vs Diabetic",
        "url": "https://public.tableau.com/views/HeartDisease_17721871709100/AgevsBMIvsDiabetic?:embed=y&:display_count=yes&:showVizHome=no"
    },
    {
        "id": 9,
        "title": "Stroke with Heart Disease & Diabetic",
        "url": "https://public.tableau.com/views/HeartDisease_17721871709100/PeopleGotStrokeFromDiabetesandHeartDisease?:embed=y&:display_count=yes&:showVizHome=no"
    },
    {
        "id": 10,
        "title": "Gender Analysis Overview",
        "url": "https://public.tableau.com/views/HeartDisease_17721871709100/GendervsHeartdisease?:embed=y&:display_count=yes&:showVizHome=no"
    }
]

DASHBOARDS = [
    {
        "id": 1,
        "title": "Heart Disease Analysis Dashboard 1",
        "url": "https://public.tableau.com/views/HeartDisease_17721871709100/Dashboard1?:embed=y&:display_count=yes&:showVizHome=no"
    }
]

STORY = {
    "title": "Heart Disease Story",
    "url": "https://public.tableau.com/views/HeartDisease_17721871709100/Story1?:embed=y&:display_count=yes&:showVizHome=no"
}


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/visualizations')
def visualizations():
    return render_template('visualizations.html', visualizations=VISUALIZATIONS)


@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html', dashboards=DASHBOARDS)


@app.route('/story')
def story():
    return render_template('story.html', story=STORY)


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/submit-contact', methods=['POST'])
def submit_contact():
    name = request.form.get('name')
    email = request.form.get('email')
    message = request.form.get('message')
    # In production, you would handle the form submission here
    return jsonify({'success': True, 'message': 'Thank you for your message!'})


if __name__ == '__main__':
    app.run(debug=True, port=5000)
