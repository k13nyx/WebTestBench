# Test Checklist

**Preconditions:** Use the default test account credentials provided by the app to log in. Tests assume default policies of all four types (Administration / Human Resources / Finance / Compliance), with at least some pending and at least one pending item with a confirmation deadline within 3 days. Desktop browser only.

## Functionality
- [ ] FT-01: User can log in with valid credentials
  - Action: Open the site, enter the default test account's username/email and password, click "Log In".
  - Expected: Login succeeds; the policy list page (or home) is shown and the logged-in user's name / personal center entry is visible.
- [ ] FT-02: User can browse the list of company policies and procedures
  - Action: Navigate to the policies/procedures page.
  - Expected: A list of policy items is displayed; each row shows its title, its policy type (Administration / Human Resources / Finance / Compliance), and its confirmation status (Confirmed / Pending).
- [ ] FT-03: User can open a specific policy item to read it
  - Action: Click a pending policy in the list.
  - Expected: The item's detail view opens showing the full title, policy type, readable body content, and a confirmation control.
- [ ] FT-04: User can complete the "read and understood" confirmation
  - Action: On the detail view, tick the "I have read and understood" acknowledgement and submit.
  - Expected: The item's status becomes Confirmed, it counts as confirmed for this user, and it is no longer pending.
- [ ] FT-05: User can see confirmed vs. pending items
  - Action: Open the Pending view/tab and the Confirmed view/tab (or apply the status filter) on the policy list.
  - Expected: Pending shows only items this user has not confirmed; Confirmed shows only items this user has confirmed; no item appears in both.
- [ ] FT-06: Pending items support priority tagging (High / Medium / Low)
  - Action: On a pending item, set the priority control to High, then Medium, then Low.
  - Expected: The chosen value is displayed as the item's priority tag and still shows that value after the page is refreshed.
- [ ] FT-07: Confirmation Progress Dashboard shows a doughnut chart of confirmed vs. pending
  - Action: Open the Personal Center and locate the "Confirmation Progress Dashboard".
  - Expected: A doughnut chart is rendered with two segments (Confirmed and Pending) whose proportions match the user's actual counts (e.g., 3 confirmed of 10 = 30% / 70%).
- [ ] FT-08: Dashboard categorizes confirmation status by policy type
  - Action: View the by-policy-type breakdown on the dashboard.
  - Expected: Administration, Human Resources, Finance, and Compliance each show their confirmed and pending counts; the per-type counts sum to the same confirmed/pending totals as the doughnut chart.

## Constraint
- [ ] CS-01: Login is required and invalid credentials are rejected
  - Action: Submit the login form with a wrong password; then, while logged out, open the policy list URL and the personal center URL directly.
  - Expected: Wrong password shows an error and stays on the login page; direct URLs redirect to the login page and no policy data is shown.
- [ ] CS-02: Confirmation requires the "read and understood" acknowledgement
  - Action: Open a pending item's detail view and try to submit the confirmation without ticking the acknowledgement.
  - Expected: Submission is blocked (control disabled and/or a validation message shown) and the item remains Pending.
- [ ] CS-03: Already-confirmed items cannot be confirmed again
  - Action: Open an item whose status is Confirmed.
  - Expected: The confirmation control is not submittable (disabled, hidden, or replaced by a Confirmed state) and no second confirmation record is created.
- [ ] CS-04: Policies with a deadline within 3 days are automatically High priority
  - Action: Locate a pending policy whose confirmation deadline is within 3 days (including today) and has no manually set priority; also locate a pending policy whose deadline is more than 3 days away.
  - Expected: The within-3-days item is automatically tagged High priority; the more-than-3-days item is not tagged High by the system.
- [ ] CS-05: High-priority pending items are pinned to the top of the list
  - Action: View the pending list containing High (deadline-driven), Medium, Low, and untagged items.
  - Expected: Every High-priority item appears above all Medium, Low and untagged pending items.

## Interaction
- [ ] IX-01: Confirmation gives immediate success feedback and updates the badge
  - Action: Confirm a pending item and observe the result in the UI.
  - Expected: A success message/toast appears and the item's status badge changes to Confirmed immediately, with no duplicated list entry.
- [ ] IX-02: Changing priority re-pins the item in the list
  - Action: Change a pending item's priority from Medium to High and return to the pending list.
  - Expected: The item is moved to the top of the pending list.
- [ ] IX-03: Doughnut chart segments respond to hover
  - Action: Hover the "Confirmed" segment of the doughnut chart, then the "Pending" segment.
  - Expected: The hovered segment is visually highlighted and a tooltip appears showing the label, the item count, and the percentage.
- [ ] IX-04: Dashboard reflects a newly confirmed policy
  - Action: Note the current confirmed/pending percentages, confirm one pending policy, then return to the Confirmation Progress Dashboard.
  - Expected: The confirmed count/percentage increases and the pending decreases by exactly that one item; no stale values are shown.

## Content
- [ ] CT-01: Dashboard is correctly titled and its chart is labeled
  - Action: Open the Personal Center and inspect the dashboard heading and chart labels.
  - Expected: A section titled "Confirmation Progress Dashboard" is present inside the personal center, and the doughnut chart has a legend labeling the Confirmed and Pending segments.
- [ ] CT-02: Policy type categories are named exactly as specified
  - Action: Inspect the policy-type breakdown on the dashboard and the type labels on list items.
  - Expected: The four categories appear verbatim as "Administration", "Human Resources", "Finance", "Compliance" — no misspellings, no missing/extra category, no placeholder names such as "Category 1".
- [ ] CT-03: Policy content is real, relevant, and complete
  - Action: Open several policies and read their titles and body text; check the labels shown on pending items.
  - Expected: Every item contains genuine company policy/procedure text relevant to its title and type (no lorem ipsum, no empty bodies, no unrelated sample text), and any item with a confirmation deadline displays that deadline.