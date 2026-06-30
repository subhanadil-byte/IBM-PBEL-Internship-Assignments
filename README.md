# IBM-PBEL-Internship-Assignments

This repository contains all my python and text-processing assignments completed during the IBM PBEL Internship program.

## Repository Structure

* **pbel_python_assignment_1.py, 2.py, 3.py** - Core local python automation scripts.
* **staff_records.csv / .xlsx** - Datasets required to run the core python scripts.
* **Assignment-4-NLP/** - Specialized folder containing natural language processing tools (Bag of Words, N-Grams, TF-IDF, and Word Embeddings).
* **Assignment-5-Activation-Functions/** - Python implementation of fundamental neural network activation functions.

---

## Tools & Libraries Used
* Python 3
* Scikit-Learn (CountVectorizer, TfidfVectorizer)
* Gensim (Word2Vec)
* Pandas
* Math Library (for Activation Functions)

---

## Deep Dive: Assignment 5 (Activation Functions)
Inside the `Assignment-5-Activation-Functions/` folder, I have written beginner-friendly Python code for four essential neural network activation functions:

1. **Sigmoid**: Squashes input values between 0 and 1 using the formula $\sigma(x) = \frac{1}{1 + e^{-x}}$.
2. **ReLU (Rectified Linear Unit)**: Returns 0 if the input is negative, and returns the number itself if positive.
3. **Tanh (Hyperbolic Tangent)**: Squashes input values between -1 and 1.
4. **Softmax**: Takes a list of scores and converts them into probabilities that sum up to exactly 1.0.
