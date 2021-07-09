import yaml
from sklearn.neighbors import KNeighborsClassifier
from sklearn import svm
from sklearn.model_selection import cross_val_score
from load_label import load_label
import dim_reduction

with open('../config/config.yaml') as f:
    config = yaml.load(f, Loader=yaml.FullLoader)

    for i in config:
        if config.get(i) is None:
            print('------------------------------------------------')
            print('Note! Miss', i, 'parameter in config.yaml! Please get it!')
            exit(0)


#########################################################################
#     Load all data including training data, test data and labels       #
#########################################################################
def load_data():
    # load config params
    data_path = config.get('data_path')
    train_start = config.get('train_start')
    train_end = config.get('train_end')
    train_label_path = config.get('train_label_path')
    label = config.get('label')
    n_components = config.get('n_components')
    dim_reduction_algorithm = config.get('dim_reduction_algorithm')

    # train data
    data_train = dim_reduction.load_image(data_path, train_start, train_end)
    label_train = load_label(train_label_path, train_start, train_end, label)
    data_train_dim = dim_reduction.dim_reduction(data_train, n_components, dim_reduction_algorithm, label_train)
    # print(data_train_dim)
    # print(label_train)

    test_start = config.get('test_start')
    test_end = config.get('test_end')
    test_label_path = config.get('test_label_path')

    # test data
    data_test = dim_reduction.load_image(data_path, test_start, test_end)
    label_test = load_label(test_label_path, test_start, test_end, label)
    data_test_dim = dim_reduction.dim_reduction(data_test, n_components, dim_reduction_algorithm, label_test)
    # print(data_test_dim)
    # print(label_test)

    # Note! data_xx_dim is a return value in dim_reduction
    return data_train_dim, data_test_dim, label_train, label_test


#########################################################################
#                             Classifier                                #
#########################################################################
def classifier(data_train_dim, data_test_dim, label_train, label_test):
    predictedLabel = score = cross_value_score = 0.
    classifier_algorithm = config.get('classifier_algorithm')

    if classifier_algorithm == 'knn':
        knn = KNeighborsClassifier(n_neighbors=config.get('n_neighbors'))
        knn.fit(data_train_dim, label_train)
        predictedLabel = knn.predict(data_test_dim)
        # print(predictedLabel)
        # print(label_test)
        score = knn.score(data_test_dim, label_test)
        # print(score)
        # K-fold cross-validation
        cross_value_score = cross_val_score(knn, data_test_dim, label_test, cv=config.get('cv'))

    elif classifier_algorithm == 'svm':
        C = config.get('C')
        kernel = config.get('kernel')
        gamma = config.get('gamma')
        decision_function_shape = config.get('decision_function_shape')

        svm_obj = svm.SVC(C=C, kernel=kernel, gamma=gamma, decision_function_shape=decision_function_shape)
        svm_obj.fit(data_train_dim, label_train)
        predictedLabel = svm_obj.predict(data_test_dim)
        # print(predictedLabel)
        # print(label_test)
        score = svm_obj.score(data_test_dim, label_test)
        # print(score)
        # K-fold cross-validation
        cross_value_score = cross_val_score(svm_obj, data_test_dim, label_test, cv=config.get('cv'))

    # TODO(huakang) Add other classifier algorithms

    f.close()

    return predictedLabel, score, cross_value_score


######################################################
#                      For test                      #
######################################################
# if __name__ == '__main__':
#     data_train_dim, data_test_dim, label_train, label_test = classifier.load_data()
#     predictedLabel, score = classifier.classifier(data_train_dim, data_test_dim, label_train, label_test)
#     print('--- Accuracy is ', score, ' ----')
