# Test Result

## Functionality
- [X] FT-01: User can log in with valid credentials
  - Action: Open the site login page and submit the form with valid employee credentials.
  - Expected: Login succeeds and the user lands on the policies/procedures list page.
  - Verified: `admin@company.com` / `admin` (demo credentials) → redirected to `/dashboard`, which displays the full policy list (8 items) with the Confirmation Progress panel and "Welcome, Admin User".

- [X] FT-02: Logged-in user can browse the full list of policies and procedures
  - Action: View the main list page after login.
  - Expected: All default policy items are displayed, each showing its title and policy type (Administration / Human Resources / Finance / Compliance).
  - Verified: All 8 policies rendered as links (`pol-001`…`pol-008`), each with its category label and title: Code of Conduct (Administration), Remote Work (HR), Data Protection (Compliance), Anti-Harassment (HR), Expense Reimbursement (Finance), Information Security (Compliance), Travel & Booking (Administration), Annual Leave (HR). Totals match category breakdowns (Admin 2, HR 3, Finance 1, Compliance 2).

- [X] FT-03: User can open a specific policy to read its full content
  - Action: Click on one policy item from the list.
  - Expected: A detail view opens showing the complete policy text (not just the title), with an option to return to the list.
  - Verified: Clicking "Remote Work Policy" opened `/policy/pol-002` with full sections (Purpose, Eligibility, Requirements 1–4, Equipment, effective/updated dates) and a "Back to Dashboard" link.

- [X] FT-04: User can confirm a pending policy as "read and understood"
  - Action: Open a pending policy, select the "I have read and understood" acknowledgment, and submit/click Confirm.
  - Expected: The item's status changes to Confirmed for this user.
  - Verified: Checkbox "I have read and understood this policy…" checked → "Confirm Policy" button enabled → after click, detail badge changed from "Pending" to "Confirmed" and a panel "Policy Confirmed — You confirmed this policy on November 8, 2026 at 11:31 AM" appeared.

- [X] FT-05: User can distinguish confirmed vs. pending items in the list
  - Action: Inspect the status indicator (badge/column or Confirmed/Pending view) on list items after completing at least one confirmation.
  - Expected: Confirmed and pending items are each clearly labeled, and the counts match the user's actual state.
  - Verified: Confirmed card shows circle-check icon + text "Confirmed Nov 8, 2026"; pending cards show clock icon + due date/priority; Status filter views returned exactly 1 item under "confirmed" and 7 under "pending", matching the "1 Confirmed / 7 Pending" dashboard counts.

- [X] FT-06: Personal center contains the Confirmation Progress Dashboard with a doughnut chart
  - Action: Navigate to the personal center / dashboard area.
  - Expected: A doughnut chart is rendered showing confirmed vs. pending proportions.
  - Verified: `/dashboard` "Confirmation Progress" card contains a Recharts doughnut (`svg.recharts-surface` → `.recharts-pie` sectors with outer radius 80 / inner radius 60) plus center label ("0% Complete" → "13% Complete") and legend "Confirmed / Pending".

- [X] FT-07: Doughnut chart proportions match the actual confirmed/pending counts
  - Action: Count confirmed and pending items in the list, then compare with the chart segments/legend values.
  - Expected: Chart proportions (e.g., 60% confirmed / 40% pending) match the real counts.
  - Verified: With 1 confirmed / 7 pending in the list, the doughnut rendered exactly two sectors — name="Confirmed" (success color) and name="Pending" (warning color) — legend showed "1 Confirmed / 7 Pending" and center label "13% Complete" (1/8 = 12.5%, rounded).

- [X] FT-08: Dashboard shows confirmation status categorized by policy type
  - Action: View the breakdown section of the dashboard.
  - Expected: Confirmed/pending status is displayed separately for Administration, Human Resources, Finance, and Compliance.
  - Verified: "Status by Category" section lists Administration 0/2, Human Resources 1/3 (after one HR confirmation; initially 0/3), Finance 0/1, Compliance 0/2, each with its own progress bar.

- [X] FT-09: Pending items display priority tags (High / Medium / Low)
  - Action: Inspect pending items in the list.
  - Expected: Each pending item shows a priority tag with exactly "High", "Medium", or "Low" wording.
  - Verified: All 7 pending cards showed exactly "High" (3), "Medium" (2), or "Low" (2) tag text; data module contains no static `priority` field (tags are computed).

- [X] FT-10: Deadline-near policies are automatically marked High and pinned to the top
  - Action: View the list containing a policy with a confirmation deadline within 3 days.
  - Expected: That policy is tagged "High" automatically and appears pinned at the top of the list, above non-deadline items.
  - Verified: Today = Nov 8, 2026. The three policies with deadlines within 3 days — Data Protection (Nov 9), Code of Conduct (Nov 10), Information Security (Nov 11) — are all tagged "High" (with triangle-alert icons) and occupy list positions 1–3, above all later-deadline items.

## Constraint
- [X] CS-01: Unauthenticated users cannot access policy content
  - Action: Try to open the policy list, a policy detail page, or the dashboard URL directly while logged out.
  - Expected: Access is blocked and the user is redirected to the login page.
  - Verified: Direct navigations to `/dashboard` and `/policy/pol-001` while logged out both resolved to `http://localhost:6048/login` (Sign in form shown; no policy content rendered).

- [X] CS-02: Confirmation requires the explicit "read and understood" acknowledgment
  - Action: Attempt to submit confirmation on a pending policy without checking/acknowledging the "I have read and understood" control.
  - Expected: Submission is rejected (button disabled or validation message) and the item stays Pending.
  - Verified: On the unchecked pending policy, the "Confirm Policy" button had the `[disabled]` attribute; it only became clickable after checking the acknowledgment. Item remained "Pending" until confirmation.

- [X] CS-03: Already-confirmed items cannot be confirmed again
  - Action: Open a policy whose status is Confirmed.
  - Expected: The confirmation control is absent or disabled; no double-confirmation is possible.
  - Verified: After confirming, the checkbox and "Confirm Policy" button were removed entirely and replaced with a "Policy Confirmed / You confirmed this policy on November 8, 2026 at 11:31 AM" panel.

- [X] CS-04: Auto High-priority rule applies only within the deadline window
  - Action: Compare a policy with a deadline ≤ 3 days against one with no deadline / a distant deadline.
  - Expected: Only the ≤3-day policy is auto-tagged High and pinned; the other retains its assigned tag and normal position.
  - Verified: Deadlines Nov 9/10/11 (≤3 days) → auto "High" + pinned at top. Annual Leave (Nov 12, 4 days out) → "Medium" in position 5; Anti-Harassment (Nov 22) and Travel & Booking (Nov 18) → "Low", not pinned. No High tag appears on any item beyond the 3-day window.

- [X] CS-05: Confirmation state persists across sessions
  - Action: Confirm a pending policy, then reload the page (and/or log out and log back in).
  - Expected: The item remains Confirmed and is excluded from the pending count/list.
  - Verified: After full page reload (session ended → re-login required), pol-002 still showed "Confirmed Nov 8, 2026", the dashboard still read "1 Confirmed / 7 Pending / 13% Complete", HR still 1/3, and the pending filter listed only 7 items (Remote Work excluded).

## Interaction
- [X] IX-01: Success feedback is shown after a confirmation is submitted
  - Action: Complete FT-04's confirmation submission.
  - Expected: A visible success message/toast (e.g., "Confirmed" / "Marked as read and understood") appears.
  - Verified: Toast appeared in the notifications region: "Policy confirmed successfully! You have confirmed \"Remote Work Policy\"".

- [X] IX-02: List status and dashboard update immediately after confirming
  - Action: From the pending list, confirm an item without a manual page reload; then open the dashboard.
  - Expected: The item's badge switches to Confirmed in place and the doughnut chart reflects the new ratio.
  - Verified: Via in-app navigation only (no reload), the detail badge flipped to "Confirmed", and returning to the dashboard showed the doughnut with a new Confirmed sector, center label "13% Complete", and legend "1 Confirmed / 7 Pending".

- [X] IX-03: Doughnut chart conveys values on hover/legend
  - Action: Hover over the Confirmed and Pending segments (or their legend entries) of the doughnut chart.
  - Expected: Tooltip/legend displays the segment label and its value or percentage.
  - Verified: Hovering the Confirmed segment rendered a Recharts tooltip "Confirmed : 1"; the adjacent legend entries explicitly display "1 Confirmed" and "7 Pending" (label + value) for both segments.

## Content
- [X] CT-01: Policy types and content match the four required categories
  - Action: Review type labels on the dashboard/filter and each policy's category and body text.
  - Expected: Only the four exact categories (Administration / Human Resources / Finance / Compliance) are used, and every policy detail shows substantive text relevant to its title (no placeholder/lorem content).
  - Verified: Dashboard, category filter, cards, and data source use only the exact four labels. Imported `/src/data/policies.ts`: all 8 policies carry one of the four categories and substantive, title-relevant bodies (437–1,361 chars each, structured Purpose/Requirements sections, e.g., Code of Conduct → "fundamental principles and standards of behavior…", Expense Reimbursement → "guidelines for employees seeking reimbursement for legitimate business expenses"). No "lorem ipsum", "placeholder", "TODO", or "TBD" strings found.
