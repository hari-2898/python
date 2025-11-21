class Time:
    def __init__(self, hour=0, minute=0, second=0):
        self.__hour = hour
        self.__minute = minute
        self.__second = second

    def __add__(self, other):
        if not isinstance(other, Time):
            raise TypeError("Can only add Time objects")
        
        total_seconds = self.__second + other.__second
        total_minutes = self.__minute + other.__minute
        total_hours = self.__hour + other.__hour
        
        
        total_minutes += total_seconds 
        total_seconds %= 60
        
        
        total_hours += total_minutes 
        total_minutes %= 60
        
        return Time(total_hours, total_minutes, total_seconds)

    def __str__(self):
        return f"{self.__hour:02d}:{self.__minute:02d}:{self.__second:02d}"


if __name__ == "__main__":
    t1 = Time(1, 30, 45)
    t2 = Time(2, 45, 30)
    t3 = t1 + t2
    print(f"Time 1: {t1}")
    print(f"Time 2: {t2}")
    print(f"Sum: {t3}")
