import random
import time
from plane import Plane


class Simulation:
    if __name__ == "__main__":
        plane = Plane()

        while True:
            new_angle = random.gauss(0, 30)
            plane.apply_new_tilt(new_angle)
            plane.correct_tilt()
            plane.print_current_tilt()
            time.sleep(0.5)
