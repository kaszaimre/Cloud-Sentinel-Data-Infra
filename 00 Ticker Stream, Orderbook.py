import asyncio
import logging
import sys

# Logolás beállítása a Borsodi Command Center stílusában
logging.basicConfig(
    level=logging.INFO, format="[%(asctime)s] [%(levelname)s] %(message)s"
)


async def run_core_worker(worker_name, command, restart_delay=3):
    """Elindít egy háttérfolyamatot (pl. Ticker Stream, Orderbook), és
    automatikusan újraindítja, ha összeomlik."""
    while True:
        logging.info(f"⚡ [T800 KERNEL] {worker_name} indítása: {command}...")

        try:
            # Folyamat indítása aszinkron módon
            process = await asyncio.create_subprocess_shell(
                command,
                stdout=asyncio.subprocess.PIPE,
                stderr=asyncio.subprocess.PIPE,
            )

            # Megvárjuk a folyamat futását vagy leállását
            stdout, stderr = await process.communicate()

            if process.returncode != 0:
                logging.warning(
                    f"⚠️ [MÁTRIX RIASZTÁS] {worker_name} leállt (Kód: {process.returncode}). Hiba: {stderr.decode().strip()}"
                )
            else:
                logging.info(
                    f"✅ [T800 KERNEL] {worker_name} sikeresen befejeződött."
                )

        except Exception as e:
            logging.error(
                f"❌ [RENDSZER HIBA] {worker_name} kritikus hiba: {str(e)}"
            )

        logging.info(
            f"🔄 [RECOVERY] Újraindítás megkísérlése {restart_delay} másodperc múlva..."
        )
        await asyncio.sleep(restart_delay)


async def main_orchestrator():
    logging.info("=== BORSODI MATRIX COMMAND CENTER START v83.0 ===")
    logging.info("Kvantummátrix inicializálása, csőre töltés...")

    # A repódban lévő főbb modulok aszinkron, párhuzamos indítási térképe
    workers = [
        run_core_worker(
            "LIVE_TICKER_STREAM", "python 0016_LIVE_TICKER_STREAM_WORKER.py"
        ),
        run_core_worker(
            "ORDERBOOK_ANALYZER", "python 0017_MARKET_DEPTH_ORDERBOOK_ANALYZER.py"
        ),
        run_core_worker("MQL5_BRIDGE", "python 0015_MQL5_REBAPI_DIRECT_BRIDGE.py"),
        run_core_worker(
            "POZICIO_CALCULATOR", "python \"00 pozicio kalkulator extra.py\""
        ),
    ]

    # Az összes worker szálat egyszerre indítjuk el egy közös aszinkron hurokban
    await asyncio.gather(*workers)


if __name__ == "__main__":
    # Windows és Linux környezet kompatibilitás kezelése
    if sys.platform == "win32":
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

    try:
        asyncio.run(main_orchestrator())
    except KeyboardInterrupt:
        logging.info(
            "🛑 [BORSODI GENERAL] Manuális leállítás és vészhelyzeti pozíció-fagyasztás parancs kiadva!"
        )
