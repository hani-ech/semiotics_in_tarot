import os
import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
data_dir = ROOT / "data"
out_csv = ROOT / "data" / "tarot_cards.csv"

rows = []
for deck_name in ["RWS", "Marseille"]:
    deck_dir = data_dir / deck_name
    for fname in os.listdir(deck_dir):
        if not fname.lower().endswith((".jpg", ".png", ".jpeg")):
            continue
        card_label = Path(fname).stem.lower()   # "fool", "sun", ...
        file_path = str(deck_dir / fname)
        rows.append({
            "deck": deck_name,
            "card_label": card_label,
            "file_path": file_path,
        })

rows.sort(key=lambda r: (r["deck"], r["card_label"]))

with out_csv.open("w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["deck", "card_label", "file_path"])
    writer.writeheader()
    writer.writerows(rows)

print(f"Wrote {len(rows)} rows to {out_csv}")
