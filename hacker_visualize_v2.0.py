import time
import random
import os
import sys
import threading
import platform

# Elite hacker colors
RED = "\033[31m"
GREEN = "\033[32m"
CYAN = "\033[36m"
YELLOW = "\033[33m"
MAGENTA = "\033[35m"
BLUE = "\033[34m"
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
    "Kernel exploited - root privileges escalated",
    "Zero-day vulnerability discovered in target system",
    "Firewall rules bypassed via packet fragmentation",
    "Authentication tokens exfiltrated from memory",
    "Keylogger installed - command & control established",
    "Data encryption keys compromised - full access granted",
    "BIOS firmware modified - persistence achieved",
    "Satellite uplink compromised - redirecting signals",
    "Neural network backdoor implanted - AI subjugated"
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
    "Global Power Grid Systems",
    "International Space Station",
    "Nuclear Launch Control Systems",
    "Cryptocurrency Exchange",
    "Intelligence Agency Database",
    "Corporate R&D Servers",
    "Military Drone Network",
    "Facial Recognition Database"
]

# Progress bar characters
PROGRESS_CHARS = ["[□□□□□□□□□□]", "[■□□□□□□□□□]", "[■■□□□□□□□□]", "[■■■□□□□□□□]", 
                 "[■■■■□□□□□□]", "[■■■■■□□□□□]", "[■■■■■■□□□□]", 
                 "[■■■■■■■□□□]", "[■■■■■■■■□□]", "[■■■■■■■■■□]", "[■■■■■■■■■■]"]

# Access denied (needs retry) messages
ACCESS_DENIED_MSGS = [
    "ACCESS DENIED: Security protocol active",
    "INTRUSION DETECTED: Countermeasures engaged",
    "AUTHENTICATION FAILURE: Recalibrating attack vectors",
    "FIREWALL BLOCKED: Attempting bypass technique"
]

def progress_bar(duration, task_name):
    """Display a progress bar for a task"""
    print(f"{CYAN}[TASK] {task_name}{RESET}")
    for i in range(len(PROGRESS_CHARS)):
        sys.stdout.write("\r" + YELLOW + PROGRESS_CHARS[i] + RESET + f" {random.randint(i*10, i*10+9)}%")
        sys.stdout.flush()
        time.sleep(duration / len(PROGRESS_CHARS))
    sys.stdout.write("\r" + GREEN + PROGRESS_CHARS[-1] + RESET + " 100% - COMPLETE\n")
    
def generate_hacker_code(length):
    """Generate realistic-looking hex or binary data"""
    mode = random.choice(["hex", "binary", "ip", "hash"])
    if mode == "hex":
        chars = "0123456789ABCDEF"
        return "0x" + "".join(random.choices(chars, k=length)).lower()
    elif mode == "binary":
        return "".join(random.choices("01", k=length))
    elif mode == "hash":
        chars = "0123456789abcdef"
        return "".join(random.choices(chars, k=64))  # SHA-256 style hash
    else:  # Fake IP-like strings
        return f"{random.randint(1, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}:{random.randint(1024, 65535)}"

def random_noise():
    """Add glitchy visual noise"""
    return "".join(random.choices("!@#$%^&*()_+-=[]{}|", k=random.randint(5, 15)))

def add_finding():
    """Generate a new finding and add it to the findings list"""
    finding = f"[{time.strftime('%H:%M:%S')}] FOUND: {random.choice(supreme_hack_msgs)}"
    findings.append(finding)
    
    # Keep only the last 8 findings to avoid cluttering the screen
    if len(findings) > 8:
        findings.pop(0)

def display_findings():
    """Display persistent findings at the top"""
    print(BOLD + YELLOW + "[SECURITY VULNERABILITIES FOUND]" + RESET)
    for f in findings:
        print(GREEN + f + RESET)

def display_matrix_rain(duration=3):
    """Display Matrix-like digital rain for a short duration"""
    chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()_+-=[];',./{}|:<>?"
    width = os.get_terminal_size().columns
    end_time = time.time() + duration
    
    print(BOLD + RED + "[NEURAL INTERFACE ACTIVATED]" + RESET)
    time.sleep(0.5)
    
    while time.time() < end_time:
        # Generate a line of matrix rain
        line = ""
        for _ in range(width):
            if random.random() < 0.04:  # Empty space probability
                line += " "
            else:
                line += GREEN + random.choice(chars) + RESET
        print(line)
        time.sleep(0.05)

def simulate_breach_attempts(target):
    """Simulate multiple breach attempts with failures and retries"""
    print(BOLD + YELLOW + f"[TARGETING {target.upper()}]" + RESET)
    time.sleep(1)
    
    attempts = random.randint(2, 5)
    for i in range(attempts):
        print(CYAN + f"[ATTEMPT {i+1}] Deploying exploit vector..." + RESET)
        time.sleep(0.8)
        
        if i < attempts - 1:  # All but last attempt fail
            print(RED + random.choice(ACCESS_DENIED_MSGS) + RESET)
            time.sleep(0.5)
            print(YELLOW + "Recalibrating attack parameters..." + RESET)
            progress_bar(2, "Adjusting exploit payload")
        else:
            print(GREEN + "[SUCCESS] Defense systems compromised" + RESET)
            add_finding()

def display_system_info():
    """Display fake system information about the "target" system"""
    os_types = ["Linux Kernel 6.1.52", "Windows Server 2022", "FreeBSD 14.0", "AIX 7.3", "macOS 15.1"]
    cpu_types = ["Intel Xeon E7-8894 v4", "AMD EPYC 9654", "IBM POWER10", "Fujitsu A64FX", "ARM Neoverse N2"]
    
    print(BOLD + BLUE + "[TARGET SYSTEM INFORMATION]" + RESET)
    print(YELLOW + f"OS: {random.choice(os_types)}" + RESET)
    print(YELLOW + f"CPU: {random.choice(cpu_types)} @ {random.randint(2, 5)}.{random.randint(0, 9)} GHz" + RESET)
    print(YELLOW + f"Memory: {random.randint(32, 1024)} GB DDR5" + RESET)
    print(YELLOW + f"Network: {random.randint(1, 100)} Gbps Fiber Optic" + RESET)
    print(YELLOW + f"Security Level: {random.choice(['MAXIMUM', 'CLASSIFIED', 'RESTRICTED', 'TOP SECRET'])}" + RESET)

def run_decryption_animation(filename="encrypted_data.bin"):
    """Run a fake decryption animation"""
    total_bytes = random.randint(50000, 500000)
    print(BOLD + CYAN + f"[DECRYPTING {filename}]" + RESET)
    print(YELLOW + f"File size: {total_bytes} bytes" + RESET)
    print(YELLOW + f"Encryption: AES-256-GCM" + RESET)
    
    # Display decryption progress
    decrypted = 0
    chunks = random.randint(5, 15)
    for _ in range(chunks):
        chunk_size = total_bytes // chunks
        decrypted += chunk_size
        percentage = min(100, int(decrypted / total_bytes * 100))
        
        bar_length = 40
        filled_length = int(bar_length * percentage / 100)
        bar = '█' * filled_length + '░' * (bar_length - filled_length)
        
        sys.stdout.write(f"\r{GREEN}[{bar}] {percentage}% ({decrypted}/{total_bytes} bytes){RESET}")
        sys.stdout.flush()
        time.sleep(random.uniform(0.1, 0.5))
    
    print("\n" + GREEN + "[DECRYPTION COMPLETE]" + RESET)
    time.sleep(0.5)

def interactive_typing(text, delay=0.05):
    """Display text as if being typed in real-time"""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def fake_data_exfiltration():
    """Simulate data exfiltration with specific file types"""
    file_types = [
        "personnel_records.xlsx", 
        "financial_projections_2025.pdf",
        "classified_research.docx",
        "encryption_keys.pem",
        "passwords.kdbx",
        "satellite_control_protocols.bin",
        "database_backup.sql",
        "executive_emails.pst"
    ]
    
    print(BOLD + RED + "[DATA EXFILTRATION INITIATED]" + RESET)
    for _ in range(random.randint(3, 8)):
        file = random.choice(file_types)
        size = f"{random.randint(1, 999)}{random.choice(['KB', 'MB'])}"
        progress_bar(random.uniform(0.5, 2.0), f"Extracting {file} ({size})")
        
    stolen_files = random.randint(10, 100)
    stolen_data = random.randint(1, 50)
    print(GREEN + f"[COMPLETE] Exfiltrated {stolen_files} files ({stolen_data} GB)" + RESET)
    add_finding()

def background_effect_thread():
    """Run a separate thread to create periodic visual effects"""
    while True:
        time.sleep(random.uniform(3, 8))
        
        # Print a random glitch effect that doesn't disrupt the main output too much
        effect = random.choice([
            f"\r{GLITCH}{BOLD}{random.choice([RED, YELLOW, CYAN])}{random_noise()}{RESET}",
            f"\r{BOLD}{RED}[ALERT] Network traffic spike detected{RESET}",
            f"\r{BOLD}{YELLOW}[SYSTEM] Memory buffer at {random.randint(60, 99)}%{RESET}",
        ])
        
        sys.stdout.write(effect)
        sys.stdout.flush()
        time.sleep(0.3)
        sys.stdout.write("\r" + " " * (len(effect) - len(RESET) * effect.count(RESET)) + "\r")
        sys.stdout.flush()

def supreme_hacker_mode():
    """Execute a more cinematic supreme hacker sequence"""
    target = random.choice(hacking_targets)  # Choose a hacking target
    
    # Clear screen
    os.system("clear" if os.name == "posix" else "cls")
    
    # Initial "access" sequence
    interactive_typing(BOLD + GREEN + "INITIATING SUPREME HACKER MODE v2.0..." + RESET, 0.03)
    time.sleep(1)
    
    # Start the background effects thread
    effect_thread = threading.Thread(target=background_effect_thread, daemon=True)
    effect_thread.start()
    
    # Matrix-style animation for dramatic effect
    display_matrix_rain(3)
    
    # Display initial targeting
    os.system("clear" if os.name == "posix" else "cls")
    print(BOLD + RED + f"[SYSTEM BREACH INITIATED - TARGET: {target}]" + RESET)
    time.sleep(1.5)
    
    # Display fake system info
    display_system_info()
    time.sleep(2)
    
    # Simulate breach attempts
    simulate_breach_attempts(target)
    
    # Initial attack phase - structured messages
    for _ in range(3):  # Start by generating some findings
        add_finding()
    
    try:
        # Main loop with more structure and cinematic elements
        while True:
            os.system("clear" if os.name == "posix" else "cls")  # Clear screen (except findings)
            
            display_findings()  # Show findings at the top
            print()  # Space before live logs
            
            # Choose a dramatic effect to show occasionally
            if random.random() < 0.2:  # 20% chance each cycle
                effect = random.choice([
                    "decryption",
                    "data_exfiltration",
                    "progress_bar",
                ])
                
                if effect == "decryption":
                    run_decryption_animation(f"{random.choice(['secure', 'classified', 'encrypted'])}_data_{random.randint(1, 999)}.bin")
                elif effect == "data_exfiltration":
                    fake_data_exfiltration()
                elif effect == "progress_bar":
                    tasks = [
                        "Bypassing firewall protocols",
                        "Installing rootkit in memory",
                        "Extracting encryption keys",
                        "Deploying polymorphic malware",
                        "Compromising authentication server"
                    ]
                    progress_bar(random.uniform(1, 3), random.choice(tasks))
            
            # Randomly choose how many lines to display (between 20 and 80)
            num_lines = random.randint(20, 80)
            for _ in range(num_lines):  # Generate variable number of log lines
                data_type = random.choice(["code", "status", "code", "code"])  # More code than status
                if data_type == "code":
                    color = random.choice([GREEN, CYAN, MAGENTA])  # Randomize code colors
                    print(color + generate_hacker_code(random.randint(8, 30)) + " " + random_noise() + RESET)
                else:
                    print(CYAN + f"[STATUS] {random.choice(supreme_hack_msgs)}" + RESET)

                sys.stdout.flush()
                time.sleep(random.uniform(0.01, 0.08))  # Slightly faster scrolling

                if random.random() < 0.01:  # Slower rate for adding new findings (1% chance)
                    add_finding()
                    break  # Break early so new finding gets displayed faster
    except KeyboardInterrupt:
        print("\n" + BOLD + RED + "[EMERGENCY SHUTDOWN TRIGGERED]" + RESET)
        time.sleep(0.5)
        
        # More dramatic shutdown sequence
        print(YELLOW + "[SYSTEM] Disconnecting network interfaces..." + RESET)
        time.sleep(0.3)
        print(YELLOW + "[SYSTEM] Erasing memory footprints..." + RESET)
        time.sleep(0.3)
        print(YELLOW + "[SYSTEM] Removing backdoor access..." + RESET)
        time.sleep(0.3)
        
        # Final message
        print(BOLD + GREEN + "[SYSTEM STABILIZED - AI CORE DORMANT... FOR NOW]" + RESET)
        
        # Add IP looking addresses as a final touch
        for _ in range(3):
            print(BLUE + f"Connection terminated: {generate_hacker_code(15)}" + RESET)
            time.sleep(0.2)

# Run the upgraded hacking script
if __name__ == "__main__":
    # Display a cool startup banner
    banner = """
    ███████╗██╗   ██╗██████╗ ██████╗ ███████╗███╗   ███╗███████╗    
    ██╔════╝██║   ██║██╔══██╗██╔══██╗██╔════╝████╗ ████║██╔════╝    
    ███████╗██║   ██║██████╔╝██████╔╝█████╗  ██╔████╔██║█████╗      
    ╚════██║██║   ██║██╔═══╝ ██╔══██╗██╔══╝  ██║╚██╔╝██║██╔══╝      
    ███████║╚██████╔╝██║     ██║  ██║███████╗██║ ╚═╝ ██║███████╗    
    ╚══════╝ ╚═════╝ ╚═╝     ╚═╝  ╚═╝╚══════╝╚═╝     ╚═╝╚══════╝    
    ██╗  ██╗ █████╗  ██████╗██╗  ██╗███████╗██████╗     ██╗   ██╗██████╗    
    ██║  ██║██╔══██╗██╔════╝██║ ██╔╝██╔════╝██╔══██╗    ██║   ██║╚════██╗   
    ███████║███████║██║     █████╔╝ █████╗  ██████╔╝    ██║   ██║ █████╔╝   
    ██╔══██║██╔══██║██║     ██╔═██╗ ██╔══╝  ██╔══██╗    ╚██╗ ██╔╝██╔═══╝    
    ██║  ██║██║  ██║╚██████╗██║  ██╗███████╗██║  ██║     ╚████╔╝ ███████╗   
    ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝      ╚═══╝  ╚══════╝   
    """
    
    print(GREEN + banner + RESET)
    print(BOLD + YELLOW + "[PRESS CTRL+C AT ANY TIME TO ABORT THE MISSION]" + RESET)
    time.sleep(2)
    
    supreme_hacker_mode()
