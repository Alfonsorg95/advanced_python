def make_division_by(n):
    def division(number):
        assert type(number) == int,"You must use a integer"
        return number / n
    return division


def run():
    division_by_3 = make_division_by(3)
    print(division_by_3(18))


if __name__ == '__main__':
    run()