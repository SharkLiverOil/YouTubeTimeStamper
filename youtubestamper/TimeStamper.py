import time


class TimeStamper:
    def __init__(self, pad: int=0, mult: float=1.0, delay: int=0):
        self.start_pad = pad
        self.multiplier = mult
        self.delay = delay
        self.start_time = time.time()
        self.stamp_list = []

    def __str__(self):
        return ', '.join(map(str, self.stamp_list))

    def __repr__(self):
        return 'Pad: {}\nMultiplier: {}\nDelay: {}\nStart Time: {}\nStamps: {}'.format(self.start_pad,
                                                                                       self.multiplier,
                                                                                       self.delay,
                                                                                       self.start_time,
                                                                                       str(self.stamp_list))

    def stamper(self):
        """
        Built-in time stamper interface.
        """
        run = True
        print('Any input quits the timer.')
        while run:
            user_in = input('Press enter for stamp.')
            if user_in == '':
                stamp = self.stamp()
            else:
                run = False
        print(self)

    def stamp(self):
        """
        Creates a time stamp and adds it to the TimeStamper's list.
        :return: float
        """
        stamp_time = time.time()
        stamp = ((stamp_time - self.start_time) * self.multiplier) + self.start_pad - self.delay
        if stamp < 0:
            stamp = 0
            self.stamp_list.append(stamp)
            return 0
        self.stamp_list.append(stamp)
        return stamp

    def set_start(self):
        """
        Sets the start time of the timer
        """
        self.start_time = time.time()

    def int_list(self):
        """
        Makes all the time stamps into an int format.
        :return:
        """
        int_list = []
        for i in self.stamp_list:
            int_list.append(int(i))
        return int_list
