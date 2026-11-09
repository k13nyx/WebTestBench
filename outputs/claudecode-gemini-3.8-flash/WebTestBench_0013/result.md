# Test Result

## Functionality
- [X] FT-01: Save personal availability profile
  - Action: Navigate to "Availability Profile", enter working hours (e.g., "09:00 - 17:00"), set break times (e.g., "12:00 - 13:00"), select "Wednesday" under "Days Never Meet", and click "Save Profile".
  - Expected: Profile settings are saved and display the updated working hours, break periods, and no-meeting days.
- [X] FT-02: Create meeting with date range and participants
  - Action: Fill in meeting title, select a date range, enter participant names and email addresses, and click "Generate Slots".
  - Expected: Meeting is created and the system navigates to the candidate time slots review page.
- [ ] FT-03: Generate slots respecting known participant profiles
  - Action: Create a meeting including known participants who have saved profile preferences.
  - Expected: Generated slots only include times within all known participants' working hours and exclude their configured break times and no-meeting days.
  - Bug Report:
    - Issue: Break Times Not Excluded from Generated Slots
    - Actual: Generated candidate time slots include times overlapping with and falling within configured break times (such as 12:00 PM - 1:00 PM and 1:00 PM - 2:00 PM) rather than excluding them.
- [X] FT-04: Generate slots using generic business hours for unknown participants
  - Action: Create a meeting including an email address that has no existing user profile.
  - Expected: System applies default business hours (e.g., 09:00 - 17:00, Monday-Friday) for the unknown participant when proposing time slots.
- [X] FT-05: Mark specific time slot as "Preferred"
  - Action: On the participant availability view, click the "Preferred" button on a candidate time slot and click "Submit Preferences".
  - Expected: Slot is saved as preferred, and the slot's ranking score increases in the candidate list.
- [X] FT-06: Mark specific time slot as "Last Resort"
  - Action: On the participant availability view, click the "Last Resort" button on a candidate time slot and click "Submit Preferences".
  - Expected: Slot is saved as last resort, and the slot is downgraded in the candidate list ranking.
- [X] FT-07: Display ranked candidate time slots
  - Action: Open the organizer view after participants submit their slot adjustments.
  - Expected: Candidate time slots are displayed in order from highest-scored to lowest-scored based on preferences.
- [X] FT-08: Confirm selected meeting time slot
  - Action: Select a candidate time slot from the ranked list and click "Confirm Meeting".
  - Expected: Meeting status updates to "Confirmed", and the chosen time is locked as the finalized meeting time.
- [X] FT-09: Reopen confirmed meeting
  - Action: On a confirmed meeting page, click the "Reopen Meeting" button.
  - Expected: Meeting status reverts to "Open", allowing the organizer to select and confirm a different candidate time slot.

## Constraint
- [X] CS-01: Exclude "Days Never Meet" from generated slots
  - Action: Generate meeting slots across a date range that includes days marked as "Never Meet" by a known participant.
  - Expected: No candidate time slots are generated or proposed on those excluded days.
- [ ] CS-02: Exclude typical break times from generated slots
  - Action: Inspect generated time slots for participants who configured break times (e.g., 12:00 - 13:00).
  - Expected: No candidate time slots overlap with or start during the defined break times.
  - Bug Report:
    - Issue: Candidate Time Slots Overlap with Break Times
    - Actual: Candidate time slots were generated that overlap with and start during configured break times (e.g., 11:30 AM - 12:30 PM, 12:00 PM - 1:00 PM, 12:30 PM - 1:30 PM, and 1:00 PM - 2:00 PM).
- [ ] CS-03: Validate required fields on meeting creation
  - Action: Leave the meeting title or date range blank and click "Generate Slots".
  - Expected: Form submission is blocked, and validation error messages appear under the missing required fields.
  - Bug Report:
    - Issue: Missing Field Validation Error Messages
    - Actual: While form progression is blocked via a disabled "Next" button, no validation error messages appear under the missing required fields when left blank.
- [ ] CS-04: Prevent confirmation without slot selection
  - Action: Click "Confirm Meeting" without selecting any candidate time slot from the list.
  - Expected: Confirmation action is disabled or blocked with an alert stating "Please select a time slot to confirm".
  - Bug Report:
    - Issue: Missing Confirmation Validation and Alert
    - Actual: No general "Confirm Meeting" action or slot selection validation exists; instead, each slot has an individual inline "Confirm" button, and no alert stating "Please select a time slot to confirm" is provided.

## Interaction
- [X] IX-01: Dynamic participant list management
  - Action: Click "+ Add Participant" to append a new input row, fill in details, then click the "Delete" icon on that row.
  - Expected: A new name and email field row appears immediately on add, and is removed from the form upon clicking delete.
- [X] IX-02: Slot preference button state toggle
  - Action: Click between "Available", "Preferred", and "Last Resort" buttons on a single slot card.
  - Expected: The active selection highlights immediately, deselecting previous states with corresponding visual styling.
- [ ] IX-03: Reopen meeting confirmation prompt
  - Action: Click the "Reopen Meeting" button on a confirmed meeting.
  - Expected: A modal dialog appears asking the user to confirm reopening before the meeting state changes.
  - Bug Report:
    - Issue: Missing Reopen Confirmation Modal Dialog
    - Actual: Clicking the "Reopen" button immediately changes the meeting status without displaying a confirmation modal dialog.

## Content
- [ ] CT-01: Candidate slot conflict and overlap indicators
  - Action: View candidate slots where participants have conflicting schedules or partial availability.
  - Expected: Relevant badges ("Conflict", "Partial Overlap", or "Tied Score") are clearly displayed on each affected slot card.
  - Bug Report:
    - Issue: Missing "Partial Overlap" Badge and Inaccurate Badge Text
    - Actual: The application does not render "Partial Overlap" badges for candidate slots with partial availability, and displays "Tied" instead of "Tied Score".
- [ ] CT-02: Known vs. unknown participant identification
  - Action: View the participant list in the meeting creation/details view containing both registered and unregistered users.
  - Expected: Known participants display a "Profile Linked" label, while unregistered emails display a "Generic Hours" label.
  - Bug Report:
    - Issue: Incorrect Participant Identification Labels
    - Actual: Known participants display a "Known" badge instead of "Profile Linked", and unregistered emails display an "External" badge instead of "Generic Hours".
- [X] CT-03: Confirmed meeting summary display
  - Action: View a confirmed meeting page.
  - Expected: The page prominently displays "Status: Confirmed", the selected date and time, and the list of participating attendees.