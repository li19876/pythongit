import time


def wapper(f):
    print('123')
    def inner(*args, **kwargs):
        start = time.time()
        res=f(*args, **kwargs)
        end = time.time()
        print("程序执行时间为:" + str(end - start))
        return res
    return inner


@wapper
def test(a):
    time.sleep(3)
    print(a)


# test('561464')
