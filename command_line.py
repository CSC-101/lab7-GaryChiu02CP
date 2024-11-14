import sys

def arg_sum():
    tally = 0
    for i in sys.argv:
        temp = i
        print(i)
        try:
            tempint = float(i)
            tally += tempint
        except Exception as e:
            print("Cannot convert {} to float.".format(e))
    return tally

if __name__ == '__main__':
    print(sys.argv)
    print(arg_sum())