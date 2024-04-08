import sys
from fastapi import FastAPI, HTTPException
import uvicorn
from pydantic import BaseModel
from calc import transportEmissions, energyEmissions, foodEmissions 
from fastapi.middleware.cors import CORSMiddleware
import requests
import logging
from starlette.responses import Response
import requests
import math
import base64 
from starlette.responses import StreamingResponse  # Import StreamingResponse for returning binary data

app = FastAPI()



origins = [
    'http://10.0.0.192:8081',
    'http://localhost:8081'
]


app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],  
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],
    allow_headers=["*"],
)


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
    localFoodPurchases: int 
    poultryConsumption: int 
    dairyConsumption: int 
    seafoodConsumption: int 
    fastFashion: int 
    sustainableShoppingFrequency: int 
    Recycling: int 


def calculate_total_emissions(data: FullData) -> float:

    # Access data fields
    average_weekly_km = (data.averageWeeklyKm)
    public_transport = (data.publicTransportFreq)  
    air_travel_hours = (data.airTravelHours)
    car_size = (data.carSize)
    car_type = (data.carType)

    electricity_usage = (data.electricityUsage)
    natural_gas = (data.naturalGasUsage)
    lightUse_time = (data.lightUseTime)
    electricity_type = (data.typeElectricity)
    redmeat_consumption = (data.redMeatConsumption)
    local_purchase = (data.localFoodPurchases)
    poultry_consumption = (data.poultryConsumption)
    dairy_consumption = (data.dairyConsumption)
    seafood_consumption = (data.seafoodConsumption)
    fast_fashion = (data.fastFashion)
    sustainable_shopping = (data.sustainableShoppingFrequency)
    recycling = (data.Recycling)

    # Perform calculations using the received data
    transportation_emissions = transportEmissions(average_weekly_km, air_travel_hours, car_size, car_type)
    energy_emissions = energyEmissions(electricity_usage, natural_gas, electricity_type)
    food_emissions = foodEmissions(redmeat_consumption, poultry_consumption, seafood_consumption, dairy_consumption)
    
    total_emissions = int(transportation_emissions + energy_emissions + food_emissions)
    
    print("Received data:", data)
    print("Total emissions:", int(total_emissions))

    return total_emissions

class LocationData(BaseModel):
    latitude: float
    longitude: float

@app.post("/")
async def dataset(data: FullData):
    terribledVal = 6000
    badVal = 4000
    okayVal = 2000
    goodVal = 1000
    greatVal = 500
    try:

        total_emissions = calculate_total_emissions(data)
        print("Received data:", data)
        print("Total emissions:", total_emissions)
    
        if total_emissions <= greatVal:
            return
        elif total_emissions <= goodVal:
            return
        elif total_emissions <= okayVal:
            return
        elif total_emissions <= badVal:
            return
        elif total_emissions >= badVal:
            return
        
        return {"total_emissions": total_emissions}
    except Exception as e:
        raise HTTPException(status_code=500, detail="Error calculating total emissions: " + str(e))

def lat_lng_to_tile(latitude, longitude, zoom):
    x = (longitude + 180) / 360 * (2 ** zoom)
    y = (1 - math.log(math.tan(latitude * math.pi / 180) + 1 / math.cos(latitude * math.pi / 180)) / math.pi) / 2 * (2 ** zoom)
    return int(x), int(y)


@app.post("/fetch_heatmap")
async def fetch_heatmap(location_data: LocationData):

    try:

        latitude = location_data.latitude
        longitude = location_data.longitude

        x, y = lat_lng_to_tile(latitude, longitude, 2)


        api_key = 'AIzaSyDI8QeqTOaMCc2C4x9zA338-zb-ebKdqfQ'
        apiUrl = f'https://airquality.googleapis.com/v1/mapTypes/CAN_EC/heatmapTiles/2/{x}/{y}?key={api_key}'

        print(f"Requesting data from API: {apiUrl}")
        
        response = requests.get(apiUrl, headers={'Content-Type': 'image/png'})

        # Check if the request was successful
        if response.status_code == 200:
            # Return the PNG image content as a streaming response
            image_data_base64 = base64.b64encode(response.content).decode("utf-8")
            return {"image_data_base64": image_data_base64}

        else:
            # If the request was not successful, raise an HTTPException
            response.raise_for_status()
    except Exception as e:
        logging.error(f"Error fetching heatmap data: {e}")
        raise HTTPException(status_code=500, detail="Error fetching heatmap data: " + str(e))

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8080)