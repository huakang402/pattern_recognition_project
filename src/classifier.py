from load_label import load_label
import dim_reduction

from sklearn.neighbors import KNeighborsClassifier

# train data
data_train = dim_reduction.load_image('../data/jpg/', 1234, 1303)
label_train = load_label('../data/faceDR', 1234, 1303, 4)
data_train_lda = dim_reduction.dim_reduction(data_train, 1, 'lda', label_train)
print(data_train_lda)
print(label_train)

# test data
data_test = dim_reduction.load_image('../data/jpg/', 1304, 1333)
label_test = load_label('../data/faceDR', 1304, 1333, 4)
data_test_lda = dim_reduction.dim_reduction(data_test, 1, 'lda', label_test)
print(data_test_lda)
print(label_test)

# classifier
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(data_train_lda, label_train)
predictedLabel = knn.predict(data_test_lda)
print(predictedLabel)
print(label_test)
score = knn.score(data_test_lda, label_test)
print(score)