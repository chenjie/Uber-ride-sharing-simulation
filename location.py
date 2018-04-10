class Location:
    """The location which describes an object on a grid.

    === Attributes ===
    @type row: int
        The number of blocks the location is from the bottom of the grid.
    @type column: int
        The number of blocks the location is from the left edge of the grid.
    """
    def __init__(self, row, column):
        """Initialize a location.

        @type self: Location
        @type row: int
        @type column: int
        @rtype: None
        """
        self.row, self.column = int(row), int(column)

    def __str__(self):
        """Return a string representation.

        @rtype: str

        >>> pt = Location(1,2)
        >>> str(pt)
        '(1, 2)'
        """
        return '({}, {})'.format(self.row, self.column)

    def __eq__(self, other):
        """Return True if self equals other, and false otherwise.

        @rtype: bool

        >>> pt1 = Location(1,2)
        >>> pt2 = Location(1,2)
        >>> pt1 == pt2
        True
        >>> pt3 = Location(2,2)
        >>> pt1 == pt3
        False
        """
        return (type(self) == type(other) and
                (self.row, self.column) == (other.row, other.column))


def manhattan_distance(origin, destination):
    """Return the Manhattan distance between the origin and the destination.

    @type origin: Location
    @type destination: Location
    @rtype: int

    >>> pt1 = Location(1,2)
    >>> pt2 = Location(3,4)
    >>> print(manhattan_distance(pt1, pt2))
    4
    """
    return (abs(origin.row - destination.row) +
            abs(origin.column - destination.column))


def deserialize_location(location_str):
    """Deserialize a location.

    @type location_str: str
        A location in the format 'row,col'
    @rtype: Location

    >>> location_str = '1,2'
    >>> str(deserialize_location(location_str))
    '(1, 2)'
    """
    location_list = location_str.split(',')
    return Location(int(location_list[0]), int(location_list[1]))
