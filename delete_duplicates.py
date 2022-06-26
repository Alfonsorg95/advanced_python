def del_duplicates(random_list:list) -> list:
    return list(set(random_list))

def run():
    random_list = [8, 8 , 5, 6, 7, 6, 9]
    print(del_duplicates(random_list))

if __name__=='__main__':
    run()