# Test Checklist

## Functionality
- [ ] FT-01: Search doctors by specialty
  - Action: On the doctor search page, select a specialty (e.g., "Cardiology") from the specialty filter and submit the search.
  - Expected: The result list shows only doctors belonging to the selected specialty.

- [ ] FT-02: Search doctors by symptoms
  - Action: Enter a symptom keyword (e.g., "headache") in the symptom search field and submit.
  - Expected: The result list shows doctors relevant to the entered symptom, with no empty/blank results page error.

- [ ] FT-03: View comparable doctor profile details
  - Action: Open the doctor search results list and inspect each doctor entry/profile.
  - Expected: Each doctor entry displays the doctor's name, specialty, years of experience, and consultation fee so they can be compared side by side.

- [ ] FT-04: Book an appointment with payment
  - Action: Select an available doctor, choose a date/time slot, proceed to booking, complete the consultation fee payment, and confirm.
  - Expected: The appointment is created with status "Booked/Confirmed" and the payment is recorded as successful for the exact consultation fee shown.

- [ ] FT-05: Cancel an existing appointment
  - Action: Open an upcoming appointment from the appointment list and click the cancel option.
  - Expected: The appointment status changes to "Cancelled" and it no longer appears as an upcoming appointment.

- [ ] FT-06: View appointment history with visit notes
  - Action: Open the appointment history section of the personal center.
  - Expected: Past appointments are listed with date, doctor, status, and a visit note accessible for each completed visit.

- [ ] FT-07: Receive follow-up instructions after a session
  - Action: Open a completed appointment record.
  - Expected: Follow-up instructions written by the doctor are displayed for that session.

- [ ] FT-08: Mark follow-up task completion status
  - Action: In the follow-up section of the personal center, toggle a follow-up task's status to completed.
  - Expected: The task is saved and displayed as completed, and the change persists after reloading the page.

- [ ] FT-09: Upload physical sign data
  - Action: In the follow-up section, enter a blood pressure value (e.g., 120/80) and a blood glucose value, then save/upload them.
  - Expected: Both values are saved and appear in the follow-up section as uploaded records with their entered values.

- [ ] FT-10: Doctor views patient task progress in real time
  - Action: As the patient, mark a follow-up task complete; then, as the doctor, open the patient's follow-up progress view.
  - Expected: The doctor sees the updated task completion progress reflecting the patient's latest change without needing a manual data re-entry.

## Constraint
- [ ] CS-01: Cannot book without completing payment
  - Action: Start booking an appointment but abandon/abort the payment step before paying.
  - Expected: No appointment is created (or it is not confirmed), and the slot is not blocked as booked.

- [ ] CS-02: Cannot cancel an already-cancelled or past appointment
  - Action: Attempt to cancel an appointment that is already cancelled or already completed.
  - Expected: The cancel action is unavailable or rejected, and the appointment status remains unchanged.

- [ ] CS-03: Invalid physical sign values are rejected
  - Action: In the follow-up section, enter a non-numeric or negative value (e.g., blood pressure "-50") and save.
  - Expected: The input is rejected with a validation error, and no invalid record is saved.

## Interaction
- [ ] IX-01: Search results update after applying a filter
  - Action: Change the specialty filter or clear the symptom keyword on the search page.
  - Expected: The result list refreshes immediately to reflect the new criteria, showing a loading state or updated list rather than stale results.

- [ ] IX-02: Success confirmation after booking and after cancellation
  - Action: Complete a booking, then cancel an appointment.
  - Expected: A visible success confirmation (e.g., toast/message) appears after each action stating the booking was confirmed and the appointment was cancelled respectively.

## Content
- [ ] CT-01: Doctor profile content is complete and relevant
  - Action: Open several doctor profiles from search results.
  - Expected: Each profile shows a relevant doctor photo/avatar, specialty description, experience summary, and consultation fee with no placeholder text, broken images, or unrelated content.

- [ ] CT-02: Visit notes and follow-up instructions are readable and relevant
  - Action: Open visit notes and follow-up instructions for past appointments.
  - Expected: The text is non-empty, legible, medically relevant to the visited specialty, and contains no lorem-ipsum or template placeholder content.