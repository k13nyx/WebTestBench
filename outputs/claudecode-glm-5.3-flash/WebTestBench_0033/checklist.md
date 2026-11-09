# Test Checklist

## Functionality
- [ ] FT-01: Doctor search by specialty
  - Action: Select a specialty (e.g., "Cardiology") from the search filter and run the search.
  - Expected: The results list shows only doctors whose specialty matches the selected one.
- [ ] FT-02: Doctor search by symptom
  - Action: Enter a symptom (e.g., "chest pain") in the symptom search field and search.
  - Expected: Results include doctors relevant to that symptom (e.g., cardiologists); irrelevant doctors are excluded.
- [ ] FT-03: Doctor profile comparison
  - Action: Open the doctor list, select at least two doctors (checkboxes or "Compare" buttons), and trigger the compare view.
  - Expected: A comparison view displays the selected doctors side by side with experience (years) and consultation fee for each.
- [ ] FT-04: Book an online appointment with payment
  - Action: Pick an available time slot for a doctor, fill in patient info, choose a payment method, and submit the booking.
  - Expected: Booking is confirmed with a success message showing appointment details and paid consultation fee.
- [ ] FT-05: Cancel an appointment
  - Action: Open the appointment history, select an upcoming appointment, and click "Cancel".
  - Expected: The appointment status changes to "Cancelled" and it no longer appears as an active appointment.
- [ ] FT-06: View appointment history with visit notes
  - Action: Open the appointment history page in the patient's personal center.
  - Expected: Each past appointment shows date, doctor, and the doctor's visit notes; completed visits have follow-up instructions from the doctor.
- [ ] FT-07: View follow-up tasks in personal center
  - Action: Open the follow-up section of the personal center after a completed visit.
  - Expected: The follow-up plan from the doctor is shown as a list of tasks (e.g., medication, check-up items).
- [ ] FT-08: Mark task completion status
  - Action: Toggle/check a follow-up task (e.g., "Take medication") to mark it complete.
  - Expected: The task's status updates to "Completed" and remains so after page reload.
- [ ] FT-09: Upload physical sign data
  - Action: In the follow-up section, enter a physical sign value (e.g., blood pressure "120/80" or blood glucose "5.5 mmol/L") and submit.
  - Expected: The record is saved and displayed in the physical sign data list with the entered value and timestamp.
- [ ] FT-10: Doctor views patient task progress in real time
  - Action: Log in as a doctor, open the patient follow-up management view for the patient who completed tasks/uploaded data.
  - Expected: The doctor sees the patient's task completion progress (completed/total tasks) and the uploaded physical sign values.

## Constraint
- [ ] CS-01: Cannot book an already-booked time slot
  - Action: Have one patient book a slot, then attempt to book the same doctor and time slot with another patient account.
  - Expected: Booking is rejected with an error message (e.g., "This time slot is no longer available"); no second booking is created.
- [ ] CS-02: Cannot book a past time slot
  - Action: Attempt to select a date/time earlier than the current date/time during booking.
  - Expected: The past slot is not selectable, or submission is blocked with a validation message.
- [ ] CS-03: Booking cannot be submitted without required fields/payment
  - Action: Leave required fields empty (or skip payment selection) and submit the booking form.
  - Expected: Submission is blocked with clear validation messages for each missing required field.
- [ ] CS-04: Physical sign values must be valid
  - Action: Enter invalid physical sign values (e.g., blood pressure "abc", blood glucose "-5") and submit.
  - Expected: Submission is rejected with an error; no invalid record is saved.
- [ ] CS-05: Cancelled appointments cannot be cancelled again or re-counted
  - Action: Cancel an appointment, then attempt to cancel it again (or verify its state in history).
  - Expected: The system prevents duplicate cancellation (button disabled or error shown), and status stays "Cancelled".

## Interaction
- [ ] IX-01: Search results update response
  - Action: Perform a specialty or symptom search.
  - Expected: A loading indicator appears during the search, and results (or an explicit "no results found" message) are shown without page errors.
- [ ] IX-02: Payment feedback after booking
  - Action: Complete a booking with payment.
  - Expected: A success toast/message appears confirming payment and booking (e.g., "Payment successful, appointment confirmed").
- [ ] IX-03: Follow-up plan updates after patient action
  - Action: While the doctor's patient view is open, mark a task complete or upload new physical sign data as the patient.
  - Expected: The doctor's view reflects the updated completion progress / new data without requiring the doctor to re-login (refresh of the view is acceptable).

## Content
- [ ] CT-01: Doctor profile data integrity
  - Action: Open several doctor profiles from search results.
  - Expected: Each profile shows realistic and consistent information: name, specialty, years of experience, consultation fee, and are relevant to a telemedicine context (no placeholder text like "Lorem ipsum").
- [ ] CT-02: Visit notes and instructions relevance
  - Action: Open appointment history and inspect visit notes / follow-up instructions.
  - Expected: Notes and instructions contain medically plausible content matching the appointment's specialty/symptoms (not generic or empty where a completed visit exists).