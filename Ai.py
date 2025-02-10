from sklearn.neighbors import KNeighborsClassifier
from PIL import Image
import os
import numpy as np

def load_dataset():
    kotak = []
    lingkaran = []
    segitiga = []
    garislurus = []

    dir_kotak = "dataset/kotak/"
    dir_lingkaran = "dataset/lingkaran/"
    dir_segitiga = "dataset/segitiga/"
    dir_garislurus = "dataset/garislurus/"

    for file in os.listdir(dir_kotak):
        img = Image.open(dir_kotak + file) 
        img = np.array(img)
        img = img.flatten()
        kotak.append(img)

    for file in os.listdir(dir_lingkaran):
        img = Image.open(dir_lingkaran + file) 
        img = np.array(img)
        img = img.flatten()
        lingkaran.append(img)

    for file in os.listdir(dir_segitiga):
        img = Image.open(dir_segitiga + file) 
        img = np.array(img)
        img = img.flatten()
        segitiga.append(img)

    for file in os.listdir(dir_garislurus):
        img = Image.open(dir_garislurus+ file) 
        img = np.array(img)
        img = img.flatten()
        garislurus.append(img)

    return kotak, lingkaran, segitiga, garislurus

def load_ai():
    model = KNeighborsClassifier(n_neighbors=5)
    print("[INFO]: Memuat Dataset")
    kotak, lingkaran, segitiga, garislurus = load_dataset()
    print("[INFO]: Memuat Model")
    y_kotak = np.zeros(len(kotak))
    y_lingkaran = np.ones(len(lingkaran))
    y_segitiga = np.ones(len(segitiga)) * 2
    y_garislurus = np.ones(len(garislurus)) * 3
    X = kotak + lingkaran + segitiga + garislurus
    y = np.concatenate([y_kotak, y_lingkaran, y_segitiga, y_garislurus])
    model.fit(X, y)
    return model