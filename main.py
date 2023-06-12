from shortest_path import shortest_path
import xmlrpc.client
import sys
import time
from pcf import common_signal
import threading
import logging
from colorama import init, Fore, Style

# 로깅 설정
init()
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logging.addLevelName(logging.INFO, f"{Fore.GREEN}{logging.getLevelName(logging.INFO)}{Style.RESET_ALL}")
logging.addLevelName(logging.WARNING, f"{Fore.RED}{logging.getLevelName(logging.INFO)}{Style.RESET_ALL}")

# RPC 설정
computer_ipadress = 'http://172.30.1.89:7942'
proxy = xmlrpc.client.ServerProxy(computer_ipadress)

def worker(stop_event):
    sleep_cnt = 0
    result_flag = False
    temp = []

    while True:
        time.sleep(1)
        results = proxy.remote_procedure_call()
        logging.info(f'shortest path : {results}')

        try:
            if results:
                stop_event.set()  # main thread stop
                shortest_path(results)  # shortest path function
                result_flag = True  # result in value check
                sleep_cnt = 0  # 갑자기 사라졌다 들어올 경우 처리
                temp = results
            elif result_flag is True and not results:  # results가 비어 있다면, 갑자기 사라진 경우 예외처리
                sleep_cnt += 1
                logging.info(f'Count : {sleep_cnt}')
                if sleep_cnt == 3:
                    stop_event.clear()
                    sleep_cnt = 0
                    result_flag = False
        except KeyboardInterrupt:
            logging.warning('Interrupted by worker')
            sys.exit(0)

class main_thread_with_exception(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name
        self.__suspend = False
        self.__exit = False

    def run(self):
        try:
            while True:
                while self.__suspend:
                    logging.info('main thread suspended')
                    time.sleep(0.5)
                logging.info('Common signal Mode')
                common_signal()

        except KeyboardInterrupt:
            logging.warning('Interrupted by main thread')
            sys.exit(0)  # 프로그램을 종료

    def mySuspend(self):
        self.__suspend = True

    def myResume(self):
        self.__suspend = False


# Main function
if __name__ == "__main__":
    stop_event = threading.Event()

    t1 = threading.Thread(target=worker, args=(stop_event,))
    t1.start()

    t2 = main_thread_with_exception('Thread 1')
    t2.start()

    suspend_flag = False

    try:
        while True:
            time.sleep(0.5)
            if stop_event.is_set():
                t2.mySuspend()
                suspend_flag = True
            if suspend_flag is True and not stop_event.is_set():
                t2.myResume()

    except KeyboardInterrupt:
        logging.warning('Interrupted by main')
        sys.exit(0)
