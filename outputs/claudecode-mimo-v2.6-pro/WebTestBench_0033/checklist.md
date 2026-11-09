# Test Checklist

## Functionality
- [ ] FT-01: Search doctors by specialty returns matching doctors.
  - Action: On the doctor search page, select a specialty (e.g., "Cardiology") from the specialty filter and submit the search.
  - Expected: A doctor list is displayed containing only doctors whose specialty matches the selected one.

- [ ] FT-02: Search doctors by symptom returns matching doctors.
  - Action: Enter a symptom (e.g., "headache") into the symptom search field and submit.
  - Expected: A doctor list is displayed containing doctors relevant to the entered symptom.

- [ ] FT-03: Patient can compare doctor profiles side by side.
  - Action: Select two doctors from the search results and click the "Compare" action.
  - Expected: A comparison view appears showing both doctors' experience and consultation fees next to each other.

- [ ] FT-04: Patient can book an online appointment with a doctor.
  - Action: Open a doctor's profile, select an available time slot, and click "Book Appointment".
  - Expected: The appointment is created and appears in the patient's appointment list with status "Booked".

- [ ] FT-05: Patient can pay the consultation fee during booking.
  - Action: During the booking flow, on the payment step, enter payment details and click "Pay".
  - Expected: Payment completes and the booking is confirmed with a paid status showing the doctor's consultation fee amount.

- [ ] FT-06: Patient can cancel a booked appointment.
  - Action: Open an existing booked (upcoming) appointment and click "Cancel Appointment".
  - Expected: The appointment status changes to "Cancelled" and it no longer appears as an upcoming appointment.

- [ ] FT-07: Patient can view appointment history with visit notes.
  - Action: Navigate to "Appointment History" in the personal center and open a past appointment.
  - Expected: The appointment record is displayed with its date, doctor, and the doctor's visit notes for that session.

- [ ] FT-08: Patient can view follow-up instructions after a session.
  - Action: Open a completed appointment's follow-up section in the personal center.
  - Expected: The doctor's follow-up instructions for that session are displayed as text.

- [ ] FT-09: Patient can mark follow-up task completion status.
  - Action: In the personal center's follow-up section, toggle a follow-up task (e.g., "Take medication daily") to completed.
  - Expected: The task's status changes to "Completed" and is saved in the follow-up list.

- [ ] FT-10: Patient can upload physical sign data in the follow-up section.
  - Action: In the follow-up section, click "Upload Sign Data", enter a blood pressure value (e.g., 120/80) and a blood glucose value (e.g., 5.6), and submit.
  - Expected: The entered blood pressure and blood glucose values are saved and listed in the patient's sign data records.

- [ ] FT-11: Doctor can view a patient's task completion progress.
  - Action: As a doctor, open a patient's follow-up page from the doctor dashboard.
  - Expected: The patient's follow-up tasks are listed with their completion status/progress (e.g., 2 of 4 completed).

- [ ] FT-12: Doctor can adjust the patient's follow-up plan.
  - Action: On the patient's follow-up page, click "Adjust Plan", modify a task or instruction, and save.
  - Expected: The updated follow-up plan is saved and shown on the patient's follow-up section.

## Constraint
- [ ] CS-01: An unavailable time slot cannot be booked.
  - Action: Attempt to book a time slot that is already booked (marked unavailable) for a doctor.
  - Expected: Booking is rejected with a message indicating the slot is unavailable; no appointment is created.

- [ ] CS-02: Booking cannot be completed without payment.
  - Action: Complete the booking flow but skip/exit the payment step without paying.
  - Expected: The appointment is not confirmed; the system requires payment before finalizing the booking.

- [ ] CS-03: A completed (past) appointment cannot be cancelled.
  - Action: Open an appointment with status "Completed" and attempt to click "Cancel Appointment".
  - Expected: Cancellation is not allowed (button disabled or action rejected); the appointment remains "Completed".

- [ ] CS-04: Invalid physical sign values are rejected on upload.
  - Action: In "Upload Sign Data", leave blood pressure/blood glucose empty or enter a non-numeric value (e.g., "abc") and submit.
  - Expected: Submission is rejected with a validation message; no invalid sign data record is saved.

## Interaction
- [ ] IX-01: Booking confirmation feedback is shown after successful payment.
  - Action: Complete payment during booking and observe the page.
  - Expected: A success confirmation (message or toast) is displayed indicating the appointment is booked and paid.

- [ ] IX-02: Doctor's progress view updates in real time after patient status change.
  - Action: With the doctor's patient progress page open, mark a follow-up task completed as the patient in another session, then observe the doctor's page.
  - Expected: The doctor's page reflects the updated task completion progress without a manual page reload.

## Content
- [ ] CT-01: Doctor profile displays relevant professional information.
  - Action: Open any doctor's profile from the search results and inspect the displayed fields.
  - Expected: The profile shows the doctor's name, specialty, years of experience, and consultation fee, all matching that doctor's data.

- [ ] CT-02: Follow-up section content matches the patient's actual records.
  - Action: In the personal center's follow-up section, compare displayed follow-up instructions and sign data entries with the data submitted/issued for that patient.
  - Expected: Only that patient's follow-up instructions and uploaded blood pressure/blood glucose values are displayed, with values shown exactly as entered (e.g., 120/80, 5.6).