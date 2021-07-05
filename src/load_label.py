import numpy as np


# col 4-sex, 7-age, 9-race, 11-face
def load_label(start, end, col):
    label = []
    data = np.loadtxt('../data/faceDR', dtype='str', delimiter=',')
    for i in range(3222 - 1223):
        datalist = data[i].split(' ')
        if (datalist[1] == str(start) and start <= end):
            if datalist[2] == '(_sex':
                label.append(datalist[col])
                start += 1

    for i in range(0, len(label)):
        if (col == 4):
            if (label[i] == 'male)'):
                label[i] = 1
            else:
                label[i] = 0
        elif (col == 7):
            if (label[i] == 'child)'):
                label[i] = 0
            elif (label[i] == 'teen)'):
                label[i] = 1
            elif (label[i] == 'adult)'):
                label[i] = 2
            else:
                label[i] = 3

        # TODO(huakang) Add race, face ... labels

    return label

######################################################
###                  For test                      ###
######################################################

# if __name__ == '__main__':
#     sex_label = load_label(1233, 1237, 4)
#     age_label = load_label(1233, 1237, 7)
#     print(sex_label)
#     print(age_label)
