# Week02 - EHE Module 02 Ethical Hacking Fundamentals.pptx
**Module:** ehe
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