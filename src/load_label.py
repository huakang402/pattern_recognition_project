import numpy as np


##################################################################
#               Load labels and return label list                #
##################################################################
# col 4-sex, 7-age, 9-race, 11-face
def load_label(path, start, end, col):
    label = []
    data = np.loadtxt(path, dtype='str', delimiter=',')
    for i in range(3222 - 1223):
        datalist = data[i].split(' ')
        if datalist[1] == str(start) and start <= end:
            if datalist[2] == '(_sex':
                label.append(datalist[col])
            start += 1

    for i in range(0, len(label)):
        if col == 4:
            if label[i] == 'male)':
                label[i] = 1
            else:
                label[i] = 0
        elif col == 7:
            if label[i] == 'child)':
                label[i] = 0
            elif label[i] == 'teen)':
                label[i] = 1
            elif label[i] == 'adult)':
                label[i] = 2
            else:
                label[i] = 3

        # TODO(huakang) Add race, face ... labels

    return label


##################################################################
#      Find all missing data number and return with a list       #
##################################################################
def missing_data():
    from classifier import config
    num = []
    data_dr = np.loadtxt(config.get('train_label_path'), dtype='str', delimiter=',')
    for i in range(3222 - 1223):
        datalist_dr = data_dr[i].split(' ')
        if datalist_dr[2] == '(_missing':
            num.append(int(datalist_dr[1]))

    data_ds = np.loadtxt(config.get('test_label_path'), dtype='str', delimiter=',')
    for i in range(5222 - 3223):
        datalist_ds = data_ds[i].split(' ')
        if datalist_ds[2] == '(_missing':
            num.append(int(datalist_ds[1]))

    return num


######################################################
#                      For test                      #
######################################################
# if __name__ == '__main__':
#     sex_label = load_label('../data/faceDR', 1233, 1237, 4)
#     age_label = load_label('../data/faceDR', 1233, 1237, 7)
#     print(sex_label)
#     print(age_label)
#     missing_data = missing_data()
#     print(missing_data)
