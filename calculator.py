# 기본 계산기
def add(a, b):
  return a+b
def subtract(a, b):
  return a-b
def multyply(a, b):
  return a*b
def divide_new(a, b):
    return a/b
def getMedian(a, b):
    return (a+b)/2
def getSum_ver1(n):
    return n(n+1)/2

def factorial(n):
    num = 1
    while n >= 1:
        num = num * n
        n = n - 1
    return num