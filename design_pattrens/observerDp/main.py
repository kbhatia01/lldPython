import time

from design_pattrens.observerDp.observers.Display import Display
from design_pattrens.observerDp.observers.Zomato import Zomato
from design_pattrens.observerDp.subject.WeatherStation import WeatherStation

if __name__ == '__main__':
    ws = WeatherStation()

    d1 = Display()
    z = Zomato()

    d1.registerSubject(ws)
    z.registerSubject(ws)

    ws.updateWeather(10, 50)
    time.sleep(2)
    ws.updateWeather(20, 100)
    time.sleep(2)

    ws.updateWeather(5, 60)
    time.sleep(2)

    z.unregisterSubject(ws)

    ws.updateWeather(60, 10)
    time.sleep(2)

    ws.updateWeather(10, 10)
    time.sleep(2)

    ws.updateWeather(10, 160)