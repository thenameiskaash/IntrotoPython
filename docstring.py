def conversion(hours, mins, seconds):
    """returns the amount of seconds from hours, mins and seconds"""
    return hours*3600+mins*60+seconds

#help(conversion)

class Elevator:
    def __init__(self, bottom, top, current):
        self.bottom = bottom
        self.top = top
        self.current = current
    def up(self):
        """Makes the elevator go up"""
        if self.current <= 10:
            self.current += 1
        pass
    def down(self):
        """Makes the elevator go down"""
        if self.current > 0:
            self.current -= 1
        pass
    def go_to(self, floor):
        """Makes the elevetor go to a specific floor"""
        self.current = floor

ele = Elevator(-1, 10, 0)
ele.up()
ele.down()
ele.down()
print(ele.current)