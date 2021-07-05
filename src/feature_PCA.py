import numpy as np
import cv2

IMAGE_SIZE = (875, 656)


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
    data_mat = np.zeros((1, image_size))
    for i in range((end - start + 1)):
        # TODO(huakang) Add judging the missing data
        image_num = 1233 + i
        image = path + str(image_num) + '.jpg'
        imgVector = img2vector(image)
        img_mat = np.reshape(imgVector, (1, image_size))
        data_mat = np.row_stack([data_mat, img_mat])

    return data_mat

# TODO(huakang) Add PCA to dimensionality reduction


######################################################
###                  For test                      ###
######################################################
if __name__ == '__main__':
    data_vec = img2vector('../data/jpg/1227.jpg')
    print(data_vec)
    data_mat = load_image('../data/jpg/', 1233, 1237)
    print(data_mat)
