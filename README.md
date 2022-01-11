# Censys--test
This is a record for software test of Censys.

The following is the requirement: 
> Using the Censys API and Python library, implement a script that queries the certificates index and
outputs a CSV of the SHA256 fingerprints and validity start and end dates for all trusted (unexpired)
X.509 certificates associated with the censys.io domain. The query for this is parsed.names:
censys.io and tags: trusted.

This script is made around library censys-python (https://github.com/Censys/censys-python) 
