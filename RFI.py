import pandas as pd
import numpy as np
import warnings
from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

warnings.filterwarnings('ignore')

class RFI:
    def seleccion_modelo_regresion(df):

        X = df.drop('target', axis=1)
        y = df['target']

        X_train, _, y_train, _ = train_test_split(X, y, test_size=0.2, random_state=1)
        rf = RandomForestRegressor().fit(X_train, y_train)
        imp = rf.feature_importances_
        importances = pd.DataFrame({'feature': X_train.columns, 'importance': np.round(imp, 3)}).sort_values('importance', ascending=False)
        percentil_75 = importances['importance'].quantile(0.75)
        columnas_buenas = importances[importances["importance"] >= percentil_75]["feature"].values
        df = pd.concat([df[columnas_buenas], df["target"]], axis=1)
        return df
    
    def seleccion_modelo_clasificacion(df):
        X = df.drop('target', axis=1)
        y = df['target']

        X_train, _, y_train, _ = train_test_split(X, y, test_size=0.2, random_state=1)
        rf = RandomForestClassifier().fit(X_train, y_train)
        imp = rf.feature_importances_
        importances = pd.DataFrame({'feature': X_train.columns, 'importance': np.round(imp, 3)}).sort_values('importance', ascending=False)
        percentil_75 = importances['importance'].quantile(0.75)
        columnas_buenas = importances[importances["importance"] >= percentil_75]["feature"].values
        df = pd.concat([df[columnas_buenas], df["target"]], axis=1)
        return df


# if __name__ == "__main__":
#     df = pd.read_csv("data.csv")
#     df = RFI.seleccion_modelo_regresion(df)
#     print(df.head())