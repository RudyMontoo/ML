import numpy as np
import pandas as pd

def gradient_descent(x, y, lr=0.01, epochs=3000):
    m, b = 0.0, 0.0
    # SCALE X AND Y USING MIN_MAX SCALER
    x_min, x_max = x.min(), x.max()
    y_min, y_max = y.min(), y.max()
    y_scaled = (y - y_min) / (y_max - y_min)
    x_scaled = (x - x_min) / (x_max - x_min)
    for epoch in range(epochs):
        y_pred = m * x_scaled + b
        error = y_scaled - y_pred
        cost = np.mean(error ** 2)
        dm = -2 * np.mean(x_scaled * error)
        db = -2 * np.mean(error)
        b = b - lr * db
        m = m - lr * dm
        if epoch % 100 == 0:
            print(f"Epoch {epoch}: m={m}, b={b}, cost={cost}")
    # Convert m and b back to original scale
    m_original = m * (y_max - y_min) / (x_max - x_min)
    b_original = b * (y_max - y_min) + y_min - m_original * x_min
    return m_original, b_original

if __name__ == "__main__":
    df = pd.read_csv("home_prices2.csv")
    x = df["area_sqr_ft"].values
    y = df["price_lakhs"].values
    m, b = gradient_descent(x, y)
    print(f"Final Results: m={m}, b={b}")