# Test Checklist

## Functionality
- [ ] FT-01: User can log in to the internal policies site with valid credentials
  - Action: Open the site, enter the default valid username and password in the login form, submit.
  - Expected: Login succeeds, the user is taken into the policies site and the logged-in user/session is shown (not the login form).
- [ ] FT-02: User can browse the list of company policies and procedures
  - Action: After login, view the main policy list.
  - Expected: A list of the default policies/procedures is displayed, each with its title.
- [ ] FT-03: User can open a specific policy item and read its content
  - Action: Click the title/link of any policy item in the list.
  - Expected: A detail view opens showing that policy's title and full body content.
- [ ] FT-04: User can complete the read-and-understood confirmation step for a policy
  - Action: In an open policy's detail view, perform the confirmation action (acknowledging "I have read and understood").
  - Expected: The confirmation is recorded for that policy and the item is recognized as confirmed.
- [ ] FT-05: User can see which items are already confirmed and which are still pending
  - Action: Return to the policy list and/or personal center after confirming one item.
  - Expected: The confirmed policy is shown with a confirmed status and the remaining items are shown as pending for the user.
- [ ] FT-06: Confirmation Progress Dashboard is reachable from the personal center
  - Action: Open the personal center and locate the "Confirmation Progress Dashboard" entry, then open it.
  - Expected: The dashboard view loads, linked from the personal center.
- [ ] FT-07: Dashboard displays a doughnut chart of confirmed vs pending proportion
  - Action: On the dashboard, locate the progress chart.
  - Expected: A doughnut (ring) chart is rendered showing the confirmed portion and the pending portion of the user's items.
- [ ] FT-08: Dashboard categorizes confirmation status by policy type
  - Action: On the dashboard, inspect the per-type breakdown.
  - Expected: Confirmation status is shown separately for Administration, Human Resources, Finance, and Compliance categories.
- [ ] FT-09: Pending items display priority tags
  - Action: Open the pending items list and inspect a pending policy.
  - Expected: Each pending item shows a priority tag of High, Medium, or Low.

## Constraint
- [ ] CS-01: Login rejects invalid credentials
  - Action: Enter an incorrect username and/or password and submit the login form.
  - Expected: Login is refused, an error message is shown, and the user stays on the login page with no session created.
- [ ] CS-02: Confirmation cannot be recorded until the acknowledgement is explicitly given
  - Action: Open a pending policy and attempt to confirm without ticking/selecting the "I have read and understood" acknowledgement.
  - Expected: The confirm/submit action stays unavailable or is rejected with a prompt to acknowledge; no confirmation is recorded.
- [ ] CS-03: Policies with a confirmation deadline within 3 days are automatically tagged High priority
  - Action: Identify a default policy whose confirmation deadline is within 3 days and inspect its priority tag.
  - Expected: Its priority tag is automatically set to High, with no manual tagging step required.
- [ ] CS-04: Policies with a near-deadline are pinned to the top of the list
  - Action: View the policy list and check the ordering of items relative to a deadline-bound policy (e.g., within 3 days).
  - Expected: The near-deadline policy appears above other pending items at the top of the list.
- [ ] CS-05: Priority tags apply only to pending items
  - Action: Inspect the status of a policy that has already been confirmed.
  - Expected: It shows a confirmed status (not a priority tag), and no pending-only priority labelling contradicts its confirmed state.

## Interaction
- [ ] IX-01: Confirming a policy gives clear success feedback
  - Action: Complete the confirmation step on an open policy.
  - Expected: A visible success confirmation message/toast appears indicating the policy was confirmed.
- [ ] IX-02: Dashboard updates immediately after a new confirmation
  - Action: Open the dashboard, note the confirmed/pending figures, then confirm one more pending policy and return to the dashboard.
  - Expected: The doughnut chart proportions and the per-type confirmed/pending counts reflect the new confirmation.
- [ ] IX-03: Selecting a policy type on the dashboard shows that type's status
  - Action: Click a policy type category (Administration / Human Resources / Finance / Compliance) in the dashboard breakdown.
  - Expected: The status detail for that policy type is shown (e.g., which items are confirmed vs pending in that category).

## Content
- [ ] CT-01: Policy list entries show accurate identifying information
  - Action: Inspect each default entry in the policy list.
  - Expected: Each entry shows its policy title, its policy type (Administration / Human Resources / Finance / Compliance), and its current confirmation status; all text is legible and not truncated or placeholder.
- [ ] CT-02: Opened policy shows its complete, relevant body content
  - Action: Open each policy type's policy detail view.
  - Expected: The view shows the full policy text corresponding to that item (not empty, not another policy's text, not generic placeholder copy).
- [ ] CT-03: Dashboard labels and legend correctly name confirmed/pending and the policy types
  - Action: Inspect the doughnut chart legend, segment labels, and per-type breakdown headings.
  - Expected: The labels explicitly read "Confirmed" and "Pending", and the breakdown headings use exactly Administration, Human Resources, Finance, and Compliance with correct confirmed/pending counts per type.