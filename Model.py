# importing library
import pickle
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestRegressor

from sklearn.linear_model import LinearRegression, Lasso, Ridge
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

# data read
df = pd.read_csv("/home/yash/project/ineuron_internship_projects/ML-project-internship/Concrete_file_path/Preprocessing_Data.csv")

# Data preprocessing
# split dataset

X = df.iloc[:,:-1] # Features
y = df.iloc[:,-1] # Target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state=2)

sc = StandardScaler()

X_train  = sc.fit_transform(X_train)
X_test  = sc.fit_transform(X_test)

file_1 = 'Scaler.pkl'
pickle.dump(sc,open(file_1,'wb'))

# Model Building
lr = LinearRegression()
lasso = Lasso()
ridge = Ridge()
dtr = DecisionTreeRegressor()
rfr = RandomForestRegressor()

# Fitting models on Training data
lr.fit(X_train,y_train)
lasso.fit(X_train,y_train)
ridge.fit(X_train,y_train)
dtr.fit(X_train, y_train)
rfr.fit(X_train, y_train)

# Fitting models on Testing data
y_pred_lr = lr.predict(X_test)
y_pred_lasso = lasso.predict(X_test)
y_pred_ridge = ridge.predict(X_test)
y_pred_dtr = dtr.predict(X_test)
y_pred_rfr = rfr.predict(X_test)


print("Model\t\t\t\t RMSE \t\t MSE \t\t MAE \t\t R2")
print("""LinerRegression \t {:.2f} \t\t{:.2f} \t\t{:.2f} \t\t{:.2f}""".format(
    np.sqrt(mean_squared_error(y_test, y_pred_lr)),mean_squared_error(y_test, y_pred_lr),
    mean_absolute_error(y_test, y_pred_lr), r2_score(y_test,y_pred_lr)))

print("""LassoRegression \t {:.2f} \t\t{:.2f} \t\t{:.2f} \t\t{:.2f}""".format(
    np.sqrt(mean_squared_error(y_test,y_pred_lasso)),mean_squared_error(y_test, y_pred_lasso),
    mean_absolute_error(y_test,y_pred_lasso),r2_score(y_test,y_pred_lasso)))

print("""RidgeRegression \t {:.2f} \t\t{:.2f} \t\t{:.2f} \t\t{:.2f}""".format(
    np.sqrt(mean_squared_error(y_test,y_pred_ridge)),mean_squared_error(y_test,y_pred_ridge),
    mean_absolute_error(y_test,y_pred_ridge),r2_score(y_test,y_pred_ridge)))

print("""Decision Tree Regressor \t {:.2f} \t\t {:.2f} \t\t {:.2f} \t\t {:.2f}""".format(
    np.sqrt(mean_squared_error(y_test, y_pred_dtr)), mean_squared_error(y_test,y_pred_dtr),
    mean_absolute_error(y_test, y_pred_dtr), r2_score(y_test, y_pred_dtr)))

print("""Random Forest Regressor \t {:.2f} \t\t {:.2f} \t\t {:.2f} \t\t {:.2f}""".format(
    np.sqrt(mean_squared_error(y_test, y_pred_dtr)), mean_squared_error(y_test,y_pred_dtr),
    mean_absolute_error(y_test, y_pred_dtr), r2_score(y_test, y_pred_dtr)))



file_2 = 'Model.pkl'
pickle.dump(rfr,open(file_2,'wb'))

# Model Evaluation

# models = [lr, lasso, ridge, dtr, rfr]
# names = ["Linear Regression", "Lasso Regression", "Ridge Regression", "Decision Tree Regressor", "Random Forest Regressor"]

# rmse = []

# for model in models:
#     rmse.append(np.sqrt(mean_squared_error(y_test, model.predict(X_test))))

# x = np.arange(len(names))
# width = 0.3

# fig, ax = plt.subplots(figsize = (10,7))
# rects = ax.bar(x, rmse, width)
# ax.set_ylabel('RMSE')
# ax.set_xlabel('Models')
# ax.set_title('RMSE with Different Alogrithms')
# ax.set_xticks(x)
# ax.set_xticklabels(names, rotation = 45)
# fig.tight_layout()
# plt.show()

