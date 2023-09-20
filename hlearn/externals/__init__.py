""" 
'Exlib' sub-package is composed of best :term:`Machine Learning` libraries called for 
:mod:`~hlearn.models` prediction with common datasets. 
`scikit-learn <https://scikit-learn.org/>`__ and 
`gradient boosting machine <https://docs.h2o.ai/h2o/latest-stable/h2o-docs/data-science/gbm.html>`__ (GBM)
especially (XGBoost) are build as top module for general prediction purpose.

"""
from .sklearn import ( 
        BaseEstimator,
        TransformerMixin,
        ClassifierMixin, 
        clone, 
        KMeans, 
        make_column_transformer,
        make_column_selector , 
        ColumnTransformer,
        ShrunkCovariance, 
        LedoitWolf, 
        FactorAnalysis,
        PCA ,
        IncrementalPCA,
        KernelPCA, 
        DummyClassifier, 
        SelectKBest, 
        f_classif,
        SelectFromModel, 
        SimpleImputer,
        permutation_importance,
        LogisticRegression, 
        SGDClassifier,
        confusion_matrix,
        classification_report ,
        mean_squared_error, 
        f1_score,
        accuracy_score,
        precision_recall_curve, 
        precision_score,
        recall_score, 
        roc_auc_score, 
        roc_curve,
        silhouette_samples, 
        make_scorer,
        matthews_corrcoef, 
        train_test_split , 
        validation_curve, 
        StratifiedShuffleSplit , 
        RandomizedSearchCV,
        GridSearchCV, 
        learning_curve , 
        cross_val_score,
        cross_val_predict,
        KNeighborsClassifier,
        Pipeline, 
        make_pipeline ,
        FeatureUnion, 
        _name_estimators,
        OneHotEncoder,
        PolynomialFeatures, 
        RobustScaler ,
        OrdinalEncoder, 
        StandardScaler,
        MinMaxScaler, 
        LabelBinarizer,
        Normalizer,
        LabelEncoder,
        SVC, 
        LinearSVC, 
        LinearSVR, 
        DecisionTreeClassifier,
        RandomForestClassifier,
        AdaBoostClassifier, 
        VotingClassifier, 
        BaggingClassifier,
        StackingClassifier , 
        ExtraTreesClassifier, 
        skl_ensemble_, 
        sklearndoc, 
        _HAS_ENSEMBLE_
        )

from .gbm import ( 
    xgboost, 
    xgboostdoc, 
    XGBClassifier 
    )

__all__=[
    "BaseEstimator",
    "TransformerMixin",
    "ClassifierMixin", 
    "clone", 
    "KMeans", 
    "make_column_transformer",
    'make_column_selector' , 
    'ColumnTransformer',
    'ShrunkCovariance', 
    'LedoitWolf', 
    'FactorAnalysis',
    'PCA' ,
    'IncrementalPCA',
    'KernelPCA', 
    'DummyClassifier', 
    'SelectKBest', 
    'f_classif',
    'SelectFromModel', 
    'SimpleImputer',
    'permutation_importance',
    'LogisticRegression', 
    'SGDClassifier',
    'confusion_matrix',
    'classification_report' ,
    'mean_squared_error', 
    'f1_score',
    'accuracy_score',
    'precision_recall_curve', 
    'precision_score',
    'recall_score', 
    'roc_auc_score', 
    'roc_curve',
    'silhouette_samples', 
    'make_scorer',
    'matthews_corrcoef', 
    'train_test_split' , 
    'validation_curve', 
    'StratifiedShuffleSplit' , 
    'RandomizedSearchCV',
    'GridSearchCV', 
    'learning_curve' , 
    'cross_val_score',
    'cross_val_predict',
    'KNeighborsClassifier',
    'Pipeline', 
    'make_pipeline' ,
    'FeatureUnion', 
    '_name_estimators',
    'OneHotEncoder',
    'PolynomialFeatures', 
    'RobustScaler' ,
    'OrdinalEncoder', 
    'StandardScaler',
    'MinMaxScaler', 
    'LabelBinarizer',
    'Normalizer',
    'LabelEncoder',
    'SVC', 
    'LinearSVC', 
    'LinearSVR', 
    'DecisionTreeClassifier',
    'RandomForestClassifier',
    'AdaBoostClassifier', 
    'VotingClassifier', 
    'BaggingClassifier',
    'StackingClassifier' , 
    'ExtraTreesClassifier', 
    'skl_ensemble_', 
    'sklearndoc', 
    '_HAS_ENSEMBLE_',
    'xgboost', 
    'xgboostdoc', 
    'XGBClassifier'
    ]