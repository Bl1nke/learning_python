class Car:
    def __init__(self, brand, model, year, speed=0, is_engine_on=False):
        self.model = model
        self.year = year
        self.brand = brand
        self.speed = speed
        self.is_engine_on = is_engine_on

    def start_engine(self):
        self.is_engine_on = True
        return "Engine started"
    def stop_engine(self):
        self.is_engine_on = False
        self.speed = 0
        return "engine stop"
    
    def accelerate(self, increace):
        if self.is_engine_on:
            self.speed += increace
        else:
            raise ValueError("start engine first")
        return self.speed
    def brake(self, decrease):
        self.speed = max(0, self.speed - decrease)
        return self.speed
    
    def __str__(self):
        return f"{self.brand} {self.model} ({self.year}) — speed {self.speed} km/h, engine {'on' if self.is_engine_on else 'off'}"
    

if __name__ == "__main__":
    bmw = Car("bmw", "x5", 2025)
    bmw.start_engine()
    bmw.accelerate(70)
    bmw.brake(50)
    print(bmw)