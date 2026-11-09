# Test Checklist

## Functionality
- [ ] FT-01: User Login
  - Action: Enter valid employee credentials on the login page and click "Login".
  - Expected: Successfully authenticate and navigate to the internal portal home page.
- [ ] FT-02: Browse Policy and Procedure List
  - Action: Navigate to the policies list page.
  - Expected: Display a list of all company policies and procedures showing title, policy type, priority, and confirmation status.
- [ ] FT-03: Open Policy Details
  - Action: Click on a specific policy item from the list.
  - Expected: Open the policy detail view displaying the complete text and guidelines of the selected policy.
- [ ] FT-04: Confirm Policy Acknowledgment
  - Action: On an unconfirmed policy detail view, click the confirmation button/checkbox stating that the policy has been read and understood.
  - Expected: The confirmation is recorded, and the policy status changes from "Pending" to "Confirmed".
- [ ] FT-05: Access Personal Center Dashboard
  - Action: Click on "Personal Center" in the navigation menu and locate the "Confirmation Progress Dashboard".
  - Expected: The Confirmation Progress Dashboard opens, displaying progress metrics, the doughnut chart, and policy category statuses.

## Constraint
- [ ] CS-01: Prevent Duplicate Confirmation
  - Action: Open a policy item that has already been confirmed.
  - Expected: The confirmation button/control is disabled or hidden, preventing re-confirmation.
- [ ] CS-02: Automatic High-Priority Assignment for Imminent Deadlines
  - Action: Locate a pending policy with a confirmation deadline within 3 days.
  - Expected: The system automatically assigns a "High" priority tag to the item.
- [ ] CS-03: Pinned High-Priority Policies Order
  - Action: View the list of pending policies containing high, medium, and low priority items.
  - Expected: High-priority policies (including auto-flagged deadline policies) are pinned at the top of the list above medium and low priority items.

## Interaction
- [ ] IX-01: Dynamic Status Update upon Confirmation
  - Action: Complete the confirmation step on a pending policy.
  - Expected: Display a success confirmation message and immediately update the status badge from "Pending" to "Confirmed" without reloading the page.
- [ ] IX-02: Doughnut Chart Hover Tooltip
  - Action: Hover the mouse cursor over the "Confirmed" and "Pending" slices of the doughnut chart.
  - Expected: The hovered slice highlights and displays a tooltip showing the exact item count and percentage.
- [ ] IX-03: Filter by Confirmation Status
  - Action: Click between the "Pending" and "Confirmed" status filter options on the policy list.
  - Expected: The policy list dynamically updates to display only items matching the selected status.

## Content
- [ ] CT-01: Doughnut Chart Proportion Accuracy
  - Action: Inspect the doughnut chart in the Confirmation Progress Dashboard.
  - Expected: The chart visually and numerically reflects the exact ratio of confirmed versus pending items for the user.
- [ ] CT-02: Policy Type Categorization Coverage
  - Action: Check the category status breakdown in the Confirmation Progress Dashboard.
  - Expected: Displays confirmation statuses across all four required categories: "Administration", "Human Resources", "Finance", and "Compliance".
- [ ] CT-03: Priority Tag Label Values
  - Action: Review the priority badges displayed across all pending policy items.
  - Expected: Priority labels strictly display one of three values: "High", "Medium", or "Low".
- [ ] CT-04: Confirmation Step Phrasing
  - Action: Inspect the confirmation control area inside an unconfirmed policy document.
  - Expected: The text explicitly states that the user has "read and understood" the policy.