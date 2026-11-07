Testing complete. All checklist items were executed against the running app (login → policy list → detail views → confirmation → dashboard/chart → filters), using DOM-level verification only.

Notable observations beyond the checklist: the "Status by Category" breakdown rows themselves are **static** (clicking them does nothing — policy-type selection is done via the clickable category chips next to the list), and the chart has no separate `recharts` legend element (Confirmed/Pending are conveyed by the ring segments' labels and the adjacent "N Confirmed / N Pending" stat chips). Also, the session is in-memory only: a hard page reload returns the user to the login screen.

# Test Result

## Functionality

- [X] FT-01: User can log in to the internal policies site with valid credentials
  - Action: Open the site, enter the default valid username and password in the login form, submit.
  - Expected: Login succeeds, the user is taken into the policies site and the logged-in user/session is shown (not the login form).
- [X] FT-02: User can browse the list of company policies and procedures
  - Action: After login, view the main policy list.
  - Expected: A list of the default policies/procedures is displayed, each with its title.
- [X] FT-03: User can open a specific policy item and read its content
  - Action: Click the title/link of any policy item in the list.
  - Expected: A detail view opens showing that policy's title and full body content.
- [X] FT-04: User can complete the read-and-understood confirmation step for a policy
  - Action: In an open policy's detail view, perform the confirmation action (acknowledging "I have read and understood").
  - Expected: The confirmation is recorded for that policy and the item is recognized as confirmed.
- [X] FT-05: User can see which items are already confirmed and which are still pending
  - Action: Return to the policy list and/or personal center after confirming one item.
  - Expected: The confirmed policy is shown with a confirmed status and the remaining items are shown as pending for the user.
- [ ] FT-06: Confirmation Progress Dashboard is reachable from the personal center
  - Action: Open the personal center and locate the "Confirmation Progress Dashboard" entry, then open it.
  - Expected: The dashboard view loads, linked from the personal center.
  - Bug Report:
    - Issue: Missing Feature / Missing Navigation Entry
    - Actual: The application has no personal center. The only routes are `/`, `/login`, `/dashboard`, `/policy/:id` and a 404 fallback; the header contains only the brand block ("Policy Portal / Welcome, Admin User") and a "Sign out" button — there is no user menu, nav bar or "Confirmation Progress Dashboard" entry to open. The dashboard renders directly at `/dashboard` (and is titled "Confirmation Progress"), so it is reachable, but it is not linked from any personal center as the expected result requires.
- [X] FT-07: Dashboard displays a doughnut chart of confirmed vs pending proportion
  - Action: On the dashboard, locate the progress chart.
  - Expected: A doughnut (ring) chart is rendered showing the confirmed portion and the pending portion of the user's items.
- [X] FT-08: Dashboard categorizes confirmation status by policy type
  - Action: On the dashboard, inspect the per-type breakdown.
  - Expected: Confirmation status is shown separately for Administration, Human Resources, Finance, and Compliance categories.
- [X] FT-09: Pending items display priority tags
  - Action: Open the pending items list and inspect a pending policy.
  - Expected: Each pending item shows a priority tag of High, Medium, or Low.

## Constraint

- [X] CS-01: Login rejects invalid credentials
  - Action: Enter an incorrect username and/or password and submit the login form.
  - Expected: Login is refused, an error message is shown, and the user stays on the login page with no session created.
- [X] CS-02: Confirmation cannot be recorded until the acknowledgement is explicitly given
  - Action: Open a pending policy and attempt to confirm without ticking/selecting the "I have read and understood" acknowledgement.
  - Expected: The confirm/submit action stays unavailable or is rejected with a prompt to acknowledge; no confirmation is recorded.
- [X] CS-03: Policies with a confirmation deadline within 3 days are automatically tagged High priority
  - Action: Identify a default policy whose confirmation deadline is within 3 days and inspect its priority tag.
  - Expected: Its priority tag is automatically set to High, with no manual tagging step required.
- [X] CS-04: Policies with a near-deadline are pinned to the top of the list
  - Action: View the policy list and check the ordering of items relative to a deadline-bound policy (e.g., within 3 days).
  - Expected: The near-deadline policy appears above other pending items at the top of the list.
- [X] CS-05: Priority tags apply only to pending items
  - Action: Inspect the status of a policy that has already been confirmed.
  - Expected: It shows a confirmed status (not a priority tag), and no pending-only priority labelling contradicts its confirmed state.

## Interaction

- [X] IX-01: Confirming a policy gives clear success feedback
  - Action: Complete the confirmation step on an open policy.
  - Expected: A visible success confirmation message/toast appears indicating the policy was confirmed.
- [X] IX-02: Dashboard updates immediately after a new confirmation
  - Action: Open the dashboard, note the confirmed/pending figures, then confirm one more pending policy and return to the dashboard.
  - Expected: The doughnut chart proportions and the per-type confirmed/pending counts reflect the new confirmation.
- [X] IX-03: Selecting a policy type on the dashboard shows that type's status
  - Action: Click a policy type category (Administration / Human Resources / Finance / Compliance) in the dashboard breakdown.
  - Expected: The status detail for that policy type is shown (e.g., which items are confirmed vs pending in that category).

## Content

- [X] CT-01: Policy list entries show accurate identifying information
  - Action: Inspect each default entry in the policy list.
  - Expected: Each entry shows its policy title, its policy type (Administration / Human Resources / Finance / Compliance), and its current confirmation status; all text is legible and not truncated or placeholder.
- [X] CT-02: Opened policy shows its complete, relevant body content
  - Action: Open each policy type's policy detail view.
  - Expected: The view shows the full policy text corresponding to that item (not empty, not another policy's text, not generic placeholder copy).
- [X] CT-03: Dashboard labels and legend correctly name confirmed/pending and the policy types
  - Action: Inspect the doughnut chart legend, segment labels, and per-type breakdown headings.
  - Expected: The labels explicitly read "Confirmed" and "Pending", and the breakdown headings use exactly Administration, Human Resources, Finance, and Compliance with correct confirmed/pending counts per type.

**Key evidence captured**
- Login: invalid `wrong@company.com / wrongpass` → toast "Invalid email or password. Try admin@company.com / admin", still on `/login`; valid `admin@company.com / admin` → `/dashboard`, header shows "Welcome, Admin User".
- Confirmation: detail view of `/policy/pol-001` showed badge `Pending`, "Confirm Policy" button `disabled`; force-clicking the disabled button left it disabled, no toast, status still "Pending", dashboard still "2 Confirmed / 6 Pending". After ticking the checkbox the button enabled; clicking it produced toast `Policy confirmed successfully! — You have confirmed "Code of Conduct"` and the card switched to "Confirmed Nov 7, 2026" / "Policy Confirmed — You confirmed this policy on November 7, 2026 at 9:15 PM".
- Dashboard: 0 Confirmed/8 Pending & 0% → 1 Confirmed/7 Pending & 13% → 2 Confirmed/6 Pending & 25%; per-type "Status by Category" Administration 0/2→1/2, Human Resources 0/3→1/3, Finance 0/1, Compliance 0/2. Chart is a ring (`recharts-pie` sector paths with inner radius 60 / outer 80) with segment names `Confirmed` and `Pending`; no `recharts-legend` element exists (legendCount 0).
- Priority/deadline: due Nov 8 (1 day), Nov 9 (2 days), Nov 10 (3 days) → all "High" and sorted to the top of the list; Nov 11/12/14 → "Medium"; Nov 17/21 → "Low". Confirmed entries (Code of Conduct, Remote Work Policy) display no priority tag, only "Confirmed Nov 7, 2026".
- Detail content: pol-001 Code of Conduct (Purpose/Scope/Core Principles/Compliance, 1454+ chars), pol-002 Remote Work Policy (Purpose/Eligibility/Requirements/1. Work Environment…Equipment), pol-005 Expense Reimbursement Policy (Purpose/Eligible Expenses/1. Travel…Non-Reimbursable Items), pol-003 Data Protection & Privacy (Purpose/Scope/Principles/1. Data Minimization…Training), pol-007 Travel & Booking Policy (Purpose/Booking Procedures/Accommodation/Approval) — all distinct and non-placeholder.