# Test Checklist

## Functionality

- [ ] FT-01: Search doctors by specialty
  - Action: On the doctor search page, select a specialty from the "Specialty" filter (e.g., the first listed option) and apply the search.
  - Expected: Only doctors whose specialty matches the selected filter are listed (count > 0), and each result's displayed specialty matches the filter.

- [ ] FT-02: Search doctors by symptom
  - Action: Enter or select a symptom (e.g., the first symptom option available) in the symptom search/filter and run the search.
  - Expected: Result list contains only doctors associated with that symptom; each result relates to the searched symptom; no unrelated doctors appear.

- [ ] FT-03: Doctor profile shows experience and consultation fee
  - Action: Open a doctor's profile from the search results.
  - Expected: Profile displays labeled "Years of Experience" (numeric) and "Consultation Fee" (amount with currency) values.

- [ ] FT-04: Compare doctor profiles by experience and fee
  - Action: Select two doctors from the results (e.g., via "Compare" on each card) and open the comparison view.
  - Expected: Both doctors appear side by side, each showing years of experience and consultation fee, with values matching their individual profiles.

- [ ] FT-05: Book an appointment and pay the consultation fee during booking
  - Action: From a doctor's profile, pick an available future date/time slot, proceed to booking, complete the payment step, and confirm.
  - Expected: Payment is accepted and a new appointment appears as "Confirmed"/"Booked" with that doctor, date and time; charged amount equals the doctor's displayed consultation fee.

- [ ] FT-06: Cancel a booked appointment
  - Action: Open the upcoming appointment created in FT-05 (or any existing upcoming appointment) and choose "Cancel".
  - Expected: Appointment status changes to "Cancelled" and it no longer appears as an active upcoming booking.

- [ ] FT-07: Appointment history displays visit notes
  - Action: In the personal center, open "Appointment History" (or Past appointments) and open a completed appointment's details.
  - Expected: Past appointments are listed in date order; each completed appointment detail shows non-empty visit notes recorded by the doctor.

- [ ] FT-08: Follow-up instructions shown after a session
  - Action: Open the details of a completed appointment from the history.
  - Expected: Doctor's follow-up instructions for that session are displayed (care/medication guidance), attributed to that session's doctor and distinct from the visit notes.

- [ ] FT-09: Mark a follow-up task as completed
  - Action: In personal center → Follow-up section, open the follow-up plan of a completed session, mark one incomplete task as completed, and save.
  - Expected: That task's status becomes "Completed" and stays "Completed" after refreshing the page.

- [ ] FT-10: Upload physical sign data in the follow-up section
  - Action: In the same Follow-up section, enter a blood pressure value (e.g., 120/80) and a blood glucose value (e.g., 95), then submit.
  - Expected: Both entries are saved and appear in the physical sign records list with the entered values and the submission date.

- [ ] FT-11: Doctor views patient progress in real time and adjusts the follow-up plan
  - Action: Open the doctor-side view of that same patient's follow-up record; check the task marked in FT-09 and the signs uploaded in FT-10 appear without re-entry; then edit the follow-up plan (add or modify a task) and save.
  - Expected: Doctor view shows the patient's current completion status and uploaded signs exactly as submitted; after saving, the patient's Follow-up section shows the updated task list.

## Constraint

- [ ] CS-01: An already occupied time slot cannot be booked
  - Action: Attempt to book a date/time slot that is already booked or shown as unavailable for a doctor.
  - Expected: The slot cannot be booked — it is disabled or the booking is rejected with a message; no duplicate appointment is created.

- [ ] CS-02: Booking is not confirmed without successful payment
  - Action: Start a booking and use a payment that fails or is declined (or abandon the payment step), then check the appointment list.
  - Expected: No confirmed appointment exists for that slot; it remains unpaid/pending or is absent from appointments.

- [ ] CS-03: A completed or already cancelled appointment cannot be cancelled again
  - Action: Open a past/completed appointment, then an already-cancelled appointment, from the history.
  - Expected: No active "Cancel" action is available for either (hidden or disabled); their statuses remain "Completed" and "Cancelled".

- [ ] CS-04: Invalid physical sign values are rejected
  - Action: In the Follow-up physical sign form, submit a non-numeric value (e.g., "abc") or a negative/empty value and try to save.
  - Expected: Save is blocked with a visible validation message and no invalid entry is added to the records list.

## Interaction

- [ ] IX-01: Doctor list updates dynamically when filters change
  - Action: With the doctor list displayed, change the specialty or symptom filter, then clear it.
  - Expected: List refreshes to the matching doctors without a full page reload (no blank or broken state); clearing filters restores the full default doctor list.

- [ ] IX-02: Confirmation feedback for booking, payment and cancellation
  - Action: Complete a booking with payment, then cancel an appointment.
  - Expected: A success/confirmation message (toast or banner) appears after booking and payment confirming the appointment, and another after cancellation confirming it was cancelled.

## Content

- [ ] CT-01: Doctor cards and profiles contain relevant, complete medical content
  - Action: Review the doctor cards in search results and one doctor profile page.
  - Expected: Each card shows doctor name, specialty and a photo/avatar that loads correctly and depicts a person/doctor (no broken image or unrelated placeholder imagery).

- [ ] CT-02: Visit notes and follow-up instructions belong to the correct appointment
  - Action: Open the details of two different completed appointments from history.
  - Expected: Each shows notes and follow-up instructions specific to that appointment and its doctor (content differs across different sessions); no "lorem ipsum" or unrelated placeholder text.

- [ ] CT-03: Physical sign records are labeled with correct units and dates
  - Action: Review the physical sign records list in the Follow-up section after FT-10.
  - Expected: Entries are labeled "Blood Pressure" (mmHg) and "Blood Glucose" (mg/dL or mmol/L) with correct units, and each entry shows the date it was recorded.