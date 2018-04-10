"""
The rider module contains the Rider class. It also contains
constants that represent the status of the rider.

=== Constants ===
@type WAITING: str
    A constant used for the waiting rider status.
@type CANCELLED: str
    A constant used for the cancelled rider status.
@type SATISFIED: str
    A constant used for the satisfied rider status
"""
from location import Location

WAITING = "waiting"
CANCELLED = "cancelled"
SATISFIED = "satisfied"


class Rider:
    """A rider for a ride-sharing service.

    === Attributes ===
    @param str id: A unique identifier for the rider.
    @param Location origin: The original location of the rider.
    @param Location destination: The destination of the rider.
    @param int patience: The number of minutes the rider will wait to be picked
                         up before they cancel their ride.
    @param str status: One of waiting to be picked up, cancelled, or satisfied
                       (after they have been picked up)
    """
    def __init__(self, identifier, origin, destination, patience):
        """Initialize a Rider.

        @param Rider self: This Rider
        @param str identifier: A unique identifier for the rider.
        @param Location origin: The original location of the rider.
        @param Location destination: The destination of the rider.
        @param int patience: The number of minutes the rider will wait to be
                             picked up before they cancel their ride.
        @rtype: None
        """
        self.id = identifier
        self.origin = origin
        self.destination = destination
        self.patience = patience
        self.status = None

    def __str__(self):
        """Return a string representation.

        @param Rider self: This Rider
        @rtype: str

        >>> r = Rider('Almond', Location(1, 1), Location(5, 5), 10)
        >>> str(r)
        'Almond'
        """
        return self.id
