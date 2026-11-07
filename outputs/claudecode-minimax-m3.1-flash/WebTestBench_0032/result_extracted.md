# Test Result

## Functionality

- [ ] FT-01: Create a financial goal with a name, target amount, and optional target date
  - Action: Open the app, click the "Add Goal" button, enter a goal name (e.g. "Emergency Fund"), target amount, and target date, then save.
  - Expected: The new goal appears in the goals list with its name and target amount, and the goal count increases by one.
  - Bug Report:
    - Issue: Missing Feature / Unreachable Control
    - Actual: No "Add Goal" button (or any goal-creation control) exists anywhere in the DOM. A full sweep of all 23 buttons, all headings, all links and all `[role=dialog]` elements found no text matching /add goal|new goal|create goal/i, and no hidden/aria-hidden element contains it. The "Financial Goals" section renders only 3 static cards (Summer Vacation, Emergency Fund, New Laptop) that are not clickable (cursor: auto, `click()` produces no DOM change). Goal count stayed at 3.

- [ ] FT-02: Create a monthly budget amount for a category
  - Action: Click "Add Budget" / "Set Budget", pick a category (e.g. "Groceries"), enter a monthly amount, and save.
  - Expected: The budget is listed against that category and is used in the by-category spending-vs-budget comparison.
  - Bug Report:
    - Issue: Missing Feature / Unreachable Control
    - Actual: No "Add Budget"/"Set Budget"/"Manage budget" control exists (sweep for /add budget|set budget|manage budget/i over all elements returned zero matches). The "Budget Categories" cards render fixed seed budgets ($600 Food & Dining, $400 Transportation, $300 Shopping, $200 Entertainment, $250 Utilities, $150 Health, $500 Travel, $200 Other) and are not clickable/editable (clicking "Health" produced no DOM change and no dialog). No category budget can be created or changed.

- [X] FT-03: Log an expense with amount, currency, date, and category
  - Action: Click "Add Expense", enter a description, amount, select a currency (e.g. EUR), select a date, select a category, and save.
  - Expected: The expense appears in the expense list showing its date, description, amount, currency, and category.

- [X] FT-04: Log an expense in a second currency and have it converted to the primary currency
  - Action: Note the primary currency, add an expense in a non-primary currency (e.g. USD) with a known amount, then view the expense list and the summary totals.
  - Expected: The expense is stored with its original currency and also displayed/valued in the primary currency at the current rate (shown amount differs from the entered amount by the conversion).
  - Note: Original currency is retained (€100.00) alongside the converted primary value ($108.70 / €100.00 when EUR primary) and the header "Total Spent" moved from $1659.00 → $1767.69 after the add.

- [ ] FT-05: Assign an expense to a goal
  - Action: Add an expense and select a specific goal from the "Goal" field; then open that goal.
  - Expected: The expense appears under/within that goal's tracked spending, and the goal's progress reflects it.
  - Bug Report:
    - Issue: Progress Not Updated / Goal Detail Unavailable
    - Actual: The "Link to Goal" field works for tagging (row renders "Food & DiningEmergency Fund"), but the goal card does not reflect the expense: after adding €100.00 (=$108.70) to the Emergency Fund goal, the card still shows "Progress $6500.00 / Remaining $3500.00" (unchanged), as do all other goals. There is no per-goal expense breakdown, and goals cannot be opened (clicking the "Emergency Fund"/"Summer Vacation" heading produced no DOM change, no modal, no route).

- [X] FT-06: Change the primary currency and view all summaries in it
  - Action: Change the primary currency selector to a different currency (e.g. USD), then view the summary/total figures and both charts.
  - Expected: All summary totals, chart values, and budget comparisons are displayed in the newly selected currency with its symbol/code.
  - Note: Switching the header selector to EUR re-rendered the header total (€1626.28), all stat cards, both chart axes (€0/€150/€300…, €0/€25/€50…), the budget-category cards and the list rows in €. (See CT-02 for a separate numeric-conversion defect on budget/goal figures.)

- [X] FT-07: Charts show spending versus budget by category
  - Action: Open the "Budget vs Spending" chart (or the by-category chart) on the dashboard.
  - Expected: A chart is rendered with one entry per budgeted category, each showing the budget amount and the actual spending for that category.
  - Note: 8 budgeted categories × 2 series = 16 `.recharts-bar-rectangle` elements; hovering the Food & Dining bar shows "Food & Dining / Spent: €100.00 / Budget: €600.00".

- [X] FT-08: Chart shows spending over time
  - Action: Open the spending-over-time chart on the dashboard.
  - Expected: A chart is rendered with spending plotted by time period (e.g. by month/date) using the expenses in the log.
  - Note: "Spending Trend (Last 14 Days)" line chart with date axis (Oct 26 – Nov 7); hovering the last point shows "Nov 7 / €100.00". Note the window is limited to the last 14 days, so older logged expenses are not plotted.

## Constraint

- [ ] CS-01: Required fields are enforced when adding an expense
  - Action: Open "Add Expense", leave description, amount, date, and category blank, and attempt to save.
  - Expected: Saving is blocked and a validation message identifies each missing required field; no new expense is added.
  - Bug Report:
    - Issue: Non-Specific Validation Message
    - Actual: Saving IS blocked and no expense is added (dialog stays open, row count unchanged), but the only feedback is a generic toast "Missing fields — Please fill in all required fields." No per-field validation exists: the dialog contains no `role=alert`/error text, no `aria-invalid`, no `aria-describedby`, and no red (`border-destructive`) styling on the empty description/amount/date inputs. The message never names which fields are missing, and "Date" is not even marked required (label "Date" has no `*`, unlike Description/Amount/Category).

- [ ] CS-02: Goal name and target amount are required
  - Action: Open "Add Goal", submit with an empty name or empty/zero target amount.
  - Expected: Submission is blocked with a validation message, and no goal is created.
  - Bug Report:
    - Issue: Missing Feature / Test Not Executable
    - Actual: There is no "Add Goal" dialog in the application (see FT-01), so no goal form can be opened or submitted. The goal list remains at 3 entries and no validation message can be produced.

- [ ] CS-03: Expense amount must be a positive number
  - Action: Enter an amount of 0 or a negative value in the Add Expense form and save.
  - Expected: Saving is blocked with a validation message, and no expense with a non-positive amount is recorded.
  - Bug Report:
    - Issue: Non-Positive Amount Accepted
    - Actual: An amount of `0` was accepted and saved: the list gained a row "QA Neg 0 | Food & Dining | $0.00 | €0.00 | Nov 7, 2026" with a success toast "Expense added — Added €0 for QA Neg 0". A negative amount (-5) was blocked, but silently — no validation message, toast or field error was displayed at all (dialog stayed open with no feedback).

- [ ] CS-04: Budget amount must be positive
  - Action: Enter a zero or negative monthly budget amount and save.
  - Expected: Saving is blocked with a validation message, and the budget is not updated.
  - Bug Report:
    - Issue: Missing Feature / Test Not Executable
    - Actual: No budget-entry UI exists anywhere (no "Add Budget"/"Set Budget" control; budget cards are read-only and non-interactive), so a zero/negative budget cannot be entered and no validation message can be triggered.

- [ ] CS-05: A start date later than the end date is rejected
  - Action: Set the filter date range with a start date after the end date and apply.
  - Expected: The invalid range is rejected (message shown or range not applied), and the expense list is not left in an inconsistent state.
  - Bug Report:
    - Issue: Invalid Date Range Silently Accepted
    - Actual: Setting From = 2026-12-01 and To = 2026-11-01 was applied without complaint: no error message/toast appeared and the expense list was emptied to 0 rows (the invalid range was accepted, not rejected). The controls retained the invalid values until they were manually cleared (clearing restored all 22 rows).

- [X] CS-06: Each expense belongs to exactly one category
  - Action: Add an expense and inspect the category field and the saved list row.
  - Expected: Exactly one category is set per expense and only that category is shown for it in the list.
  - Note: The "Category *" control is a single-select (Radix select with one value); every saved row renders exactly one category badge (goal is a separate badge).

- [X] CS-07: Over-budget categories are flagged rather than silently accepted
  - Action: Log a large expense in a category that has a small monthly budget, then view the by-category comparison.
  - Expected: That category is visibly marked as over budget (e.g. exceeded indicator / negative remaining shown), and the amount reflects the overspend.
  - Note: Adding €500 to Health (budget €150) renders the card as "€500.00 of €150.00" with the percentage badge in the destructive style (`bg-destructive/10 text-destructive`) vs. the success style (`bg-success/10 text-success`) used for non-over-budget categories. Caveat: the badge text is capped at "100%" instead of showing the real 333%, and no textual "over budget" label exists.

## Interaction

- [X] IX-01: Filters update the expense list immediately
  - Action: Change any one of the date range, category, or goal filters.
  - Expected: The list re-renders without a page reload and reflects the new filter selection.

- [X] IX-02: Filters combine with AND semantics
  - Action: Set a category filter and a goal filter together, then apply.
  - Expected: The list shows only expenses matching BOTH the selected category and the selected goal.
  - Note: Transportation + Emergency Fund → 0 rows; Food & Dining + Emergency Fund → exactly 1 row ("QA EUR Dinner").

- [X] IX-03: Clearing filters restores the full expense list
  - Action: Apply one or more filters, then click "Clear"/"Reset filters".
  - Expected: All default expenses reappear in the list and the filter controls return to their unfiltered state.
  - Note: "Clear" button appears in the filter panel; clicking it restored all 22 rows and reset the controls to "All categories" / "All" / empty dates.

- [ ] IX-04: Confirmation feedback after creating an expense, goal, or budget
  - Action: Save an expense, then save a goal, then save a budget.
  - Expected: Each save shows a visible success confirmation (toast or message) and the relevant list/chart updates without a manual refresh.
  - Bug Report:
    - Issue: Partial Implementation / Missing Feature
    - Actual: Only the expense save is possible and it does show a visible confirmation ("Expense added — Added €100 for QA EUR Dinner") with the list and charts updating live. Goal and budget saves cannot be performed at all (no Add Goal / Add Budget controls), so the expected confirmation for those two entity types is not delivered.

- [X] IX-05: Primary currency change updates displayed values live
  - Action: Change the primary currency selector while on the dashboard.
  - Expected: Summary totals and chart value labels re-render in the new currency without needing to navigate away and back.

- [X] IX-06: Chart elements respond to hover/interaction
  - Action: Hover over a bar, slice, or point in either chart.
  - Expected: A tooltip or highlight shows the category/period and its value so the user can read exact numbers.
  - Note: By-category tooltip: "Food & Dining / Spent: €100.00 / Budget: €600.00"; trend tooltip: "Nov 7 / €100.00".

## Content

- [X] CT-01: Currency symbols and codes are displayed correctly
  - Action: View summaries, chart labels, and the expense list for an amount in a non-primary currency.
  - Expected: Each amount carries the correct symbol or ISO code of its currency and is formatted with the correct number of decimals (e.g. 2 for EUR/USD).
  - Note: "$108.70 / €100.00", "$23.42 / £18.50", "$38.04 / €35.00" — correct symbols, 2 decimals. Caveat: chart axis ticks are rounded without decimals (€150, €600).

- [ ] CT-02: Summary and chart content is denominated in the primary currency
  - Action: Inspect the total spending summary and both charts.
  - Expected: Every displayed monetary value uses the primary currency's symbol/code and no summary value is left in a non-primary currency.
  - Bug Report:
    - Issue: Seeded Budget/Goal Values Not Converted (Mixed-Currency Summary)
    - Actual: With EUR selected as primary, expenses are correctly converted (Total Spent €1626.28 = $1659.00 converted + €100.00) but the seeded USD budgets and goal amounts are only re-labelled with the € symbol, never converted: "Monthly Budget €2600.00" (seed $2600), Health "€500.00 of €150.00" (budget seed $150), goal "Progress €6500.00 / Remaining €3500.00" (seed $6500/$3500). The summary therefore mixes a converted spend with an unconverted budget ("23% of budget", Remaining €2000.00), and budget-vs-spending comparisons are numerically wrong in any non-USD primary currency.

- [ ] CT-03: Chart labels and legends are relevant and complete
  - Action: Inspect the axes, category labels, legend entries, and period labels of both charts.
  - Expected: Each budgeted category is named in the by-category chart, time periods are named on the over-time chart, and a legend explains spending vs budget.
  - Bug Report:
    - Issue: Missing Legend
    - Actual: Category labels (🍽️ 🚗 🛍️ 🎬 💡 🏥 ✈️ 📦) and period labels (Oct 26 … Nov 7) are present, but neither chart has a legend: `document.querySelectorAll('.recharts-legend').length === 0` and `.recharts-legend-item-text` is empty for both charts. Nothing in the UI explains which bar/series is budget vs. spending (the two series are also drawn in the same muted fill).

- [ ] CT-04: List and goal content shows the correct attributes for each record
  - Action: Read several rows of the expense list and several entries in the goals list.
  - Expected: Each expense row shows a non-empty date, description, amount, currency, and category; each goal shows its name and target amount; no row shows "undefined", "null", or "NaN".
  - Bug Report:
    - Issue: Goal Target Amount / Target Date Not Displayed
    - Actual: Expense rows are complete and clean (e.g. "QA EUR Dinner | Food & Dining | $108.70 | €100.00 | Nov 7, 2026"; no "undefined"/"null"/"NaN" anywhere in the document). But the goals list shows only "Emergency Fund | Deadline passed | Progress $6500.00 | Remaining $3500.00" — the goal's **target amount** ($10,000) is never displayed (nor is the target date; every goal shows the generic "Deadline passed"), so a goal's target cannot be read from the goals list.
