import threading


DATA_LIST = [i for i in xrange(1000)]


class LoopThread(threading.Thread):
    def __init__(self, id):
        threading.Thread.__init__(self)
        self.id = id
        self.data_collect = list()

    def run(self):
        self.data_collect.append(self.id)

def write_list(list, data):
    list.append(data)

def decorator(list, data):
    return write_list(list, data)

if __name__ == "__main__":
    data = list()
    loaders = list()
    for i in DATA_LIST:
        loader = threading.Thread(target=decorator, args=(data, i))
        loader.setDaemon(True)
        loader.start()
        loaders.append(loader)
    #
    for loader in loaders:
        loader.join()

    print data