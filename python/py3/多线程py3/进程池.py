from multiprocessing import Pool
import os


def long_time_task(name):
    print('Run task %s (%s)...' % (name, os.getpid()))
    f = open('downlink.txt', "r")
    print(f.readline())
    # print('Run task %s (%s)...' % (name, os.getpid()))
    # start = time.time()
    # time.sleep(random.random() * 3)
    # # f = open("test.txt", "a+")
    # # f.write(str(os.getpid()) + "\n")
    # # print("%s写入完成" % self.arg)
    # end = time.time()
    # print('Task %s runs %0.2f seconds.' % (name, (end - start)))


if __name__=='__main__':

    print('Parent process %s.' % os.getpid())
    p = Pool(9)
    for i in range(2):
        p.apply_async(long_time_task, args=(i,))
    print('Waiting for all subprocesses done...')
    p.close()
    p.join()
    print('All subprocesses done.')