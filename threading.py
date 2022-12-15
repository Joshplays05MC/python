import requests
import threading

class main():
    def __init__(self):
        self.url = "https://api.minehut.com/server/%s?byName=true"
        self.worldList = []
        self.freeServerNames = []
        self.threadLock = threading.Lock()
        self.shutdown = False

    def runManual(self):
        while True:
            server = input("\n-----\nServer Name\n>> ")
            if self.nameIsTooLong(server):
                print("\nServer name is too long.")
                continue
            elif self.nameIsTooShort(server):
                print("\nServer name is too short.")
                continue
            if self.serverExists(server):
                print(f'\n"{server}" exists.')
            else:
                print(f'\n"{server}" does not exist.')

    def runAutomatic(self):
        threadCount = int(input("Thread count: "))
        with open("dict.txt", "r") as dict:
            self.wordList = dict.read().splitlines()
        for i in range(threadCount):
            print("Thread %s started." % str(i + 1))
            thread = threading.Thread(target=self.checkListNameThread)
            thread.start()
        while True:
            if len(self.wordList) == 0:
                # print("\n-----\nDone.\n-----\n")
                # print("Free server names:")
                # for server in self.freeServerNames:
                #     print(f'  - {server}')
                stringBuilder = ""
                stringBuilder = stringBuilder + "\n-----\nDone.\n-----\n"
                stringBuilder = stringBuilder + "Free server names:\n"
                for server in self.freeServerNames:
                    stringBuilder = stringBuilder + f'  - {server}\n'
                with self.threadLock:
                    print(stringBuilder)
                break

    def checkListNameThread(self):
        while True:
            try:
                if self.shutdown:
                    break
                server = self.wordList.pop()
                if not self.nameIsTooLong(server) and not self.nameIsTooShort(server):
                    spacingNeeded = 12 - len(server)
                    if self.serverExists(server):
                        with self.threadLock:
                            print(f'"{server}"{" " * spacingNeeded}exists.')
                    else:
                        with self.threadLock:
                            print(f'"{server}"{" " * spacingNeeded}does not exist.')
                        self.freeServerNames.append(server)
            except IndexError:
                break

    def nameIsTooLong(self, server):
        return len(server) > 12

    def nameIsTooShort(self, server):
        return len(server) < 4

    def getServer(self, server):
        return requests.get(self.url % server).json()

    def serverExists(self, server):
        try:
            return self.getServer(server)["server"] != None
        except:
            return False

    def getServerInfo(self, server):
        return self.getServer(server)["server"]


if __name__ == "__main__":
    mainClass = main()
    try:
        while True:
            mode = input("Manual OR Auto\n>> ")
            if mode.lower() == "manual":
                mainClass.runManual()
            elif mode.lower() == "auto":
                mainClass.runAutomatic()
            else:
                print("\nMode does not exist.\n")
    except KeyboardInterrupt:
        print("\nExiting...")
        print('Shutting down threads...')
        mainClass.shutdown = True
        for thread in threading.enumerate():
            if thread.is_alive() and thread != threading.current_thread():
                thread.join()
        print('Threads shut down.')
        exit(0)
