import numpy as np
import cv2
from sklearn.decomposition import PCA
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis

# # import load_label for test
# from load_label import load_label

IMAGE_SIZE = (128, 128)


##################################################################
#                         Data process                           #
##################################################################
def img2vector(image):
    rows = IMAGE_SIZE[0]
    cols = IMAGE_SIZE[1]
    img = cv2.imread(image, 0)
    img = cv2.resize(img, (cols, rows))
    imgVector = np.zeros((1, rows * cols))
    imgVector = np.reshape(img, (1, rows * cols))
    return imgVector


def load_image(path, start, end):
    image_size = IMAGE_SIZE[0] * IMAGE_SIZE[1]
    image_mat = np.zeros((1, image_size))
    for i in range((end - start + 1)):
        # TODO(huakang) Add judging the missing data
        image_num = start + i
        image = path + str(image_num) + '.jpg'
        imgVector = img2vector(image)
        img_mat = np.reshape(imgVector, (1, image_size))
        image_mat = np.row_stack([image_mat, img_mat])

    # Remove image_mat first row which always be 0
    image_mat = np.delete(image_mat, 0, axis=0)

    return image_mat


##################################################################
#                 PCA Dimensionality reduction                   #
##################################################################
def pca(train, n_components, label=None):
    pca_obj = PCA(n_components)
    pca_obj.fit(train, y=None)
    train_pca = pca_obj.transform(train)

    return train_pca


##################################################################
#                 LDA Dimensionality reduction                   #
##################################################################
def lda(train, n_components, label):
    lda_obj = LinearDiscriminantAnalysis(n_components=n_components)
    lda_obj.fit(train, label)
    train_lda = lda_obj.transform(train)

    return train_lda


def dim_reduction(train, n_components, algorithm, label=None):
    if algorithm == 'pca':
        return pca(train, n_components)
    else:
        return lda(train, n_components, label)


######################################################
#                      For test                      #
######################################################
# if __name__ == '__main__':
#     # sex_label = load_label('../data/faceDR', 1233, 1237, 4)
#     sex_label = [1, 1, 3, 4, 4]
#
#     data_vec = img2vector('../data/jpg/1227.jpg')
#     print(data_vec)
#     print('########################################')
#     data_mat = load_image('../data/jpg/', 1233, 1237)
#     print(data_mat)
#     print('########################################')
#     data_mat_pca = dim_reduction(data_mat, 3, 'pca')
#     print(data_mat_pca)
#     print('########################################')
#     data_mat_lda = dim_reduction(data_mat, 2, 'lda', sex_label)
#     print(data_mat_lda)
#     # print(sex_label)
