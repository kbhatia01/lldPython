from design_pattrens.observerDp.subject.subject import Subject


class WeatherStation(Subject):
    def __init__(self):
        super().__init__()
        self.temp = 0
        self.humidity = 0

    def updateWeather(self, temp, hum):
        self.temp = temp
        self.humidity = hum
        self.notify(temp, hum)
