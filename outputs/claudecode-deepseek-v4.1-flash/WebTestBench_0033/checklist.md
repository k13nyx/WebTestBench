# Test Checklist

## Functionality
- [ ] FT-01: Search doctors by specialty
  - Action: Enter/select a specialty (e.g., "Cardiology") in the search field and submit.
  - Expected: A list of doctors matching that specialty is displayed.

- [ ] FT-02: Search doctors by symptoms
  - Action: Enter a symptom (e.g., "headache") in the search field and submit.
  - Expected: A list of doctors relevant to that symptom is displayed.

- [ ] FT-03: Compare doctor profiles
  - Action: Open a doctor's profile and view the experience and consultation fee fields.
  - Expected: Both "Years of Experience" and "Consultation Fee" are shown for the doctor.

- [ ] FT-04: Book an online appointment
  - Action: On a doctor's profile, select an available time slot and confirm booking.
  - Expected: The appointment is created and appears in the patient's appointment list.

- [ ] FT-05: Cancel an online appointment
  - Action: In the patient's appointment list, select a future appointment and click "Cancel".
  - Expected: The appointment is removed/marked as "Cancelled".

- [ ] FT-06: Pay for a consultation during booking
  - Action: Proceed through the booking flow and complete the payment step.
  - Expected: Payment is accepted and the booking is confirmed only after successful payment.

- [ ] FT-07: View appointment history with visit notes
  - Action: Open a past appointment in the patient's history.
  - Expected: The visit notes recorded by the doctor are displayed.

- [ ] FT-08: Receive follow-up instructions after a session
  - Action: Open a completed session in the patient's personal center.
  - Expected: The doctor's follow-up instructions for that session are displayed.

- [ ] FT-09: Mark follow-up task completion status
  - Action: In the personal center follow-up section, mark a task as complete.
  - Expected: The task status changes to "Completed".

- [ ] FT-10: Upload physical sign data
  - Action: In the follow-up section, enter blood pressure / blood glucose values and submit.
  - Expected: The uploaded values are saved and displayed in the patient's records.

- [ ] FT-11: Doctor views patient task progress in real time
  - Action: As a doctor, open the patient's follow-up progress while the patient updates a task.
  - Expected: The updated task completion status is reflected without manual page reload.

- [ ] FT-12: Doctor adjusts follow-up plan
  - Action: As a doctor, modify the patient's follow-up plan and save.
  - Expected: The revised follow-up plan is saved and visible to the patient.

## Constraint
- [ ] CS-01: Prevent double-booking of an occupied slot
  - Action: Attempt to book a time slot already taken by another patient.
  - Expected: Booking is blocked with a message that the slot is unavailable.

- [ ] CS-02: Block booking without completed payment
  - Action: Start booking and skip/abandon the payment step.
  - Expected: The appointment is not confirmed and no slot is reserved.

- [ ] CS-03: Validate uploaded physical sign values
  - Action: Enter an invalid value (e.g., non-numeric or out-of-range) for blood pressure/glucose and submit.
  - Expected: Submission is rejected with a validation error message.

- [ ] CS-04: Restrict cancellation to eligible appointments
  - Action: Attempt to cancel a past/completed appointment.
  - Expected: The "Cancel" action is unavailable or blocked with a message.

## Interaction
- [ ] IX-01: Show confirmation on booking success
  - Action: Complete a valid booking.
  - Expected: A success message/toast confirms the appointment was booked.

- [ ] IX-02: Show confirmation prompt before cancelling
  - Action: Click "Cancel" on an appointment.
  - Expected: A confirmation prompt appears before the cancellation is executed.

## Content
- [ ] CT-01: Doctor profile content relevance
  - Action: Inspect doctor profile details (name, specialty, experience, fee).
  - Expected: All displayed information is relevant to the doctor and to telemedicine consultation.

- [ ] CT-02: Visit notes and follow-up instructions relevance
  - Action: Inspect visit notes and follow-up instructions for a session.
  - Expected: The text is relevant to that patient's session and condition, not placeholder/generic content.