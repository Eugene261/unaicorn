from django.shortcuts import render
from . import ml_predict

def home(request):
    return render(request, 'index.html')

def result(request):
    pclass = int(request.GET["pclass"])
    sex = request.GET["sex"]  # Keep as string
    age = float(request.GET["age"])  # Age might be a float
    sibsp = int(request.GET["sibsp"])
    parch = int(request.GET["parch"])
    fare = float(request.GET["fare"])  # Fare can be a float
    embarked = request.GET["embarked"]  # Keep as string
    title = request.GET["title"]  # Keep as string

    prediction = ml_predict.prediction_model(pclass, sex, age, sibsp, parch, fare, embarked, title)
    return render(request, 'result.html', {'prediction': prediction})  # Pass the first prediction result
