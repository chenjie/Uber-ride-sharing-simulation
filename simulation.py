from container import PriorityQueue
from dispatcher import Dispatcher
from event import Event, create_event_list
from monitor import Monitor
import os.path


class Simulation:
    """A simulation.

    This is the class which is responsible for setting up and running a
    simulation.

    The API is given to you: your main task is to implement the run
    method below according to its docstring.

    Of course, you may add whatever private attributes and methods you want.
    But because you should not change the interface, you may not add any public
    attributes or methods.

    This is the entry point into your program, and in particular is used for
    auto-testing purposes. This makes it ESSENTIAL that you do not change the
    interface in any way!
    """

    # === Private Attributes ===
    # @type _events: PriorityQueue[Event]
    #     A sequence of events arranged in priority determined by the event
    #     sorting order.
    # @type _dispatcher: Dispatcher
    #     The dispatcher associated with the simulation.

    def __init__(self):
        """Initialize a Simulation.

        @type self: Simulation
        @rtype: None
        """
        self._events = PriorityQueue()
        self._dispatcher = Dispatcher()
        self._monitor = Monitor()

    def run(self, initial_events):
        """Run the simulation on the list of events in <initial_events>.

        Return a dictionary containing statistics of the simulation,
        according to the specifications in the assignment handout.

        @type self: Simulation
        @type initial_events: list[Event]
            An initial list of events.
        @rtype: dict[str, object]
        """
        # Add all initial events to the event queue.
        for event in initial_events:
            self._events.add(event)

        # Until there are no more events, remove an event
        # from the event queue and do it. Add any returned
        # events to the event queue.
        while not self._events.is_empty():
            do_event = self._events.remove()
            print(do_event)
            re_event = do_event.do(self._dispatcher, self._monitor)
            if re_event is not None:
                for i in re_event:
                    self._events.add(i)

        return self._monitor.report()


if __name__ == "__main__":
    filename = input('Events file: ')
    while not os.path.exists(filename):
        print("File does not exist.")
        filename = input('Events file: ')
    events = create_event_list(filename)
    sim = Simulation()
    final_stats = sim.run(events)
    print(final_stats)
