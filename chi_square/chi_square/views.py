from django.shortcuts import render
from django.http import HttpResponse
import numpy as np 

from estimators import Estimate

def post_data(request):
    datastorage = {"error":404}

    try:
        datastorage["mean"] = float(request.GET.get("mean"))
        datastorage["std"] = float(request.GET.get("stdev"))
        datastorage["count"] = float(request.GET.get("count"))
        datastorage["confidence"] = float(request.GET.get("confidence"))
    except Exception as e: 
        print(e)
        return render(request, "index.html", datastorage)

    estimator = Estimate(x_bar=datastorage["mean"], n=datastorage["count"], S=datastorage["std"], confidence=datastorage["confidence"])
    standard_deviations = [np.sqrt(X) for X in estimator.var_estimate()]
    variations = [X for X in estimator.var_estimate()]
    means = [X for X in estimator.mean_estimate()]

    datastorage =  { 
        "mean": f"The mean estimate: {means}",
        "var": f"The estimate for variance: {variations}", 
        "std": f"The standard deviation estimate: {standard_deviations}"
    }


    return render(request, "index.html", datastorage)

    
        


    



    

    
        
