All tests executed. Here is the complete checklist with results:

# Test Result

## Functionality
- [X] FT-01: Add a one-off income transaction
  - Action: Open the "Add Transaction" form, select type "Income", frequency "One-off", enter a valid amount (e.g., 1000), assign a category, project, and payment method, save.
  - Expected: The transaction is saved and appears in the transaction list with the correct amount, type, and assignments.
- [X] FT-02: Add a one-off expense transaction
  - Action: Add an expense with frequency "One-off", amount (e.g., 250), category, project, and payment method, save.
  - Expected: The transaction appears in the list marked as an expense with the entered details.
- [X] FT-03: Add a recurring transaction
  - Action: Add a transaction with frequency "Recurring" (e.g., monthly) and save.
  - Expected: The transaction is saved with its recurrence visible (e.g., "Monthly") in the transaction list.
- [X] FT-04: Edit an existing transaction
  - Action: Open an existing transaction from the list, change its amount or category, save.
  - Expected: The list and any summary figures reflect the updated values.
- [X] FT-05: Delete a transaction
  - Action: Delete a transaction from the list and confirm (if prompted).
  - Expected: The transaction no longer appears in the list.
- [X] FT-06: Mark a transaction status
  - Action: Change a transaction's status to "Paid" (and verify another shows "Pending" / "Expected").
  - Expected: The status is updated and displayed in the list (e.g., a "Paid" badge).
- [X] FT-07: View historical cash flow chart
  - Action: Open the historical cash flow chart section of the dashboard.
  - Expected: A chart renders showing past income and expenses/balance over time, consistent with the recorded transactions.
- [X] FT-08: View cash balance forecast
  - Action: Open the forecast view.
  - Expected: A future balance projection is displayed that accounts for upcoming "Expected" payments and recurring items.
- [X] FT-09: Create a custom view for a business area
  - Action: Create a new custom view named "Marketing" (or similar), optionally tied to specific categories/projects, and save it.
  - Expected: The view is saved and selectable from the views switcher.
- [X] FT-10: Switch to a custom view and see its tailored summary
  - Action: Switch to the saved custom view.
  - Expected: The dashboard shows summaries/charts filtered to that view's scope (e.g., only marketing-related transactions).

## Constraint
- [ ] CS-01: Amount field rejects invalid input
  - Action: In the transaction form, enter a negative value, zero, or non-numeric text in the amount field and attempt to save.
  - Expected: Submission is blocked with a clear validation message; no invalid transaction is created.
  - Bug Report:
    - Issue: Missing Form Validation / Incorrect Form Submission
    - Actual: Negative amount (-50) was accepted and saved as a transaction displayed as "-$0" ("QA Invalid", later cleaned up); zero (0) was also accepted — a "QA Zero" transaction was created with no validation message and the dialog closed on submit. Non-numeric text cannot be typed (native number input rejects letters) but no validation message is shown either. No clear validation feedback appears for any invalid value.
- [ ] CS-02: Required fields must be filled
  - Action: Submit the transaction form with empty required fields (e.g., amount or type).
  - Expected: The form is not saved and highlights the missing required field(s).
  - Bug Report:
    - Issue: Missing Required-Field Highlighting
    - Actual: Submitting the form with empty description and amount did not save (dialog stayed open, no row created), but no field was highlighted and no validation message was displayed — the form just silently did nothing. Also, category/project may be left unset, and the row then displays "Unknown | Unknown" (e.g., "QA Toast Check | ... | Unknown | Office & Utilities | Pending | -$10") instead of enforcing those assignments.
- [X] CS-03: Filters combine without showing out-of-scope data
  - Action: Apply two filters together (e.g., status "Expected" and a specific category).
  - Expected: Only transactions matching ALL active filters are listed; no unrelated transactions appear.

## Interaction
- [X] IX-01: Filter updates the transaction list immediately
  - Action: Select a filter option (e.g., status "Pending").
  - Expected: The transaction list updates immediately to show only matching transactions without requiring a page reload.
- [ ] IX-02: Sort toggles the transaction ordering
  - Action: Click a column header (e.g., "Amount" or "Date") to sort; click again to reverse.
  - Expected: The list re-orders accordingly and the sort direction is indicated (e.g., arrow icon).
  - Bug Report:
    - Issue: Missing Sort-Direction Indicator
    - Actual: Sorting works via the sort dropdown ("Date"/"Amount"/"Name") and the adjacent toggle button does reverse the order (verified: descending → ascending → descending by amount). However, the toggle button's icon is a static "arrow-up-down" lucide icon whose class, SVG markup, and pressed state never change in either direction — the current sort direction is not visually indicated anywhere.
- [ ] IX-03: Saving a transaction gives visible feedback
  - Action: Save a new transaction.
  - Expected: A success confirmation (e.g., toast or highlighted row) appears, and the new transaction is visible in the list.
  - Bug Report:
    - Issue: Missing Success Feedback
    - Actual: A MutationObserver watching the whole document captured every DOM node added during a save — no toast, notification, or success confirmation appeared (the app's notification regions remained empty), and the new row received no highlight styling. The only feedback is the dialog closing and the row appearing in the list.
- [X] IX-04: Chart details are inspectable
  - Action: Hover over a point/bar in the cash flow chart.
  - Expected: A tooltip or label shows the exact value and period for that data point.

## Content
- [X] CT-01: Dashboard summary figures are accurate
  - Action: Compare the dashboard totals (e.g., total income, total expenses, current balance) with the transactions in the list.
  - Expected: Displayed figures match the sums of the underlying transactions.
- [ ] CT-02: Transaction rows show all assigned attributes
  - Action: Inspect transactions in the list.
  - Expected: Each row displays its amount, type (income/expense), status, and assigned category, project, and payment method.
  - Bug Report:
    - Issue: Incomplete Attribute Display (payment method not identifiable)
    - Actual: Rows correctly display amount ("+$1,000"/"-$4,500"), type (trending-up/trending-down icon + sign), status badge (Paid/Pending/Expected), and category and project as text badges. However, the payment method is shown only as an unlabeled generic icon (e.g., lucide-credit-card, lucide-building) with no text, title attribute, or aria-label — the actual assigned method (e.g., "PayPal" vs "Business Credit Card") cannot be determined from the list row; hovering the icon shows no tooltip.
- [ ] CT-03: Charts have labeled axes and legends
  - Action: Inspect the cash flow and forecast charts.
  - Expected: Axes, time periods, and series (income vs. expense) are labeled or have a legend, and values are readable and correctly formatted as currency.
  - Bug Report:
    - Issue: Missing Chart Legend on Forecast Chart
    - Actual: The Dashboard "Cash Flow Overview" chart is fully compliant (legend pills "Income / Expenses / Forecast", month axis Jul–Mar, currency y-axis $0k–$80k). The Forecast page's "3-Month Forecast" chart has labeled axes (Jan/Feb/Mar, $0k–$26k currency) and currency-formatted tooltips ("Feb (Projected) Income: $70,000 Expenses: $48,000 Net: $22,000"), but no legend or on-chart series labels — the income vs. expense vs. projected lines are visually indistinguishable without hovering.

---

**Additional observation (not checklist-scoped):** All data lives in an in-memory store — a full page reload (direct URL navigation) discards every transaction/view created during the session, reverting to seed data. All CRUD results above were verified before any reload; the app itself works correctly within a session, but persistence across page loads is absent.