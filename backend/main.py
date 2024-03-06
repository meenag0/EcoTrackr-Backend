from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from calc import transportEmissions 

app = FastAPI()

class TransportationData(BaseModel):

    averageWeeklyKm: float
    publicTransportFreq: float  
    airTravelHours: int       
    carSize: int            
    carType: int 


transportation_data = TransportationData(

    averageWeeklyKm=0.0,           
    publicTransportFreq=0,
    airTravelHours=0,
    carSize=0,
    carType=0
    
)


@app.post("/")
async def calculate(data: TransportationData):

    # Access data fields
    average_weekly_km = int(data.averageWeeklyKm)
    public_transport = int(data.publicTransportFreq)  
    air_travel_hours = int(data.airTravelHours)    #hour
    car_size = int(data.carSize)                
    car_type = int(data.carType)

    # Perform calculations using the received data
    carbon_footprint = transportEmissions(average_weekly_km, air_travel_hours, car_size, car_type)

    # Return the result
    return {"carbon_footprint": carbon_footprint}

    print("Received data:", data)


@app.get("/")
async def read_root():
    return transportation_data.dict()