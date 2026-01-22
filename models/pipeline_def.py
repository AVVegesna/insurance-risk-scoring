from sklearn.preprocessing import StandardScaler, OneHotEncoder, KBinsDiscretizer
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import AdaBoostClassifier

def get_pipeline():
    preprocessor = ColumnTransformer(
        transformers=[
            ("age_bucket", KBinsDiscretizer(n_bins=4, encode="onehot-dense", strategy="uniform"), ["age"]),
            ("num_scale", StandardScaler(), ["tenure", "claims_history"]),
            ("cat", OneHotEncoder(handle_unknown="ignore"), ["vehicle_type"])
        ]
    )

    base_estimator = DecisionTreeClassifier(max_depth=1)
    adaboost_clf = AdaBoostClassifier(estimator=base_estimator, n_estimators=10, learning_rate=1.0, random_state=42)

    pipeline = Pipeline(
        steps=[
            ("preprocessing", preprocessor),
            ("adaboost_classifier", adaboost_clf)
        ]
    )
    return pipeline