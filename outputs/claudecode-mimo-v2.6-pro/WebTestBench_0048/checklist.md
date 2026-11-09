# Test Checklist

## Functionality
- [ ] FT-01: User can log in with valid credentials.
  - Action: Enter valid username and password on the login page, click "Log In".
  - Expected: Login succeeds and the main policy list page is displayed.

- [ ] FT-02: User can browse the list of company policies and procedures.
  - Action: After login, view the policies and procedures list page.
  - Expected: A list of default policy items is displayed with each item's title and type.

- [ ] FT-03: User can open a specific policy item to read it.
  - Action: Click a policy item title in the list.
  - Expected: The detail view of that policy opens, showing its full readable content.

- [ ] FT-04: User can complete the read-and-understood confirmation for a policy.
  - Action: Open a pending policy item, click the confirm/acknowledge control (e.g., "I have read and understood" checkbox) and submit it via the "Confirm" button.
  - Expected: The confirmation is accepted and recorded for that item.

- [ ] FT-05: User can see which items are confirmed and which are pending.
  - Action: View the policy list after logging in.
  - Expected: Each item shows a clear confirmation status label, e.g., "Confirmed" or "Pending".

- [ ] FT-06: Personal Center displays a doughnut chart of confirmed vs pending proportion.
  - Action: Navigate to Personal Center > Confirmation Progress Dashboard.
  - Expected: A doughnut chart is rendered showing two segments: confirmed items and pending items, with the proportion of each.

- [ ] FT-07: Dashboard categorizes confirmation status by policy type.
  - Action: View the Confirmation Progress Dashboard.
  - Expected: Confirmation status is shown broken down by the four policy types: Administration, Human Resources, Finance, and Compliance.

- [ ] FT-08: Pending items display priority tags.
  - Action: View the policy list and locate pending items.
  - Expected: Each pending item displays a priority tag of "High", "Medium", or "Low".

## Constraint
- [ ] CS-01: Login is rejected with invalid credentials.
  - Action: Enter a wrong username or password on the login page, click "Log In".
  - Expected: Login fails with an error message; the policy list is not accessible.

- [ ] CS-02: Unauthenticated users cannot access the policy list or Personal Center.
  - Action: Without logging in, attempt to open the policy list or the Personal Center page directly.
  - Expected: Access is blocked and the user is redirected to the login page.

- [ ] CS-03: Confirmation cannot be submitted without acknowledging read-and-understood.
  - Action: Open a pending policy item and click "Confirm" without ticking the "I have read and understood" checkbox.
  - Expected: Submission is blocked (e.g., "Confirm" button is disabled or an error message is shown) and the item remains "Pending".

- [ ] CS-04: An already-confirmed item cannot be confirmed again.
  - Action: Open an item already marked "Confirmed" and look for the confirm control.
  - Expected: The confirm control is disabled or absent, and the item stays "Confirmed" without duplicate confirmation records.

- [ ] CS-05: Policies with a confirmation deadline within 3 days are automatically marked High priority.
  - Action: View the policy list and locate an item whose confirmation deadline is within 3 days of today (default data).
  - Expected: That item's priority tag is automatically "High", regardless of its original priority.

- [ ] CS-06: Auto High-priority deadline items are pinned to the top of the list.
  - Action: View the policy list sorted in its default order.
  - Expected: All items with deadlines within 3 days appear at the top of the list, above non-high-priority items.

## Interaction
- [ ] IX-01: A success message appears after a confirmation is submitted.
  - Action: Submit a valid confirmation for a pending item.
  - Expected: A success toast/message (e.g., "Confirmation submitted successfully") is displayed.

- [ ] IX-02: Status and dashboard update immediately after confirming an item.
  - Action: Confirm a pending item, then view the policy list and the Confirmation Progress Dashboard.
  - Expected: The item's status changes to "Confirmed" and the doughnut chart/counts update without a manual refresh.

- [ ] IX-03: Hovering over a doughnut chart segment reveals its details.
  - Action: Hover the mouse over a segment of the doughnut chart in the Confirmation Progress Dashboard.
  - Expected: A tooltip/label appears showing that segment's category (Confirmed or Pending) and its count or percentage.

## Content
- [ ] CT-01: Policy list rows show relevant identifying information.
  - Action: View the policy list page.
  - Expected: Each row displays the policy title, its policy type (Administration / Human Resources / Finance / Compliance), and its confirmation status — all matching the actual policy data.

- [ ] CT-02: Policy detail content matches the selected item.
  - Action: Open a specific policy item from the list and read its detail page.
  - Expected: The displayed title and body text are the full content of that exact policy item, with no mismatch or missing content.

- [ ] CT-03: Dashboard shows the four policy type category labels correctly.
  - Action: View the Confirmation Progress Dashboard's per-type breakdown.
  - Expected: The categories are labeled exactly "Administration", "Human Resources", "Finance", and "Compliance", each with its own confirmation status figures.