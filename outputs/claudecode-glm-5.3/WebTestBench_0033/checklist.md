# Test Checklist

## Functionality

- [ ] FT-01: Patient can search for doctors by specialty
  - Action: Open the doctor search page, select or type a specialty (e.g., "Cardiology") from the default data, and run the search.
  - Expected: A result list is returned showing only doctors whose listed specialty matches "Cardiology".

- [ ] FT-02: Patient can search for doctors by symptoms
  - Action: On the doctor search page, enter a symptom (e.g., "chest pain" or "headache") into the symptom search field and run the search.
  - Expected: A result list is returned showing doctors whose profile indicates they treat the entered symptom.

- [ ] FT-03: Patient can compare doctor profiles with experience and consultation fees
  - Action: From search results, select two or more doctors and open the compare view.
  - Expected: A side-by-side comparison displays each doctor's name, specialty, years of experience, and consultation fee.

- [ ] FT-04: Patient can book an online appointment
  - Action: From a doctor's profile, pick an available date/time slot and confirm the booking.
  - Expected: The appointment is created and appears in the patient's upcoming appointments with the selected doctor, date, and time.

- [ ] FT-05: Patient can pay for the consultation during booking
  - Action: During the booking flow, complete the payment step with valid payment details matching the doctor's consultation fee.
  - Expected: Payment succeeds and the appointment status shows as paid/confirmed with the correct fee amount.

- [ ] FT-06: Patient can cancel a booked appointment
  - Action: Open an existing upcoming appointment and click the cancel button, confirming the cancellation.
  - Expected: The appointment is removed from upcoming appointments (or marked "Cancelled") and no longer occupies the time slot.

- [ ] FT-07: Patient can view appointment history with visit notes
  - Action: Open the appointment history section in the patient's personal center.
  - Expected: Past appointments are listed with doctor name, date, and each completed consultation shows its visit notes.

- [ ] FT-08: Patient receives follow-up instructions from the doctor after each session
  - Action: Open the follow-up section for a completed consultation.
  - Expected: Follow-up instructions written by the doctor for that session (e.g., medication reminders, activity tasks) are displayed.

- [ ] FT-09: Patient can mark follow-up task completion status
  - Action: In the follow-up section of the personal center, click the completion checkbox/toggle for an unfinished follow-up task.
  - Expected: The task status changes to completed and the overall follow-up completion progress reflects the update.

- [ ] FT-10: Patient can upload physical sign data (blood pressure, blood glucose)
  - Action: In the follow-up section, fill in blood pressure (e.g., "120/80") and blood glucose (e.g., "5.6 mmol/L") values and submit.
  - Expected: The submitted values are saved and displayed in the patient's follow-up sign data list with correct values and timestamps.

- [ ] FT-11: Doctor can view patient task completion progress in real time and adjust the follow-up plan
  - Action: In the doctor's patient follow-up view, open the patient's follow-up plan; then have the patient mark a task complete (or use default progress data) and, from the doctor side, edit the plan (e.g., add or modify a follow-up task) and save.
  - Expected: The doctor's view shows the patient's task completion progress and uploaded sign data; the saved plan changes appear in the patient's follow-up section.

## Constraint

- [ ] CS-01: Appointment is not confirmed without successful payment
  - Action: Start a booking and attempt to confirm with empty or invalid payment details (e.g., blank card number or failed payment).
  - Expected: The booking is not confirmed, no appointment is created, and an error message about payment is shown.

- [ ] CS-02: Already-booked time slot cannot be double-booked
  - Action: Attempt to book the same doctor for a time slot that is already booked (use a slot occupied by an existing appointment in default data).
  - Expected: The slot is shown as unavailable and the booking is rejected; the slot remains booked by the original appointment.

- [ ] CS-03: Physical sign data cannot be submitted with missing or invalid values
  - Action: In the sign data upload form, leave a required field empty or enter non-numeric text (e.g., "abc") and submit.
  - Expected: The submission is rejected with a validation message, and no invalid entry is added to the sign data list.

- [ ] CS-04: A completed consultation appointment cannot be cancelled
  - Action: From appointment history, open a completed (past) appointment and check for a cancel option.
  - Expected: No cancel action is available for completed appointments; only upcoming appointments can be cancelled.

## Interaction

- [ ] IX-01: Booking confirmation feedback is shown after successful payment
  - Action: Complete a booking with valid payment.
  - Expected: A success toast/message confirms the booking and payment (e.g., "Appointment booked successfully") and the appointment appears in upcoming appointments.

- [ ] IX-02: Cancellation requires confirmation before taking effect
  - Action: Click the cancel button on an upcoming appointment.
  - Expected: A confirmation dialog appears; the appointment is cancelled only after confirming, and feedback (e.g., "Appointment cancelled") is shown.

- [ ] IX-03: Task completion toggle updates progress display immediately
  - Action: Toggle a follow-up task's completion status on and off.
  - Expected: The task's visual state (checkbox/icon) and the follow-up completion progress (e.g., "2/5 tasks completed") update instantly without page errors.

- [ ] IX-04: Doctor's progress view reflects patient updates without requiring re-login or manual refresh
  - Action: With the doctor's patient progress view open, have the patient mark a task complete or upload sign data.
  - Expected: The doctor's view updates the completion progress and sign data (immediately or on next view load) without the patient data being lost or stale.

## Content

- [ ] CT-01: Doctor search results match the queried specialty or symptom
  - Action: Review the result lists from FT-01 and FT-02 searches.
  - Expected: Every listed doctor's profile (name, specialty, title) is relevant to the searched specialty/symptom, with no unrelated doctors shown.

- [ ] CT-02: Visit notes in appointment history match their consultations
  - Action: Open a past appointment from history and read its visit notes.
  - Expected: The visit notes contain coherent, medically relevant content for that consultation (doctor, date, and reason consistent with the appointment record).

- [ ] CT-03: Follow-up instructions and sign data are relevant and accurately displayed
  - Action: Check the follow-up section for a completed session, including the doctor's instructions and uploaded sign data entries.
  - Expected: Instructions are relevant to that consultation's theme, and uploaded blood pressure/blood glucose values are displayed exactly as submitted with correct units (e.g., mmHg, mmol/L).