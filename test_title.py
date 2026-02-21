import asyncio
from motor.motor_asyncio import AsyncIOMotorClient

async def main():
    client = AsyncIOMotorClient("mongodb+srv://tg-stremio-h2r:PDQk1f7BeOl3xE9BKyxE8QAhgBd5mwnx@cluster0.sqo2szn.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    db = client["dbFyvio"]
    stream_id = "LCVXJwXrK0kV3sAbZPRSmIksn65HDyqGujnSw4kE6RIUyruRJCC7mJKhuQ4"
    
    tv = await db["tv"].find_one({"seasons.episodes.telegram.id": stream_id})
    if tv:
        print("Found TV by exact stream_id hash match!")
    else:
        print("Failed to map TV by exact stream_id hash match.")

if __name__ == "__main__":
    asyncio.run(main())
