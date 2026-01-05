from loguru import logger
import math


length_of_land = 100
breadth_of_land = 200
bricks_cost_per_piece = 10.5
labour_mistri1 = "Jagmohan"
labour_mistri2 = "Rampyare"
is_home =True

#calculatre the area of land

total_area_of_land = length_of_land * breadth_of_land

#calculate the perimeter of land
#use bodmas formula Brackets,orders,division,multiplication,addition,subtraction
perimeter_of_land = 2 * (length_of_land + breadth_of_land)

#Modulo operator

print(15/7)
#floor division
print(15//7)

#Ceiling division
print(math.ceil(15/7))


#concatenate string
a = "25"
b = "1"

print(a+b)

#type casting explicit
a = 25
b = "1"

print(a+int(b))

#type casting implicit
c=11.5
d= 5
print(c+d)



logger.info(f"Total are of my land is {total_area_of_land} sq ft")
logger.info(f"Perimeter of land is {perimeter_of_land} ft")


length_of_land = float(input("Enter the length of land in ft: "))
breadth_of_land = input("Enter the breadth of land in ft: ")

total_area_of_your_land = length_of_land * float(breadth_of_land)
logger.info(f"Total area of your land is {total_area_of_your_land} sq ft")

