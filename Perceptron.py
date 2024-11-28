w1 = float(input("Enter the value of weight 1 : "))
w2 = float(input("Enter the value of weight 2 : "))
alpha = float(input("Enter the value of Learning Rate (0-1) : ")) 
error = 1 
threshold = 0.5  
bias = 0

x1 = [0, 0, 1, 1]
x2 = [0, 1, 0, 1]
t = [0, 0, 0, 1]  
output = [' ', ' ', ' ', ' '] 

print("Training.......")


while error != 0:
    error = 0  
    for i in range(len(x1)):
        a1 = x1[i]
        a2 = x2[i]
        gx = a1 * w1 + a2 * w2 + bias

        if gx > threshold:
            y = 1
        else:
            y = 0

        output[i] = y  
        local_error = t[i] - y 

        if local_error != 0:
            error = 1 
            w1 = w1 + alpha * local_error * a1
            w2 = w2 + alpha * local_error * a2
            bias = bias + alpha * local_error

print("\nTesting")
def test_perceptron(x1_input, x2_input):
    gx = x1_input * w1 + x2_input * w2 + bias
    if gx > threshold:
        return 1
    else:
        return 0

while True:
    x1_input = int(input("Enter the first input: "))
    x2_input = int(input("Enter the second input: "))
    print(f"Output is: {test_perceptron(x1_input, x2_input)}")

    cont = input("Want to do more? (y/n) ").strip().lower()
    if cont != 'y':
        break
