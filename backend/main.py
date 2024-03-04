from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from calc import calculate_carbon_footprint


app = FastAPI()

class TransportationData(BaseModel):

    averageWeeklyMiles: float
    vehicleFuelEfficiency: float  
    airTravelFrequency: int       
    carSize: int            
    carType: int 

transportation_data = TransportationData(

    vehicleFuelEfficiency=0.0,           
    airTravelFrequency=0,
    publicTransportationUsage=0,
    carMaintanence=0,
    bikingWalkingFrequency=0
)


@app.post("/")
async def calculate(data: TransportationData):

    # Access data fields
    average_weekly_miles = data.averageWeeklyMiles
    vehicle_fuel_efficiency = float(data.vehicleFuelEfficiency)  
    air_travel_frequency = int(data.airTravelFrequency)    //hour
    car_size = int(data.carSize)                
    car_type = int(data.carType)

    # Perform calculations using the received data
    carbon_footprint = calculate_carbon_footprint(average_weekly_miles, vehicle_fuel_efficiency, air_travel_frequency, car_size, car_type)

    # Return the result
    return {"carbon_footprint": carbon_footprint}

    print("Received data:", data)

    # Return the result
    return {"carbon_footprint": carbon_footprint}


@app.get("/")
async def read_root():
    return transportation_data.dict()