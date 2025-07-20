# Simple Python Port Scanner 🔍

This is a basic port scanner built using Python and the `socket` library. It scans for open ports on a given IP address or domain within a specified range.

## How It Works
- Takes a domain or IP input from the user
- Scans ports between a start and end port
- Prints and saves the results to `results.txt`

## Example Usage

```bash
python scanner.py

Enter the target IP or domain: scanme.nmap.org
Start Port: 20
End Port: 100


[+] Port 22 is OPEN | Service: ssh  
[+] Port 80 is OPEN | Service: http  
