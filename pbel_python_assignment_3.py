import numpy as np
import matplotlib.pyplot as plt
from scipy.special import factorial
from scipy.integrate import quad
import random

# Q1
arr = np.array([10, 20, 30, 40, 50])
ans = np.sum(arr)
print("Array:", arr)
print("Sum:", ans)

# Q2
arr2 = np.array([5, 10, 15, 20, 25])
avg = np.mean(arr2)
mx = np.max(arr2)
print("Array:", arr2)
print("Mean:", avg)
print("Max:", mx)

# Q3
x = [1, 2, 3, 4]
y = [10, 20, 30, 40]
plt.plot(x, y)
plt.title("Line Graph")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.show()

# Q4
names = ['Aman', 'Priya', 'Rahul', 'Sneha', 'Vikas']
marks = [85, 92, 78, 88, 95]
plt.bar(names, marks)
plt.title("Student Marks")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.show()

# Q5
ans_fact = factorial(5, exact=True)
print("Factorial of 5:", ans_fact)

# Q6
def fx(x):
    return x**2
ans_int, error = quad(fx, 0, 2)
print("Integration result:", ans_int)

# Q7
# Using numpy array to represent a tensor for compatibility
t = np.array([1, 2, 3, 4])
print("Tensor:", t)

# Q8
# Adding two arrays together like tensors
t1 = np.array([1, 2, 3])
t2 = np.array([4, 5, 6])
ans_t = t1 + t2
print("Result:", ans_t)

# Q9
words = [
    "apple", "banana", "cat", "dog", "elephant", 
    "frog", "goat", "house", "ice", "juice", 
    "kite", "lion", "monkey", "nest", "owl", 
    "pen", "queen", "rat", "sun", "tree"
]
my_words = random.sample(words, 5)
sentence = " ".join(my_words)
print("Sentence:", sentence)

# Q10
chars = ["A boy", "A girl", "A king", "A robot"]
places = ["in a forest", "at school", "in a city", "at home"]
acts = ["found a toy", "played a game", "read a book", "ate food"]
c = random.choice(chars)
p = random.choice(places)
a = random.choice(acts)
story = c + " " + p + " " + a + "."
print("Story:", story)