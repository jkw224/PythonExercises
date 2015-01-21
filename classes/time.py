class Time:
    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def __lt__(self, other):
        return (self.hours, self.minutes, self.seconds) < (other.hours, other.minutes, other.seconds)

    def __gt__(self, other):
        return (self.hours, self.minutes, self.seconds) > (other.hours, other.minutes, other.seconds)

    def __eq__(self, other):
        return (self.hours, self.minutes, self.seconds) == (other.hours, other.minutes, other.seconds)

    def __str__(self):
        current_time = str(self.hours) + str(self.minutes) + str(self.seconds)
        return current_time

morning = Time(6, 30, 10)
afternoon = Time(13, 00, 00)

print(morning)
print(morning < afternoon)
print(morning.__lt__(afternoon))
print(afternoon < morning)