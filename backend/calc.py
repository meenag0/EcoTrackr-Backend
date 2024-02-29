def get_carbon_emission_per_litre(car_type):
    if car_type == "gas":
        return 2.3  # kg CO2 per litre for gasoline engines
    elif car_type == "diesel":
        return 2.7  # kg CO2 per litre for diesel engines
    elif car_type == "electric":
        return None  # Carbon emissions for electric vehicles depend on electricity source


def calculate_carbon_emissions(progress, averageWeeklyMiles, vehicleFuelEfficiency, airTravelFrequency_domestic, airTravelFrequency_inter, carSizeIndex, carTypeIndex):
    car_sizes = ["medium", "small", "big"]
    car_types = ["gas", "diesel", "electric"]

    car_size = car_sizes[carSizeIndex]
    car_type = car_types[carTypeIndex]

    car_emission_per_litre = get_carbon_emission_per_litre(car_type)

    if car_emission_per_litre is not None:
        car_emission = car_emission_per_litre * (averageWeeklyMiles * vehicleFuelEfficiency) / 100
    else:
        electricity_carbon_intensity = 0.1  # hypothetical value for electricity carbon intensity
        car_emission = electricity_carbon_intensity * (averageWeeklyMiles * vehicleFuelEfficiency) / 100

    # Calculate carbon emissions for plane travel
    plane_emission = (airTravelFrequency_domestic * 90) + (airTravelFrequency_inter * 90)

    total_emissions = car_emission + plane_emission
    return total_emissions

# Example usage:
progress = 0
averageWeeklyMiles = 200  # Example value
vehicleFuelEfficiency = 10  # Example value (miles per gallon)
airTravelFrequency_domestic = 2  # Example value
airTravelFrequency_inter = 11  # Example value
carSizeIndex = 0  # Index selected from dropdown menu
carTypeIndex = 0  # Index selected from dropdown menu

carbon_emissions = calculate_carbon_emissions(progress, averageWeeklyMiles, vehicleFuelEfficiency, airTravelFrequency_domestic, airTravelFrequency_inter, carSizeIndex, carTypeIndex)
print("Total carbon emissions:", carbon_emissions, "kg CO2")
