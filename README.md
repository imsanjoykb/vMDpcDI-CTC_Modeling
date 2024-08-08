## Validation of a Microfluidic Device Prototype for Cancer Detection and Identification: Circulating Tumor Cells Classification Based on Cell Trajectory Analysis Leveraging Cell-Based Modeling and Machine Learning
<hr>

![alt text](model_architecture/readme_banner.png "GRU Architecture")

[![Python](https://img.shields.io/badge/Python-3776AB.svg?logo=python&logoColor=white)](https://www.python.org/)
[![Numpy](https://img.shields.io/badge/Numpy-013243.svg?logo=numpy&logoColor=white)](https://numpy.org/)
[![Pandas](https://img.shields.io/badge/Pandas-150458.svg?logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![Matplotlib](https://img.shields.io/badge/Matplotlib-11557c.svg?logo=matplotlib&logoColor=white)](https://matplotlib.org/)
[![Seaborn](https://img.shields.io/badge/Seaborn-3776ab.svg?logo=python&logoColor=white)](https://seaborn.pydata.org/)
[![Scikit-learn](https://img.shields.io/badge/Scikit--learn-F7931E.svg?logo=scikit-learn&logoColor=white)](https://scikit-learn.org/)
[![TensorFlow](https://img.shields.io/badge/TensorFlow-FF6F00.svg?logo=tensorflow&logoColor=white)](https://www.tensorflow.org/)
[![Open Notebook](https://colab.research.google.com/assets/colab-badge.svg)](https://drive.google.com/file/d/147op9PkdE6MS007_jOWV5w5K7Ned2aQF/view?usp=sharing)
[![MIT](https://img.shields.io/badge/license-MIT-5eba00.svg)](https://github.com/imsanjoykb/Text-Generation/LICENCE.txt)
[![DOI](https://img.shields.io/badge/DOI-10.1000%2Fxyz123-blue)](https://doi.org/10.1000/xyz123)
[![GitHub stars](https://badgen.net/github/stars/imsanjoykb/vMDpcDI-CTC_Modeling)](https://github.com/imsanjoykb/vMDpcDI-CTC_Modeling/stargazers)

<hr>

## Abstract
>Microfluidic devices (MDs) offer an advanced approach for detecting circulating tumor cells (CTCs), improving detection through targeted methods and visual inspection. Despite these advancements, existing techniques often produce heterogeneous CTC populations, requiring further processing for thorough analysis and phenotype identification. This study investigates the use of a hyperuniform micropost MD for CTC classification. We integrate mathematical modeling of fluid-structure interactions within a simulated microfluidic channel with machine learning techniques to enhance classification accuracy.
<hr>

## Project Installation and Run

<b>Create the virtual environment</b>
```
pip install virtualenv
virtualenv venv 
venv\Scripts\activate  
```
<b>Install Dependencies</b>
```
pip3 install -r requirements.txt
```
<b>Run GRU Code/Notebook</b>
```
python gru_model.py
or,
GRU_Model.ipynb
```
<b>Run CNN Code/Notebook</b>
```
python cnn_model.py
or,
CNN_Model.ipynb
```
```
python main.py
```
<b>Run Final and Merge Model</b>
```
GRU-CNN_Final_Model.ipynb
```
<hr>

## GRU Architecture & Model
![alt text](model_architecture/GRU_Model_Arch.png "GRU Architecture")
```python
# Define the GRU model for classification
model = Sequential([
    Bidirectional(GRU(128, return_sequences=True), input_shape=(max_length, 6)),
    BatchNormalization(),
    Dropout(0.3),
    Bidirectional(GRU(64, return_sequences=True)),
    BatchNormalization(),
    Dropout(0.3),
    Bidirectional(GRU(32)),
    BatchNormalization(),
    Dropout(0.3),
    Dense(16, activation='relu'),
    Dense(2, activation='softmax')
])

# Compile the model with a different learning rate
model.compile(optimizer=tf.keras.optimizers.Adam(learning_rate=0.0005), loss='categorical_crossentropy', metrics=['accuracy'])

# Early stopping and learning rate reduction on plateau
early_stopping = EarlyStopping(monitor='val_loss', patience=10, restore_best_weights=True)
reduce_lr = ReduceLROnPlateau(monitor='val_loss', factor=0.2, patience=5, min_lr=0.00001)
```
## CNN Architecture & Model
![alt text](model_architecture/CNN_Arch.png "CNN Architecture")
```python
# Separate inputs for position and velocity
position_input = Input(shape=input_shape)
velocity_input = Input(shape=input_shape)

# Convolutions for position
x_pos = Conv1D(64, kernel_size=3, activation='relu')(position_input)
x_pos = MaxPooling1D(2)(x_pos)
 x_pos = Conv1D(64, kernel_size=3, activation='relu')(x_pos)
x_pos = GlobalAveragePooling1D()(x_pos)

# Convolutions for velocity
x_vel = Conv1D(64, kernel_size=3, activation='relu')(velocity_input)
x_vel = MaxPooling1D(2)(x_vel)
x_vel = Conv1D(64, kernel_size=3, activation='relu')(x_vel)
x_vel = GlobalAveragePooling1D()(x_vel)

# Combine features
combined = concatenate([x_pos, x_vel])

# Dense layers
x = Dense(128, activation='relu')(combined)
x = Dense(64, activation='relu')(x)
output = Dense(2, activation='softmax')(x)
```
<hr>

## Citing
```
@misc{vMDpcDI: CTC Modeling,
  author = {Rifat Rejuan1, Eugenio Aulisa1, Wei Li3‡, Travis Thompson1, Sanjoy Kumar, Suncica Canic, Yifan Wang1},
  title = {Validation of a Microfluidic Device Prototype for Cancer Detection and Identification: Circulating Tumor Cells Classification Based on Cell Trajectory Analysis Leveraging Cell-Based Modeling and Machine Learning},
  year = {2024},
  publisher = {Will be updated},
  journal = {Will be updated},
  url="Will be updated",
}
```
<hr>

###
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style)](http://makeapullrequest.com)
[![GitHub](https://badgen.net/badge/icon/github?icon=github&label)](https://github.com)
[![Visual Studio](https://badgen.net/badge/icon/visualstudio?icon=visualstudio&label)](https://visualstudio.microsoft.com)
[![Awesome Badges](https://img.shields.io/badge/badges-awesome-green.svg)](https://github.com/Naereen/badges)

<hr>


