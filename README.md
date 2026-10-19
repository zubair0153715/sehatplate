# SehatPlate 🍛

**Honest AI calorie tracker with a South Asian food database** — the anti-Cal-AI.

Cal AI proved the market ($30–50M/yr, 15M downloads) — and the failure modes: deceptive
billing (pulled from the App Store Apr 2026), photo estimates that miss ~1/3 of calories
(NIH NIDDK, NUTRITION 2026), and zero coverage of desi food. SehatPlate is a clean-room
original that fills those gaps:

1. **Honest free tier** — full logging + AI estimates free. No quiz paywall, no trial traps.
2. **95-food desi database** — biryani, nihari, haleem, daal, roti, chai… every row
   source-tagged (USDA FoodData Central or documented recipe decomposition — see DATA_NOTES.md).
3. **Accuracy-honest by design** — text-first logging with explicit grams; AI estimates are
   always labeled as estimates; frequent foods are quick-addable.

Live: https://clinic-demo.fastapicloud.dev/sehatplate (mobile-friendly web app)

## How it works

- **Targets** — Mifflin-St Jeor BMR × activity factor, −500 kcal (lose) / +300 (gain),
  protein 1.6 g/kg. Verified by hand calculation in `tests/verify.py`.
- **Food DB** — `app/sehatplate/foods.py`: per-100g kcal/protein/carbs/fat, searchable.
- **AI estimate** — type *"2 chicken biryani plates and 1 cup chai"* → Gemini
  (`gemini-2.5-flash`) returns structured nutrition JSON, labeled `AI estimate` in the UI.
  Server reads `GEMINI_API_KEY` from the environment at call time; key never committed.
- **Diary** — stored on the user's device (browser localStorage): private, and survives
  server redeploys. Nothing is uploaded.

## Run locally

```bash
pip install "fastapi[standard]"
uvicorn app_main:app --reload   # see clinic-demo-apps for the full host app
```

Or run the verification suite (no server needed):

```bash
python3 tests/verify.py
```

## Honest limits

- `recipe`-tagged values are documented estimates, not lab measurements — weigh portions
  for precision. A photo can't weigh food; neither can we, so we don't pretend.
- Study/fitness aid, **not medical advice**. For diabetes, kidney disease, or eating
  disorders, see a real clinician/dietitian.

## License

MIT — original code, no affiliation with Cal AI / MyFitnessPal.
