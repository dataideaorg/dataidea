"""
Functions for saving and loading machine learning models
"""
import joblib
from sklearn.metrics import (
    mean_squared_error, mean_absolute_error, r2_score, 
    accuracy_score, precision_score, recall_score, 
    f1_score)
import numpy as np

def load_model(filename='model.di'):
    """
    Load a machine learning model from a file.
    
    Parameters:
    -----------
    filename : str, default='model.di'
        The path to the file containing the model
        
    Returns:
    --------
    object
        The loaded model
        
    Raises:
    -------
    FileNotFoundError
        If the file does not exist
    """
    return joblib.load(filename)

def save_model(model, filename='model.di'):
    """
    Save a machine learning model to a file.
    
    Parameters:
    -----------
    model : object
        The model to be saved
    filename : str, default='model.di'
        The path to the file where the model will be saved
        
    Returns:
    --------
    str
        The path to the saved model file
    """
    joblib.dump(model, filename)
    return filename


def regression_report(y_true, y_pred, n_features=None):
    n = len(y_true)
    r2 = r2_score(y_true, y_pred)
    if n_features is not None:
        adjusted_r2 = 1 - ((1 - r2) * (n - 1) / (n - n_features - 1))
    else:
        adjusted_r2 = None
    report = {
        'MSE': mean_squared_error(y_true, y_pred),
        'RMSE': mean_squared_error(y_true, y_pred, squared=False),
        'MAE': mean_absolute_error(y_true, y_pred),
        'R2': r2,
        'Adjusted R2': adjusted_r2,
        'Correlation': np.corrcoef(y_true, y_pred)[0,1]
    }
    return report

def classification_report(y_true, y_pred):
    report = {
        'Accuracy': accuracy_score(y_true, y_pred),
        'Precision': precision_score(y_true, y_pred),
        'Recall': recall_score(y_true, y_pred),
        'F1 Score': f1_score(y_true, y_pred)
    }
    return report


__all__ = ['load_model', 'save_model', 'regression_report', 'classification_report'] 