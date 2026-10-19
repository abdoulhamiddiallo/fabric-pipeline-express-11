"""Recalcule ce que la requête Price board doit renvoyer."""
import json
from decimal import Decimal, ROUND_HALF_UP
from pathlib import Path

d = json.loads((Path(__file__).resolve().parent.parent / "data" / "catalogue" / "mombasa_sale42_2026-10-20.json").read_text(encoding="utf-8"))
r = lambda x, n: Decimal(repr(x)).quantize(Decimal(1).scaleb(-n), rounding=ROUND_HALF_UP)
lots = d["lots"]; sold = [l for l in lots if l["price_usd_kg"] is not None]
kg = sum(l["kg"] for l in sold); val = sum(l["kg"] * l["price_usd_kg"] for l in sold)
top = max(sold, key=lambda l: (l["price_usd_kg"], -l["lot_no"]))
print(f"lots {len(lots)}  vendus {len(sold)}  tonnes {r(kg/1000,2)}  prix moyen {r(val/kg,2)}  valeur {r(val,0)} USD")
print(f"meilleur lot {top['lot_no']} {top['garden']} ({top['origin']}) {top['grade']} {top['price_usd_kg']}")
by = {}
for l in lots: by.setdefault(l["origin"], []).append(l)
rows = []
for o, ls in by.items():
    s = [l for l in ls if l["price_usd_kg"] is not None]
    k = sum(l["kg"] for l in s); v = sum(l["kg"] * l["price_usd_kg"] for l in s)
    rows.append((o, len(ls), len(s), r(k / 1000, 2), r(v / k, 2), max(l["price_usd_kg"] for l in s)))
for x in sorted(rows, key=lambda x: -x[4]): print(x)
