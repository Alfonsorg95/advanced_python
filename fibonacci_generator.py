from re import X
import time

def fibo_gen(maximum = None):
    n1 = 0
    n2 = 1
    counter = 0
    next_num = 0
    while not maximum or next_num < maximum:
        if counter == 0:
            counter += 1
            yield n1
        elif counter == 1:
            counter +=1
            yield n2
        else:
            aux = n1 + n2
            n1, n2 = n2, aux
            counter += 1
            next_num = n1 + n2
            yield aux


def run():
    maximum = input("Write the maximum number: ")

    if not maximum:
        fibonacci = fibo_gen()
    else:
        fibonacci = fibo_gen(int(maximum))
        
    for element in fibonacci:
        print(element)
        time.sleep(0.75)


if __name__ == '__main__':
    run()