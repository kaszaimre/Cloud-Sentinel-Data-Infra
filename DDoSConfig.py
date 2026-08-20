# Add hozzá a meglévő FastAPI appodhoz az új szimulációs végpontokat:

class DDoSConfig(BaseModel):
    attack_vector: str    # Pl.: "HTTP_GET_FLOOD"
    target_resource: str  # Pl.: "/api/v1/checkout"
    botnet_size: int      # Pl.: 500
    intensity: int        # Pl.: 75
    secret_key: str

@app.post("/v1/ddos-simulate")
async def start_ddos_simulation(config: DDoSConfig, background_tasks: BackgroundTasks):
    if config.secret_key != SECRET_KEY:
        raise HTTPException(status_code=403, detail="OpSec hiba! Hozzáférés megtagadva.")
    
    # A nehéz szimulációt kilőjük a háttérbe, a frontend azonnal kap egy "LAUNCHED" státuszt
    background_tasks.add_task(run_heavy_botnet_simulation, config)
    
    return {
        "status": "ATTACK_INITIALIZED",
        "target": config.target_resource,
        "bots_deployed": config.botnet_size
    }

async def run_heavy_botnet_simulation(config: DDoSConfig):
    # Ide jön a háttérben futó T-1000-es mag, ami generálja a grafikonra az adatokat (RPS, Latency)
    print(f"[BOTNET] Indítás -> {config.botnet_size} zombi támadja a {config.target_resource} végpontot!")
    await asyncio.sleep(5) # Szimulált támadási időablak
