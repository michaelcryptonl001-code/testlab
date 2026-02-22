import os
import time

HASH_FILE = "wallet.hash"

attacks = [
    # 1. hızlı saldırı
    "hashcat -a 0 -m 11300 hash.txt smart_wordlist.txt --status --status-timer=10",

    # 2. akıllı rule
    "hashcat -a 0 -m 11300 hash.txt smart_wordlist.txt -r ultra.rule --status --status-timer=10",

    # 3. filtrelenmiş büyük saldırı
    "hashcat -a 0 -m 11300 hash.txt rockyou.txt -r elite_filtered.rule --status --status-timer=10",
]

def check_cracked():
    result = os.popen("hashcat --show -m 11300 hash.txt").read()
    return len(result.strip()) > 0

for attack in attacks:
    print(f"[+] Running: {attack}")
    os.system(attack)

    time.sleep(5)

    if check_cracked():
        print("[🔥] PASSWORD FOUND!")
        break
    else:
        print("[-] Not found, moving to next stage...\n")