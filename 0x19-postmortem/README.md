Summary : SSH connection issue on my servers
•	Duration: 3-April-2024 to 6-April-2024 UTC+1 WEST Africa
•	Impact: my server still unreachable
•	Root cause: Misconfiguration during the SSH session
Timeline: 
•	Issue has been detected on 5-April-2024
•	I found it by myself
•	I checked the entire SSH access to my whole servers
•	No team/individual the incident escalated to
•	I redo the SSH project to be sure
Root cause and resolution:
•	The moment I realize that I was having issues by tying to access my servers, I’ve decided to redo the project in case to be sure I did not miss anything during the SSH configuration process.
•	I’ve also pushed my private key to GitHub by mistake, I received a warning email from GitGuardians that said, I mistakenly pushed my private key to a public repo. I revoked the key immediately. 

Corrective and preventive measures:
I redo the SSH project, that solve the problem.
Preventive measure:
•	Automate the connection process using bash
•	Automate server’s configuration using a Configuration Management Tools (Puppet)
•	Patched my nginx server to allow only connection from certain ports



