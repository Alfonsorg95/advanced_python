from datetime import datetime

def execution_time(func):
    def wrapper(*args, **kwargs): # *args and **kwargs, this function will work with or without parameters
        initial_time = datetime.now()
        func(*args, **kwargs)
        final_time = datetime.now()
        time_elapsed = final_time - initial_time
        print(str(time_elapsed.total_seconds()) + " seconds passed")
        if args or kwargs:
            return func(*args, **kwargs)
    return wrapper

@execution_time
def random_func():
    for _ in range(1,1000000):
        pass


@execution_time
def sum(a: int, b: int) -> int:
    return a + b
 
def run():
    random_func()
    print(sum(7, 4))


if __name__ == '__main__':
    run()