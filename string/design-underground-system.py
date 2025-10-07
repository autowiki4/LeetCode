class UndergroundSystem:

    def __init__(self):
        self.times = {}
        self.stations = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.times[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        from_station, time = self.times[id]
        diff = t-time
        route = (from_station, stationName)
        if route not in self.stations:
            self.stations[route] = [0,0]
        self.stations[route][0] += diff
        self.stations[route][1] += 1

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        route = (startStation, endStation)
        return self.stations[route][0] / self.stations[route][1]
        


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)