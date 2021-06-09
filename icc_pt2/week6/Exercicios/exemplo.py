
def x(n):
    if n == 0:
        return n
    else:
        print(n)
        return x(n-1)
        
        
if __name__ == '__main__':
    teste = x(10)
