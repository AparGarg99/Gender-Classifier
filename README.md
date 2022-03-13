# OVERVIEW 📚
This project uses a Bidirectional LSTM network and numerous machine learning models such as Gaussian Naive Bayes, Random Forest, and KNN to classify a person's gender (M/F) based on his/her first name. The dataset consists of 95,025 first names and their corresponding gender.

Key Tools & Technologies Used - TensorFlow, Keras, scikit-learn, Flask, HTML, CSS

---

# DEMO 🎥
<kbd>
  <img src="https://github.com/AparGarg99/Gender-Classifier/blob/main/demo.gif">
</kbd>

---

# INSTALLATION AND USAGE 🔌
1. Open Anaconda command prompt
2. Create new anaconda environment
```
conda create -n "gc_project" python==3.7
```
3. Activate anaconda environment
```
conda activate "gc_project"
```
4. Open the project
```
git clone https://github.com/AparGarg99/Gender-Classifier.git
cd Gender-Classifier
```
5. Install the required dependencies
```
pip install -r requirements.txt
```
6. Create `models` directory
```
mkdir models
```
7. Launch Jupyter Notebook
```
jupyter notebook
```
8. Execute [`1_BiLSTM_Modeling.ipynb`](https://github.com/AparGarg99/Gender-Classifier/blob/main/1_BiLSTM_Modeling.ipynb) and [`3_ML_Modeling.ipynb`](https://github.com/AparGarg99/Gender-Classifier/blob/main/3_ML_Modeling.ipynb) notebooks to train and save models in `models` directory

9. Run flask web app
```
python app.py
```
10. Open a browser and type in the URL displayed. e.g. `http://127.0.0.1:5000/`
