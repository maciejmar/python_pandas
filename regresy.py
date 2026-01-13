import numpy as np
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_auc_score, brier_score_loss, classification_report

# ---- Przykładowe dane (syntetyczne) ----
rng = np.random.default_rng(42)
n = 2000

df = pd.DataFrame({
    # "cechy charakteru" / socio-emotional (0..1)
    "conscientiousness": rng.beta(2, 2, n),
    "openness": rng.beta(2, 2, n),
    "self_control": rng.beta(2, 2, n),
    "curiosity": rng.beta(2, 2, n),

    # kontekst
    "ses_band": rng.choice(["low", "mid", "high"], size=n, p=[0.3, 0.5, 0.2]),

    # aktualna umiejętność matematyczna (np. wynik testu w szkole)
    "math_baseline_score": rng.normal(0, 1, n),
})

# Generujemy etykietę: "dorosły wynik matematyczny wysoki" (syntetycznie)
logit = (
    1.2 * df["math_baseline_score"]
    + 0.9 * df["conscientiousness"]
    + 0.4 * df["openness"]
    + 0.3 * df["self_control"]
    + 0.2 * df["curiosity"]
    + df["ses_band"].map({"low": -0.4, "mid": 0.0, "high": 0.3}).astype(float)
    - 0.2
)
p = 1 / (1 + np.exp(-logit))
y = rng.binomial(1, p, n)

X_train, X_test, y_train, y_test = train_test_split(
    df, y, test_size=0.25, random_state=0, stratify=y
)

num_cols = ["conscientiousness", "openness", "self_control", "curiosity", "math_baseline_score"]
cat_cols = ["ses_band"]

preprocess = ColumnTransformer(
    transformers=[
        ("num", Pipeline([
            ("imputer", SimpleImputer(strategy="median")),
            ("scaler", StandardScaler()),
        ]), num_cols),
        ("cat", Pipeline([
            ("imputer", SimpleImputer(strategy="most_frequent")),
            ("onehot", OneHotEncoder(handle_unknown="ignore")),
        ]), cat_cols),
    ],
)

model = Pipeline([
    ("prep", preprocess),
    ("clf", LogisticRegression(max_iter=2000))
])

model.fit(X_train, y_train)

proba = model.predict_proba(X_test)[:, 1]
pred = (proba >= 0.5).astype(int)

print("ROC-AUC:", roc_auc_score(y_test, proba))
print("Brier (kalibracja, im niżej tym lepiej):", brier_score_loss(y_test, proba))
print(classification_report(y_test, pred))

# Przykładowe "oszacowanie szansy" dla nowego profilu
child_profile = pd.DataFrame([{
    "conscientiousness": 0.8,
    "openness": 0.8,
    "self_control": 0.75,
    "curiosity": 0.85,
    "ses_band": "mid",
    "math_baseline_score": 0.9,
}])

print("P(y=1) dla profilu:", model.predict_proba(child_profile)[:, 1][0])
