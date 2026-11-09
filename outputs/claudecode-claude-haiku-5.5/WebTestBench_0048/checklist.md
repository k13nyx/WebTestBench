# Test Checklist

## Functionality
- [ ] FT-01: Valid user can log in and reach the policy list
  - Action: Enter a valid username and password on the login page, then click "Login".
  - Expected: The policy list page opens and the logged-in user's name is shown in the header.
- [ ] FT-02: Policy list shows each policy's type and confirmation status
  - Action: View the policy list after logging in.
  - Expected: Every default policy appears with its title, one of the four types (Administration / Human Resources / Finance / Compliance), and a status of "Confirmed" or "Pending".
- [ ] FT-03: User can open a policy and read its full content
  - Action: Click the title of any policy in the list.
  - Expected: A detail page opens showing the policy title, type, full body text, and a confirmation control labeled "I have read and understood".
- [ ] FT-04: User can confirm a pending policy
  - Action: On a Pending policy's detail page, tick "I have read and understood" and click "Confirm".
  - Expected: The policy status changes to "Confirmed" on the detail page and in the policy list.
- [ ] FT-05: Personal Center doughnut chart shows the confirmed vs. pending proportion
  - Action: Open "Personal Center" and view the "Confirmation Progress Dashboard".
  - Expected: A doughnut chart is displayed with "Confirmed" and "Pending" segments, and the counts match the statuses shown in the policy list.
- [ ] FT-06: Dashboard breaks down confirmation status by the four policy types
  - Action: In the Personal Center dashboard, view the section for each policy type.
  - Expected: Four sections (Administration, Human Resources, Finance, Compliance) each show confirmed and pending counts, and the four totals equal the overall totals in FT-05.
- [ ] FT-07: User can assign High, Medium, or Low priority to a pending policy
  - Action: Open a Pending policy, select "High" from its priority selector, then select "Medium", then "Low".
  - Expected: Each selection is saved and displayed as the policy's priority tag, and the tag remains after navigating away and returning.
- [ ] FT-08: Policies with a deadline within 3 days are auto-flagged High and pinned to the top
  - Action: Using the default data, view the policy list and locate a Pending policy with a confirmation deadline within 3 days of today.
  - Expected: That policy shows a "High" priority tag without manual selection and appears above all policies without a deadline within 3 days.

## Constraint
- [ ] CS-01: Login is rejected for an incorrect password
  - Action: Enter a valid username with an incorrect password and click "Login".
  - Expected: An error message "Invalid username or password" is shown, and the user remains on the login page.
- [ ] CS-02: Policy cannot be confirmed without the acknowledgment tick
  - Action: On a Pending policy's detail page, leave "I have read and understood" unticked and click "Confirm".
  - Expected: The policy is not confirmed; the status remains "Pending" and a message asks the user to tick the acknowledgment first.
- [ ] CS-03: Confirmed policy cannot be confirmed again
  - Action: Open a policy with status "Confirmed".
  - Expected: The "Confirm" control is absent or disabled, and the status stays "Confirmed".
- [ ] CS-04: Priority tag cannot be set on a Confirmed policy
  - Action: Open a policy with status "Confirmed" and look for the priority selector.
  - Expected: No priority selector is available for the policy, and no priority can be changed.
- [ ] CS-05: Policy pages are not accessible without logging in
  - Action: Log out, then enter the address of a policy detail page directly in the browser address bar.
  - Expected: The user is redirected to the login page and the policy content is not shown.

## Interaction
- [ ] IX-01: Confirmation gives immediate success feedback
  - Action: Confirm a Pending policy as in FT-04.
  - Expected: A toast message "Policy confirmed" appears, and the "Confirm" button changes to a disabled "Confirmed" state without a page reload.
- [ ] IX-02: Dashboard updates after a confirmation without re-login
  - Action: Confirm a Pending policy, then open "Personal Center".
  - Expected: The doughnut chart and the matching policy-type counts reflect the new confirmed count without logging out.
- [ ] IX-03: Hovering a doughnut segment shows its details
  - Action: Move the mouse pointer over the "Pending" segment of the doughnut chart.
  - Expected: A tooltip shows the label "Pending", the item count, and the percentage of total policies.
- [ ] IX-04: Logout ends the session and returns to the login page
  - Action: Click the user menu or "Logout" control in the header.
  - Expected: The user is returned to the login page, and pressing the browser back button does not show the policy list.

## Content
- [ ] CT-01: Each policy's type label matches its subject matter
  - Action: View the policy list and read the title and type label of each policy.
  - Expected: Every policy is labeled with the type that fits its content (e.g., a leave or hiring policy under Human Resources, a spending policy under Finance), with no mislabeled items.
- [ ] CT-02: Policy detail text is complete and readable
  - Action: Open each default policy's detail page and read the body text from start to end.
  - Expected: Text is complete with no truncated sentences, no placeholder text (e.g., "lorem ipsum"), and no broken characters.
- [ ] CT-03: Priority tags and deadlines are shown with the exact labels and date format
  - Action: View the policy list and the detail page of a policy with a confirmation deadline.
  - Expected: Priority tags read exactly "High", "Medium", or "Low", and the deadline is displayed as a visible calendar date on the policy.