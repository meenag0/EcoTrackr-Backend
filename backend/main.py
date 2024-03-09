import sys
from fastapi import FastAPI, HTTPException
import uvicorn
from pydantic import BaseModel
from calc import transportEmissions, energyEmissions, foodEmissions 
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()


origins = [
    "http://localhost:8081",
    "localhost:8081"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8081)

class FullData(BaseModel):
    averageWeeklyKm: int
    publicTransportFreq: int  
    airTravelHours: int       
    carSize: int            
    carType: int 
    electricityUsage: int
    naturalGasUsage:  int
    lightUseTime: int
    typeElectricity: int
    redMeatConsumption: int
    vegetarianVeganMeals: int
    localFoodPurchases: int
    poultryConsumption: int
    dairyConsumption: int
    seafoodConsumption: int
    fastFashion: int
    sustainableShoppingFrequency: int
    Recycling: int


@app.post("/")
async def dataset(data: FullData):
    # Access data fields
    average_weekly_km = int(data.averageWeeklyKm)
    public_transport = int(data.publicTransportFreq)  
    air_travel_hours = int(data.airTravelHours)
    car_size = int(data.carSize)
    car_type = int(data.carType)

    electricity_usage = int(data.electricityUsage)
    natural_gas = int(data.naturalGasUsage)
    lightUse_time = int(data.lightUseTime)
    electricity_type = int(data.typeElectricity)
    redmeat_consumption = int(data.redMeatConsumption)
    veg_meals = int(data.vegetarianVeganMeals)
    local_purchase = int(data.localFoodPurchases)
    poultry_consumption = int(data.poultryConsumption)
    dairy_consumption = int(data.dairyConsumption)
    seafood_consumption = int(data.seafoodConsumption)
    fast_fashion = int(data.fastFashion)
    sustainable_shopping = int(data.sustainableShoppingFrequency)
    recycling = int(data.Recycling)

    # Perform calculations using the received data
    transportation_emissions = transportEmissions(average_weekly_km, air_travel_hours, car_size, car_type)
    energy_emissions = energyEmissions(electricity_usage, natural_gas, electricity_type)
    food_emissions = foodEmissions(redmeat_consumption, poultry_consumption, seafood_consumption, dairy_consumption)
    
    total_emissions = transportation_emissions + energy_emissions + food_emissions
    
    print("Received data:", data)
    print("Total emissions:", total_emissions)

    return {"total_emissions": total_emissions}


