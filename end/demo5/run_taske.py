from tasks import work1

if __name__ == '__main__':
    # work1()
    r1 = work1.delay()
    print("r1的执行结果为", r1.get(timeout=6))
    r2 = work1.delay()
    r3 = work1.delay()
    r4 = work1.delay()
    print("任务完成", r1, r2, r3, r4)
