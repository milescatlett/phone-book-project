import logging
import threading
import time

def thread_function(name):
    logging.info(f"Thread {name}: Starting")
    time.sleep(5)
    logging.info(f"Thread {name}: Ending")

if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")
    threads = []
    for t in range(10):
        logging.info("Main: Before creating thread")
        thread = threading.Thread(target=thread_function, args=(t,))
        threads.append(thread)
        thread.start()

    for index, thread in enumerate(threads):
        logging.info(f"Main: Before joining thread {index}")
        thread.join()
        logging.info(f"Main: thread {index} done")

    for t in threads:
        logging.info("Main: Before joining thread")
        thread.join()
        logging.info("Main: thread")


