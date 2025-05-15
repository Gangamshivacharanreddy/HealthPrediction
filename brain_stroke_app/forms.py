from django import forms

class BrainStrokeForm(forms.Form):
    gender = forms.ChoiceField(label='Gender', choices=[(0, 'Male'), (1, 'Female'), (2, 'Other')])
    age = forms.FloatField(label='Age')
    hypertension = forms.ChoiceField(label='Hypertension', choices=[(0, 'No'), (1, 'Yes')])
    heart_disease = forms.ChoiceField(label='Heart Disease', choices=[(0, 'No'), (1, 'Yes')])
    ever_married = forms.ChoiceField(label='Ever Married', choices=[(0, 'No'), (1, 'Yes')])
    work_type = forms.ChoiceField(label='Work Type', choices=[(0, 'Govt_job'), (1, 'Never_worked'), (2, 'Private'), (3, 'Self-employed'), (4, 'children')])
    Residence_type = forms.ChoiceField(label='Residence Type', choices=[(0, 'Rural'), (1, 'Urban')])
    avg_glucose_level = forms.FloatField(label='Average Glucose Level')
    bmi = forms.FloatField(label='BMI')
    smoking_status = forms.ChoiceField(label='Smoking Status', choices=[(0, 'formerly smoked'), (1, 'never smoked'), (2, 'smokes'), (3, 'Unknown')])
