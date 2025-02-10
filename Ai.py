from sklearn.neighbors import KNeighborsClassifier
from PIL import Image
import os
import numpy as np

dir_k = "dataset/kotak/"
dir_l = "dataset/lingkaran/"
dir_s = "dataset/segitiga/"
dir_g = "dataset/garislurus/"

def load_dataset():
    kotak = []
    lingkaran = []
    segitiga = []
    garislurus = []

    for file in os.listdir(dir_k):
        img = Image.open(dir_k + file) 
        img = np.array(img)
        img = img.flatten()
        kotak.append(img)

    for file in os.listdir(dir_l):
        img = Image.open(dir_l + file) 
        img = np.array(img)
        img = img.flatten()
        lingkaran.append(img)

    for file in os.listdir(dir_s):
        img = Image.open(dir_s + file) 
        img = np.array(img)
        img = img.flatten()
        segitiga.append(img)

    for file in os.listdir(dir_g):
        img = Image.open(dir_g + file) 
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