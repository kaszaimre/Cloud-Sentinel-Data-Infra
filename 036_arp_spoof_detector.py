# ==============================================================================
# FÁJL NÉV: 037_brute_force_account_lockout.py
# SORSZÁM: 037
#
# LEÍRÁS ÉS FELADAT:
# Automatikus fiók-zárolási házirend (Account Lockout Policy) modul. Számolja a 
# sikertelen bejelentkezési kísérleteket felhasználónként. Ha a próbálkozások 
# száma eléri a kritikus küszöbértéket, a fiókot biztonsági okokból időalapon 
# zárolja, megakadályozva a szótár- és jelszótalálgatásos (Brute-Force) támadásokat.
# ==============================================================================

import time

class AccountLockoutPolicy:
    def __init__(self, max_attempts=3, lockout_duration_seconds=10):
        self.max_attempts = max_attempts
        self.lockout_duration = lockout_duration_seconds
        self.failed_attempts = {}  # Felhasználó -> Sikertelen próbálkozások száma
        self.lockout_expiry = {}   # Felhasználó -> Zárolás lejárati időbélyege

    def attempt_login(self, username, is_password_correct):
        jelenlegi_ido = time.time()
        
        # Ellenőrizzük, hogy a fiók jelenleg zárolva van-e
        if username in self.lockout_expiry:
            if jelenlegi_ido < self.lockout_expiry[username]:
                hatralevo_ido = int(self.lockout_expiry[username] - jelenlegi_ido)
                print(f"  [❌ LOCKOUT ACTIVE] User '{username}' is BLOCKED. Try again in {hatralevo_ido}s.")
                return False
            else:
                # A zárolási idő letelt, felszabadítjuk a fiókot
                del self.lockout_expiry[username]
                self.failed_attempts[username] = 0

        if is_password_correct:
            print(f"  [🟢 ACCESS GRANTED] Authentication successful for user: '{username}'")
            self.failed_attempts[username] = 0
            return True
        else:
            # Sikertelen próbálkozás növelése
            self.failed_attempts[username] = self.failed_attempts.get(username, 0) + 1
            print(f"  [⚠️ AUTH FAILED] Incorrect credentials for user: '{username}' (Attempt {self.failed_attempts[username]}/{self.max_attempts})")
            
            # Elérte a limitet? Ha igen, zárolás élesítése
            if self.failed_attempts[username] >= self.max_attempts:
                self.lockout_expiry[username] = jelenlegi_ido + self.lockout_duration
                print(f"\n[🚨 LOCKOUT TRIGGERED] User '{username}' has been locked out for {self.lockout_duration} seconds.")
                
            return False

if __name__ == "__main__":
    print("=========================================================")
    print("   CYBER-BORSOD AUTH -> BRUTE-FORCE LOCKOUT POLICY      ")
    print("=========================================================")
    
    policy = AccountLockoutPolicy(max_attempts=3, lockout_duration_seconds=5)
    target_user = "cloud_admin"
    
    # Szimulálunk 3 hibás belépést az automatikus zárolás kiváltásához
    for i in range(3):
        policy.attempt_login(target_user, is_password_correct=False)
        
    print("-" * 57)
    # Negyedik próbálkozás már a blokkoló falba ütközik
    print("[*] Attempting 4th login during active lockout phase...")
    policy.attempt_login(target_user, is_password_correct=True)
    print("=========================================================")
