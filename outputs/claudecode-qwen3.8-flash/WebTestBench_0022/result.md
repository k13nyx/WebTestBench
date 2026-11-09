# Test Result

## Functionality
- [ ] FT-01: Add pantry ingredient with quantity and expiration date
  - Action: In the "Add Ingredient" form, enter name "Spinach", quantity "200 g", expiration date "2026-11-10", and submit.
  - Expected: "Spinach" appears in the pantry list showing both "200 g" and "2026-11-10".
  - Bug Report:
    - Issue: Incorrect date display (expiration date not rendered as a date)
    - Actual: "Spinach — 200 g" appears, but the expiration is shown only as a relative badge "2 days". The text "2026-11-10" (or "Nov 10") appears nowhere in the DOM, and the badge has no `title`/`aria-label` tooltip exposing the date.

- [X] FT-02: Expiration date is optional when adding an ingredient
  - Action: Add an ingredient with name "Rice" and quantity "1 kg", leaving the expiration date field empty, and submit.
  - Expected: Submission succeeds and "Rice" is listed with quantity "1 kg" and no expiration date (blank/"—"), with no error.

- [X] FT-03: Generate a multi-day meal plan from the current pantry
  - Action: With the default pantry present, click "Generate Plan" for a 3-day span.
  - Expected: A plan renders covering 3 consecutive days, with at least one recipe assigned to each day.

- [X] FT-04: Plan is displayed day-by-day with recipes per meal
  - Action: Inspect the generated plan section.
  - Expected: Days are shown as separate, labeled blocks (e.g., "Day 1 / Mon Nov 9"), each listing meals (Breakfast/Lunch/Dinner) with a named recipe under each.

- [ ] FT-05: Exact ingredient usage amounts are shown
  - Action: Open any recipe card in the plan and view its ingredient lines.
  - Expected: Each ingredient line shows a specific amount used (e.g., "Spinach — 100 g"), not just the ingredient name.
  - Bug Report:
    - Issue: Missing recipe detail / non-expandable card
    - Actual: Recipe cards show only name, description, time, servings, and a "6 items" count — clicking a card opens nothing and no ingredient lines appear on the card. Exact amounts exist only in the separate aggregated "Ingredient Usage" panel (grouped per ingredient, e.g., "Garlic Chicken Stir-Fry: 400 g"), not in an openable recipe card.

- [ ] FT-06: Grocery list is produced for missing/insufficient items
  - Action: After generating the plan, view the "Grocery List" section.
  - Expected: The list contains only items not available (or not available in sufficient quantity) in the pantry, each with a required amount.
  - Bug Report:
    - Issue: Incorrect grocery entry due to pantry quantity miscount (unit conversion)
    - Actual: List shows "Rice — 400 g" even though the pantry actually holds 1000 g (default) + 1 kg (added item) = 2000 g against a 1400 g requirement. The usage panel reports Rice "1000 / 1400 g", proving the newly added 1 kg entry is not counted into available stock, so a fully covered item is listed. Other entries (Chicken 1300 g, Yogurt 100 g, Peppers 3 pcs, Onions 2 pcs, Garlic 0.5 heads) are correct and each has an amount.

- [X] FT-07: Lock an individual meal
  - Action: Click the "Lock" control on one meal slot (e.g., Day 2 Dinner).
  - Expected: That meal is marked locked and its recipe assignment is retained.

- [ ] FT-08: Lock an entire day
  - Action: Click the "Lock Day" control on one day block (e.g., Day 1).
  - Expected: The day block is marked locked and all of its meal assignments are retained.
  - Bug Report:
    - Issue: Missing control ("Lock Day" does not exist)
    - Actual: Day blocks contain no lock control of any kind. A DOM scan of all buttons in the page found only per-meal "Lock meal"/"Unlock meal" buttons; there is no day-level lock element or any button whose label/title matches "lock day".

- [X] FT-09: Regenerate the rest of the plan without starting over
  - Action: With one meal and one day locked, click "Regenerate Plan".
  - Expected: A new plan is produced for the unlocked days/meals; the plan remains a complete multi-day plan (no empty unlocked slots).

- [ ] FT-10: Simple preferences are applied to the generated plan
  - Action: Enable the "Vegetarian" and "Budget-friendly" preference toggles, then click "Generate Plan".
  - Expected: Every recipe in the plan is labeled/tagged as satisfying both selected preferences (no meat-containing or non-budget recipes appear).
  - Bug Report:
    - Issue: Missing preference labels/tags on recipes
    - Actual: Filtering itself works — the regenerated plan contains only meat-free recipes (Greek Yogurt Parfait, Tomato Pasta Primavera, Spinach & Cheese Quesadilla). However, no recipe card displays any tag/label indicating "Vegetarian" or "Budget Friendly"; the only occurrences of those words are the preference-switch labels in the sidebar.

## Constraint
- [ ] CS-01: Ingredient name and quantity are required
  - Action: Submit the "Add Ingredient" form with the name empty, then again with the quantity empty.
  - Expected: Both submissions are blocked with a validation message; no partial item is added to the pantry list.
  - Bug Report:
    - Issue: Missing validation message (silent rejection)
    - Actual: Both submissions were blocked (dialog stayed open, nothing added to the pantry), but no validation/error message was rendered in either case — DOM scan for `[role="alert"]`, error, or "required/must/enter" text found zero matches. The user receives no feedback explaining why nothing happened.

- [X] CS-02: Plan never uses more of an ingredient than the pantry holds
  - Action: Sum the per-recipe usage amounts for one constrained pantry item (e.g., "Spinach") across the whole plan and compare to the pantry quantity.
  - Expected: Total used ≤ quantity on hand; any shortfall appears only on the grocery list, and no ingredient shows a negative remaining amount.

- [X] CS-03: Locked meals and locked days are immutable after regeneration
  - Action: With Day 1 locked and Day 3 Dinner locked, click "Regenerate Plan" twice.
  - Expected: The recipes assigned to Day 1 (all meals) and Day 3 Dinner are identical before and after each regeneration; only unlocked slots change.

- [ ] CS-04: Food closest to expiring is prioritized
  - Action: Ensure the pantry holds an expiring-soon item (expiration within the plan range) and an equivalent non-expiring item, then click "Generate Plan".
  - Expected: The soon-expiring item is used in the plan on or before its expiration date, and it is not displaced by the later-expiring/equivalent item.
  - Bug Report:
    - Issue: Expiration priority not enforced in plan generation
    - Actual: The pantry held Spinach expiring in 2 days (2026-11-10, within the 3-day plan window) alongside equivalent non-expiring staples (Rice, Pasta, Olive Oil with no dates). The generated plan used **zero** spinach (no Spinach line in Ingredient Usage) and instead used the undated staples (Pasta, Rice). Spinach only entered the plan after manually enabling the Vegetarian toggle (which happens to select "Spinach & Cheese Quesadilla"), showing the expiring-soon item was displaced by the equivalent non-expiring item.

## Interaction
- [X] IX-01: Lock controls reflect state visibly and toggle back
  - Action: Click "Lock" on an unlocked meal, then click it again.
  - Expected: On the first click the control shows a locked state (e.g., filled lock icon / "Locked" label); on the second click it returns to the unlocked state with no page reload.

- [ ] IX-02: Generation gives immediate feedback and updates the view in place
  - Action: Click "Generate Plan" / "Regenerate Plan".
  - Expected: A busy/loading indication appears, followed by a success confirmation (e.g., toast or "Plan generated for 3 days"), and the plan + grocery list areas refresh without a full page reload.
  - Bug Report:
    - Issue: No busy/loading indication
    - Actual: Success toast ("Meal Plan Generated! Created 3-day plan with … locked meals preserved.") appears and the plan/grocery areas refresh in place with no page reload (SPA state verified preserved). However, no busy/loading state was ever observable: sampling the DOM at 0–300 ms after clicking showed the button never disabled and no spinner/`animate-spin`/`aria-busy` element at any sampling point, on both first generation and regenerations.

- [ ] IX-03: Expiring-soon pantry items are flagged in the UI
  - Action: Load the page with default data and inspect the pantry list.
  - Expected: Items whose expiration date is within/near the plan window are visually flagged (e.g., "Use by Nov 10" warning style), while items with no date or distant dates are not flagged.
  - Bug Report:
    - Issue: Over-flagging (distant expiration dates also flagged)
    - Actual: Near-expiry items are flagged ("2 days" badge on Spinach 2026-11-10; "Expired" badges on dated items) and undated items (Rice 1000 g, Pasta, Olive Oil) correctly show no badge. But an added test item with expiration 2027-01-01 — far outside the plan window — was also flagged with the same badge style ("54 days"), violating "items with distant dates are not flagged".

## Content
- [X] CT-01: Default pantry data is present on load
  - Action: Open the page without adding anything.
  - Expected: The pantry list shows several pre-existing ingredients, each with a quantity, and at least one with an expiration date.

- [ ] CT-02: Recipe content is consistent with the displayed plan
  - Action: Compare the recipe name and ingredient list on each recipe card with the plan's meal assignment and usage amounts.
  - Expected: Every recipe shown has a real dish name and an ingredient list whose items/amounts match the usage figures reported for that recipe (no blank, "Recipe #N", or placeholder text).
  - Bug Report:
    - Issue: Recipe cards contain no ingredient list
    - Actual: All recipe names are real dishes with descriptions (no "Recipe #N" or placeholders), and card item counts match the usage panel (e.g., "6 items" for Garlic Chicken Stir-Fry vs 6 per-recipe usage lines). However, the cards themselves display no ingredient list, so the required card-level comparison is impossible; ingredient/amount data exists only in the aggregated per-ingredient "Ingredient Usage" panel.

- [ ] CT-03: Grocery list entries are relevant and non-duplicated
  - Action: Review the grocery list against the pantry and the plan.
  - Expected: Every entry is an ingredient actually required by a planned recipe and missing/short in the pantry; no item already fully covered by the pantry appears, and no ingredient is listed twice.
  - Bug Report:
    - Issue: Grocery list includes a fully covered pantry item
    - Actual: "Rice — 400 g" is listed although the pantry holds Rice 1000 g + Rice 1 kg (2000 g), covering the 1400 g requirement. The app's stock math ignores the 1 kg entry (usage panel shows Rice "1000 / 1400 g"), so an item already fully covered by the pantry appears on the list. No duplicate entries were observed (6 unique items), and all other entries trace to planned recipes with genuine shortfalls.

---

**Summary: 7 PASS / 10 FAIL** across 20 checks. Root causes cluster into four defects: (1) no "Lock Day" control and no expandable recipe-card ingredient lists, (2) missing validation messages and missing busy/loading state (silent feedback gaps), (3) expiration priority not enforced for expiring-soon items when meat recipes win, plus relative-date-only display (and over-flagging of distant dates), (4) kg-unit pantry entries not counted in stock/shortfall math, producing a spurious grocery line.