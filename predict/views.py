# predict/views.py
from django.shortcuts import render
from .forms import HeartDiseaseForm
from .model_loader import predict

def predict_heart_disease(request):
    if request.method == 'POST':
        form = HeartDiseaseForm(request.POST)
        if form.is_valid():
            data = [
                form.cleaned_data['age'],
                int(form.cleaned_data['sex']),
                int(form.cleaned_data['cp']),
                form.cleaned_data['trestbps'],
                form.cleaned_data['chol'],
                int(form.cleaned_data['fbs']),
                int(form.cleaned_data['restecg']),
                form.cleaned_data['thalach'],
                int(form.cleaned_data['exang']),
                form.cleaned_data['oldpeak'],
                int(form.cleaned_data['slope']),
                int(form.cleaned_data['ca']),
                int(form.cleaned_data['thal']),
            ]
            prediction = predict(data)
            result = "Positive" if prediction == 1 else "Negative"
            return render(request, 'predict/result.html', {'result': result})
    else:
        form = HeartDiseaseForm()
    return render(request, 'predict/predict.html', {'form': form})