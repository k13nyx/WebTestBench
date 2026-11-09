# Test Result

## Functionality

- [X] FT-01: User can log in to the internal website with valid credentials.
  - Action: Enter valid login credentials and select **“Log In.”**
  - Expected: The user is authenticated and taken to the policy list or personal center.

- [X] FT-02: User can browse the available company policies and procedures.
  - Action: Open the policy list after logging in.
  - Expected: The list displays the available policy and procedure items with their titles and confirmation status.

- [X] FT-03: User can open a specific policy or procedure.
  - Action: Select any policy from the list.
  - Expected: A detail view opens and displays the selected policy’s complete content.

- [X] FT-04: User can confirm that a policy has been read and understood.
  - Action: Open a pending policy, complete the read-and-understood confirmation step, and submit it.
  - Expected: The policy is recorded as confirmed for the logged-in user.

- [X] FT-05: User can view confirmed and pending policies in the personal center.
  - Action: Open the personal center after confirming at least one policy.
  - Expected: Policies are separated or clearly identified as **Confirmed** or **Pending**.

- [X] FT-06: Confirmation status persists after leaving and returning to the page.
  - Action: Confirm a policy, navigate away from the policy list, then return to it.
  - Expected: The policy remains marked **Confirmed** and is not shown as pending.

## Constraint

- [X] CS-01: Invalid login credentials do not grant access.
  - Action: Enter invalid credentials and select **“Log In.”**
  - Expected: Access is denied, an authentication error is displayed, and protected policy content remains inaccessible.

- [X] CS-02: Each policy has one current confirmation state.
  - Action: Review the status of a policy in the list and personal center.
  - Expected: The same policy is not simultaneously marked both **Confirmed** and **Pending**.

- [X] CS-03: Pending policies display only the supported priority levels.
  - Action: Review pending policies in the policy list.
  - Expected: Each priority tag shown for a pending policy is exactly one of **High**, **Medium**, or **Low**.

- [X] CS-04: Policies with confirmation deadlines within three days are automatically high priority.
  - Action: Review a pending policy whose confirmation deadline is within three days.
  - Expected: The policy is automatically tagged **High** without user assignment.

- [X] CS-05: Automatically high-priority deadline policies are pinned above other policies.
  - Action: Open the policy list when at least one pending policy has a deadline within three days.
  - Expected: Every qualifying high-priority deadline policy appears above non-qualifying policies.

## Interaction

- [X] IX-01: The interface provides confirmation feedback after submission.
  - Action: Submit the read-and-understood confirmation for a pending policy.
  - Expected: A visible success state or message confirms that the policy was recorded.

- [X] IX-02: The confirmation dashboard updates after a policy is confirmed.
  - Action: Confirm one pending policy and open or refresh the personal center.
  - Expected: The confirmed count increases, the pending count decreases, and the policy status changes accordingly.

- [X] IX-03: The personal center displays a confirmed-versus-pending doughnut chart.
  - Action: Open the **Confirmation Progress Dashboard** in the personal center.
  - Expected: A doughnut chart displays distinct **Confirmed** and **Pending** segments.

- [X] IX-04: The doughnut chart proportions match the user’s policy statuses.
  - Action: Compare the chart segments with the number of confirmed and pending policies.
  - Expected: The chart proportions represent the actual confirmed-to-pending distribution.

- [X] IX-05: The dashboard shows confirmation status by policy type.
  - Action: Review the policy-type section of the Confirmation Progress Dashboard.
  - Expected: Status information is separately categorized for **Administration**, **Human Resources**, **Finance**, and **Compliance**.

## Content

- [X] CT-01: Policy items display relevant and complete policy information.
  - Action: Compare a policy’s list entry with its detail view.
  - Expected: The title, policy type, content, deadline information, and confirmation status in the detail view correspond to the selected list item.

- [X] CT-02: Policy-type labels use the required category names.
  - Action: Review category labels in the policy list and dashboard.
  - Expected: The applicable labels are clearly presented as **Administration**, **Human Resources**, **Finance**, or **Compliance**, with no unrelated policy categories shown.