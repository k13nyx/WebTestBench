I have gathered all necessary evidence. Here is the completed test result.

# Test Result

## Functionality

- [X] FT-01: Log in to the internal website with valid credentials
  - Action: Enter a valid username and password on the login page and click "Log In".
  - Expected: User is authenticated and lands on the policy list / home page.
  - Result: Logged in with `admin@company.com` / `admin`; redirected to `http://localhost:6048/dashboard` showing "Welcome, Admin User" and the policy list.

- [X] FT-02: Browse the list of company policies and procedures
  - Action: Open the policy list view.
  - Expected: The default list of policies and procedures is displayed with each item's title and status.
  - Result: Default ("All") list shows 8 policies, each with a title, category badge, a status indicator (clock icon for pending / "Confirmed <date>" for confirmed), priority tag, and due date.

- [X] FT-03: Open a specific policy item to read it
  - Action: Click a policy title in the list.
  - Expected: The policy detail view opens showing the full content (title and body), readable.
  - Result: Clicking "Remote Work Policy" opened `/policy/pol-002` with heading "Remote Work Policy", category + Pending badge, Effective/Updated dates, and full body sections (Purpose, Eligibility, Requirements, Equipment, etc.).

- [X] FT-04: Complete the confirmation step for a policy
  - Action: On an unconfirmed policy detail page, perform the "I have read and understood" confirmation action (check the acknowledgement box and submit).
  - Expected: The policy is recorded as confirmed for the logged-in user.
  - Result: After checking the acknowledgement box and clicking "Confirm Policy", the badge changed to "Confirmed" and the page showed "Policy Confirmed — You confirmed this policy on November 8, 2026 at 1:12 PM".

- [X] FT-05: Distinguish confirmed vs. pending items in the list
  - Action: View the policy list containing both confirmed and unconfirmed items.
  - Expected: Each item clearly shows a Confirmed or Pending status that matches the stored state.
  - Result: Confirmed item ("Remote Work Policy") shows a green check icon and the label "Confirmed Nov 8, 2026"; pending items show a clock (warning) icon and "Due <date>". Status filters (All/Pending/Confirmed) correctly separate them (Confirmed → 1 item, Pending → 7 items).

- [X] FT-06: Confirmation Progress Dashboard shows confirmed/pending proportion via doughnut chart
  - Action: Open the Confirmation Progress Dashboard in the personal center.
  - Expected: A doughnut chart displays the proportion of Confirmed vs. Pending items as two segments with a legend.
  - Result: A Recharts doughnut (annular pie with center label "13% Complete") renders two sectors — success (green, confirmed) and warning (amber, pending) — with a legend reading "1 Confirmed / 7 Pending".

- [X] FT-07: Dashboard categorizes confirmation status by policy type
  - Action: View the dashboard's per-type breakdown.
  - Expected: Confirmation status is grouped and shown for Administration, Human Resources, Finance, and Compliance.
  - Result: "Status by Category" shows Administration 0/2, Human Resources 1/3, Finance 0/1, Compliance 0/2, each with a progress bar.

- [ ] FT-08: Pending items support priority tagging (High / Medium / Low)
  - Action: Assign a priority of High, Medium, or Low to a pending item.
  - Expected: The selected priority tag is applied and displayed on that item.
  - Bug Report:
    - Issue: Missing Feature / No control for priority assignment (read-only display only)
    - Actual: No UI exists anywhere to assign a priority. The High/Medium/Low tags are static read-only badges — they have no `onclick` handler, no `role`, and no dropdown/menu/select (`selects: []`, and the only buttons on the dashboard are "Sign out", "All", "Pending", "Confirmed"). Clicking a priority badge simply navigates to the policy detail (URL changed to `/policy/pol-008`). The policy detail page also has no priority control (only the acknowledgement checkbox and the "Confirm Policy" button). Therefore a priority cannot be manually assigned.

- [X] FT-09: Policies with a deadline within 3 days are auto-marked High priority
  - Action: View a pending item whose confirmation deadline is within 3 days.
  - Expected: The system automatically sets its priority to High without manual action.
  - Result: With today = Nov 8, 2026, the items due Nov 9 (pol-003), Nov 10 (pol-001), and Nov 11 (pol-006) — all within 3 days — are automatically displayed as "High" (with a warning triangle icon), with no manual action taken.

## Constraint

- [X] CS-01: Login rejected for invalid credentials
  - Action: Enter an invalid username or password and click "Log In".
  - Expected: Login is denied with an error message; no access to protected content is granted.
  - Result: Submitted `wrong@company.com` / `wrongpass` → error "Invalid email or password. Try admin@company.com / admin" displayed; remained on `/login` with no access granted.

- [X] CS-02: Cannot confirm without completing the acknowledgement step
  - Action: Attempt to submit the confirmation on a policy without checking the "I have read and understood" acknowledgement.
  - Expected: Submission is blocked (disabled/submit rejected) and the item remains Pending.
  - Result: On the pending detail page the "Confirm Policy" button has `disabled: true` while the checkbox is unchecked; it only became enabled after the acknowledgement box was checked.

- [ ] CS-03: Auto-high override wins over manual priority tag
  - Action: Manually set a within-3-days-deadline pending item to Low, then reload.
  - Expected: The item is displayed as High priority (automatic rule takes precedence).
  - Bug Report:
    - Issue: Test action cannot be performed — no manual priority control exists (Missing Feature)
    - Actual: There is no way to manually set a pending item to "Low"; priority tags are non-interactive read-only badges (see FT-08), so the required setup ("manually set … to Low") is impossible. Additionally, a full page reload cannot be used as the step requires, because the session is held only in memory: navigating directly to `http://localhost:6048/policy/pol-002` (a full document load) immediately redirected to `/login`, i.e., a reload logs the user out. The auto-high precedence therefore could not be verified.

- [X] CS-04: Deadline boundary correctly separates auto-high from normal
  - Action: Compare a pending item with deadline within 3 days against one with deadline beyond 3 days.
  - Expected: Only the within-3-days item is auto-marked High; the other keeps its manual/default priority.
  - Result: Within 3 days → High (Nov 9 pol-003, Nov 10 pol-001, Nov 11 pol-006). Beyond 3 days → normal defaults, not High (Nov 12 pol-008 Medium, Nov 13 pol-005 Medium, Nov 15 pol-002 Medium, Nov 18 pol-007 Low, Nov 22 pol-004 Low). Only the ≤3-day items are High.

## Interaction

- [X] IX-01: Success feedback shown after completing confirmation
  - Action: Submit the read-and-understood confirmation on a pending item.
  - Expected: A success notification (toast/message) confirms the item was recorded.
  - Result: A toast appeared: "Policy confirmed successfully! — You have confirmed 'Remote Work Policy'".

- [X] IX-02: Dashboard and status refresh immediately after confirming
  - Action: Confirm a policy, then return to the list and the dashboard.
  - Expected: The item shows Confirmed and the doughnut chart/type breakdown reflects the updated counts without a manual reload.
  - Result: Using in-app "Back to Dashboard" navigation (no reload), the dashboard updated to "13% Complete / 1 Confirmed / 7 Pending", Human Resources changed from 0/3 to 1/3, and the list moved "Remote Work Policy" to the bottom labeled "Confirmed Nov 8, 2026".

- [X] IX-03: Auto-high items are pinned to the top of the list
  - Action: Open the pending policy list containing a within-3-days-deadline item.
  - Expected: The auto-high item appears at the top of the list, above lower-priority pending items.
  - Result: The three High (auto, within-3-days) items — Code of Conduct, Data Protection & Privacy, Information Security Policy — appear first, above the Medium items (Expense Reimbursement, Annual Leave, Remote Work) and Low items (Anti-Harassment, Travel & Booking).

## Content

- [X] CT-01: Policy types match the required four categories
  - Action: Inspect the type labels used in the list and dashboard.
  - Expected: Exactly Administration, Human Resources, Finance, and Compliance are used, with no other/incorrect categories.
  - Result: Only these four categories appear, both in the dashboard "Status by Category" and on list/detail badges (Administration, Human Resources, Finance, Compliance). No extra/incorrect categories observed.

- [X] CT-02: Priority labels match the required three levels
  - Action: Inspect priority labels on pending items.
  - Expected: Only High, Medium, and Low tags are used, spelled and displayed correctly.
  - Result: Only "High", "Medium", and "Low" tags are used, correctly spelled/displayed.

- [X] CT-03: Displayed content is relevant to company policies and procedures
  - Action: Review the titles and body text of listed items.
  - Expected: All content is genuine company policy/procedure material relevant to the stated purpose.
  - Result: Titles and bodies are genuine policy material (e.g., Code of Conduct, Remote Work Policy, Annual Leave Policy, Expense Reimbursement, Data Protection & Privacy, Information Security), each with meaningful sections (Purpose, Requirements, etc.) and Effective/Updated dates.

---

### Summary
- **Passed:** 15 / 17
- **Failed:** 2 — **FT-08** (no manual priority-assignment control; tags are read-only) and **CS-03** (its manual-set prerequisite is impossible without that control, and a page reload logs the user out since auth is not persisted).

**Notable secondary observation (not a checklist item):** A full-page reload/URL navigation does not preserve the session — directly loading a protected URL (`/policy/pol-002`) redirects to `/login`, because authentication is held only in memory rather than in persistent storage.