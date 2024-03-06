

# publicTransportFreqIndex: 
# 0: Rarely (2/month or less)
# 1: Occasionally (3-5/month)
# 2: Regularly (1/week or more)

# carTypeIndex:
# 0: Petrol
# 1: Diesel
# 2: Hybrid
# 3: Electric
# 4: None

# carSizeIndex:
# 0: Compact
# 1: SUV
# 2: Minivan
# 3: Pickup Truck



# def get_carbon_emission_by_type(car_type):
#     if car_type == 0:   #Petrol
#         return 0.164  # in Kg/km average petrol car produced the equivalent of 164 grams of CO₂e per km 
#     elif car_type == 1: #Diesel
#         return 0.17  # in Kg  diesel cars averaged roughly 170 grams of CO₂e per km
#     elif car_type == 2: #Hybrid
#         return 0.144  # in Kg hybrid car will emit 51.6 pounds (23.1 kilograms) of carbon dioxide every 100 miles (161 kilometers)
#     elif car_type == 3: #Electric
#         return 0  # Carbon emissions for electric vehicles depend on electricity source


# def get_mpg_by_size(car_size):
#     if car_size == 0: #Compact
#         return 7.35  # in L/100km - The average fuel efficiency for a small car is 32 MPG
#     elif car_size == 1: #SUV
#         return 8.11   # in L/100km - The average fuel economy for modern SUVs is 29 mpg .
#     elif car_size == 2 or car_size == 3: #Minivan
#         return 10.69  # in L/100km - The average fuel efficiency for a minivan is 22 MPG, The average fuel efficiency for a full-size truck is 22 MPG



def transportEmissions(averageWeeklyKm, airTravelHours, carSize, carType):
    car_sizes = [0.0735, 0.0811, 0.1069, 0.1069]  #l/km
    car_types = [2.3, 2.7, 2.3, 0] #kg emissions per fuel type

    if carType == 3:
        carCarbonEmissions = 0
    else:
        carCarbonEmissions = car_sizes[carSize] * averageWeeklyKm * car_types[carType]
    
    flightEmissions = airTravelHours * 90
    
    totalEmissions = carCarbonEmissions + flightEmissions

    return totalEmissions


def energyEmissions(electricityUsage, naturalGasUsage, typeElectricity):
    co2_elec = [1.0433, 0.44, 1.08] #Coal, Natural Gas, Petroleum Co2 per kwh

    energy_emissions = (co2_elec[typeElectricity]*electricityUsage) + (naturalGasUsage*co2_elec[1])
    
    return energy_emissions


#One serving of Beef (100g). One serving of Beef (100g) is equivalent to 15.5kg CO2e, or 78.7km of driving. 
# One serving of Beef (100g) is equivalent to 15.5kg CO2e.
#One serving (100g) of Fish is equivalent to 1.34kg CO2e, or 6.8km of driving.
#One serving of Chicken (100g) is equivalent to 1.82kg CO2e, or 9.3km of driving. 
#One serving of Chicken (100g) is equivalent to 1.82kg CO2e.

def foodEmissions(redMeatConsumption, poultryConsumption, seafoodConsumption, dairyConsumption):
    