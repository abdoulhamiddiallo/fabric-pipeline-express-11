"""Génère le catalogue de la vente n° 42 de l'enchère du thé de Mombasa, 20 octobre 2026 (données fictives).

Un seul fichier JSON imbriqué : l'en-tête de la vente, puis un tableau "lots".
Un lot invendu (retiré) a un prix null : c'est la vraie vie des enchères.
"""
import json, random
from pathlib import Path

random.seed(4228)
OUT = Path(__file__).resolve().parent.parent / "data" / "catalogue"
OUT.mkdir(parents=True, exist_ok=True)

ORIGINS = [
    # pays, jardins, lots, prix moyen visé (USD/kg), part invendue
    ("Kenya", ["Kangaita", "Gitugi", "Ragati", "Iriaini", "Mataara", "Kapkoros", "Michimikuru", "Kambaa"], 64, 2.55, 0.12),
    ("Rwanda", ["Gisovu", "Pfunda", "Rubaya", "Nyabihu"], 22, 3.05, 0.05),
    ("Ouganda", ["Mabale", "Kayonza", "Igara"], 20, 1.55, 0.20),
    ("Tanzanie", ["Mufindi", "Kibena", "Luponde"], 14, 1.75, 0.14),
    ("Burundi", ["Teza", "Rwegura"], 10, 2.35, 0.10),
    ("RD Congo", ["Butuhe", "Kitabi"], 6, 1.40, 0.33),
]
GRADES = {"BP1": 1.08, "PF1": 1.04, "PD": 0.97, "D1": 0.90, "FNGS": 0.85, "DUST1": 0.80}
lots, n = [], 0
for country, gardens, count, base, unsold in ORIGINS:
    for i in range(count):
        n += 1
        grade = random.choice(list(GRADES))
        pkgs = random.choice([20, 30, 40, 40, 50, 60])
        kg = pkgs * 65
        price = None if random.random() < unsold else round(base * GRADES[grade] * random.uniform(0.85, 1.18), 2)
        lots.append({"lot_no": 1000 + n, "garden": random.choice(gardens), "origin": country, "grade": grade,
                     "packages": pkgs, "kg": kg, "price_usd_kg": price})
random.shuffle(lots)
sale = {"centre": "Mombasa", "sale_no": 42, "auction_date": "2026-10-20", "currency": "USD", "broker": "East African Tea Brokers (fictif)", "lots": lots}
(OUT / "mombasa_sale42_2026-10-20.json").write_text(json.dumps(sale, ensure_ascii=False, indent=2), encoding="utf-8")
print(len(lots), "lots écrits")
