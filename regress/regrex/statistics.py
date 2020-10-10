def score(model, x, y):
    r_sq = model.score(x, y)
    return r_sq
def intercept(model):
    return model.intercept_
def coef(model):
    return model.coef_