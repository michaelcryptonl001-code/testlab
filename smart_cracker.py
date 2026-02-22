import os
import time

HASH_FILE = "wallet.hash"

def detect_mode():
    with open(HASH_FILE, "r") as f:
        h = f.readline().strip()

    if h.startswith("$bitcoin$"):
        return 11300
    elif len(h) == 64:
        return 1400  # SHA256
    else:
        return 0  # fallback

def run(cmd):
    print(f"[+] {cmd}")
    os.system(cmd)

def cracked():
    result = os.popen(f"hashcat --show -m {mode} {HASH_FILE}").read()
    return len(result.strip()) > 0

mode = detect_mode()
print(f"[🧠] Detected mode: {mode}")

attacks = [
    f"hashcat -a 0 -m {mode} {HASH_FILE} smart_wordlist.txt --runtime=300",
    f"hashcat -a 0 -m {mode} {HASH_FILE} smart_wordlist.txt -r ultra.rule --runtime=300",
    f"hashcat -a 0 -m {mode} {HASH_FILE} rockyou.txt -r elite_filtered.rule --runtime=600",
    f"hashcat -a 6 -m {mode} {HASH_FILE} smart_wordlist.txt ?d?d?d --runtime=300"
]

for attack in attacks:
    run(attack)
    time.sleep(5)

    if cracked():
        print("[🔥] PASSWORD FOUND!")
        os.system(f"hashcat --show -m {mode} {HASH_FILE}")
        break
    else:
        print("[-] Next attack...\n")