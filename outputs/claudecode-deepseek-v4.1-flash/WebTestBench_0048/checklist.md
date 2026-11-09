# Test Checklist

## Functionality
- [ ] FT-01: Log in to the internal website with valid credentials
  - Action: Enter a valid username and password on the login page and click "Log In".
  - Expected: User is authenticated and lands on the policy list / home page.

- [ ] FT-02: Browse the list of company policies and procedures
  - Action: Open the policy list view.
  - Expected: The default list of policies and procedures is displayed with each item's title and status.

- [ ] FT-03: Open a specific policy item to read it
  - Action: Click a policy title in the list.
  - Expected: The policy detail view opens showing the full content (title and body), readable.

- [ ] FT-04: Complete the confirmation step for a policy
  - Action: On an unconfirmed policy detail page, perform the "I have read and understood" confirmation action (check the acknowledgement box and submit).
  - Expected: The policy is recorded as confirmed for the logged-in user.

- [ ] FT-05: Distinguish confirmed vs. pending items in the list
  - Action: View the policy list containing both confirmed and unconfirmed items.
  - Expected: Each item clearly shows a Confirmed or Pending status that matches the stored state.

- [ ] FT-06: Confirmation Progress Dashboard shows confirmed/pending proportion via doughnut chart
  - Action: Open the Confirmation Progress Dashboard in the personal center.
  - Expected: A doughnut chart displays the proportion of Confirmed vs. Pending items as two segments with a legend.

- [ ] FT-07: Dashboard categorizes confirmation status by policy type
  - Action: View the dashboard's per-type breakdown.
  - Expected: Confirmation status is grouped and shown for Administration, Human Resources, Finance, and Compliance.

- [ ] FT-08: Pending items support priority tagging (High / Medium / Low)
  - Action: Assign a priority of High, Medium, or Low to a pending item.
  - Expected: The selected priority tag is applied and displayed on that item.

- [ ] FT-09: Policies with a deadline within 3 days are auto-marked High priority
  - Action: View a pending item whose confirmation deadline is within 3 days.
  - Expected: The system automatically sets its priority to High without manual action.

## Constraint
- [ ] CS-01: Login rejected for invalid credentials
  - Action: Enter an invalid username or password and click "Log In".
  - Expected: Login is denied with an error message; no access to protected content is granted.

- [ ] CS-02: Cannot confirm without completing the acknowledgement step
  - Action: Attempt to submit the confirmation on a policy without checking the "I have read and understood" acknowledgement.
  - Expected: Submission is blocked (disabled/submit rejected) and the item remains Pending.

- [ ] CS-03: Auto-high override wins over manual priority tag
  - Action: Manually set a within-3-days-deadline pending item to Low, then reload.
  - Expected: The item is displayed as High priority (automatic rule takes precedence).

- [ ] CS-04: Deadline boundary correctly separates auto-high from normal
  - Action: Compare a pending item with deadline within 3 days against one with deadline beyond 3 days.
  - Expected: Only the within-3-days item is auto-marked High; the other keeps its manual/default priority.

## Interaction
- [ ] IX-01: Success feedback shown after completing confirmation
  - Action: Submit the read-and-understood confirmation on a pending item.
  - Expected: A success notification (toast/message) confirms the item was recorded.

- [ ] IX-02: Dashboard and status refresh immediately after confirming
  - Action: Confirm a policy, then return to the list and the dashboard.
  - Expected: The item shows Confirmed and the doughnut chart/type breakdown reflects the updated counts without a manual reload.

- [ ] IX-03: Auto-high items are pinned to the top of the list
  - Action: Open the pending policy list containing a within-3-days-deadline item.
  - Expected: The auto-high item appears at the top of the list, above lower-priority pending items.

## Content
- [ ] CT-01: Policy types match the required four categories
  - Action: Inspect the type labels used in the list and dashboard.
  - Expected: Exactly Administration, Human Resources, Finance, and Compliance are used, with no other/incorrect categories.

- [ ] CT-02: Priority labels match the required three levels
  - Action: Inspect priority labels on pending items.
  - Expected: Only High, Medium, and Low tags are used, spelled and displayed correctly.

- [ ] CT-03: Displayed content is relevant to company policies and procedures
  - Action: Review the titles and body text of listed items.
  - Expected: All content is genuine company policy/procedure material relevant to the stated purpose.