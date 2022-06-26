from grp import struct_group


def make_repeater_of(n):
    def repeater(string):
        assert type(string) == str, "You can only use strings"
        return string * n
    return repeater


def run():
    repeat_5 = make_repeater_of(5)
    print(repeat_5("closure"))


if __name__ == '__main__':
    run()