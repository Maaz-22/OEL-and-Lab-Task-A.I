import math

alpha = 1  
w0 = [0.5, -0.4] 
w1 = [0.2, -0.1]  
w2 = [0.3, 0.1]   
v0 = 0.2 
v = [0.4, -0.3]  

x = [(0, 0), (0, 1), (1, 0), (1, 1)]
target = [0, 1, 1, 0]  
print('Training.......')

z = [0, 0] 
gradient = [0, 0]  
count = 0

while count < 50000:
    output = []
    for i in range(len(x)):
        a1, a2 = x[i]  
        t = target[i]  

    
        for j in range(len(z)):
            Zin = w0[j] + a1 * w1[j] + a2 * w2[j]
            z[j] = 1 / (1 + math.exp(-Zin)) 

        Yin = v0 + z[0] * v[0] + z[1] * v[1]
        y = 1 / (1 + math.exp(-Yin)) 
        output.append(y)

        error = (t - y) * y * (1 - y) 
        v0 = v0 + alpha * error  

        for j in range(len(z)):
            gradient[j] = z[j] * (1 - z[j]) * error * v[j]  
            v[j] = v[j] + alpha * error * z[j]  
            w1[j] = w1[j] + alpha * gradient[j] * a1 
            w2[j] = w2[j] + alpha * gradient[j] * a2
            w0[j] = w0[j] + alpha * gradient[j] 

    count += 1

print('Trained')

while True:
    print('Testing')
    x1 = int(input('Enter the first input: '))
    x2 = int(input('Enter the second input: '))

    for j in range(len(z)):
        Zin = w0[j] + x1 * w1[j] + x2 * w2[j]
        z[j] = 1 / (1 + math.exp(-Zin))

    Yin = v0 + z[0] * v[0] + z[1] * v[1]
    y = 1 / (1 + math.exp(-Yin))

    print('Output is: ', round(y)) 

  
    cont = input("Want to do more? (y/n): ").strip().lower()
    if cont != 'y':
        break  