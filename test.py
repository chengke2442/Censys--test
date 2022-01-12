from censys.search import CensysCertificates
import pandas as pd

# get certifiate
c = CensysCertificates()

# build the list for the infomation that is required
fields = [
    "parsed.fingerprint_sha256",
    "parsed.validity.start",
    "parsed.validity.end",
]

# seperate the information to save the information
info = []
pageInfo = []

for page in c.search(
    "censys.io and tags: trusted",
    fields,
):
    pageInfo = [page["parsed.fingerprint_sha256"],
                page["parsed.validity.start"], page["parsed.validity.end"]]
    info.append(pageInfo)

# transfer list into dataframe to save to csv file
df = pd.DataFrame(info, columns=[
                  "SHA-256", "start-date", "end-date"])

# save to csv file
df.to_csv("result.csv", index=False)
