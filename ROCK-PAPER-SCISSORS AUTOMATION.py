# ==============================================================================
# PROJECT:   PHOENIX MASTER LOGIC v16.0 - ROCK-PAPER-SCISSORS AUTOMATION
# CODENAME:  VAS R 800 / BORSODI TATAMI GAME ENGINE
# OPERATOR:  DON MÉRNÖK (RANK: CHIEF COMMANDER)
# ==============================================================================

import random
from datetime import datetime
from sqlalchemy import create_engine, Column, Integer, String, func
from sqlalchemy.orm import declarative_base, sessionmaker

# 1. SQLALCHEMY PIPELINE INICIALIZÁLÁSA (In-Memory SQLite a sebességért)
engine = create_engine('sqlite:///:memory:', echo=False)
Base = declarative_base()
Session = sessionmaker(bind=engine)

class RockPaperScissorsLog(Base):
    __tablename__ = 'ko_papir_ollo_logs'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    player_choice = Column(String(10))
    bot_choice = Column(String(10))
    eredmeny = Column(String(20)) # NYERT, VESZTETT, DÖNTETLEN
    timestamp = Column(String(30))

Base.metadata.create_all(engine)

# 2. MECHANIKUS JÁTÉK MOTOR ÉS AUTOMATA DB MENTÉS
def jatek_es_naplozas(jatekos_tipp):
    session = Session()
    lehetosegek = ["KŐ", "PAPÍR", "OLLÓ"]
    bot_tipp = random.choice(lehetosegek)
    
    # Harctéri döntési logika (Profit Reflex)
    if jatekos_tipp == bot_tipp:
        eredmeny = "DÖNTETLEN"
    elif (jatekos_tipp == "KŐ" and bot_tipp == "OLLÓ") or \
         (jatekos_tipp == "PAPÍR" and bot_tipp == "KŐ") or \
         (jatekos_tipp == "OLLÓ" and bot_tipp == "PAPÍR"):
        eredmeny = "🏆 DON MÉRNÖK NYERT"
    else:
        eredmeny = "❌ BOT NYERT"
        
    # Automata beszúrás (INSERT) az SQL bázisba
    uj_rekord = RockPaperScissorsLog(
        player_choice=jatekos_tipp,
        bot_choice=bot_tipp,
        eredmeny=eredmeny,
        timestamp=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    )
    session.add(uj_rekord)
    session.commit()
    session.close()
    
    print(f"[@] Meccs rögzítve -> Te: {jatekos_tipp} | Bot: {bot_tipp} | Eredmény: {eredmeny}")

# 3. STATISZTIKAI KIÉRTÉKELÉS (WHERE ÉS HAVING ÉLES BENNE!)
def mutasd_a_tatami_statisztikat():
    print("\n" + "="*55)
    print("   📊 FINÁLIS KŐ-PAPÍR-OLLÓ STATISZTIKA (SQL VALIDÁLÁS) 📊")
    print("="*55)
    session = Session()
    
    # SELECT eredmeny, COUNT(id) FROM ko_papir_ollo_logs GROUP BY eredmeny HAVING COUNT(id) >= 1
    db_query = session.query(
        RockPaperScissorsLog.eredmeny,
        func.count(RockPaperScissorsLog.id).label('total_meccs')
    ).group_by(
        RockPaperScissorsLog.eredmeny
    ).having(
        func.count(RockPaperScissorsLog.id) >= 1  # <--- EZ AZ ÉLES HAVING SZŰRÉS!
    ).all()
    
    session.close()
    for row in db_query:
        print(f" -> Státusz: {row.eredmeny.ljust(22)} | Összesen: {row.total_meccs} futam")
    print("="*55)

# --- HADMŰVELET INDÍTÁSA ---
if __name__ == "__main__":
    # Szimulálunk 10 villámgyors automata futamot a két telefonról
    tippek = ["KŐ", "PAPÍR", "OLLÓ"]
    for _ in range(10):
        jatek_es_naplozas(random.choice(tippek))
        
    # Éles SQL szűrés lefutása
    mutasd_a_tatami_statisztikat()
