# IBM-PBEL-Internship-Assignments

This repository contains all my python and text-processing assignments completed during the IBM PBEL Internship program.

## 📂 Repository Structure

* **pbel_python_assignment_1.py, 2.py, 3.py** - Core local python automation scripts.
* **staff_records.csv / .xlsx** - Datasets required to run the core python scripts.
* **Assignment-4-NLP/** - Specialized folder containing natural language processing tools (Bag of Words, N-Grams, TF-IDF, and Word Embeddings).
* **Assignment-5-Neural-Networks/** - Comprehensive implementation of deep learning fundamentals divided into two distinct parts:
  * `pbel_assignment_5_part1.py`: A scratch implementation of a 2-Layer Neural Network utilizing backpropagation.
  * `pbel_assignment_5_part2.py`: A modular code evaluation comparing different non-linear activation functions.

---

## 🛠️ Tools & Libraries Used

* Python 3
* Scikit-Learn (CountVectorizer, TfidfVectorizer)
* Gensim (Word2Vec)
* Pandas
* Math Library (for manual activation calculations)

---

## 🧠 Deep Dive: Assignment 5 (Neural Networks & Activations)

Inside the `Assignment-5-Neural-Networks/` folder, the codebase explores foundational deep learning pillars through separate executable milestones:

### 1. 2-Layer Neural Network Architecture (Part 1)
Builds a basic network from scratch with a Hidden Layer and an Output Layer. It details:
* **Forward Propagation:** Matrix dot multiplication tracking weights and biases.
* **Backward Propagation:** Calculus chain-rule optimization updates to systematically decrease prediction error.

### 2. Activation Functions Comparison Analysis (Part 2)
An empirical evaluation measuring structural error minimization between core activation mechanics:
* **Sigmoid:** Squashes input values strictly between 0 and 1 using the formula $\sigma(x) = \frac{1}{1 + e^{-x}}$.
* **ReLU (Rectified Linear Unit):** Returns 0 if the input is negative, and the exact same input value if positive ($\max(0, x)$). Safely avoids the vanishing gradient problem.
* **Tanh (Hyperbolic Tangent):** Zero-centered alternative squashing input ranges between -1 and +1.
* **Softmax:** Multi-class classification function converting raw output logits into absolute probability metrics summing to exactly 1.0.s
