import pickle
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.pipeline import make_pipeline
from sklearn.datasets import fetch_openml
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, accuracy_score

X, y = fetch_openml(name="mnist_784", version=1, return_X_y=True, as_frame=False)

# Split training set into training and testing set
X_train, X_test, Y_train, Y_test = train_test_split(
        X, y, test_size=1/4.0, random_state=0
    )

def train(X_train, Y_train):
    # Learn the model
    pca = PCA(n_components=10)
    knn = KNeighborsClassifier(n_neighbors=3)
    model = make_pipeline(pca, knn)
    model.fit(X_train, Y_train)

    with open('model.obj', 'wb') as f:
        pickle.dump(model, f)


def test(X_test, Y_test):
    with open('model_pca.obj', 'rb') as f:
        model = pickle.load(f)
    
    Y_test_predictions = model.predict(X_test)

    # Evaluate model on the testing set
    print("Accuracy on testing set = ", accuracy_score(Y_test, Y_test_predictions))

    # Plot a confusion matrix
    cm = confusion_matrix(Y_test, Y_test_predictions, normalize='true')
    sns.heatmap(cm, annot=True)
    plt.title('Confusion matrix of the classifier')
    plt.xlabel('Predicted')
    plt.ylabel('True')
    plt.show()

    # plot_k_neighbors(model, [X_test[0]], 3)

def plot_k_neighbors(model, X, k):
    _, neighbors = model.kneighbors(X)
    plt.subplot(1,k+1,1)
    plt.imshow(X[0].reshape(28, 28))
    i = 2
    for n in neighbors[0]:
        plt.subplot(1,k+1,i)
        plt.imshow(X_train[n].reshape(28, 28))
        i += 1
    plt.show()

# train(X_train, Y_train)
test(X_test, Y_test)
