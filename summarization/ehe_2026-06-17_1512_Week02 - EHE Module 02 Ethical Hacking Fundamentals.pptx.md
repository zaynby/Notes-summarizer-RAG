# Week02 - EHE Module 02 Ethical Hacking Fundamentals.pptx
**Module:** ehe
**Style:** structured_academic (experimenting)

Here’s a structured summary of **Module 02: Ethical Hacking Fundamentals** using the required academic format:

---

### [[Cyber Kill Chain Methodology]]
**Definition**: A framework for understanding and disrupting the lifecycle of cyber attacks, categorizing attacker actions into stages to enable proactive defense.
**Formula**: N/A
**Example**: Identifying reconnaissance activities to block initial attacker reconnaissance.

---

### [[Tactics, Techniques, and Procedures (TTPs)]]
**Definition**: Patterns of behaviors, methods, and actions used by threat actors to execute attacks.
**Formula**: N/A
**Example**: APT groups using phishing emails with malicious attachments to gain access.

---

### [[Indicators of Compromise (IoCs)]]
**Definition**: Forensic data artifacts indicating potential malicious activity in a network or system.
**Formula**: N/A
**Example**: 
- **Behavioral**: Unusual PowerShell script execution.
- **Email**: Suspicious sender domain (e.g., `admin@yourcompany-support.com`).
- **Network**: Unexpected outbound traffic to a known C2 server IP.
- **Host-Based**: Presence of a malicious file hash (e.g., `MD5: 5f4dcc3b5aa765d61d8327deb882cf99`).

---

### [[Hacking]]
**Definition**: The act of exploiting system vulnerabilities to gain unauthorized access or alter system behavior.
**Formula**: N/A
**Example**: Exploiting a buffer overflow vulnerability in a web server to execute arbitrary code.

---

### [[Hacker Classes/Threat Actors]]
**Definition**: Categories of individuals or groups based on their motivations and methods.
**Formula**: N/A
**Examples**:
- **Black Hats**: Malicious actors (e.g., ransomware developers).
- **White Hats**: Ethical hackers (e.g., penetration testers).
- **Gray Hats**: Mixed motivations (e.g., disclosing vulnerabilities without permission).
- **Script Kiddies**: Use pre-built tools for attacks (e.g., DDoS attacks via LOIC).
- **Cyber Terrorists**: Target critical infrastructure (e.g., Stuxnet).

---

### [[Reconnaissance]]
**Definition**: The initial phase of gathering information about a target before an attack.
**Types**:
1. **Passive Reconnaissance**: Non-intrusive data collection (e.g., searching public records).
2. **Active Reconnaissance**: Direct interaction with the target (e.g., port scanning).
**Formula**: N/A
**Example**: Using `theHarvester` to collect email addresses and subdomains.

---

### [[Scanning Phase]]
**Definition**: Proactive exploration of a target network to identify vulnerabilities.
**Tools**: Nmap, Unicornscan, Hping3.
**Example**: `nmap -sV 192.168.1.1` to identify open ports and service versions.

---

### [[Gaining Access]]
**Definition**: Exploiting vulnerabilities to compromise a system.
**Methods**: Password cracking, buffer overflows, session hijacking.
**Example**: Using `Metasploit` to exploit a CVE-2021-44228 (Log4Shell) vulnerability.

---

### [[Maintaining Access]]
**Definition**: Ensuring persistent access to a compromised system.
**Techniques**: Backdoors, rootkits, Trojans.
**Example**: Installing a reverse shell to retain remote access.

---

### [[Clearing Tracks]]
**Definition**: Actions taken by attackers to erase evidence of their presence.
**Methods**: Log deletion, timestamp manipulation.
**Example**: Using `rm -rf /var/log/auth.log` to remove login records.

---

### [[Ethical Hacking]]
**Definition**: Authorized hacking to identify and remediate vulnerabilities.
**Scope**: 
- Simulating attacks to test defenses.
- Compliance with legal standards (e.g., GDPR).
**Limitations**: 
- Requires explicit permission.
- Cannot guarantee 100% security.
**Example**: Conducting a penetration test to exploit a misconfigured AWS S3 bucket.

---

### [[Ethical Hacking Tools]]
**Definition**: Software used to simulate attacks and assess security.
**Examples**:
- **Reconnaissance**: Google Dorks, Shodan.
- **Scanning**: Nmap, Nessus.
- **Enumeration**: Nbtstat, NetBIOS Enumerator.
- **Exploitation**: Metasploit, SQLmap.

---

### [[Skills of an Ethical Hacker]]
**Technical Skills**:
- Proficiency in OS (Windows, Linux), networking, and scripting (Python, Bash).
- Knowledge of security tools (Wireshark, Burp Suite).
**Non-Technical Skills**:
- Problem-solving, communication, and adherence to ethics/legal standards.
**Example**: Writing a Python script to automate vulnerability reporting.

---

### [[Google Hacking]]
**Definition**: Using advanced search operators to uncover sensitive information.
**Example**: `intitle:"Index of" /wp-content/uploads` to find exposed WordPress files.

---

This summary connects concepts like [[Ethical Hacking]] to [[Hacking]] and tools like [[Nmap]] to [[Scanning Phase]], enabling cross-referencing in further studies.