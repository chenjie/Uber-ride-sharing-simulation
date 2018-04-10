from driver import Driver
from rider import Rider
from location import Location, manhattan_distance


class Dispatcher:
    """A dispatcher fulfills requests from riders and drivers for a
    ride-sharing service.

    When a rider requests a driver, the dispatcher assigns a driver to the
    rider. If no driver is available, the rider is placed on a waiting
    list for the next available driver. A rider that has not yet been
    picked up by a driver may cancel their request.

    When a driver requests a rider, the dispatcher assigns a rider from
    the waiting list to the driver. If there is no rider on the waiting list
    the dispatcher does nothing. Once a driver requests a rider, the driver
    is registered with the dispatcher, and will be used to fulfill future
    rider requests.
    """

    def __init__(self):
        """Initialize a Dispatcher.

        @type self: Dispatcher
        @rtype: None
        """
        self.req_driver = []
        self.wait_rider = []

    def __str__(self):
        """Return a string representation.

        @type self: Dispatcher
        @rtype: str

        >>> a = Dispatcher()
        >>> a.req_driver.append(Driver('Amaranth', Location(1, 1), 1))
        >>> str(a)
        '1 drivers are available and 0 riders are waiting.'
        """
        return '{0} drivers are available and {1} riders are waiting.'.format(
            len(self.req_driver), len(self.wait_rider)
        )

    def request_driver(self, rider):
        """Return a driver for the rider, or None if no driver is available.

        Add the rider to the waiting list if there is no available driver.

        @type self: Dispatcher
        @type rider: Rider
        @rtype: Driver | None
        """
        if len(self.req_driver) == 0:
            self.wait_rider.append(rider)
            return None
        else:
            index = 0
            distance = manhattan_distance(self.req_driver[0].location,
                                          rider.origin)
            for num in range(1, len(self.req_driver)):
                m = manhattan_distance(self.req_driver[num].location,
                                       rider.origin)
                if m < distance:
                    distance = m
                    index = num
            return self.req_driver.pop(index)

    def request_rider(self, driver):
        """Return a rider for the driver, or None if no rider is available.

        If this is a new driver, register the driver for future rider requests.

        @type self: Dispatcher
        @type driver: Driver
        @rtype: Rider | None
        """
        if len(self.wait_rider) == 0:
            self.req_driver.append(driver)
            return None
        else:
            return self.wait_rider.pop(0)

    def cancel_ride(self, rider):
        """Cancel the ride for rider.

        @type self: Dispatcher
        @type rider: Rider
        @rtype: None
        """
        if rider in self.wait_rider:
            self.wait_rider.remove(rider)
        rider.status = "cancelled"
