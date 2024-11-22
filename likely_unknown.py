# This is just a little script I made for a lab for chem, we had to find the most likely element that was our unknown.
# Colors were averaged using the averager in this repo.
# Yes, this is the real data from that lab that me and my lab partner got.

colors = {
    "Lithium": 0xf79be2,
    "Strontium": 0xf89fbf,
    "Potassium": 0xd6b6d8,
    "Sodium": 0xeed878,
    "Barium": 0xefd36c,
    "Copper": 0xa5e3a3,
    "Calcium": 0xe49d6a,
}

unknown = 0xe6c275
diffs = {}
diffs_k = {}

for (k, v) in colors.items():
    diff = unknown - v if v < unknown else v - unknown
    diffs[k] = diff
    diffs_k[diff] = k
    hex_diff = "{:02x}".format(diff)
    print(f"{k}: #{hex_diff} [{diff}]")

x = max(diffs.values())
n = min(diffs.values())
margin = x - n
hex_x = "{:02x}".format(x)
hex_n = "{:02x}".format(n)
hex_margin = "{:02x}".format(margin)

print(f"Likely unknown: {diffs_k[n]} (difference #{hex_n}, margin #{hex_margin} to least likely, {diffs_k[x]} at #{hex_x})")
