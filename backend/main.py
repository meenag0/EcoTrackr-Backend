from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class TransportationData(BaseModel):
    averageWeeklyMiles: float
    vehicleFuelEfficiency: str
    airTravelFrequency: str
    publicTransportationUsage: str
    carMaintanence: str
    bikingWalkingFrequency: str

transportation_data = TransportationData(
    averageWeeklyMiles=0,
    vehicleFuelEfficiency="",
    airTravelFrequency="",
    publicTransportationUsage="",
    carMaintanence="",
    bikingWalkingFrequency=""
)


@app.post("/")
async def calculate(data: TransportationData):

    # Access data fields
    average_weekly_miles = data.averageWeeklyMiles
    vehicle_fuel_efficiency = data.vehicleFuelEfficiency
    air_travel_frequency = data.airTravelFrequency
    public_transportation_usage = data.publicTransportationUsage
    car_maintenance = data.carMaintanence
    biking_walking_frequency = data.bikingWalkingFrequency

    # Perform calculations using the received data

    carbon_footprint = average_weekly_miles * 0.05  # Example calculation

    print("Received data:", data)

    # Return the result
    return {"carbon_footprint": carbon_footprint}


@app.get("/")
async def read_root():
    return transportation_data.dict()