class Plane:

    current_tilt = 0
    max_correction = 10
    correction = 0

    def print_current_tilt(self):
        print "Current tilt = " + str(self.current_tilt)

    def apply_new_tilt(self, tilt):
        self.current_tilt += tilt

    def correct_tilt(self):
        if abs(self.current_tilt) > self.max_correction:
            self.correction = self.max_correction
            if self.current_tilt > 0:
                self.current_tilt -= self.max_correction
            else:
                self.current_tilt += self.max_correction
        else:
            self.correction = 0 - self.current_tilt
            self.current_tilt = 0
