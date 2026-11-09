# Test Result

## Functionality
- [X] FT-01: Filter doctors by specialty and symptoms
  - Action: On the doctor listing page, select "Neurologist" from the specialty dropdown and select or search for "Headache" in the symptoms filter.
  - Expected: The doctor list dynamically updates to show only doctors matching both criteria (e.g., Dr. David Kim).
- [X] FT-02: Compare doctor profiles
  - Action: Select two or more doctors (e.g., Dr. Sarah Mitchell and Dr. James Wilson) using the "Compare" checkbox/button and navigate to the comparison page.
  - Expected: Side-by-side comparison view displays both doctors' experience (e.g., 15 years vs 12 years) and consultation fees (e.g., $150 vs $80).
- [X] FT-03: Book appointment with consultation payment
  - Action: Select an available time slot for a doctor, enter valid payment details, and click "Pay & Confirm Booking".
  - Expected: Payment processes successfully and the appointment appears as "Confirmed" in the patient's schedule.
- [X] FT-04: Cancel an upcoming appointment
  - Action: Navigate to the upcoming appointments list, locate an active booking, and click "Cancel Appointment".
  - Expected: The appointment status changes to "Cancelled" and the booked slot is released.
- [X] FT-05: View appointment history and visit notes
  - Action: Go to appointment history, find a completed consultation, and click on it or expand details.
  - Expected: Shows doctor name, consultation date, fee paid, and doctor's visit notes summarizing the consultation.
- [X] FT-06: Mark follow-up task completion status
  - Action: In the follow-up section of the personal center, locate an incomplete task and toggle its checkbox.
  - Expected: The task is marked as completed and the UI updates immediately to reflect the change.
- [X] FT-07: Upload physical sign data
  - Action: In the follow-up/health metrics section, enter blood pressure (e.g., 120/80 mmHg) and blood glucose (e.g., 95 mg/dL) values, then click submit/upload.
  - Expected: The data is saved and displayed in the patient's physical sign history or chart.
- [X] FT-08: Doctor views patient task completion progress
  - Action: Log in/switch to the doctor role, open the patient's follow-up management view.
  - Expected: Displays the patient's real-time task completion rate (e.g., percentage or completed/total) and uploaded vitals log.
- [X] FT-09: Doctor adjusts follow-up plan
  - Action: From the doctor's follow-up plan view, add a new task or modify an existing plan for the patient, then save.
  - Expected: The updated plan is saved and immediately reflected in both the doctor view and the patient's personal center.

## Constraint
- [ ] CS-01: Form validation for required booking/payment fields
  - Action: In the booking modal, leave required payment fields (e.g., card number) blank and click "Pay & Confirm Booking".
  - Expected: Submission is blocked and inline validation messages indicate the required fields that need attention.
  - Bug Report:
    - Issue: Missing Inline Form Validation
    - Actual: While form submission was blocked, no inline validation error elements were rendered adjacent to the required inputs; feedback was only dispatched via a floating toast notification ("Please enter a valid card number").
- [ ] CS-02: Slot availability verification before booking
  - Action: Attempt to select a time slot that is already booked or marked unavailable.
  - Expected: The booked slot is disabled or displays an error (e.g., "Time slot is unavailable") and cannot be selected.
  - Bug Report:
    - Issue: Lack of Slot Availability Verification
    - Actual: All 12 time slots render as active selectable buttons without checking appointment conflicts against existing doctor bookings; booked slots are neither disabled nor prevented from being selected.
- [ ] CS-03: Restrict invalid physical sign input values
  - Action: Attempt to submit negative numbers, non-numeric characters, or out-of-range values in the physical sign upload form.
  - Expected: Submission is rejected with an inline error message indicating valid ranges (e.g., "Please enter a valid numeric value").
  - Bug Report:
    - Issue: Missing Input Validation
    - Actual: Submitting negative numbers (e.g., "-50") was accepted without rejection, no inline error messages were displayed, and the invalid value "-50 mg/dL" was added directly to recent measurements.
- [X] CS-04: Prevent cancellation of past appointments
  - Action: Locate a past/completed appointment in the appointment history list.
  - Expected: The "Cancel Appointment" button is absent or disabled.

## Interaction
- [X] IX-01: Cancellation confirmation dialog
  - Action: Click "Cancel Appointment" on an active booking.
  - Expected: A confirmation modal appears asking the user to confirm the cancellation before the action executes.
- [X] IX-02: Real-time progress bar update on task toggle
  - Action: Toggle a follow-up task checkbox in the personal center.
  - Expected: The task completion progress bar increments smoothly without requiring a page reload.
- [X] IX-03: Success feedback on vitals submission
  - Action: Fill in valid physical sign data and click submit.
  - Expected: A success message (e.g., toast notification or banner) confirms that the vitals have been recorded.

## Content
- [X] CT-01: Side-by-side comparison displays all key attributes
  - Action: View the comparison table/view with selected doctors.
  - Expected: Displays doctor name, specialty, years of experience, consultation fee, rating, and hospital/clinic affiliation for each doctor.
- [X] CT-02: Post-session follow-up instructions display
  - Action: View the details/notes section of a completed appointment.
  - Expected: Displays post-session instructions written by the doctor, including basic guidance such as lifestyle, medication, or follow-up timelines.
