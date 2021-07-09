from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import cross_val_score
import matplotlib.pylab as plt
import classifier


#########################################################################
#       Use K-fold cross-validation to optimize model parameters        #
#########################################################################
def param_optimize_k_fold():
    data_train_dim, data_test_dim, label_train, label_test = classifier.load_data()
    clf_algorithm = classifier.config.get('classifier_algorithm')

    if clf_algorithm == 'knn':
        n = []
        score = []
        # K-fold cross-validation
        for n_neighbors in range(1, 50, 1):
            n.append(n_neighbors)
            knn = KNeighborsClassifier(n_neighbors=n_neighbors)
            sc = cross_val_score(knn, data_train_dim, label_train, scoring='accuracy', cv=5)
            score.append(sc.mean())
        plt.plot(n, score)
        plt.xlabel('K')
        plt.ylabel('Accuracy')
        plt.show()

    # TODO(huakang) Add SVM parameters optimization

    return


# TODO(huakang) Add other classifier algorithm parameters optimization


######################################################
#                      For test                      #
######################################################
# if __name__ == '__main__':
#     param_optimize_k_fold()
