
from collections import deque
numeros = input("")
stack = deque(map(int, numeros.split()))

print("", stack)

while stack:
    elemento = stack.pop()
    print(elemento * 2)