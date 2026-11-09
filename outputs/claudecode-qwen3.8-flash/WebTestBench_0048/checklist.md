# Test Checklist

## Functionality
- [ ] FT-01: User can log in with valid credentials
  - Action: Open the site login page and submit the form with valid employee credentials.
  - Expected: Login succeeds and the user lands on the policies/procedures list page.

- [ ] FT-02: Logged-in user can browse the full list of policies and procedures
  - Action: View the main list page after login.
  - Expected: All default policy items are displayed, each showing its title and policy type (Administration / Human Resources / Finance / Compliance).

- [ ] FT-03: User can open a specific policy to read its full content
  - Action: Click on one policy item from the list.
  - Expected: A detail view opens showing the complete policy text (not just the title), with an option to return to the list.

- [ ] FT-04: User can confirm a pending policy as "read and understood"
  - Action: Open a pending policy, select the "I have read and understood" acknowledgment, and submit/click Confirm.
  - Expected: The item's status changes to Confirmed for this user.

- [ ] FT-05: User can distinguish confirmed vs. pending items in the list
  - Action: Inspect the status indicator (badge/column or Confirmed/Pending view) on list items after completing at least one confirmation.
  - Expected: Confirmed and pending items are each clearly labeled, and the counts match the user's actual state.

- [ ] FT-06: Personal center contains the Confirmation Progress Dashboard with a doughnut chart
  - Action: Navigate to the personal center / dashboard area.
  - Expected: A doughnut chart is rendered showing confirmed vs. pending proportions.

- [ ] FT-07: Doughnut chart proportions match the actual confirmed/pending counts
  - Action: Count confirmed and pending items in the list, then compare with the chart segments/legend values.
  - Expected: Chart proportions (e.g., 60% confirmed / 40% pending) match the real counts.

- [ ] FT-08: Dashboard shows confirmation status categorized by policy type
  - Action: View the breakdown section of the dashboard.
  - Expected: Confirmed/pending status is displayed separately for Administration, Human Resources, Finance, and Compliance.

- [ ] FT-09: Pending items display priority tags (High / Medium / Low)
  - Action: Inspect pending items in the list.
  - Expected: Each pending item shows a priority tag with exactly "High", "Medium", or "Low" wording.

- [ ] FT-10: Deadline-near policies are automatically marked High and pinned to the top
  - Action: View the list containing a policy with a confirmation deadline within 3 days.
  - Expected: That policy is tagged "High" automatically and appears pinned at the top of the list, above non-deadline items.

## Constraint
- [ ] CS-01: Unauthenticated users cannot access policy content
  - Action: Try to open the policy list, a policy detail page, or the dashboard URL directly while logged out.
  - Expected: Access is blocked and the user is redirected to the login page.

- [ ] CS-02: Confirmation requires the explicit "read and understood" acknowledgment
  - Action: Attempt to submit confirmation on a pending policy without checking/acknowledging the "I have read and understood" control.
  - Expected: Submission is rejected (button disabled or validation message) and the item stays Pending.

- [ ] CS-03: Already-confirmed items cannot be confirmed again
  - Action: Open a policy whose status is Confirmed.
  - Expected: The confirmation control is absent or disabled; no double-confirmation is possible.

- [ ] CS-04: Auto High-priority rule applies only within the deadline window
  - Action: Compare a policy with a deadline ≤ 3 days against one with no deadline / a distant deadline.
  - Expected: Only the ≤3-day policy is auto-tagged High and pinned; the other retains its assigned tag and normal position.

- [ ] CS-05: Confirmation state persists across sessions
  - Action: Confirm a pending policy, then reload the page (and/or log out and log back in).
  - Expected: The item remains Confirmed and is excluded from the pending count/list.

## Interaction
- [ ] IX-01: Success feedback is shown after a confirmation is submitted
  - Action: Complete FT-04's confirmation submission.
  - Expected: A visible success message/toast (e.g., "Confirmed" / "Marked as read and understood") appears.

- [ ] IX-02: List status and dashboard update immediately after confirming
  - Action: From the pending list, confirm an item without a manual page reload; then open the dashboard.
  - Expected: The item's badge switches to Confirmed in place and the doughnut chart reflects the new ratio.

- [ ] IX-03: Doughnut chart conveys values on hover/legend
  - Action: Hover over the Confirmed and Pending segments (or their legend entries) of the doughnut chart.
  - Expected: Tooltip/legend displays the segment label and its value or percentage.

## Content
- [ ] CT-01: Policy types and content match the four required categories
  - Action: Review type labels on the dashboard/filter and each policy's category and body text.
  - Expected: Only the four exact categories (Administration / Human Resources / Finance / Compliance) are used, and every policy detail shows substantive text relevant to its title (no placeholder/lorem content).