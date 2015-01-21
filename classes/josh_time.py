class Time(object):
    """
    This is the class for time
    """

    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds
        self.combo = self.hours + (self.minutes / 60.) + (self.seconds / 3600.)

    #
    # def __str__(self):
    #     hours_string = "Hours: " + str(self.hours) + "\n"
    #     minutes_string = "Minutes: " + str(self.minutes) + "\n"
    #     seconds_string = "Seconds: " + str(self.seconds) + "\n"
    #
    #     combo = hours_string + minutes_string + seconds_string
    #     return combo


    def __lt__(self, other):
        return self.combo < other.combo


    def __gt__(self, other):
        return self.combo > other.combo


    def __eq__(self, other):
        return self.combo == other.combo


    # def __del__(self):
    #     print "Hitting the __del__ method"


morning = Time(00, 45, 23)
afternoon = Time(14, 00, 00)

print(morning > afternoon)
print(morning < afternoon)
print(morning == afternoon)
print(morning.combo)
print(afternoon.combo)