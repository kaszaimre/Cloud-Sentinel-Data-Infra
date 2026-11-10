# gladiatorEngine.py - Phoenix Master Autonóm Kvantitatív Szelekciós Motor
import random
import time

class GladiatorAgent:
    def __init__(self, agent_id, atr_multiplier, trailing_sl_ratio, mcdx_weight):
        self.agent_id = agent_id
        self.atr_multiplier = atr_multiplier       # Mutációs ATR szorzó
        self.trailing_sl_ratio = trailing_sl_ratio # Dinamikus csúszó stop arány
        self.mcdx_weight = mcdx_weight             # Bankár Smart Money súlyozás
        self.profit_factor = 4.1                   # Kezdő prémium PF
        self.win_rate = 0.65                       # 65% Alapértelmezett Win Rate
        self.is_alive = True

    def mutate(self):
        """Mikromutációk végrehajtása a Gladiátor Laborban"""
        self.atr_multiplier += random.uniform(-0.1, 0.1)
        self.trailing_sl_ratio += random.uniform(-0.05, 0.05)
        self.mcdx_weight += random.uniform(-0.05, 0.05)

class GladiatorArena:
    def __init__(self, total_clans=50):
        self.arena_id = "PHOENIX_LAB_V5.2"
        # 50 Elit Klán inicializálása apró eltérésekkel
        self.clans = [
            GladiatorAgent(
                agent_id=f"Clan_{i}",
                atr_multiplier=random.uniform(1.2, 2.5),
                trailing_sl_ratio=random.uniform(0.8, 1.8),
                mcdx_weight=random.uniform(0.3, 0.6)
            ) for i in range(total_clans)
        ]

    def evaluate_generation(self, market_volatility, market_regime):
        """A 0 CPU és az Éles Végrehajtás közötti híd"""
        survivors = []
        
        for agent in self.clans:
            if not agent.is_alive:
                continue
                
            # Piaci stressz szimuláció a futó trade-ek alapján
            performance_shock = random.uniform(-0.5, 0.6) * market_volatility
            agent.profit_factor += performance_shock
            
            # 💀 KÍMÉLETLEN DARWINISTA SZELEKCIÓ
            if agent.profit_factor < 3.0:
                agent.is_alive = False
                print(f"[💀 ARÉNA - ELHULLOTT]: {agent.agent_id} | PF: {agent.profit_factor:.2f} -> LIKVIDÁLVA")
            else:
                survivors.append(agent)
                
        # Győztesek klónozása és újragenerálása az elhullottak helyére
        while len(survivors) < 50 and len(survivors) > 0:
            best_parent = max(survivors, key=lambda a: a.profit_factor)
            clone = GladiatorAgent(
                agent_id=f"{best_parent.agent_id}_Clone_{int(time.time())}",
                atr_multiplier=best_parent.atr_multiplier,
                trailing_sl_ratio=best_parent.trailing_sl_ratio,
                mcdx_weight=best_parent.mcdx_weight
            )
            clone.mutate() # Mutáció ráengedése az új generációra
            survivors.append(clone)
            
        self.clans = survivors
        
        # 👑 A GYŐZTES ÁTADÁSA A T800 PARANCSNOKNAK
        elite_commander = max(self.clans, key=lambda a: a.profit_factor)
        return {
            "t800_target_agent": elite_commander.agent_id,
            "optimized_atr": elite_commander.atr_multiplier,
            "optimized_trailing": elite_commander.trailing_sl_ratio,
            "top_profit_factor": elite_commander.profit_factor
        }

# Éles tesztfutás a SzalonnaNet háttérkörnyezetben
if __name__ == "__main__":
    arena = GladiatorArena()
    # Szimulálunk egy komolyabb BTC csapkodást (volatilitás: 1.5, trend rezsim)
    t800_update = arena.evaluate_generation(market_volatility=1.5, market_regime="BULL_TREND")
    print(f"\n[👑 T800 PARANCSNOK FRISSÍTVE]: Legerősebb ágens élesítve: {t800_update['t800_target_agent']} | TOP PF: {t800_update['top_profit_factor']:.2f}")
