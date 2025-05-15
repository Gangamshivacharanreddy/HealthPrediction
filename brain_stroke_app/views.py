from django.shortcuts import render
from .forms import BrainStrokeForm
from .model_loader import predict

def predict_brain_stroke(request):
    if request.method == 'POST':
        form = BrainStrokeForm(request.POST)
        if form.is_valid():
            data = [
                form.cleaned_data['gender'],
                form.cleaned_data['age'],
                form.cleaned_data['hypertension'],
                form.cleaned_data['heart_disease'],
                form.cleaned_data['ever_married'],
                form.cleaned_data['work_type'],
                form.cleaned_data['Residence_type'],
                form.cleaned_data['avg_glucose_level'],
                form.cleaned_data['bmi'],
                form.cleaned_data['smoking_status'],
            ]
            prediction = predict(data)
            result = "Stroke Positive" if prediction == 1 else "Stroke Negative" # Modify as needed.
            return render(request, 'brain_stroke_app/result.html', {'result': result})
    else:
        form = BrainStrokeForm()
    return render(request, 'brain_stroke_app/predict.html', {'form': form})
