# EHE Journal

---

## 2026-06-16 22:43 — Week01 - Information Security Fundamentals.pptx
**Style:** structured_academic (experimenting)

Here's a structured academic summary of the provided content on **Information Security Fundamentals**:

---

### **Term: Information Security**  
**Definition**: A state of well-being of information and infrastructure where the risk of theft, tampering, or disruption is low or tolerable.  
**Formula**: Not applicable.  
**Example**: Protecting corporate financial data from unauthorized access to prevent breaches.  

---

### **Term: Elements of Information Security**  
**Definition**: Core principles ensuring information protection:  
1. **Confidentiality**: Data accessible only to authorized users.  
2. **Integrity**: Trustworthiness of data (preventing unauthorized changes).  
3. **Availability**: Systems accessible when needed by authorized users.  
4. **Authenticity**: Guarantee of data genuineness.  
5. **Non-Repudiation**: Proof of data origin/receipt (e.g., digital signatures).  
**Formula**: CIA Triad (Confidentiality, Integrity, Availability).  
**Example**: Encryption ensures confidentiality, while access logs support non-repudiation.  

---

### **Term: Security, Functionality, and Usability Triangle**  
**Definition**: A balance between three components:  
- **Security (Restrictions)**: Strength of safeguards.  
- **Functionality (Features)**: System capabilities.  
- **Usability (GUI)**: User interface simplicity.  
**Formula**: Security ↑ → Functionality/Usability ↓ (trade-off relationship).  
**Example**: Strict multi-factor authentication improves security but reduces usability.  

---

### **Term: Classification of Attacks**  
**Definition**: Types of attacks based on methodology:  
1. **Passive Attacks**: Monitor data without alteration (e.g., eavesdropping).  
2. **Active Attacks**: Modify or disrupt data (e.g., DoS attacks).  
3. **Close-in Attacks**: Physical proximity exploits (e.g., shoulder surfing).  
4. **Insider Attacks**: Authorized users misusing access (e.g., data theft).  
5. **Distribution Attacks**: Tampering with hardware/software pre-installation.  
**Formula**: Not applicable.  
**Example**: SQL injection is an active attack; phishing is a close-in attack.  

---

### **Term: Information Security Attack Vectors**  
**Definition**: Pathways for exploiting vulnerabilities:  
1. **Cloud Computing Threats**: Multi-tenant data breaches.  
2. **Advanced Persistent Threats (APTs)**: Stealthy, long-term breaches.  
3. **Ransomware**: Data encryption for extortion.  
4. **Botnets**: Networked compromised devices.  
5. **IoT Threats**: Exploiting insecure smart devices.  
**Formula**: Not applicable.  
**Example**: WannaCry ransomware exploited SMB vulnerabilities globally.  

---

### **Term: Information Security Laws and Regulations**  
**Definition**: Legal frameworks for data protection:  
1. **PCI DSS**: Secure handling of payment card data.  
2. **ISO/IEC 27001**: Information Security Management System (ISMS) standards.  
3. **HIPAA**: Protection of healthcare data in the U.S.  
4. **SOX**: Corporate financial reporting integrity.  
5. **GDPR**: EU data privacy and protection.  
6. **DPA 2018**: UK data processing regulations.  
**Formula**: Not applicable.  
**Example**: GDPR fines up to 4% of global revenue for non-compliance.  

---

### **Term: Security Challenges**  
**Definition**: Key obstacles in implementing security:  
1. Regulatory compliance.  
2. Cybersecurity skill shortages.  
3. Distributed system vulnerabilities.  
4. BYOD policy risks.  
5. Cloud migration misconfigurations.  
**Formula**: Not applicable.  
**Example**: Unpatched legacy systems in cloud environments.  

---

### **Term: Motives for Information Security Attacks**  
**Definition**: Drivers behind attacks:  
1. Financial gain (e.g., theft).  
2. Disruption of services.  
3. Reputation damage.  
4. Espionage or political motives.  
**Formula**: Attack = Motive + Method + Vulnerability.  
**Example**: Ransomware attacks on hospitals for quick financial payouts.  

---

### **Linked Concepts**  
- [[Ethical Hacking]]  
- [[Cybersecurity]]  
- [[Data Protection]]  
- [[Network Security]]  

This summary integrates definitions, relationships, and practical examples to align with polytechnic students' academic needs.

---

---

## 2026-06-16 22:46 — Week02 - EHE Module 02 Ethical Hacking Fundamentals.pptx
**Style:** structured_academic (experimenting)

# Summary: Ethical Hacking Essentials (Module 02)

## **Cyber Kill Chain Methodology**  
**Definition**: A framework for understanding and disrupting adversarial attacks by mapping their tactics, techniques, and procedures (TTPs).  
**Formula**: N/A  
**Example**: Identifying phases like reconnaissance, weaponization, and command/control to prevent breaches.  

## **Tactics, Techniques, and Procedures (TTPs)**  
**Definition**: Patterns of behavior and methods used by threat actors to execute attacks.  
**Formula**: N/A  
**Example**: Use of PowerShell for adversary behavioral identification or DNS tunneling for data exfiltration.  

## **Indicators of Compromise (IoCs)**  
**Definition**: Artifacts or data points indicating potential malicious activity in a network or system.  
**Formula**: N/A  
**Categories**:  
- **Behavioral**: PowerShell script execution.  
- **Email**: Malicious attachments or sender addresses.  
- **Network**: Suspicious IPs or URLs.  
- **Host-Based**: File hashes, registry keys.  
**Example**: A sudden spike in unknown IP connections flagged by network monitoring tools.  

## **Hacking**  
**Definition**: Exploiting vulnerabilities to gain unauthorized access to systems or modify them beyond intended purposes.  
**Formula**: N/A  
**Example**: Using SQL injection to bypass authentication mechanisms.  

## **Hacker Classes/Threat Actors**  
### **Black Hat**  
**Definition**: Malicious hackers who exploit systems for personal gain or disruption.  
**Example**: Ransomware attackers encrypting data for extortion.  

### **White Hat**  
**Definition**: Ethical hackers who identify vulnerabilities to improve security.  
**Example**: Penetration testers conducting authorized security audits.  

### **Gray Hat**  
**Definition**: Hackers who operate between legal and illegal activities.  
**Example**: Disclosing vulnerabilities to an organization without permission.  

### **Script Kiddie**  
**Definition**: Inexperienced hackers using pre-built tools for attacks.  
**Example**: Running automated DDoS scripts downloaded from the dark web.  

## **Phases of Hacking Cycle**  
### **1. Reconnaissance**  
**Definition**: Gathering information about a target before an attack.  
**Types**:  
- **Passive**: Searching public records.  
- **Active**: Direct interaction (e.g., port scanning).  
**Example**: Using Google Hacking Techniques to find exposed sensitive data.  

### **2. Scanning**  
**Definition**: Probing the target network/system for vulnerabilities.  
**Tools**: Nmap, Unicornscan.  
**Example**: Identifying open ports and OS versions via Nmap scans.  

### **3. Gaining Access**  
**Definition**: Exploiting vulnerabilities to compromise the system.  
**Methods**: Password cracking, buffer overflows.  
**Example**: Exploiting a weak password via brute-force attacks.  

### **4. Maintaining Access**  
**Definition**: Ensuring persistent access to the compromised system.  
**Techniques**: Installing backdoors or rootkits.  
**Example**: Using a web shell to retain remote control.  

### **5. Clearing Tracks**  
**Definition**: Erasing evidence of the attack to avoid detection.  
**Methods**: Modifying logs, deleting footprints.  
**Example**: Overwriting server logs to hide unauthorized access.  

## **Ethical Hacking**  
**Definition**: Authorized simulation of cyberattacks to identify and remediate vulnerabilities.  
**Scope**:  
- Identifying risks.  
- Compliance with security standards.  
**Limitations**:  
- Requires organizational buy-in.  
- Cannot guarantee 100% security.  
**Example**: Conducting a vulnerability scan with tools like Metasploit.  

## **Skills of an Ethical Hacker**  
**Technical**:  
- Mastery of OS (Windows, Linux), networking, and security tools.  
**Non-Technical**:  
- Problem-solving, communication, and adherence to laws.  
**Example**: An ethical hacker using Wireshark to analyze network traffic for anomalies.  

## **Ethical Hacking Tools**  
### **Reconnaissance**  
- **Google Hacking**: Advanced search operators (e.g., `filetype:pdf`).  
- **Web Data Extractor**: Scraping contact information from websites.  

### **Scanning**  
- **Nmap**: Port and service discovery.  
- **Hping3**: TCP/IP stack testing.  

### **Enumeration**  
- **Nbtstat**: NetBIOS name resolution.  
- **Advanced IP Scanner**: Discovering devices on a network.  

---

**[[Cyber Kill Chain Methodology]]** | **[[Indicators of Compromise (IoCs)]]** | **[[Ethical Hacking]]**  
**[[Hacker Classes]]** | **[[Phases of Hacking Cycle]]** | **[[Ethical Hacking Tools]]**

---

---

## 2026-06-17 15:09 — Week01 - Information Security Fundamentals.pptx
**Style:** structured_academic (experimenting)

# Summary: Information Security Fundamentals (Module 01)  

## **Term: Information Security**  
**Definition**: A state of well-being where the risk of theft, tampering, or disruption of information and infrastructure is low or tolerable.  
**Formula**: Not applicable.  
**Example**: Securing customer databases to prevent unauthorized access.  
**Linked Concepts**: [[Cybersecurity]], [[Data Protection]]  

---

## **Term: Elements of Information Security**  
**Definition**: Core principles ensuring information protection:  
1. **Confidentiality**: Access restricted to authorized users.  
2. **Integrity**: Prevention of unauthorized data alterations.  
3. **Availability**: Systems accessible when needed.  
4. **Authenticity**: Guarantee of data genuineness.  
5. **Non-Repudiation**: Proof of data origin/receipt (e.g., digital signatures).  
**Formula**: CIA Triad (Confidentiality, Integrity, Availability).  
**Example**: Encryption ensures confidentiality; access logs support non-repudiation.  
**Linked Concepts**: [[Information Security]]  

---

## **Term: Security, Functionality, and Usability Triangle**  
**Definition**: A balance between three components:  
- **Security (Restrictions)**: Strength of safeguards.  
- **Functionality (Features)**: System capabilities.  
- **Usability (GUI)**: User interface simplicity.  
**Formula**: Security ↑ → Functionality/Usability ↓ (trade-off).  
**Example**: Multi-factor authentication improves security but complicates usability.  
**Linked Concepts**: [[Information Security]]  

---

## **Term: Security Challenges**  
**Definition**: Key obstacles in implementing security:  
1. Regulatory compliance.  
2. Cybersecurity skill shortages.  
3. Distributed system vulnerabilities.  
4. BYOD policy risks.  
5. Cloud migration misconfigurations.  
**Formula**: Not applicable.  
**Example**: Unpatched legacy systems in cloud environments.  
**Linked Concepts**: [[Cybersecurity]]  

---

## **Term: Motives for Information Security Attacks**  
**Definition**: Drivers behind attacks:  
1. Financial gain.  
2. Disruption of services.  
3. Reputation damage.  
4. Espionage/political motives.  
**Formula**: Attack = Motive + Method + Vulnerability.  
**Example**: Ransomware attacks on hospitals for financial payouts.  
**Linked Concepts**: [[Ethical Hacking]]  

---

## **Term: Classification of Attacks**  
**Definition**: Types of attacks based on methodology:  
1. **Passive Attacks**: Monitoring without alteration (e.g., eavesdropping).  
2. **Active Attacks**: Data modification/disruption (e.g., DoS).  
3. **Close-in Attacks**: Physical proximity exploits (e.g., shoulder surfing).  
4. **Insider Attacks**: Misuse by authorized users.  
5. **Distribution Attacks**: Tampering pre-installation.  
**Formula**: Not applicable.  
**Example**: SQL injection (active); phishing (close-in).  
**Linked Concepts**: [[Ethical Hacking]]  

---

## **Term: Information Security Attack Vectors**  
**Definition**: Pathways for exploiting vulnerabilities:  
1. **Cloud Computing Threats**: Multi-tenant breaches.  
2. **Advanced Persistent Threats (APTs)**: Stealthy breaches.  
3. **Ransomware**: Data encryption for extortion.  
4. **Botnets**: Networked compromised devices.  
5. **IoT Threats**: Exploiting insecure devices.  
**Formula**: Not applicable.  
**Example**: WannaCry ransomware exploiting SMB vulnerabilities.  
**Linked Concepts**: [[Cybersecurity]]  

---

## **Term: Payment Card Industry Data Security Standard (PCI DSS)**  
**Definition**: A standard for organizations handling cardholder data to prevent fraud.  
**Formula**: Not applicable.  
**Example**: Merchants securing payment systems to meet PCI DSS compliance.  
**Linked Concepts**: [[Data Protection]]  

---

## **Term: ISO/IEC 27001:2013**  
**Definition**: Standard for an Information Security Management System (ISMS).  
**Formula**: Not applicable.  
**Example**: Organizations implementing ISO 27001 for risk management.  
**Linked Concepts**: [[Information Security]]  

---

## **Term: Health Insurance Portability and Accountability Act (HIPAA)**  
**Definition**: U.S. law protecting sensitive healthcare data.  
**Formula**: Not applicable.  
**Example**: Healthcare providers encrypting patient records to comply with HIPAA.  
**Linked Concepts**: [[Data Protection]]  

---

## **Term: Sarbanes-Oxley Act (SOX)**  
**Definition**: U.S. law ensuring corporate financial reporting integrity.  
**Formula**: Not applicable.  
**Example**: CEOs certifying financial reports to adhere to SOX.  
**Linked Concepts**: [[Cybersecurity]]  

---

## **Term: General Data Protection Regulation (GDPR)**  
**Definition**: EU law regulating data privacy and protection.  
**Formula**: Not applicable.  
**Example**: Companies facing fines for GDPR non-compliance.  
**Linked Concepts**: [[Data Protection]]  

---

## **Term: Data Protection Act 2018 (DPA)**  
**Definition**: UK law regulating personal data processing.  
**Formula**: Not applicable.  
**Example**: Organizations obtaining consent for data collection under DPA.  
**Linked Concepts**: [[Data Protection]]  

---

## **Linked Concepts**  
- [[Ethical Hacking]]  
- [[Cybersecurity]]  
- [[Data Protection]]  
- [[Network Security]]  

This summary aligns with polytechnic students' needs by integrating foundational concepts, real-world examples, and regulatory frameworks in information security.

---

---

## 2026-06-17 15:12 — Week02 - EHE Module 02 Ethical Hacking Fundamentals.pptx
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

---

