import numpy as np
from model import train_and_predict, get_accuracy

def test_predictions_not_none():
    preds, _ = train_and_predict()
    assert preds is not None, "Predictions should not be None."

def test_predictions_length():
    preds, y_test = train_and_predict()
    assert len(preds) > 0, "Predictions should not be empty."
    assert len(preds) == len(y_test), "Prediction length mismatch."

def test_predictions_value_range():
    preds, _ = train_and_predict()
    for p in preds:
        assert 0 <= p <= 2, f"Prediction out of expected range: {p}"

def test_model_accuracy():
    acc = get_accuracy()
    assert acc >= 0.7, f"Model accuracy is too low: {acc:.2f}"
