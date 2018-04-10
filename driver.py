from location import Location, manhattan_distance
from rider import Rider


class Driver:
    """A driver for a ride-sharing service.

    === Attributes ===
    @type id: str
        A unique identifier for the driver.
    @type location: Location
        The current location of the driver.
    @type is_idle: bool
        A property that is True if the driver is idle and False otherwise.
    """

    def __init__(self, identifier, location, speed):
        """Initialize a Driver.

        @type self: Driver
        @type identifier: str
        @type location: Location
        @type speed: int
        @rtype: None
        """
        self.id, self.location, self.speed = identifier, location, speed
        self.destination = None
        self.is_idle = True

    def __str__(self):
        """Return a string representation.

        @type self: Driver
        @rtype: str

        >>> d = Driver('Amaranth', Location(1, 1), 1)
        >>> str(d)
        'Amaranth'
        """
        return self.id

    def __eq__(self, other):
        """Return True if self equals other, and false otherwise.

        @type self: Driver
        @type other: Driver
        @rtype: bool

        >>> c = Driver('Amaranth', Location(1, 1), 1)
        >>> d = Driver('Amaranth', Location(1, 1), 1)
        >>> c == d
        True
        >>> e = Driver('Crocus', Location(3, 1), 1)
        >>> c == e
        False
        """
        return (type(self) == type(other) and
                (self.id, self.location, self.speed) ==
                (other.id, other.location, other.speed) and
                (self.destination, self.is_idle) ==
                (other.destination, other.is_idle))

    def get_travel_time(self, destination):
        """Return the time it will take to arrive at the destination,
        rounded to the nearest integer.

        @type self: Driver
        @type destination: Location
        @rtype: int

        >>> d = Driver('Amaranth', Location(1, 1), 1)
        >>> pt = Location(2, 2)
        >>> print(d.get_travel_time(pt))
        2
        """
        return round(manhattan_distance(self.location, destination) /
                     self.speed)

    def start_drive(self, location):
        """Start driving to the location and return the time the drive will take.

        @type self: Driver
        @type location: Location
        @rtype: int

        >>> d = Driver('Amaranth', Location(1, 1), 1)
        >>> pt = Location(2, 2)
        >>> print(d.get_travel_time(pt))
        2
        """
        self.destination = location
        self.is_idle = False
        return self.get_travel_time(location)

    def end_drive(self):
        """End the drive and arrive at the destination.

        Precondition: self.destination is not None.

        @type self: Driver
        @rtype: None
        """
        self.location = self.destination
        self.destination = None
        self.is_idle = True

    def start_ride(self, rider):
        """Start a ride and return the time the ride will take.

        @type self: Driver
        @type rider: Rider
        @rtype: int

        >>> d = Driver('Amaranth', Location(1, 1), 1)
        >>> r = Rider('Almond', Location(1, 1), Location(5, 5), 10)
        >>> print(d.start_ride(r))
        8
        """
        self.destination = rider.destination
        self.is_idle = False
        return self.get_travel_time(rider.destination)

    def end_ride(self):
        """End the current ride, and arrive at the rider's destination.

        Precondition: The driver has a rider.
        Precondition: self.destination is not None.

        @type self: Driver
        @rtype: None
        """
        self.is_idle = True
        self.location = self.destination
        self.destination = None
