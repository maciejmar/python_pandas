import numpy as np
import matplotlib.pyplot as plt

from sklearn.linear_model import LinearRegression, LogisticRegression


def plot_linear_regression():
    # --- Dane syntetyczne: y = a*x + b + szum ---
    rng = np.random.default_rng(7)
    n = 120

    x = rng.uniform(0, 10, n)
    true_a, true_b = 2.3, 5.0
    noise = rng.normal(0, 2.0, n)
    y = true_a * x + true_b + noise

    X = x.reshape(-1, 1)

    # --- Model ---
    lin = LinearRegression()
    lin.fit(X, y)

    a_hat = float(lin.coef_[0])
    b_hat = float(lin.intercept_)

    # --- Linia do wykresu ---
    x_line = np.linspace(x.min(), x.max(), 200).reshape(-1, 1)
    y_line = lin.predict(x_line)

    # --- Wykres ---
    plt.figure()
    plt.scatter(x, y, label="dane")
    plt.plot(x_line.ravel(), y_line, label="dopasowana prosta")
    plt.title(f"Regresja liniowa: ŷ = a·x + b,  a={a_hat:.3f}, b={b_hat:.3f}")
    plt.xlabel("x (cecha)")
    plt.ylabel("y (wartość)")
    plt.legend()


def plot_logistic_regression():
    # --- Dane syntetyczne: P(y=1|x) = sigmoid(w*x + b0) ---
    rng = np.random.default_rng(42)
    n = 160

    x = rng.uniform(-4, 4, n)
    true_w, true_b0 = 1.4, -0.3
    logit = true_w * x + true_b0
    p = 1 / (1 + np.exp(-logit))
    y = rng.binomial(1, p, n)  # obserwacje 0/1

    X = x.reshape(-1, 1)

    # --- Model ---
    clf = LogisticRegression()
    clf.fit(X, y)

    w_hat = float(clf.coef_[0][0])
    b0_hat = float(clf.intercept_[0])

    # --- Krzywa prawdopodobieństwa ---
    x_line = np.linspace(x.min(), x.max(), 400).reshape(-1, 1)
    p_line = clf.predict_proba(x_line)[:, 1]

    # --- Wykres ---
    # jitter tylko po to, żeby punkty 0/1 nie leżały idealnie na 0 i 1 (lepsza czytelność)
    jitter = rng.normal(0, 0.02, n)

    plt.figure()
    plt.scatter(x, y + jitter, label="obserwacje 0/1 (z jitterem)")
    plt.plot(x_line.ravel(), p_line, label="P(y=1|x)")
    plt.title(f"Regresja logistyczna: w={w_hat:.3f}, b0={b0_hat:.3f}")
    plt.xlabel("x (cecha)")
    plt.ylabel("P(y=1 | x)")
    plt.ylim(-0.1, 1.1)
    plt.legend()


if __name__ == "__main__":
    plot_linear_regression()
    plot_logistic_regression()
    plt.show()
