# Censys task
This is a record for software test of Censys.

The following is the requirement: 
> Using the Censys API and Python library, implement a script that queries the certificates index and
outputs a CSV of the SHA256 fingerprints and validity start and end dates for all trusted (unexpired)
X.509 certificates associated with the censys.io domain. The query for this is parsed.names:
censys.io and tags: trusted.

This script is made around library censys-python (https://github.com/Censys/censys-python) 

# How to run the code
1. Register on https://censys.io/ to get an account.
2. Follow the instruction of **Getting Start** in https://github.com/Censys/censys-python.
3. Get the code from this github
4. Go to the main directory and run 
```
  python test.py
```
   A CSV file called "result.csv" will appear in the folder, which contains the infomation that is required.
