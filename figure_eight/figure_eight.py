import numpy as np


class FigureEight:
    def __init__(self, ampx, ampy, freqx, freqy):
        """Constructor for the FigureEight class.

        @param ampx Amplitude of the x wave.
        @param ampy Amplitude of the y wave.
        @param freqx Frequency of the x wave.
        @param freqy Frequency of the y wave.
        """
        self.ampx = ampx
        self.ampy = ampy
        self.freqx = freqx
        self.freqy = freqy
        self.two_pi = 2.0 * np.pi

    def position(self, t):
        x = self.ampx * np.sin(self.two_pi * self.freqx * t)
        y = self.ampy * np.sin(self.two_pi * self.freqy * t)
        return np.array([x, y])

    def velocity(self, t):
        dx = self.ampx * self.two_pi * self.freqx * np.cos(self.two_pi * self.freqx * t)
        dy = self.ampy * self.two_pi * self.freqy * np.cos(self.two_pi * self.freqy * t)
        return np.array([dx, dy])

    def acceleration(self, t):
        Ax = -self.ampx * self.two_pi**2 * self.freqx**2
        Ay = -self.ampy * self.two_pi**2 * self.freqy**2
        ddx = Ax * np.sin(self.two_pi * self.freqx * t)
        ddy = Ay * np.sin(self.two_pi * self.freqy * t)
        return np.array([ddx, ddy])
