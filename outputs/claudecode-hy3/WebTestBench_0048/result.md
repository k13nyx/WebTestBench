All verifications are complete. The fresh dashboard now reflects the confirmation (1 Confirmed / 7 Pending, 13% complete, Administration 1/2), and the confirmed "Code of Conduct" item now shows "Confirmed Nov 7, 2026" and moved out of the High-priority top grouping. The earlier stale reading was just the browser-back cache.

Here is the complete test result.

# Test Result

## Functionality
- [X] FT-01: User can log in to the internal website
  - Action: Enter valid credentials and submit the login form.
  - Expected: User is authenticated and lands inside the internal site (policy list or home).

- [X] FT-02: User can browse the list of company policies and procedures
  - Action: Navigate to the policies section after login.
  - Expected: A list of company policies and procedures is displayed.

- [X] FT-03: User can open a specific policy item to read it
  - Action: Click on a policy item in the list.
  - Expected: The policy's full content/detail view opens and is readable.

- [X] FT-04: User can complete the read-and-understood confirmation
  - Action: On an opened policy, activate the confirmation control.
  - Expected: The item is marked as confirmed for the current user.

- [X] FT-05: User can see confirmed vs pending status per item
  - Action: View the policy list / personal status area.
  - Expected: Each item clearly indicates whether it is confirmed or pending for the user.

- [X] FT-06: User can access the Confirmation Progress Dashboard
  - Action: Open the personal center and navigate to the dashboard.
  - Expected: The Confirmation Progress Dashboard is displayed.

- [X] FT-07: Dashboard categorizes status by policy type
  - Action: View the dashboard.
  - Expected: Confirmation status is broken down by Administration, Human Resources, Finance, and Compliance.

## Constraint
- [X] CS-01: Confirmation is only allowed after opening/reading the item
  - Action: Attempt to confirm an item without opening it.
  - Expected: Confirmation is blocked or not offered until the item is opened.

- [X] CS-02: Deadline-within-3-days policies auto-marked High priority
  - Action: Inspect a policy whose confirmation deadline is within 3 days.
  - Expected: It is automatically assigned High priority.

- [X] CS-03: High-priority items are pinned to the top of the list
  - Action: View the policy list.
  - Expected: High-priority flagged items appear at the top, above non-high-priority items.

## Interaction
- [X] IX-01: Dashboard doughnut chart shows confirmed/pending proportion
  - Action: View the doughnut chart on the dashboard.
  - Expected: A doughnut chart displays the proportion of confirmed vs pending items.

- [X] IX-02: Pending items display priority tags
  - Action: View pending items in the list.
  - Expected: Each pending item shows a priority tag of High, Medium, or Low.

- [X] IX-03: Dashboard updates after a confirmation
  - Action: Confirm a pending policy, then return to the dashboard.
  - Expected: The doughnut chart and status counts reflect the newly confirmed item.

## Content
- [X] CT-01: Policies and categories are relevant to the theme
  - Action: Inspect listed policies and their categories.
  - Expected: All items are company policies/procedures tagged under Administration, Human Resources, Finance, or Compliance.

- [X] CT-02: Confirmation control is clearly labeled
  - Action: Open a policy and locate the confirmation control.
  - Expected: A control clearly labeled as confirmation of reading/understanding (e.g., "I've read and understood") is present and active.

---

**Summary:** 15/15 checks PASS.

**Notes from verification:**
- Login lands directly on the dashboard (`/dashboard`), which is the "Confirmation Progress Dashboard" (FT-06): a doughnut chart (SVG, verified via DOM — `hasChart: true`) showing confirmed/pending proportion plus a "Status by Category" breakdown for Administration/HR/Finance/Compliance (FT-07, IX-01).
- Confirmation flow (FT-04/CT-02/CS-01): a policy detail page presents a checkbox labeled *"I have read and understood this policy. I agree to comply…"* and a *"Confirm Policy"* button that is `disabled` until the checkbox is ticked. After confirming, a success notification appears and the item status flips to "Confirmed" with a timestamp. The list itself offers no confirm control, so confirmation requires opening the item first.
- Priority & pinning (CS-02/CS-03/IX-02): every item whose due date is within 3 days of today (Nov 7) — Data Protection (Nov 8), Information Security (Nov 10), and previously Code of Conduct (Nov 9, now confirmed) — carries a **High** tag; later-due items are Medium/Low. High items render at the top of the list, above Medium/Low, and confirmed items drop to the bottom with a "Confirmed" badge (FT-05).
- Dashboard reactivity (IX-03): after confirming, the doughnut and counts updated from 0% / 0 Confirmed / 8 Pending to 13% / 1 Confirmed / 7 Pending, and Administration moved from 0/2 to 1/2. (Note: a *hard browser reload* to `/dashboard` logs the session out — auth state is in-memory — so the dashboard must be reached via in-app navigation; this is an observation, not a checklist failure.)