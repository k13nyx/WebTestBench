# Test Result

## Functionality
- [X] FT-01: User can log in with valid credentials.
  - Action: Enter valid username and password on the login page, click "Log In".
  - Expected: Login succeeds and the main policy list page is displayed.

- [X] FT-02: User can browse the list of company policies and procedures.
  - Action: After login, view the policies and procedures list page.
  - Expected: A list of default policy items is displayed with each item's title and type.

- [X] FT-03: User can open a specific policy item to read it.
  - Action: Click a policy item title in the list.
  - Expected: The detail view of that policy opens, showing its full readable content.

- [X] FT-04: User can complete the read-and-understood confirmation for a policy.
  - Action: Open a pending policy item, click the confirm/acknowledge control (e.g., "I have read and understood" checkbox) and submit it via the "Confirm" button.
  - Expected: The confirmation is accepted and recorded for that item.

- [ ] FT-05: User can see which items are confirmed and which are pending.
  - Action: View the policy list after logging in.
  - Expected: Each item shows a clear confirmation status label, e.g., "Confirmed" or "Pending".
  - Bug Report:
    - Issue: Missing confirmation status label on pending policy rows (icon-only status indicator)
    - Actual: In the policy list, pending items display only an unlabeled clock icon (`lucide-clock`, no `aria-label`/`title`) together with the deadline text "Due Nov 9, 2026" — no "Pending" status label appears anywhere in the row (verified via full DOM textContent). Only confirmed items show a status label ("Confirmed Nov 8, 2026"). Pending vs. confirmed is therefore not shown as a clear status label on every item as required.

- [X] FT-06: Personal Center displays a doughnut chart of confirmed vs pending proportion.
  - Action: Navigate to Personal Center > Confirmation Progress Dashboard.
  - Expected: A doughnut chart is rendered showing two segments: confirmed items and pending items, with the proportion of each.

- [X] FT-07: Dashboard categorizes confirmation status by policy type.
  - Action: View the Confirmation Progress Dashboard.
  - Expected: Confirmation status is shown broken down by the four policy types: Administration, Human Resources, Finance, and Compliance.

- [X] FT-08: Pending items display priority tags.
  - Action: View the policy list and locate pending items.
  - Expected: Each pending item displays a priority tag of "High", "Medium", or "Low".

## Constraint
- [X] CS-01: Login is rejected with invalid credentials.
  - Action: Enter a wrong username or password on the login page, click "Log In".
  - Expected: Login fails with an error message; the policy list is not accessible.

- [X] CS-02: Unauthenticated users cannot access the policy list or Personal Center.
  - Action: Without logging in, attempt to open the policy list or the Personal Center page directly.
  - Expected: Access is blocked and the user is redirected to the login page.

- [X] CS-03: Confirmation cannot be submitted without acknowledging read-and-understood.
  - Action: Open a pending policy item and click "Confirm" without ticking the "I have read and understood" checkbox.
  - Expected: Submission is blocked (e.g., "Confirm" button is disabled or an error message is shown) and the item remains "Pending".

- [X] CS-04: An already-confirmed item cannot be confirmed again.
  - Action: Open an item already marked "Confirmed" and look for the confirm control.
  - Expected: The confirm control is disabled or absent, and the item stays "Confirmed" without duplicate confirmation records.

- [X] CS-05: Policies with a confirmation deadline within 3 days are automatically marked High priority.
  - Action: View the policy list and locate an item whose confirmation deadline is within 3 days of today (default data).
  - Expected: That item's priority tag is automatically "High", regardless of its original priority.

- [X] CS-06: Auto High-priority deadline items are pinned to the top of the list.
  - Action: View the policy list sorted in its default order.
  - Expected: All items with deadlines within 3 days appear at the top of the list, above non-high-priority items.

## Interaction
- [X] IX-01: A success message appears after a confirmation is submitted.
  - Action: Submit a valid confirmation for a pending item.
  - Expected: A success toast/message (e.g., "Confirmation submitted successfully") is displayed.

- [X] IX-02: Status and dashboard update immediately after confirming an item.
  - Action: Confirm a pending item, then view the policy list and the Confirmation Progress Dashboard.
  - Expected: The item's status changes to "Confirmed" and the doughnut chart/counts update without a manual refresh.

- [X] IX-03: Hovering over a doughnut chart segment reveals its details.
  - Action: Hover the mouse over a segment of the doughnut chart in the Confirmation Progress Dashboard.
  - Expected: A tooltip/label appears showing that segment's category (Confirmed or Pending) and its count or percentage.

## Content
- [ ] CT-01: Policy list rows show relevant identifying information.
  - Action: View the policy list page.
  - Expected: Each row displays the policy title, its policy type (Administration / Human Resources / Finance / Compliance), and its confirmation status — all matching the actual policy data.
  - Bug Report:
    - Issue: Missing confirmation status display on pending policy rows (icon-only, unlabeled status indicator)
    - Actual: Rows correctly display title and type matching the policy data (e.g., "Data Protection & Privacy" / "Compliance" matches its detail page), and confirmed rows show "Confirmed Nov 8, 2026". However, pending rows do not display their confirmation status: they show only the deadline text ("Due Nov 9, 2026") and an unlabeled clock icon (no "Pending" text/aria-label anywhere in the row DOM), so the confirmation status of pending items is not displayed on the row.
