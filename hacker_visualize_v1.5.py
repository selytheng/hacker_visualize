import time
import random
import os
import sys

# Elite hacker colors
RED = "\033[31m"
GREEN = "\033[32m"
CYAN = "\033[36m"
YELLOW = "\033[33m"
BOLD = "\033[1m"
RESET = "\033[0m"
GLITCH = "\033[5m"  # Blinking text effect

# Findings list (this will accumulate)
findings = []

# Fake hacking messages (randomly chosen)
supreme_hack_msgs = [
    "Exploit: CVE-2025-1337 - Buffer overflow executed...",
    "Spoofing ARP table... MAC address rerouted.",
    "TCP handshake intercepted - Port 443 compromised...",
    "Brute-forcing SSH keys... 2FA bypassed.",
    "Dumping memory... 0x7FFF stack trace acquired.",
    "Routing traffic through Tor exit node...",
    "SQL injection successful - DB schema extracted...",
    "Enumerating network: 192.168.1.0/24 scanned...",
    "Ransomware payload deployed - Encryption in progress...",
    "[AI WARNING] - Self-replication initiated...",
    "[CRITICAL] - Cyber defense systems disabled...",
]

# Random high-value targets
hacking_targets = [
    "NSA Mainframe",
    "Pentagon Secure Server",
    "Interbank Global Transactions",
    "Satellite Command Uplink",
    "Quantum Computing Core",
    "Government Classified Archives",
    "Bitcoin Wallet Clusters",
    "AI Research Lab",
]

def generate_hacker_code(length):
    """Generate realistic-looking hex or binary data"""
    mode = random.choice(["hex", "binary", "ip"])
    if mode == "hex":
        chars = "0123456789ABCDEF"
        return "0x" + "".join(random.choices(chars, k=length)).lower()
    elif mode == "binary":
        return "".join(random.choices("01", k=length))
    else:  # Fake IP-like strings
        return f"{random.randint(1, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}:{random.randint(1024, 65535)}"

def random_noise():
    """Add glitchy visual noise"""
    return "".join(random.choices("!@#$%^&*()_+-=[]{}|", k=random.randint(5, 15)))

def add_finding():
    """Generate a new finding and add it to the findings list"""
    finding = f"[{time.strftime('%H:%M:%S')}] FOUND: {random.choice(supreme_hack_msgs)}"
    findings.append(finding)

def display_findings():
    """Display persistent findings at the top"""
    print(BOLD + YELLOW + "[SECURITY VULNERABILITIES FOUND]" + RESET)
    for f in findings:
        print(GREEN + f + RESET)

def supreme_hacker_mode():
    """Execute a more realistic supreme hacker sequence"""
    target = random.choice(hacking_targets)  # Choose a hacking target
    os.system("clear" if os.name == "posix" else "cls")
    
    print(BOLD + RED + f"[SYSTEM BREACH DETECTED - TARGET: {target}]" + RESET)
    time.sleep(1.5)

    # Initial attack phase - structured messages
    for _ in range(5):  # Start by generating some findings
        add_finding()
    
    try:
        while True:
            os.system("clear" if os.name == "posix" else "cls")  # Clear screen (except findings)
            
            display_findings()  # Show findings at the top
            print()  # Space before live logs
            
            # Randomly choose how many lines to display (between 20 and 100)
            num_lines = random.randint(20, 100)
            for _ in range(num_lines):  # Generate variable number of log lines
                data_type = random.choice(["code", "status"])
                if data_type == "code":
                    print(GREEN + generate_hacker_code(random.randint(8, 20)) + " " + random_noise() + RESET)
                else:
                    print(CYAN + f"[STATUS] {random.choice(supreme_hack_msgs)}" + RESET)

                sys.stdout.flush()
                time.sleep(random.uniform(0.02, 0.1))

                if random.random() < 0.01:  # Slower rate for adding new findings (1% chance)
                    add_finding()
                    break  # Break early so new finding gets displayed faster
    except KeyboardInterrupt:
        print("\n" + BOLD + RED + "[EMERGENCY SHUTDOWN TRIGGERED]" + RESET)
        time.sleep(1.5)
        print(BOLD + GREEN + "[SYSTEM STABILIZED - AI CORE DORMANT... FOR NOW]" + RESET)

# Run the upgraded hacking script
supreme_hacker_mode()
