import multiprocessing
# define function
if __name__ == "__main__":
    processes = list()
    for i in range(5):
        p = multiprocessing.Process(name=<name>, target=<func>, args=(<arg1>, …)
        # to run in the background
        # p.daemon = True
        processes.append(p)
        p.start()
        p.join() # if daemon then no need to join