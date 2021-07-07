import classifier

if __name__ == '__main__':
    data_train_dim, data_test_dim, label_train, label_test = classifier.load_data()
    predictedLabel, score = classifier.classifier(data_train_dim, data_test_dim, label_train, label_test)
    print('------------------------------------------------')
    print('--- Use', classifier.config.get('dim_reduction_algorithm'), 'and ', end='')
    print(classifier.config.get('classifier_algorithm'), 'algorithm. ---')
    print('--- Accuracy is ', score, ' ----')

