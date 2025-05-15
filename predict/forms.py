# predict/forms.py
from django import forms

class HeartDiseaseForm(forms.Form):
    age = forms.IntegerField(label='Age')
    sex = forms.ChoiceField(label='Sex', choices=[(1, 'Male'), (0, 'Female')])
    cp = forms.ChoiceField(label='Chest Pain Type', choices=[(1, 'Typical Angina'), (2, 'Atypical Angina'), (3, 'Non-anginal Pain'), (4, 'Asymptomatic')])
    trestbps = forms.IntegerField(label='Resting Blood Pressure')
    chol = forms.IntegerField(label='Serum Cholestoral (mg/dl)')
    fbs = forms.ChoiceField(label='Fasting Blood Sugar > 120 mg/dl', choices=[(1, 'Yes'), (0, 'No')])
    restecg = forms.ChoiceField(label='Resting Electrocardiographic Results', choices=[(0, 'Normal'), (1, 'ST-T wave abnormality'), (2, 'Left ventricular hypertrophy')])
    thalach = forms.IntegerField(label='Maximum Heart Rate Achieved')
    exang = forms.ChoiceField(label='Exercise Induced Angina', choices=[(1, 'Yes'), (0, 'No')])
    oldpeak = forms.FloatField(label='Oldpeak (ST depression induced by exercise relative to rest)')
    slope = forms.ChoiceField(label='Slope of the Peak Exercise ST Segment', choices=[(0, 'Upsloping'), (1, 'Flat'), (2, 'Downsloping')])
    ca = forms.ChoiceField(label='Number of Major Vessels (0-3) Colored by Flourosopy', choices=[(0, '0'), (1, '1'), (2, '2'), (3, '3')])
    thal = forms.ChoiceField(label='Thal', choices=[(3, 'Normal'), (6, 'Fixed Defect'), (7, 'Reversable Defect')])