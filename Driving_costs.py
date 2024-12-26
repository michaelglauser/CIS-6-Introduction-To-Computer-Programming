
#2.14 LAB: Driving costs

#Driving is expensive. Write a program with a car's gas mileage (miles/gallon) and the cost of gas (dollars/gallon) as floating-point input, and output the gas cost for 20 miles, 75 miles, and 500 miles.

#Output each floating-point value with two digits after the decimal point, which can be achieved as follows:

#print(f'{your_value1:.2f} {your_value2:.2f} {your_value3:.2f}')

#Ex: If the input is:

#25.0
#3.1599

#where the gas mileage is 25.0 miles/gallon and the cost of gas is $3.1599/gallon, the output is:

#2.53 9.48 63.20

#Note: Real per-mile cost would also include maintenance and depreciation.


gas_mileage = float(input())
cost_of_gas = float(input())

gas_cost = cost_of_gas/gas_mileage

your_value1 = gas_cost * 20.0
your_value2 = gas_cost * 75.0
your_value3 = gas_cost * 500.0

print(f'{your_value1:.2f} {your_value2:.2f} {your_value3:.2f}')