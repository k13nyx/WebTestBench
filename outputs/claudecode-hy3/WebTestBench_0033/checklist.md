# Test Checklist

## Functionality
- [ ] FT-01: Patient can search doctors by specialty
  - Action: Enter a specialty (e.g., "Cardiology") in the doctor search field and click "Search".
  - Expected: A list of doctors matching the specialty is displayed.

- [ ] FT-02: Patient can search doctors by symptom
  - Action: Enter a symptom (e.g., "headache") in the symptom search field and click "Search".
  - Expected: A list of doctors relevant to that symptom is displayed.

- [ ] FT-03: Patient can compare doctor profiles
  - Action: Open two or more doctor profiles from the search results.
  - Expected: Each profile shows years of experience and consultation fee, enabling side-by-side comparison.

- [ ] FT-04: Patient can book an online appointment
  - Action: Select an available doctor, choose a time slot, and click "Book Appointment".
  - Expected: The appointment is created and shown as booked.

- [ ] FT-05: Patient can cancel an online appointment
  - Action: Open a booked appointment and click "Cancel Appointment".
  - Expected: The appointment is removed from active bookings and marked cancelled.

- [ ] FT-06: Patient can pay for consultation during booking
  - Action: On the booking screen, complete payment via the "Pay Now" button.
  - Expected: Payment succeeds and the booking is confirmed as paid.

- [ ] FT-07: Patient can view appointment history with visit notes
  - Action: Open "Appointment History" in the personal center.
  - Expected: Past appointments are listed, each showing the doctor's visit notes.

- [ ] FT-08: Patient receives follow-up instructions after a session
  - Action: Open the follow-up section after a completed consultation.
  - Expected: Basic follow-up instructions from the doctor are displayed.

- [ ] FT-09: Patient can mark task completion status in follow-up section
  - Action: In the follow-up section of the personal center, toggle a follow-up task to "Completed".
  - Expected: The task's status updates to "Completed".

- [ ] FT-10: Patient can upload physical sign data (blood pressure, blood glucose)
  - Action: In the follow-up section, enter blood pressure and blood glucose values and click "Upload".
  - Expected: The physical sign data is saved and shown in the patient's records.

- [ ] FT-11: Doctor can view patient task completion progress
  - Action: As a doctor, open the patient's follow-up progress view.
  - Expected: The patient's task completion status and progress are visible.

- [ ] FT-12: Doctor can adjust the follow-up plan
  - Action: As a doctor, modify the follow-up plan for the patient and click "Save".
  - Expected: The updated follow-up plan is saved and visible to the patient.

## Constraint
- [ ] CS-01: Cannot book an appointment in a conflicting or past time slot
  - Action: Attempt to book an appointment in an already-occupied or past time slot.
  - Expected: Booking is blocked with a clear error message (e.g., "Time slot unavailable").

- [ ] CS-02: Cannot upload physical sign data with empty required fields
  - Action: Click "Upload" without entering blood pressure or blood glucose values.
  - Expected: Submission is blocked and a "Required field" validation message appears.

- [ ] CS-03: Cannot finalize booking without completing payment
  - Action: Attempt to confirm a booking while skipping the payment step.
  - Expected: Booking is not confirmed; a prompt to complete payment is shown.

## Interaction
- [ ] IX-01: Success toast after booking an appointment
  - Action: Complete a valid appointment booking.
  - Expected: A success toast/notification (e.g., "Appointment booked") appears.

- [ ] IX-02: Success toast after payment
  - Action: Complete the payment step during booking.
  - Expected: A success toast/notification (e.g., "Payment successful") appears.

- [ ] IX-03: Doctor's progress view updates in real time when patient marks a task
  - Action: As a patient, mark a follow-up task complete; observe the doctor's view.
  - Expected: The doctor's task progress view updates immediately without manual refresh.

## Content
- [ ] CT-01: Doctor profiles display experience and consultation fees
  - Action: Open any doctor profile from search results.
  - Expected: Profile clearly shows years of experience and consultation fee, relevant to comparison.

- [ ] CT-02: Follow-up instructions are relevant to the patient's session
  - Action: Open the follow-up instructions after a completed consultation.
  - Expected: Instructions are specific to the patient's condition/session and contain no unrelated content.