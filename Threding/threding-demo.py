import concurrent.futures
import threading
import time
from .decorators import RuntimePrinter


def do_something_with_print(seconds):
    print(f"Sleeping {seconds} second(s)...")
    time.sleep(seconds)
    print(f"Done Sleeping...{seconds}")


@RuntimePrinter
def manual_threding():
    """
    Manually creating the threds, then joining them all to the main thread
    So the main thread will wait for every thread to be completed
    """
    threads = []
    secs = [5, 4, 3, 2, 1]
    for sec in secs:
        t = threading.Thread(target=do_something_with_print, args=[sec])
        t.start()
        threads.append(t)

    for thread in threads:
        thread.join()


def do_something_with_return(seconds):
    print(f"Sleeping {seconds} second(s)...")
    time.sleep(seconds)
    return f"Done Sleeping...{seconds}"


@RuntimePrinter
def threading_pool_using_submit():
    with concurrent.futures.ThreadPoolExecutor() as executor:
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
def threading_pool_using_executer_map():
    with concurrent.futures.ThreadPoolExecutor() as executor:
        secs = [5, 4, 3, 2, 1]
        # Submits and gets the result of the future for every element in secs
        results = executor.map(do_something_with_return, secs)

        for result in results:
            print(result)


def main():
    # manual_threding()
    threading_pool_using_submit()
    # threading_pool_using_executer_map()


if __name__ == "__main__":
    main()
