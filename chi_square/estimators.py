from scipy.stats import t as t 
from scipy.stats import chi2 as chi
import numpy as np 
import pandas as pd 


class Estimate:

    n : int 
    x_bar: float
    S : float 
    sample: np.array
    confidence: float
    df : int  
    myu: list
    var: list 
    

    def __init__(self, sample=[], x_bar=0, S=1, n=30, confidence=0.95):
        if confidence >= 1 or confidence < 0:
            raise ValueError("Value of confidence should be between 0 and 1")
        else: self.confidence = confidence 
        self.sample = sample 
        self.myu = []
        self.var = []
        if len(sample) !=0:
            self.x_bar = np.mean(sample)
            self.S = np.std(sample)
            self.n = len(sample)
        else:
            self.x_bar = x_bar
            self.S = S 
            self.n = n 

        self.df = self.n - 1

    def mean_estimate(self): 
        t_score = t.ppf(self.confidence + (1- self.confidence)/2, self.df)
        self.myu  = [self.x_bar - (t_score*self.S/np.sqrt(self.n)), self.x_bar + (self.S*t_score/np.sqrt(self.n))]
        return self.myu 

    def var_estimate(self): 
        chi_score1 = chi.isf((1 - self.confidence)/2, self.df)
        chi_score2 = chi.isf((self.confidence + (1 - self.confidence)/2), self.df)
        if chi_score1 > chi_score2:
            self.var = [self.df*(self.S/np.sqrt(self.n))**2/chi_score1, self.df*(self.S/np.sqrt(self.n))**2/chi_score2]
        else: self.var = [self.df*(self.S/np.sqrt(self.n))**2/chi_score2, self.df*(self.S/np.sqrt(self.n))**2/chi_score1]
        return self.var 

    def get_string(self):
        self.mean_estimate()
        self.var_estimate()
        estimates = f"\nPopulation mean estimate       : {self.myu}\nPopulation variance estimate   : {self.var}\nPopulation std estimate        : {np.sqrt(self.var)}\nConfidence                     : {self.confidence*100} percent"
        return estimates

    def __repr__(self):
        self.mean_estimate()
        self.var_estimate()
        estimates = f"\nPopulation mean estimate       : {self.myu}\nPopulation variance estimate   : {self.var}\nPopulation std estimate        : {np.sqrt(self.var)}\nConfidence                     : {self.confidence*100} percent"
        return estimates 


        


        
        

    
            


        