import random

#uses random to pick one driver from an array of available drivers, returns the driverid picked
def allocateDriver(driver_arr):
    pickone=random.randint(-1, len(driver_arr)-1)
    return driver_arr[pickone]