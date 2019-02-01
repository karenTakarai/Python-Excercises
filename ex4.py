cars = 100
space_in_car = 4.0
drivers = 30
passengers = 90
cars_not_drive = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_car
average_passengers_per_car = passengers / cars_driven


print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_drive, "empty cars today.")
print("We can transport", carpool_capacity, "people today")
print("We have", passengers, "to carpool today.")
print("we need to put about", average_passengers_per_car,
"in each car.")

#book error explanation
#In line 7 maybe you defined "carpool_capacity" 
#then you tried to asign car_pool_capacity / passenger to
#to average_passengers_per_car, but car_pool_capacity did not exist
#maybe you forgot that the name of that variable was carpool_capacity and not car_pool_capacity