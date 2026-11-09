# Test Checklist

## Functionality
- [ ] FT-01: Search doctors by specialty and symptoms
  - Action: Enter a symptom (e.g., "Headache") and select a specialty (e.g., "Neurology") in the search filters, then click "Search".
  - Expected: Doctor list updates to display only doctors matching both the specified symptom and specialty.
- [ ] FT-02: Compare doctor profiles
  - Action: Select two doctor cards from the doctor list and click "Compare".
  - Expected: A side-by-side comparison view displays both doctors with their years of experience and consultation fees.
- [ ] FT-03: Book appointment with consultation payment
  - Action: Select an available time slot for a doctor, enter valid payment details, and click "Pay & Confirm Booking".
  - Expected: Payment processes successfully and the appointment appears as "Confirmed" in the patient's schedule.
- [ ] FT-04: Cancel an upcoming appointment
  - Action: Navigate to the upcoming appointments list, locate an active booking, and click "Cancel Appointment".
  - Expected: The appointment status changes to "Cancelled" and the booked slot is released.
- [ ] FT-05: View appointment history and visit notes
  - Action: Navigate to "Appointment History" in the personal center and select a completed appointment.
  - Expected: Session summary opens displaying the doctor's name, date, consultation fee, and doctor visit notes.
- [ ] FT-06: Mark follow-up task completion status
  - Action: Navigate to the "Follow-up" section in the personal center and click the checkbox next to an assigned follow-up task.
  - Expected: The task status toggles to completed and the completion indicator updates.
- [ ] FT-07: Upload physical sign data
  - Action: In the follow-up section, enter blood pressure values (e.g., "120/80") and blood glucose (e.g., "95"), then click "Save Vitals".
  - Expected: The entered blood pressure and blood glucose values appear in the recorded vitals history log.
- [ ] FT-08: Doctor views patient task completion progress
  - Action: Log in as a doctor, open the patient list, and select a patient with assigned follow-up tasks.
  - Expected: The doctor dashboard displays the patient's real-time task completion rate and uploaded vitals log.
- [ ] FT-09: Doctor adjusts follow-up plan
  - Action: On the doctor's patient follow-up page, click "Edit Plan", add a new follow-up instruction/task, and click "Update Plan".
  - Expected: The new task is saved and immediately reflected in the patient's follow-up task list.

## Constraint
- [ ] CS-01: Prevent booking without payment
  - Action: In the booking modal, select an appointment slot and click "Pay & Confirm Booking" leaving payment details blank.
  - Expected: Booking submission is prevented and inline validation messages indicate required payment fields.
- [ ] CS-02: Prevent duplicate booking of unavailable time slots
  - Action: Attempt to select and book a time slot that is already booked or marked as unavailable.
  - Expected: The time slot is disabled from selection or an error message states "Time slot is unavailable".
- [ ] CS-03: Restrict invalid physical sign input values
  - Action: In the vitals upload form, enter non-numeric text or negative numbers into the blood glucose field and click "Save Vitals".
  - Expected: Form rejects submission and displays an error stating "Please enter a valid numeric value".
- [ ] CS-04: Prevent cancellation of past appointments
  - Action: Locate a past/completed appointment in the appointment history list.
  - Expected: The "Cancel Appointment" button is absent or disabled.

## Interaction
- [ ] IX-01: Cancellation confirmation dialog
  - Action: Click "Cancel Appointment" on an active booking.
  - Expected: A confirmation modal appears asking the user to confirm the cancellation before the action executes.
- [ ] IX-02: Real-time progress bar update on task toggle
  - Action: Click an incomplete follow-up task checkbox in the personal center.
  - Expected: The task completion progress bar increments smoothly without a full-page reload.
- [ ] IX-03: Success feedback on vitals submission
  - Action: Enter valid physical sign data and click "Save Vitals".
  - Expected: A temporary success toast message appears stating "Physical sign data uploaded successfully".

## Content
- [ ] CT-01: Doctor profile displays experience and consultation fee
  - Action: View any doctor profile card in search results or detail view.
  - Expected: Doctor's name, specialty, years of experience, and consultation fee amount are clearly displayed.
- [ ] CT-02: Post-session follow-up instructions display
  - Action: Open the detail page of a completed session in the patient personal center.
  - Expected: The follow-up section displays the doctor's written instructions and dietary/medication guidance for that session.