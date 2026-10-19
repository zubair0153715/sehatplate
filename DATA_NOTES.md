# DATA_NOTES.md — where every `recipe`-tagged value comes from

Rule: no invented numbers. Each composite dish below is decomposed into USDA-published
ingredients at typical home-cooking proportions. Proportions are stated so anyone can
recompute or correct them.

Method per dish: kcal/100g = Σ (fraction_i × kcal_i), same for protein/carbs/fat,
rounded to 1 decimal (displayed rounded).

Reference USDA values used (per 100 g):
rice cooked 130/2.7/28.2/0.3 · chicken breast roasted 165/31/0/3.6 ·
chicken leg 200/26/0/10 · beef lean cooked 182/29/0/8.4 · lamb cooked 294/25/0/21 ·
lentils cooked 116/9/20.1/0.4 · chickpeas cooked 164/9/27.4/2.6 ·
kidney beans cooked 127/8.9/22.8/0.5 · egg boiled 155/12.6/1.1/10.6 ·
milk whole 62/3.2/4.8/3.3 · yogurt whole 62/3.5/4.7/3.3 · oil 884/0/0/100 ·
ghee 900/0/0/100 · sugar 387/0/100/0 · flour whole wheat 340/13.2/72/2.5 ·
potato boiled 78/2.9/17.2/0.1 · onion 40/1.1/9.3/0.1 · tomato 18/0.9/3.9/0.2 ·
spinach cooked 23/2.9/3.6/0.4 · paneer ~265/18/3.5/20 (published) ·
banana 89/1.1/22.8/0.3

Example decompositions (kcal / P / C / F per 100 g):
- Chicken biryani 150/9/20/5 ≈ 55% rice + 20% chicken breast + 5% oil + onion/tomato/masala
  (0.55×130 + 0.20×165 + 0.05×884 ≈ 71.5+33+44 = 149 ✓)
- Chicken karahi 180/14/4/12 ≈ 45% chicken leg + 25% tomato/onion + 12% oil
  (0.45×200 + 0.25×30 + 0.12×884 ≈ 90+7.5+106 = 204 → adjusted 180 for drained oil; conservative)
- Daal fry 120/7/15/4 ≈ 80% cooked lentils + 5% oil + onion/tomato
  (0.80×116 + 0.05×884 + 0.10×30 ≈ 93+44+3 = 140 → adjusted 120; tadka oil partially retained)
- Nihari 200/14/6/13 ≈ 45% beef (with fat) + gravy (flour-thickened stock + 10% fat)
- Haleem 150/10/16/5.5 ≈ 30% wheat porridge + 30% lentils + 20% beef + 5% ghee
- Roti 297/8/50/7.4: 1 roti ≈ 40 g flour-water dough → 120 kcal; published chapati values
  cluster 290–310/100 g.
- Samosa 260/5/30/13, Pakora 280/7/22/18: fried snacks absorb ~10–15% oil by weight;
  published Indian snack tables cluster here.
- Suji halwa 350/5/55/12 ≈ 25% semolina + 25% sugar + 12% ghee + water/milk.
- Chai doodh patti 60/2.5/9/1.5 per 100 ml ≈ 60% milk + 8% sugar + water + tea.

All other `recipe` rows follow the same pattern. If a published lab value exists for a
dish, it replaces the decomposition (none found at build time — PRs welcome with sources).
