"""SehatPlate verification suite — run: python3 tests/verify.py (no server needed)."""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from app.sehatplate import engine, foods  # noqa: E402


def check(name, cond, detail=""):
    print(("PASS " if cond else "FAIL ") + name + (f" — {detail}" if detail else ""))
    if not cond:
        raise SystemExit(f"FAILED: {name}")


# Mifflin-St Jeor, hand-computed:
# male 70kg/175cm/25y: 10*70 + 6.25*175 - 5*25 + 5 = 1673.75
check("bmr male", abs(engine.bmr_mifflin(70, 175, 25, "male") - 1673.75) < 0.01)
# female: same minus 166 -> 1507.75
check("bmr female", abs(engine.bmr_mifflin(70, 175, 25, "female") - 1507.75) < 0.01)

t = engine.targets(70, 175, 25, "male", "moderate", "maintain")
# tdee = 1673.75 * 1.55 = 2594.3 -> 2594 kcal
check("targets maintain kcal", t["kcal"] == 2594, str(t["kcal"]))
check("targets protein 1.6g/kg", t["protein_g"] == 112)
check("targets fat 25pct", t["fat_g"] == round(0.25 * 2594 / 9) == 72)
check("targets carbs remainder",
      t["carbs_g"] == round((2594 - 112 * 4 - 72 * 9) / 4) == 374)
check("targets lose -500",
      engine.targets(70, 175, 25, "male", "moderate", "lose")["kcal"] == 2094)
check("targets gain +300",
      engine.targets(70, 175, 25, "male", "moderate", "gain")["kcal"] == 2894)
check("kcal safety floor >= 1200",
      engine.targets(40, 150, 20, "female", "sedentary", "lose")["kcal"] >= 1200)
check("bmi 22.9 healthy", t["bmi"] == 22.9 and t["bmi_band"] == "Healthy")

ds = foods.to_dicts()
check("db has 90+ foods", len(ds) >= 90, str(len(ds)))
check("no duplicate names", len(ds) == len({d["name"] for d in ds}))
check("src tags valid", all(d["src"] in ("usda", "recipe") for d in ds))
check("macros in range",
      all(0 <= d["protein"] <= 100 and 0 <= d["carbs"] <= 100
          and 0 <= d["fat"] <= 100 and d["kcal"] >= 0 for d in ds))
check("biryani searchable", any("Chicken biryani" in d["name"]
                                for d in foods.search("biryani")))
check("prefix match ranks first", foods.search("roti")[0]["name"].startswith("Roti"))
s = foods.scale(ds[0], 250)
check("scale 250g = 2.5x", s["kcal"] == round(ds[0]["kcal"] * 2.5, 1))

print("\nALL CHECKS PASSED")
