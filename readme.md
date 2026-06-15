# Borsodi Mátrix - Modulok Tára

| Modul neve | Leírás |
| :--- | :--- |
| `00001 pathlib import Path.py` | --- |
| `0014_mt5_symbol_metadata_extractor.py` | LEÍRÁS (HU):  MetaTrader 5 szimbólum-metaadat kinyerő és validáló modul. Közvetlen kapcsolatot létesít a helyi MT5 terminállal. Automatikusan kiszívja  a valós idejű piaci szinteket (Bid, Ask, Tick Size, Last) a kiválasztott  eszközökhöz (pl. GOOGL, BTC-USD, HOOD), kizárva a manuális adatbeviteli hibákat. Mottó: A borsodi nem hackel, a borsodi optimalizál.  DESCRIPTION (EN):  MetaTrader 5 symbol metadata extractor and validator module. Establishes a direct connection with the local MT5 terminal. Automatically  extracts real-time market levels (Bid, Ask, Tick Size, Last) for selected  assets (e.g., GOOGL, BTC-USD, HOOD), eliminating manual data entry errors. Motto: The Borsodi doesn't hack, the Borsodi optimizes.  SZERZŐ: Don Mérnök (Tábornok) | BORSODI WAR ROOM |
| `0015_MQL5_WEBAPI_DIRECT_BRIDGE.py` | LEÍRÁS (HU):  MQL5 WebAPI közvetlen szerveroldali adathíd modul. Lehetővé teszi az élő számlaadatok (egyenleg, tőke, nyitott pozíciók) lekérését közvetlenül az MQL5 központi szervereiről, kiküszöbölve a helyi terminálfuttatás  és az IPC (Inter-Process Communication) inicializációs hibák kényszerét. Mottó: A borsodi nem hackel, a borsodi optimalizál.  DESCRIPTION (EN):  MQL5 WebAPI direct server-side data bridge module. Enables fetching live account data (balance, equity, open positions) directly  from MQL5 central servers, eliminating the need for local terminal execution  and avoiding IPC initialization errors. Motto: The Borsodi doesn't hack, the Borsodi optimizes.  SZERZŐ: Don Mérnök (Tábornok) | BORSODI WAR ROOM |
| `0016_LIVE_TICKER_STREAM_WORKER.py` | LEÍRÁS (HU):  Élő adatfolyam-kezelő és folyamatos telemetria-naplózó modul (Stream Worker). A Phoenix Master Oracle v5.1 valós idejű órajel-generátora. 5 másodpercenként  frissíti a lokális adatbázist és a tőzsdei szinteket, biztosítva a folyamatos  fájlrendszer-aktivitást és a Git statisztikák magasan tartását. Mottó: A borsodi nem hackel, a borsodi optimalizál.  DESCRIPTION (EN):  Live ticker stream worker and continuous telemetry logging module. The real-time clock generator of the Phoenix Master Oracle v5.1. Updates the  local database and market levels every 5 seconds, ensuring continuous file system  activity and maintaining high Git traffic statistics. Motto: The Borsodi doesn't hack, the Borsodi optimizes.  SZERZŐ: Don Mérnök (Tábornok) | BORSODI WAR ROOM |
| `0018_SPREAD_ANOMALY_SENSOR.py` | LEÍRÁS (HU):  Bróker spread-tágulás és piaci anomália detektáló modul. Folyamatosan méri a Bid és Ask árak közötti távolságot. Ha a spread átlépi  a megengedett biztonsági limitet (pl. hírek vagy éjszakai likviditáshiány miatt),  a rendszer letiltja a pozíciónyitást a számlavédelem érdekében. Mottó: A borsodi nem hackel, a borsodi optimalizál.  DESCRIPTION (EN):  Broker spread widening and market anomaly sensor module. Continuously measures the gap between Bid and Ask prices. If the spread exceeds  the safety threshold (due to news or nightly liquidity drops), the system  blocks trade execution for equity protection. Motto: The Borsodi doesn't hack, the Borsodi optimizes.  SZERZŐ: Don Mérnök (Tábornok) | BORSODI WAR ROOM |
| `005_PATH_ENVIRONMENT_VALIDATOR.py` | LEÍRÁS (HU):  Rendszerútvonal és környezet-validáló alapmodul (Path Validator). Automatikusan ellenőrzi és biztosítja a Phoenix Master futási környezetének, mappaszerkezetének és a szükséges kritikus naplófájlok meglétét a PC-n. Mottó: A borsodi nem hackel, a borsodi optimalizál.  DESCRIPTION (EN):  System path and environment validation base module (Path Validator). Automatically verifies and ensures the availability of the Phoenix Master runtime environment, directory structure, and critical log files on the PC. Motto: The Borsodi doesn't hack, the Borsodi optimizes.  SZERZŐ: Don Mérnök (Tábornok) | BORSODI WAR ROOM |
| `006_BRIGAD_WAR_ROOM_DASHBOARD.py` | LEÍRÁS (HU):  Borsodi Brigád Központi Parancsnoki Felület (War Room Dashboard). Összefogja és egyetlen felületen vizualizálja a hálózati biztonsági,  kiber-védelmi és tőzsdei Oracle alrendszerek státuszát.  Valós idejű telemetria-központ az operátori döntések támogatásához. Mottó: A borsodi nem hackel, a borsodi optimalizál.  DESCRIPTION (EN):  Borsodi Brigád Central War Room Dashboard. Aggregates and visualizes the status of network security, cyber deception,  and trading Oracle subsystems in a single interface. Real-time telemetry  hub supporting operator decisions. Motto: The Borsodi doesn't hack, the Borsodi optimizes.  SZERZŐ: Don Mérnök (Tábornok) | BORSODI WAR ROOM |
| `007_GIT_WORKSPACE_INTEGRITY_CHECKER.py` | LEÍRÁS (HU):  Git munkakörnyezet és adat-integritás ellenőrző modul (Integrity Checker). Validálja a lokális Git repó állapotát, és kiszűri a fals tőzsdei adatbeviteleket, megakadályozva, hogy a Phoenix Master Oracle hibás kalkulációkat futtasson. Mottó: A borsodi nem hackel, a borsodi optimalizál.  DESCRIPTION (EN):  Git workspace and data integrity checker module. Validates the state of the local Git repo and filters out corrupted market inputs, preventing the Phoenix Master Oracle from running flawed calculations. Motto: The Borsodi doesn't hack, the Borsodi optimizes.  SZERZŐ: Don Mérnök (Tábornok) | BORSODI WAR ROOM |
| `009_router_security_audit.py` | --- |
| `010_crypto_market_analytics.py` | --- |
| `011_trade_risk_manager.py` | --- |
| `012_moving_average_crossover.py` | --- |
| `0130 Honyautospace.py` | --- |
| `0131Autotracker.py` | --- |
| `014_LIVE_PRICE_FEED.py` | LEÍRÁS (HU):Képalapú információ-elrejtő modul (LSB - Least Significant Bit technika).Lehetővé teszi hadi utasítások és bizalmas adatok beágyazását képfájlok pixeladataiba, láthatatlan módon. Bot-biztos operátori csatorna.Mottó: A borsodi nem hackel, a borsodi optimalizál.DESCRIPTION (EN):Image-based data hiding module (LSB - Least Significant Bit technique).Enables embedding sensitive instructions and data into image pixel data invisibly. Bot-proof operator channel.Motto: The Borsodi doesn't hack, the Borsodi optimizes.SZERZŐ: Don Mérnök (Tábornok) | BORSODI WAR ROOM |
| `017_MARKET_DEPTH_ORDERBOOK_ANALYZER.py` | LEÍRÁS (HU):  Piaci ajánlati könyv (Orderbook) mélység-elemző modul. Kiszámítja a vételi és eladási oldali likviditási falak arányát (Imbalance). Segít a Phoenix Master Oracle-nek észlelni, ha a bálnák mesterséges falakkal  próbálják manipulálni a Bitcoin vagy a részvények árfolyamát. Mottó: A borsodi nem hackel, a borsodi optimalizál.  DESCRIPTION (EN):  Market depth and orderbook analyzer module. Calculates the ratio of buy and sell side liquidity walls (Imbalance). Helps the Phoenix Master Oracle detect when whales try to manipulate  the price of Bitcoin or stocks using artificial order walls. Motto: The Borsodi doesn't hack, the Borsodi optimizes.  SZERZŐ: Don Mérnök (Tábornok) | BORSODI WAR ROOM |
| `019_MULTI_ASSET_WATCHLIST_MATRIX.py` | LEÍRÁS (HU):  Többeszközös figyelőlista mátrix modul (Javított, valós piaci árakkal). A Phoenix Master felület élő árfolyam-követő alrendszere.  Biztosítja a Bitcoin pontos, valós alapú ($65k) megjelenítését,  kiszűrve a korábbi hibás fallback értékeket. Mottó: A borsodi nem hackel, a borsodi optimalizál.  DESCRIPTION (EN):  Multi-asset watchlist matrix module (Fixed with real market prices). The live price tracking subsystem of the Phoenix Master interface. Ensures accurate, reality-based ($65k) display for Bitcoin,  filtering out previous faulty fallback values. Motto: The Borsodi doesn't hack, the Borsodi optimizes.  SZERZŐ: Don Mérnök (Tábornok) | BORSODI WAR ROOM |
| `01_infrastructure_milestone_vault.py` | --- |
| `021_steganography_lsb_core.py` | --- |
| `022_network_packet_packetizer.py` | --- |
| `023_system_telemetry_logger.py` | --- |
| `024_secure_symmetric_cipher.py` | --- |
| `025_firewall_rate_limiter.py` | --- |
| `026_file_integrity_monitor.py` | --- |
| `027_dns_exfiltration_detector.py` | --- |
| `028_memory_buffer_overflow_shield.py` | --- |
| `029_secure_env_vault.py` | --- |
| `02_trader_price_predictor.py` | --- |
| `030_log_rotation_policy.py` | --- |
| `031_network_port_knocking.py` | --- |
| `032_hardware_token_authenticator.py` | --- |
| `033_sql_injection_waf_filter.py` | --- |
| `034_ssh_honeypot_node.py` | --- |
| `035_tls_certificate_validator.py` | --- |
| `036_arp_spoof_detector.py` | --- |
| `038_ransomware_canary_file_deployer.py` | --- |
| `039_linux_capabilities_privilege_audit.py` | --- |
| `03_trader_price_predictor.py` | --- |
| `040_secure_session_token_generator.py` | --- |
| `041_shadow_password_hash_auditor.py` | --- |
| `042_cloud_metadata_ssrf_shield.py` | --- |
| `043_host_intrusion_rootkit_hunter.py` | --- |
| `045_zero_trust_api_gateway.py` | --- |
| `046_secure_memory_wipe.py` | --- |
| `047_active_directory_ldap_auditor.py` | --- |
| `048_siem_syslog_forwarder.py` | --- |
| `049_pcap_packet_sniffer.py` | --- |
| `04_android_play_store_ready.py` | --- |
| `050_cloud_iam_privilege_audit.py` | --- |
| `051_data_anonymizer_pipeline.py` | --- |
| `052_secure_time_sync_validator.py` | --- |
| `053_linux_pam_backdoor_hunter.py` | --- |
| `054_steganography_watermark_verifier.py` | --- |
| `055_cloud_kms_key_rotator.py` | --- |
| `057_network_data_exfiltration_limiter.py` | --- |
| `058_windows_registry_tamper_sensor.py` | --- |
| `059_linux_auditd_syslog_analyzer.py` | --- |
| `060_automated_incident_playbook_orchestrator.py` | --- |
| `061_web_parameter_xss_filter.py` | --- |
| `062_windows_active_process_hardener.py` | --- |
| `063_cloud_api_token_leak_scanner.py` | --- |
| `065_cryptographic_file_packer.py` | --- |
| `066_kubernetes_rbac_compliance_auditor.py` | --- |
| `067_linux_kernel_sysctl_hardener.py` | --- |
| `068_web_api_jwt_token_validator.py` | --- |
| `069_docker_security_compliance_auditor.py` | --- |
| `06_brigad_war_room_dashboard.py` | --- |
| `071_felelem_simulalas_anomalia.py` | --- |
| `072_reakcio_teszt_milisecond.py` | --- |
| `073_market_analizator_volatility.py` | --- |
| `074_gyors_strategia_pipeline.py` | --- |
| `075_reakcio_optimalizalo_sandbox.py` | --- |
| `076_bigquery_parquet_archive_roaster.py` | --- |
| `077_shib_engine_load_balancer.py` | --- |
| `078_hardware_resource_throttle_mitigator.py` | --- |
| `082_watchlist_matrix_aggregator.py` | --- |
| `083_infrastructure_janitor.py` | --- |
| `084_risk_position_sizer.py` | --- |
| `087_git_bash_taskkill_hardener.py` | --- |
| `088_sh_script_formatter.py` | --- |
| `089_git_repository_path_resolver.py` | --- |
| `08_pipeline_shutdown_sequence.py` | --- |
| `090_automated_git_push_trigger.py` | --- |
| `091_absolute_path_sanitizer.py` | --- |
| `092_commit_pipeline_auditor.py` | --- |
| `093_automated_autosync_daemon.py` | --- |
| `094_automated_telemetry_test.py` | --- |
| `095_network_socket_keepalive.py` | --- |
| `096_git_remote_url_sanitizer.py` | --- |
| `097_secure_channel_audit.py` | --- |
| `098_git_auto_push_scheduler.py` | --- |
| `099_staging_area_validator.py` | --- |
| `101_ai_command_image_processor.py` | --- |
| `102_terminal_prompt_stabilizer.py` | --- |
| `103_infrastructure_milestone_vault.py` | --- |
| `104_water_polo_pixel_extractor.py` | --- |
| `107_gemini_browser_api_optimizer.py` | --- |
| `117_CYBER_DECEPTION_TELEMETRY_SINK.py` | LEÍRÁS (HU):  Központi csapda-alapú telemetria-gyűjtő modul (Telemetry Sink). Összeköti a kiber-csapdákat (116_cyber_deception_trap) a Phoenix Master naplózóval. Elkapja, strukturált JSON formátumba rendezi és a központi Sentinel logba menti az illetéktelen hálózati mozgásokat és támadási kísérleteket. Mottó: A borsodi nem hackel, a borsodi optimalizál.  DESCRIPTION (EN):  Central deception-based telemetry collection module (Telemetry Sink). Connects cyber deception traps to the Phoenix Master logger. Intercepts, structures into JSON, and saves unauthorized network movements and attack attempts into the central Sentinel log file. Motto: The Borsodi doesn't hack, the Borsodi optimizes.  SZERZŐ: Don Mérnök (Tábornok) | BORSODI WAR ROOM |
| `118_T800_KERNEL_PANIC_INTERCEPT.py` | LEÍRÁS (HU):  Kritikus rendszerhiba és Kernel Panic elhárító modul. Figyeli a Phoenix Master futási környezetét, elkapja a végzetes hardveres  vagy szoftveres kivételeket, és automatikus elhárítási protokollt indít,  megakadályozva a teljes rendszerleállást. Mottó: A borsodi nem hackel, a borsodi optimalizál.  DESCRIPTION (EN):  Critical system failure and Kernel Panic interception module. Monitors the Phoenix Master runtime environment, catches fatal hardware  or software exceptions, and triggers an automated mitigation protocol,  preventing a complete system crash. Motto: The Borsodi doesn't hack, the Borsodi optimizes.  SZERZŐ: Don Mérnök (Tábornok) | BORSODI WAR ROOM |
| `119_SHADOW_STATE_ROLLBACK_MECHANISM.py` | LEÍRÁS (HU):  Árnyék-állapot visszaállítási modul (Rollback Mechanism). Biztosítja a Phoenix Master memóriájának konzisztenciáját. Ha egy tőzsdei vagy  védelmi alrendszer hibás adatot generál, a rendszer azonnal visszaáll egy korábbi,  ellenőrzött és stabil állapot-pillanatképbe (Snapshot). Mottó: A borsodi nem hackel, a borsodi optimalizál.  DESCRIPTION (EN):  Shadow-state rollback mechanism module. Ensures the memory consistency of the Phoenix Master. If a trading or security  subsystem generates corrupted data, the system immediately rolls back to a previous,  verified and stable state snapshot. Motto: The Borsodi doesn't hack, the Borsodi optimizes.  SZERZŐ: Don Mérnök (Tábornok) | BORSODI WAR ROOM |
| `120_ORACLE_PREDICTIVE_CONFIDENCE_SCORER.py` | LEÍRÁS (HU):  Prediktív megbízhatósági szint-értékelő modul (Oracle Confidence Scorer). A Phoenix Master Oracle v5.1 alrendszere. Kiszámítja a generált kereskedési  és biztonsági jelzések matematikai valószínűségét és megbízhatóságát.  Alacsony pontszám esetén blokkolja a végrehajtást. Mottó: A borsodi nem hackel, a borsodi optimalizál.  DESCRIPTION (EN):  Predictive confidence scoring module (Oracle Confidence Scorer). Subsystem of the Phoenix Master Oracle v5.1. Calculates the mathematical probability  and reliability of generated trading and security signals. Blocks execution  in case of low scores. Motto: The Borsodi doesn't hack, the Borsodi optimizes.  SZERZŐ: Don Mérnök (Tábornok) | BORSODI WAR ROOM |
| `121_GIT_TRAFFIC_SIGMA_STABILIZER.py` | LEÍRÁS (HU):  Git forgalom- és szigma-stabilizáló automatizált modul. Megakadályozza a GitHub Traffic statisztikák (Clones, Visitors) visszaesését. Rendszeres, strukturált mikro-frissítéseket generál a háttérben, fenntartva  a repó folyamatos aktivitását és a Phoenix Master Oracle szigma szintjét. Mottó: A borsodi nem hackel, a borsodi optimalizál.  DESCRIPTION (EN):  Automated Git traffic and sigma stabilization module. Prevents drops in GitHub Traffic statistics (Clones, Visitors). Generates regular, structured micro-updates in the background, maintaining continuous repo activity and the Phoenix Master Oracle sigma level. Motto: The Borsodi doesn't hack, the Borsodi optimizes.  SZERZŐ: Don Mérnök (Tábornok) | BORSODI WAR ROOM |
| `122_COIN_SHAKEOUT_ZONE_MONITOR.py` | LEÍRÁS (HU):  COIN (Coinbase) piaci kirázási zóna (Shakeout Zone) monitorozó modul. Észleli a hirtelen likviditási anomáliákat és stop-vadászatokat a tőzsdén. Figyelmeztetést ad ki, ha az árfolyam eléri a kritikus volatilitási sávokat. Mottó: A borsodi nem hackel, a borsodi optimalizál.  DESCRIPTION (EN):  COIN (Coinbase) market shakeout zone monitoring module. Detects sudden liquidity anomalies and stop-hunting behavior on the exchange. Issues alerts when the price hits critical volatility bands. Motto: The Borsodi doesn't hack, the Borsodi optimizes.  SZERZŐ: Don Mérnök (Tábornok) | BORSODI WAR ROOM |
| `123_SPX_INDEX_MACRO_TREND_SYNC.py` | LEÍRÁS (HU):  SPX (S&P 500) index makro-trend szinkronizáló modul (Dinamikus verzió). Manuális adatbekéréssel ellenőrzi a piacvezető index globális irányát. Biztosítja, hogy a Phoenix Master alrendszerei ne kereskedjenek a fő  piaci iránnyal szemben, minimalizálva a rendszerszintű kockázatokat. Mottó: A borsodi nem hackel, a borsodi optimalizál.  DESCRIPTION (EN):  SPX (S&P 500) index macro trend synchronization module (Dynamic version). Verifies the global direction of the market-leading index via manual input. Ensures that Phoenix Master subsystems do not trade against the main market  direction, minimizing systemic risks. Motto: The Borsodi doesn't hack, the Borsodi optimizes.  SZERZŐ: Don Mérnök (Tábornok) | BORSODI WAR ROOM |
| `124_BRIGAD_SECURE_TOKEN_VAULT.py` | LEÍRÁS (HU):  Biztonságos token- és kulcstároló modul (Secure Token Vault). Kezeli, maszkolja és környezeti változókon keresztül elkülöníti a Phoenix  Master Oracle legérzékenyebb API kulcsait és hozzáférési jelszavait. Garantálja, hogy bizalmas adat ne szivárogjon ki a Git kommitok során. Mottó: A borsodi nem hackel, a borsodi optimalizál.  DESCRIPTION (EN):  Secure token and key vault module (Secure Token Vault). Manages, masks, and isolates the most sensitive API keys and passwords of the  Phoenix Master Oracle using environment variables. Guarantees that confidential  data never leaks into Git commits. Motto: The Borsodi doesn't hack, the Borsodi optimizes.  SZERZŐ: Don Mérnök (Tábornok) | BORSODI WAR ROOM |
| `125_brigad_access_authenticator.py` | --- |
| `126_auto_infrastructure_indexer.py` | --- |
| `127_hr_recruiter_telemetry_webhook.py` | --- |
| `129_cyber_amoba_matrix.py` | --- |
| `130 cyber_attack_simulator.py` | --- |
| `131_Perpetual_Search_Launcher_Engine v4.0.py` | --- |
| `132_CRYPTO-JÓS_2500_PRO v1.6.py` | --- |
| `133_sodi_t800_meszaros_szin_v1.8.py` | --- |
| `134_cyber_borsod_navigacios_app_v2.5.py` | --- |
| `135_cyber_borsod_obfuscator_v3.2.py` | --- |
| `136_cyber_borsod_kraken3x_app_v1.5.py` | --- |
| `137_crypto_jos_2500_pro_v1.5.py` | --- |
| `138_crypto_jos_2500_pro_v1.6_hacker.py` | --- |
| `139_RAKOSCSABA_LIVE_MONITOR_v1.0.py` | --- |
| `140_cyber_borsod_incident_simulator_v2.5.py` | --- |
| `141_CYBER_BORSOD_SECURITY_CORE_v2.6_MOBILE.py` | --- |
| `142_cyber_borsod_core_v3.0_borsodi.py` | --- |
| `143_CYBER_BORSOD_MATRIX_LOOP.py` | --- |
| `144_KIBER_BORSODI_LOGIC_BOMB_SIMULATOR_v1.0.py` | --- |
| `145_CYBER_BORSOD_TRAFFIC_AUDIT_v5.8.py` | --- |
| `146_CYBER_BORSOD_CORE_ADMIN_v3.10.py` | --- |
| `147_PORK_PROTOCOL_v4.10_MEGA_MATRIX.py` | --- |
| `148_PORK_PROTOCOL_v3.80_UNIVERSA.py` | --- |
| `148_PORK_PROTOCOL_v3.80_UNIVERSAL.py` | --- |
| `149_T800_STEALTH_CRAWLER_WHISPERER_v2.0.py` | --- |
| `150_CYBER_BORSOD_AI_04_CORE_v3.7.1.py` | --- |
| `151_Cyberdyne_T800_Simulation.py` | --- |
| `152_CYBER_BORSOD_AI_04_CORE_v3.7.1.py` | --- |
| `153_pork_protocol_v3_panel.py` | --- |
| `154_PORK_PROTOCOL_v3_DATA_STREAM.py` | --- |
| `155_KRAKEN_LIVE_CRYPTO_OBFUSCATOR_v4.1.py` | --- |
| `157_PORK_PROTOCOL_v3.6_KRAKEN_DECENTRALIZED.py` | --- |
| `158_PORK_PROTOCOL_v4.0_COMPOUND_SIMULATOR.py` | --- |
| `159_KIBER_BORSODI_LOG_PARSER_MATRIX.py` | --- |
| `160_BORSODI_BRIGAD_STEGANOGRAPHY_LSB.py` | --- |
| `44_container_escape_mitigator.py` | --- |
| `56_kernel_core_dump_shield.py` | --- |
| `64_linux_ssh_audit_hardening.py` | --- |
| `BORSOD RADAR PULSING.py` | --- |
| `Bacon farmer calculator app03.py` | --- |
| `Cyber Borsod Engine Data System.py` | --- |
| `NokiasharePRICEscannerBorsodmoney.py` | --- |
| `ROCK-PAPER-SCISSORS AUTOMATION.py` | --- |
| `cloud-sentinel-core.py` | --- |
| `cyber_sentinel.py` | --- |
| `downloadermultiplikatorbyborsod.py` | --- |
| `generate readme 2.py` | --- |
| `git bash ciber sentinelhez.py` | --- |
| `import os.py` | --- |
| `import tkinter as tk.py` | --- |
| `import tkinter as tk1.py` | --- |
| `import tkinter as tk2.py` | --- |
| `import tkinter as tk4.py` | --- |
| `kergeto .py` | --- |
| `main.py` | --- |
| `majomfa2.py` | --- |
| `majomkergeto sakk rpg.py` | --- |
| `metatelepito.py` | --- |
| `tablasvalami.code-workspace.py` | --- |
