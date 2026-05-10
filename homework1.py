class car():
    speed = 90
    car_model = ""
    car_brand = "" 
    wheel_size = 0.3
    def __init__(self):
        pass
    def accelarate(self):
        self.speed += 10
    def show_details(self):
        print(self.speed,self.car_brand,self.car_model," the wheel size is " + self.wheel_size)
    def change_details(self):
        self.speed = int(input("enter car speed "))
        self.car_brand = input("enter car brand ")
        self.car_model = input("enter car model ")
        self.wheel_size = input("enter car wheels tall ") + " tall"

show = car()
show.change_details()
show.show_details()
i = input("would you like to accelerate? ")
if i == "yes":
    show.accelarate()
    show.show_details()