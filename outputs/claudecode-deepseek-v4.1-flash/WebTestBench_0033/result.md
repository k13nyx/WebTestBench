All checklist items executed. Here are the results.

# Test Result

## Functionality
- [X] FT-01: Search doctors by specialty
  - Action: Enter/select a specialty (e.g., "Cardiology") in the search field and submit.
  - Expected: A list of doctors matching that specialty is displayed.
  - Actual: Selecting "Cardiologist" in the Specialty filter returned "1 doctors found" — only Dr. Sarah Mitchell (Cardiologist).

- [X] FT-02: Search doctors by symptoms
  - Action: Enter a symptom (e.g., "headache") in the search field and submit.
  - Expected: A list of doctors relevant to that symptom is displayed.
  - Actual: Selecting the "Headache" symptom chip returned "2 doctors found" — Dr. James Wilson (General Physician) and Dr. David Kim (Neurologist).

- [X] FT-03: Compare doctor profiles
  - Action: Open a doctor's profile and view the experience and consultation fee fields.
  - Expected: Both "Years of Experience" and "Consultation Fee" are shown for the doctor.
  - Actual: Profile shows "15 years experience", "4.9 (328 reviews)", "$150 per consultation", plus Education/Hospital/Languages and Conditions Treated. (Verified for Dr. Sarah Mitchell and Dr. James Wilson: "12 years experience", "$80 per consultation".)

- [X] FT-04: Book an online appointment
  - Action: On a doctor's profile, select an available time slot and confirm booking.
  - Expected: The appointment is created and appears in the patient's appointment list.
  - Actual: After completing booking, "My Appointments → Upcoming" listed the new appointment (Dr. James Wilson, Nov 9, 2026, 9:00 AM, $80 • paid, matching the entered symptoms).

- [X] FT-05: Cancel an online appointment
  - Action: In the patient's appointment list, select a future appointment and click "Cancel".
  - Expected: The appointment is removed/marked as "Cancelled".
  - Actual: Confirming cancellation removed it from Upcoming (2→1) and showed toast "Appointment Cancelled…"; it appears in the "Cancelled" tab marked "cancelled" with "$80 • refunded".

- [X] FT-06: Pay for a consultation during booking
  - Action: Proceed through the booking flow and complete the payment step.
  - Expected: Payment is accepted and the booking is confirmed only after successful payment.
  - Actual: Booking flow is Date/Time → Symptoms → "Payment Details", with a "Pay $150" action; confirmation only after paying ("Your appointment with Dr. James Wilson has been confirmed for November 9, 2026 at 9:00 AM").

- [X] FT-07: View appointment history with visit notes
  - Action: Open a past appointment in the patient's history.
  - Expected: The visit notes recorded by the doctor are displayed.
  - Actual: Completed appointment's "Visit Notes" panel shows recorded notes ("Patient presented with tension-type headache and low-grade fever… Vital signs were stable.").

- [X] FT-08: Receive follow-up instructions after a session
  - Action: Open a completed session in the patient's personal center.
  - Expected: The doctor's follow-up instructions for that session are displayed.
  - Actual: My Health dashboard shows per-session follow-up plans ("Follow-up from Dr. James Wilson / Dr. Emily Chen") with the doctor's instructions (medication, hydration, rest, etc.); the visit-notes panel also shows a "Follow-up Instructions" section.

- [X] FT-09: Mark follow-up task completion status
  - Action: In the personal center follow-up section, mark a task as complete.
  - Expected: The task status changes to "Completed".
  - Actual: Marking "Get adequate rest" changed its status from "Pending" to "Completed" and updated the completion metric from 5/7 (71%) to 6/7 (86%).

- [X] FT-10: Upload physical sign data
  - Action: In the follow-up section, enter blood pressure / blood glucose values and submit.
  - Expected: The uploaded values are saved and displayed in the patient's records.
  - Actual: Recording "Blood Pressure 130/85" saved the entry — it appears at the top of "Recent Measurements" (Blood Pressure | 130/85 mmHg | 11/8/2026) and the "Vital Signs Recorded" counter incremented (5→6).

- [X] FT-11: Doctor views patient task progress in real time
  - Action: As a doctor, open the patient's follow-up progress while the patient updates a task.
  - Expected: The updated task completion status is reflected without manual page reload.
  - Actual: After the patient marked "Get adequate rest" complete, the Doctor Dashboard (opened via in-app navigation, no reload) showed that task as "Completed: 11/8/2026" and updated compliance (Tasks Completed 6/7, Overall Compliance 86%; plan shows today's update date).

- [X] FT-12: Doctor adjusts follow-up plan
  - Action: As a doctor, modify the patient's follow-up plan and save.
  - Expected: The revised follow-up plan is saved and visible to the patient.
  - Actual: "Modify Plan" → "Add New Task" saved a new task ("Record blood pressure every morning", Daily, due 2026-11-20); it is visible to the patient in My Health and the plan totals increased (7→8 tasks).

## Constraint
- [ ] CS-01: Prevent double-booking of an occupied slot
  - Action: Attempt to book a time slot already taken by another patient.
  - Expected: Booking is blocked with a message that the slot is unavailable.
  - Bug Report:
    - Issue: Double-booking allowed — no slot-availability validation
    - Actual: The identical slot (Dr. Emily Chen, Nov 10, 2026, 10:00 AM) was booked twice successfully. The "10:00 AM" slot button remained enabled on the second attempt, the second payment produced "Your appointment with Dr. Emily Chen is confirmed for November 10, 2026 at 10:00 AM", and both bookings appear as "Upcoming" (Upcoming count went to 3). No "slot unavailable/taken" message was ever shown.

- [X] CS-02: Block booking without completed payment
  - Action: Start booking and skip/abandon the payment step.
  - Expected: The appointment is not confirmed and no slot is reserved.
  - Actual: Reaching "Payment Details" and closing the dialog without paying left "Upcoming" at 1 with no new appointment created for that doctor.

- [ ] CS-03: Validate uploaded physical sign values
  - Action: Enter an invalid value (e.g., non-numeric or out-of-range) for blood pressure/glucose and submit.
  - Expected: Submission is rejected with a validation error message.
  - Bug Report:
    - Issue: Missing input validation on vital-sign values
    - Actual: Entering the non-numeric value "abc" for "Value (mmHg)" and clicking "Record Measurement" was accepted — the record was saved and displayed as "Blood Pressure — abc mmHg" (timestamped 11/8/2026), and the "Vital Signs Recorded" counter incremented (6→7). No validation error message was displayed.

- [X] CS-04: Restrict cancellation to eligible appointments
  - Action: Attempt to cancel a past/completed appointment.
  - Expected: The "Cancel" action is unavailable or blocked with a message.
  - Actual: In the "Completed" tab, appointments expose only a "Visit Notes" button (0 "Cancel" buttons found); cancellation is not offered for completed (past) appointments. (Note: an oddly seeded record dated Dec 15, 2024 is labelled status "upcoming" and therefore exposes Cancel; this is a data/label inconsistency, but the Completed/past case correctly offers no Cancel action.)

## Interaction
- [X] IX-01: Show confirmation on booking success
  - Action: Complete a valid booking.
  - Expected: A success message/toast confirms the appointment was booked.
  - Actual: Success toast "Appointment Booked! Your appointment with Dr. Sarah Mitchell is confirmed." (and equivalent toasts for other bookings) is displayed.

- [X] IX-02: Show confirmation prompt before cancelling
  - Action: Click "Cancel" on an appointment.
  - Expected: A confirmation prompt appears before the cancellation is executed.
  - Actual: An alert dialog "Cancel Appointment?" appears ("Are you sure you want to cancel this appointment? A full refund of $80 will be processed.") with "Keep Appointment" / "Yes, Cancel" before the cancellation proceeds.

## Content
- [X] CT-01: Doctor profile content relevance
  - Action: Inspect doctor profile details (name, specialty, experience, fee).
  - Expected: All displayed information is relevant to the doctor and to telemedicine consultation.
  - Actual: Profiles show coherent telemedicine-relevant content — name, specialty, "X years experience", reviews, "$Y per consultation", About (specialty-specific), Education/Hospital/Languages, Available days, Conditions Treated, and "Video consultations available on …".

- [X] CT-02: Visit notes and follow-up instructions relevance
  - Action: Inspect visit notes and follow-up instructions for a session.
  - Expected: The text is relevant to that patient's session and condition, not placeholder/generic content.
  - Actual: For the headache/fever session the notes read "Patient presented with tension-type headache and low-grade fever… Vital signs were stable", with follow-up instructions specific to that condition (Acetaminophen 500mg dosing, hydration, rest, when to seek follow-up). Content matches the session symptoms and is not generic placeholder text.

---

### Summary of failures
| ID | Result | Defect |
|----|--------|--------|
| CS-01 | FAIL | Same doctor/date/time slot could be booked twice; no "unavailable" block or message |
| CS-03 | FAIL | Non-numeric vital-sign value ("abc") accepted and stored; no validation error |

All other items (FT-01–FT-12, CS-02, CS-04, IX-01, IX-02, CT-01, CT-02) passed.