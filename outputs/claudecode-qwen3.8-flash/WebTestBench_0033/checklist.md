# Test Checklist

## Functionality
- [ ] FT-01: Patient can search doctors by specialty
  - Action: On the doctor search page, enter/select a specialty (e.g., "Cardiology") and submit the search.
  - Expected: A results list is returned showing only doctors whose specialty matches the selected value.

- [ ] FT-02: Patient can search doctors by symptom
  - Action: Enter a symptom keyword (e.g., "headache") in the symptom search field and submit.
  - Expected: Results list doctors who treat that symptom, and the matched symptom is visible on each result.

- [ ] FT-03: Search results allow comparison of experience and fees
  - Action: Run any specialty/symptom search and inspect the result cards/rows.
  - Expected: Each result simultaneously displays the doctor's years of experience and consultation fee (with currency), so profiles can be compared side by side; opening a profile shows the same values in full detail.

- [ ] FT-04: Patient can book an appointment with a chosen doctor
  - Action: From a doctor profile, click "Book Appointment", pick an available date/time slot, complete the patient/consultation details, and submit.
  - Expected: Booking is accepted and a new appointment with doctor name, date, time, and status "Booked"/"Upcoming" is created.

- [ ] FT-05: Consultation payment is taken during the booking flow
  - Action: Proceed through booking to the payment step, enter valid payment details, and confirm.
  - Expected: A payment step is presented before confirmation, showing the exact consultation fee of that doctor, and payment is marked as completed for the appointment.

- [ ] FT-06: Patient can cancel an existing appointment
  - Action: Open the booked appointment and click "Cancel Appointment", then confirm.
  - Expected: The appointment status changes to "Cancelled" and the slot is released; no completed/past appointment is deletable.

- [ ] FT-07: Appointment history is visible to the patient
  - Action: Open the patient's personal center → "Appointment History".
  - Expected: A list of past appointments is shown with date, doctor, specialty, status, and payment status.

- [ ] FT-08: Visit notes are available per completed consultation
  - Action: In appointment history, open the detail of a consultation with status "Completed".
  - Expected: The doctor's visit notes for that session are displayed and are non-empty.

- [ ] FT-09: Follow-up instructions appear after each completed session
  - Action: Open the follow-up section for a completed appointment.
  - Expected: Doctor-issued follow-up instructions for that session are shown (e.g., medication/diet guidance), tied to that specific appointment.

- [ ] FT-10: Patient can mark follow-up task completion status
  - Action: In personal center → Follow-up, toggle a follow-up task item to "Done"/"Completed".
  - Expected: The task's status changes and persists after reload, with an overall completion count/percentage shown.

- [ ] FT-11: Patient can upload physical sign values in the follow-up section
  - Action: In Follow-up, submit a blood pressure reading (e.g., 120/80) and a blood glucose value (e.g., 5.6), then save.
  - Expected: Records are stored with the entered values and a date/time stamp, and appear in the patient's measurement list.

- [ ] FT-12: Doctor can view patient progress and adjust the follow-up plan
  - Action: Log in as the doctor and open the assigned patient's follow-up dashboard; edit a follow-up task/instruction and save.
  - Expected: The doctor sees the patient's per-task completion status and uploaded vitals, and the saved plan change is immediately reflected in the patient's follow-up section.

## Constraint
- [ ] CS-01: A time slot already booked cannot be booked again
  - Action: Attempt to book a slot that is already occupied for that doctor.
  - Expected: The slot is shown as unavailable/unselectable, and submitting is blocked with an "already booked" or equivalent error.

- [ ] CS-02: Booking cannot be completed without required information or payment
  - Action: Submit the booking form with a required field left empty, then with the payment step skipped.
  - Expected: Booking is rejected in both cases and an inline error names the missing field / unpaid consultation; no appointment record is created.

- [ ] CS-03: Only future, non-cancelled appointments can be cancelled
  - Action: Attempt to cancel an appointment that is already Cancelled, and one whose date is in the past.
  - Expected: No cancel action is offered/accepted for either, and their statuses remain unchanged.

- [ ] CS-04: Physical sign input is validated
  - Action: Enter non-numeric or out-of-range values (e.g., blood glucose "abc" or "-5") and save.
  - Expected: Save is rejected with a validation message identifying the invalid field, and no malformed record is stored.

## Interaction
- [ ] IX-01: Feedback is shown after a successful booking
  - Action: Complete a booking with payment.
  - Expected: A visible confirmation (toast or confirmation screen) states the booking succeeded and shows the booked date/time; the UI reflects the new appointment without a manual reload.

- [ ] IX-02: Cancellation requires confirmation and updates state everywhere
  - Action: Click "Cancel Appointment" on a booked appointment.
  - Expected: A confirmation dialog appears first; after confirming, the status badge in history updates to "Cancelled" and cancelling from the dialog (dismiss) leaves the appointment intact.

- [ ] IX-03: Task progress syncs live between patient and doctor views
  - Action: Mark a follow-up task complete as the patient, then refresh/open the doctor's dashboard for that patient.
  - Expected: The doctor's view shows that task as completed and the aggregate progress bar/count increases accordingly.

## Content
- [ ] CT-01: Default doctor dataset is present and on-theme
  - Action: Load the search page with no filters applied.
  - Expected: Multiple pre-existing doctor profiles are listed, each with a telemedicine-relevant specialty, experience, consultation fee, and treated symptoms; no placeholder/lorem text or broken avatar images.

- [ ] CT-02: Default appointments carry coherent clinical content
  - Action: Inspect the seeded history, visit notes, follow-up instructions, and vitals of the default patient account.
  - Expected: Each entry is consistent and relevant to its appointment (notes/instructions match the doctor and specialty shown), with no empty required fields or contradictory dates/statuses.