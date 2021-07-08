## pattern_recognition_project

### It is pattern recognition class homework.

#### 1. Content

- Feature extraction from the original image
- Use PCA or LDA algorithms for dimensionality reduction
- Classification using KNN and SVM classification algorithms
- Get the accuracy and running time

#### 2. Project structure

- **config/**   Store configuration files, used to set all the parameters required by the program
- **data/**   Store data sets, including rawdata and processed data
- **preprocess/**   Store the code for preprocessing the data, mainly the ```.m ``` file
- **src/**   Store source code
- **test/**   Store unit test programs, such as ```pytest```
- **README.md**   Project description document

#### 3. Instructions

- Process the original image
    - Unzip ```data/rawdata/rawdata.zip``` to get the original picture
    [![ROirSx.png](https://z3.ax1x.com/2021/07/08/ROirSx.png)](https://imgtu.com/i/ROirSx)

    > [!NOTE]
    > **All original picture should be placed in ```data/rawdata/``` ,** 
    > **because the file path must be the same as the one marked in ```format.m``` !**

    [![RXVoHf.png](https://z3.ax1x.com/2021/07/08/RXVoHf.png)](https://imgtu.com/i/RXVoHf)

    - Run ```preprocess/format.m``` to get a picture in ```.jpg``` format
    [![ROFhbF.png](https://z3.ax1x.com/2021/07/08/ROFhbF.png)](https://imgtu.com/i/ROFhbF)

- Set parameters in ```config/config.yaml```, for example
    - Set gender classification and use ```LDA```dimensionality reduction algorithm
    [![ROkTeS.png](https://z3.ax1x.com/2021/07/08/ROkTeS.png)](https://imgtu.com/i/ROkTeS)

    - Set to use the ```SVM``` classification algorithm, and set the corresponding parameters
    [![ROkOWn.png](https://z3.ax1x.com/2021/07/08/ROkOWn.png)](https://imgtu.com/i/ROkOWn)

- Run ```main.py``` to get the result
[![ROkvQ0.png](https://z3.ax1x.com/2021/07/08/ROkvQ0.png)](https://imgtu.com/i/ROkvQ0)

#### 4. Improvement

This code has many shortcomings, you can improve the code, such as

- Add feature selection algorithms
- Add algorithms to optimize classifier parameters
- Add unit test program

#### 5. Development environment

- Win10
- IDE: PyCharm2020
- python version: python3.8