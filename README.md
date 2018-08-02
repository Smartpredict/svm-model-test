# svm-model-test
Python 3.6.2
extract -> svm.rar
# Les fichiers : 
  - svm.pkl : 
          - de svm.rar  -> modèle entrainé avec les labels 0,1,2,3,4,5 (machine faible)
          - de svm full.rar -> modèle entrainé avec tous les labels 
  - svm_model.ipynb : jupyter notebook implémentation svm utilisant scikit-learn
  - FlaskServer.py : contient le server flask, utilise svm.pkl
  - client.py : permet d'envoyer une requète a prédire, entrée : image 28*28 (grayscale)
  - imageTest/test.tif : image 28 * 28 à modifier pour le tester
# Usage
  - exécuter FlaskServer.py
  - Modifier l'image test.tif
  - exécuter client.py
# Dépendances
  - flask (Flask, jsonify, request)
  - scikit-learn
  - numpy
  - pillow

