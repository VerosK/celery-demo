import time

import sys

from demo.tasks import get_my_address

if __name__ == '__main__':
    # return address in sync program

    address_1 = get_my_address()
    print ("My address is {}".format(address_1))

    # Call imediately
    result = get_my_address.apply_async()
    print("Got AsyncResult {}".format(result.id))
    while not result.ready():
        sys.stderr.write('.')
        time.sleep(0.01)
    sys.stderr.write('\n')
    print(result.get())

    # Schedule call in 10 seconds from now
    result = get_my_address.apply_async(countdown=10)
    print("Got AsyncResult {}".format(result.id))
    while not result.ready():
        sys.stderr.write('.')
        time.sleep(1)
    sys.stderr.write('\n')
    print(result.get())
