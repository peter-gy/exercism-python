class SpaceAge:

    periodMap = {
        "mercury": 0.2408467,
        "venus": 0.61519726,
        "earth": 1.0,
        "mars": 1.8808158,
        "jupiter": 11.862615,
        "saturn": 29.447498,
        "uranus": 84.016846,
        "neptune": 164.79132,
    }

    EARTH_YEAR_IN_SECONDS = 31557600

    def __init__(self, seconds):
        self.seconds = seconds

    def __on(self, planet):
        return round(self.seconds / SpaceAge.EARTH_YEAR_IN_SECONDS / SpaceAge.periodMap[planet], 2)

    def on_mercury(self):
        return self.__on('mercury')

    def on_venus(self):
        return self.__on('venus')

    def on_earth(self):
        return self.__on('earth')

    def on_mars(self):
        return self.__on('mars')

    def on_jupiter(self):
        return self.__on('jupiter')

    def on_saturn(self):
        return self.__on('saturn')

    def on_uranus(self):
        return self.__on('uranus')

    def on_neptune(self):
        return self.__on('neptune')
