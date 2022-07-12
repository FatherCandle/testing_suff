import multiprocessing
import concurrent.futures
import time
from typing import List
from decorators import RuntimePrinter


def do_something_with_print(seconds):
    print(f"Sleeping {seconds} second(s)...")
    time.sleep(seconds)
    print(f"Done Sleeping...{seconds}")


@RuntimePrinter
def manual_process():
    """
    Manually creating the threds, then joining them all to the main thread
    So the main thread will wait for every thread to be completed
    """
    processes = []
    secs = [5, 4, 3, 2, 1]
    for sec in secs:
        p = multiprocessing.Process(target=do_something_with_print, args=(sec,))
        p.start()
        processes.append(p)

    for process in processes:
        process.join()


def do_something_with_return(seconds):
    print(f"Sleeping {seconds} second(s)...")
    time.sleep(seconds)
    return f"Done Sleeping...{seconds}"


@RuntimePrinter
def process_pool_using_submit():
    with concurrent.futures.ProcessPoolExecutor() as executor:
        secs = [5, 4, 3, 2, 1]

        """
            Submits a callable to be executed with the given arguments.
            Schedules the callable to be executed as fn(*args, **kwargs)
            Returns: A Future representing the given call.
        """
        my_futures = [executor.submit(do_something_with_return, sec) for sec in secs]

        # # Getting the results at the order the futures were created
        # for f in my_futures:
        #     print(f.result())

        # Getting the results at the order the futures are completed
        for f in concurrent.futures.as_completed(my_futures):
            print(f.result())


@RuntimePrinter
def process_pool_using_executer_map():
    with concurrent.futures.ProcessPoolExecutor() as executor:
        secs = [5, 4, 3, 2, 1]
        results = executor.map(do_something_with_return, secs)

        for result in results:
            print(result)


def main():
    # manual_process()
    process_pool_using_submit()
    # process_pool_using_executer_map()


if __name__ == "__main__":
    main()
