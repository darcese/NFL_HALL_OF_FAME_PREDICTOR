from joblib import load

pathForPreMadeModels = 'AlreadyTrainedModelFiles/'
clf = load(pathForPreMadeModels + 'QB' + '.joblib') 

print(clf.predict_proba([[15,0,14,2,0,0]])[0][1])