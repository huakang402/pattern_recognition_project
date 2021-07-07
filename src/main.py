import classifier
import time

if __name__ == '__main__':
    start_time = time.time()
    data_train_dim, data_test_dim, label_train, label_test = classifier.load_data()
    predictedLabel, score = classifier.classifier(data_train_dim, data_test_dim, label_train, label_test)
    end_time = time.time()
    print('------------------------------------------------')
    print('--- Use', classifier.config.get('dim_reduction_algorithm'), 'and ', end='')
    print(classifier.config.get('classifier_algorithm'), 'algorithm. ---')
    print('--- Accuracy is ', score, ' ----')
    print('--- Run time is ', end_time - start_time, 's ----')

