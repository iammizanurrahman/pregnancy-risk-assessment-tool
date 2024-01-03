from flask import Flask, render_template, request

app = Flask(__name__)

def calculate_pregnancy_risk(params):
    risk_score = 0

    # Age factor
    age = int(params['age'])
    if age < 18 or age > 35:
        risk_score += 2

    # Health conditions factor
    health_conditions = params.getlist('health_conditions')
    if "diabetes" in health_conditions:
        risk_score += 3
    if "hypertension" in health_conditions:
        risk_score += 2
    # Add more health condition factors

    # Lifestyle factors
    lifestyle_factors = params.getlist('lifestyle_factors')
    if "smoking" in lifestyle_factors:
        risk_score += 3
    if "excessive_alcohol" in lifestyle_factors:
        risk_score += 2
    # Add more lifestyle factor parameters

    # Medical history factors
    if params.get('previous_miscarriage'):
        risk_score += 2
    if params.get('previous_preterm_birth'):
        risk_score += 3
    # Add more medical history factors

    # Genetic factors
    if params.get('family_history_of_genetic_conditions'):
        risk_score += 2
    # Add more genetic factors

    # Additional parameters
    bmi = float(params.get('bmi', 0))
    if bmi < 18.5 or bmi > 24.9:
        risk_score += 2

    nutritional_status = params.get('nutritional_status', '')
    if nutritional_status.lower() == 'poor':
        risk_score += 2

    exercise_habits = params.get('exercise_habits', '')
    if exercise_habits.lower() == 'low':
        risk_score += 2

    psychological_health = params.get('psychological_health', '')
    if psychological_health.lower() == 'poor':
        risk_score += 2

    family_planning_history = params.get('family_planning_history', '')
    if family_planning_history.lower() == 'no':
        risk_score += 2

    infections_and_immunizations = params.get('infections_and_immunizations', '')
    if infections_and_immunizations.lower() == 'yes':
        risk_score += 2

    environmental_exposures = params.get('environmental_exposures', '')
    if environmental_exposures.lower() == 'yes':
        risk_score += 2

    blood_pressure = params.get('blood_pressure', '')
    if blood_pressure.lower() == 'high':
        risk_score += 2

    blood_sugar_levels = params.get('blood_sugar_levels', '')
    if blood_sugar_levels.lower() == 'elevated':
        risk_score += 2

    partner_health = params.get('partner_health', '')
    if partner_health.lower() == 'poor':
        risk_score += 2

    medication_and_supplement_usage = params.get('medication_and_supplement_usage', '')
    if medication_and_supplement_usage.lower() == 'yes':
        risk_score += 2

    number_of_previous_pregnancies = int(params.get('number_of_previous_pregnancies', 0))
    if number_of_previous_pregnancies > 2:
        risk_score += 2

    # Additional parameters
    dietary_habits = params.get('dietary_habits', '')
    if dietary_habits.lower() == 'poor':
        risk_score += 2

    allergies = params.get('allergies', '')
    if allergies.lower() == 'yes':
        risk_score += 2

    chronic_health_conditions = params.getlist('chronic_health_conditions')
    for condition in chronic_health_conditions:
        risk_score += 1
    # Add more chronic health conditions

    occupational_hazards = params.get('occupational_hazards', '')
    if occupational_hazards.lower() == 'yes':
        risk_score += 2

    social_support = params.get('social_support', '')
    if social_support.lower() == 'low':
        risk_score += 2

    routine_checkups = params.get('routine_checkups', '')
    if routine_checkups.lower() == 'irregular':
        risk_score += 2

    educational_background = params.get('educational_background', '')
    if educational_background.lower() == 'low':
        risk_score += 2

    substance_use = params.get('substance_use', '')
    if substance_use.lower() == 'yes':
        risk_score += 2

    financial_stability = params.get('financial_stability', '')
    if financial_stability.lower() == 'low':
        risk_score += 2

    sleep_patterns = params.get('sleep_patterns', '')
    if sleep_patterns.lower() == 'poor':
        risk_score += 2

    # Assess risk level
    if risk_score <= 3:
        return "Low risk"
    elif risk_score <= 6:
        return "Moderate risk"
    else:
        return "High risk"

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None

    if request.method == 'POST':
        params = request.form
        risk_level = calculate_pregnancy_risk(params)
        result = {'risk_level': risk_level, 'params': params}

    return render_template('index.html', result=result)

if __name__ == "__main__":
    app.run(debug=True)
