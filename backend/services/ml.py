from sklearn.linear_model import LinearRegression

def analyze_simulation_data(data):
    X = np.array(data['time']).reshape(-1, 1)
    y = np.array(data['frequency'])
    model = LinearRegression()
    model.fit(X, y)
    return model.coef_, model.intercept_
