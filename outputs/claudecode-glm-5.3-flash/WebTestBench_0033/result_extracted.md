# Test Result

## Functionality
- [X] FT-01: Doctor search by specialty
  - Action: Select a specialty (e.g., "Cardiology") from the search filter and run the search.
  - Expected: The results list shows only doctors whose specialty matches the selected one.
- [X] FT-02: Doctor search by symptom
  - Action: Enter a symptom (e.g., "chest pain") in the symptom search field and search.
  - Expected: Results include doctors relevant to that symptom (e.g., cardiologists); irrelevant doctors are excluded.
- [X] FT-03: Doctor profile comparison
  - Action: Open the doctor list, select at least two doctors (checkboxes or "Compare" buttons), and trigger the compare view.
  - Expected: A comparison view displays the selected doctors side by side with experience (years) and consultation fee for each.
- [X] FT-04: Book an online appointment with payment
  - Action: Pick an available time slot for a doctor, fill in patient info, choose a payment method, and submit the booking.
  - Expected: Booking is confirmed with a success message showing appointment details and paid consultation fee.
- [X] FT-05: Cancel an appointment
  - Action: Open the appointment history, select an upcoming appointment, and click "Cancel".
  - Expected: The appointment status changes to "Cancelled" and it no longer appears as an active appointment.
- [X] FT-06: View appointment history with visit notes
  - Action: Open the appointment history page in the patient's personal center.
  - Expected: Each past appointment shows date, doctor, and the doctor's visit notes; completed visits have follow-up instructions from the doctor.
- [X] FT-07: View follow-up tasks in personal center
  - Action: Open the follow-up section of the personal center after a completed visit.
  - Expected: The follow-up plan from the doctor is shown as a list of tasks (e.g., medication, check-up items).
- [ ] FT-08: Mark task completion status
  - Action: Toggle/check a follow-up task (e.g., "Take medication") to mark it complete.
  - Expected: The task's status updates to "Completed" and remains so after page reload.
  - Bug Report:
    - Issue: Data not persisted after page reload
    - Actual: Marking "Get adequate rest (7-8 hours sleep)" as complete worked in-session (status changed to "Completed: 11/8/2026", progress updated 71% → 86%, 6/7). However, after a full page reload of /my-health, the task reverted to "Pending" and progress returned to 71% (5/7). The app stores no state (localStorage/sessionStorage are empty), so task completion does not survive a page reload.
- [X] FT-09: Upload physical sign data
  - Action: In the follow-up section, enter a physical sign value (e.g., blood pressure "120/80" or blood glucose "5.5 mmol/L") and submit.
  - Expected: The record is saved and displayed in the physical sign data list with the entered value and timestamp.
- [X] FT-10: Doctor views patient task progress in real time
  - Action: Log in as a doctor, open the patient follow-up management view for the patient who completed tasks/uploaded data.
  - Expected: The doctor sees the patient's task completion progress (completed/total tasks) and the uploaded physical sign values.

## Constraint
- [ ] CS-01: Cannot book an already-booked time slot
  - Action: Have one patient book a slot, then attempt to book the same doctor and time slot with another patient account.
  - Expected: Booking is rejected with an error message (e.g., "This time slot is no longer available"); no second booking is created.
  - Bug Report:
    - Issue: Missing uniqueness/double-booking validation
    - Actual: After booking Dr. Sarah Mitchell for Mon, Nov 9 at 10:00 AM (booking confirmed, "$150 • paid"), the same doctor/slot remained selectable in a new booking flow. The second booking was accepted and a success toast "Appointment Booked! Your appointment with Dr. Sarah Mitchell is confirmed." was shown again. My Appointments then listed TWO separate "upcoming / $150 • paid" appointments for the identical slot (Nov 9, 2026, 10:00 AM). No error or rejection occurred. (Note: the app has no account/login system, so the second booking was made in the same session as the only available means to re-attempt the slot.)
- [X] CS-02: Cannot book a past time slot
  - Action: Attempt to select a date/time earlier than the current date/time during booking.
  - Expected: The past slot is not selectable, or submission is blocked with a validation message.
- [X] CS-03: Booking cannot be submitted without required fields/payment
  - Action: Leave required fields empty (or skip payment selection) and submit the booking form.
  - Expected: Submission is blocked with clear validation messages for each missing required field.
- [ ] CS-04: Physical sign values must be valid
  - Action: Enter invalid physical sign values (e.g., blood pressure "abc", blood glucose "-5") and submit.
  - Expected: Submission is rejected with an error; no invalid record is saved.
  - Bug Report:
    - Issue: Missing input validation
    - Actual: With Measurement Type "Blood Pressure", entering value "abc" and clicking "Record Measurement" succeeded: toast "Vital sign recorded successfully" appeared, the counter incremented 5 → 6, and the record "Blood Pressure: abc mmHg, 11/8/2026, 8:51:15 AM" was added to the Recent Measurements list. No validation error was shown and the invalid record was saved.
- [X] CS-05: Cancelled appointments cannot be cancelled again or re-counted
  - Action: Cancel an appointment, then attempt to cancel it again (or verify its state in history).
  - Expected: The system prevents duplicate cancellation (button disabled or error shown), and status stays "Cancelled".

## Interaction
- [ ] IX-01: Search results update response
  - Action: Perform a specialty or symptom search.
  - Expected: A loading indicator appears during the search, and results (or an explicit "no results found" message) are shown without page errors.
  - Bug Report:
    - Issue: Missing loading indicator
    - Actual: Search results themselves update correctly and an explicit empty state is shown for no matches ("0 doctors found / No doctors found / Try adjusting your filters or search query") with no page errors. However, no loading indicator ever appears: DOM polling (sampling for `[class*="spin"]`, `[class*="loading"]`, `[role="status"]`, `[aria-busy]` every animation frame for 1.5 s during a name search) found zero loading/spinner elements at any moment — filtering is instantaneous client-side with no loading feedback.
- [X] IX-02: Payment feedback after booking
  - Action: Complete a booking with payment.
  - Expected: A success toast/message appears confirming payment and booking (e.g., "Payment successful, appointment confirmed").
- [X] IX-03: Follow-up plan updates after patient action
  - Action: While the doctor's patient view is open, mark a task complete or upload new physical sign data as the patient.
  - Expected: The doctor's view reflects the updated completion progress / new data without requiring the doctor to re-login (refresh of the view is acceptable).

## Content
- [X] CT-01: Doctor profile data integrity
  - Action: Open several doctor profiles from search results.
  - Expected: Each profile shows realistic and consistent information: name, specialty, years of experience, consultation fee, and are relevant to a telemedicine context (no placeholder text like "Lorem ipsum").
- [X] CT-02: Visit notes and instructions relevance
  - Action: Open appointment history and inspect visit notes / follow-up instructions.
  - Expected: Notes and instructions contain medically plausible content matching the appointment's specialty/symptoms (not generic or empty where a completed visit exists).
