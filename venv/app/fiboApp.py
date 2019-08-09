import sys
import os

currentPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(currentPath)[0]
print("currentPath: ", currentPath)
print("rootPath: ", rootPath)
sys.path.append(rootPath)
if __name__ == "__main__":
    import module.fibonacci.fibo as fibo

    fibo.fib(int(sys.argv[1]))
