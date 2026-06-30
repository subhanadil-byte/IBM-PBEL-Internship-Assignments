import math

# 1. SIGMOID FUNCTION
def sigmoid(x):
    # Formula: 1 / (1 + e^-x)
    return 1 / (1 + math.exp(-x))


# 2. RELU FUNCTION
def relu(x):
    # Agar x chota hai 0 se toh 0 return karega, nahi toh x
    if x < 0:
        return 0
    else:
        return x


# 3. TANH FUNCTIO
def tanh(x):
    # Python ke math library ka built-in function
    return math.tanh(x)


# 4. SOFTMAX FUNCTION
def softmax(scores):
    # Step 1: Har score ke liye e^x nikalna
    exp_scores = [math.exp(x) for x in scores]
    
    # Step 2: Sabhi e^x values ko aapas mein plus (sum) karna
    sum_exp_scores = sum(exp_scores)
    
    # Step 3: Har e^x ko total sum se divide karna
    probabilities = [exp / sum_exp_scores for exp in exp_scores]
    return probabilities


# --- TESTING THE FUNCTIONS (Output check karne ke liye) ---
print("--- Activation Function Tests ---")
print("Sigmoid of 2: ", sigmoid(2))
print("ReLU of -5:   ", relu(-5))
print("ReLU of 3:    ", relu(3))
print("Tanh of 2:    ", tanh(2))

test_scores = [1.0, 2.0, 3.0]
print("Softmax of [1.0, 2.0, 3.0]:", softmax(test_scores))