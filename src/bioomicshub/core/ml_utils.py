
from __future__ import annotations
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn.ensemble import RandomForestClassifier

def train_rf_classifier(X: pd.DataFrame, y: pd.Series, test_size: float = 0.2, random_state: int = 42):
    X_tr, X_te, y_tr, y_te = train_test_split(X, y, test_size=test_size, random_state=random_state, stratify=y)
    clf = RandomForestClassifier(random_state=random_state, n_estimators=300)
    clf.fit(X_tr, y_tr)
    report = classification_report(y_te, clf.predict(X_te), output_dict=True)
    return clf, report
