# Fibonacci reeks veel gebruikt voor (recursie, groei simuleren, wiskundige, natuurkundige structuren)

def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

n = 10
resultaat = fibonacci(n)
print(resultaat)
