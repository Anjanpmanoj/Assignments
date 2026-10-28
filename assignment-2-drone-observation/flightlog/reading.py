class Reading:
    """Represents a single sensor measurement."""

    def __init__(self, label, value, unit):
        self.label = label
        self.value = value
        self.unit = unit

    def describe(self):
        return "{} = {} {}".format(
            self.label, self.value, self.unit
        )