"""Stateful classroom controller that suppresses repeated target commands."""


class ClassroomAgent:
    """Simulated controller; this code does not connect to HVAC hardware."""
    def __init__(self):
        self.previous_mode = None

    @staticmethod
    def choose_target(temp, occupied):
        # Occupancy has priority over temperature, as in the supplied example.
        if not occupied:
            return "ECO"
        if temp > 26:
            return "COOL"
        if temp < 20:
            return "WARM"
        return "IDLE"

    def act(self, temp, occupied):
        target = self.choose_target(temp, occupied)
        send_command = target != self.previous_mode
        previous = self.previous_mode
        # Remember the target whether or not a command was sent.
        self.previous_mode = target
        return previous, target, send_command
