# Test Result

## Functionality

- [X] FT-01: Patient can search for doctors by specialty
  - Action: Open the doctor search page, select or type a specialty (e.g., "Cardiology") from the default data, and run the search.
  - Expected: A result list is returned showing only doctors whose listed specialty matches "Cardiology".

- [X] FT-02: Patient can search for doctors by symptoms
  - Action: On the doctor search page, enter a symptom (e.g., "chest pain" or "headache") into the symptom search field and run the search.
  - Expected: A result list is returned showing doctors whose profile indicates they treat the entered symptom.
  - (Verified via the "Chest Pain" symptom filter; result was Dr. Sarah Mitchell, whose profile lists "Chest Pain" under Conditions Treated.)

- [X] FT-03: Patient can compare doctor profiles with experience and consultation fees
  - Action: From search results, select two or more doctors and open the compare view.
  - Expected: A side-by-side comparison displays each doctor's name, specialty, years of experience, and consultation fee.
  - (Compare view showed Dr. Sarah Mitchell — Cardiologist, 15 years, $150 — and Dr. James Wilson — General Physician, 12 years, $80, side by side.)

- [X] FT-04: Patient can book an online appointment
  - Action: From a doctor's profile, pick an available date/time slot and confirm the booking.
  - Expected: The appointment is created and appears in the patient's upcoming appointments with the selected doctor, date, and time.
  - (New appointment "Dr. Sarah Mitchell, Nov 9, 2026, 9:00 AM" appeared in Upcoming with the entered symptoms.)

- [X] FT-05: Patient can pay for the consultation during booking
  - Action: During the booking flow, complete the payment step with valid payment details matching the doctor's consultation fee.
  - Expected: Payment succeeds and the appointment status shows as paid/confirmed with the correct fee amount.
  - (Appointment shows "$150 • paid", matching Dr. Sarah Mitchell's consultation fee.)

- [X] FT-06: Patient can cancel a booked appointment
  - Action: Open an existing upcoming appointment and click the cancel button, confirming the cancellation.
  - Expected: The appointment is removed from upcoming appointments (or marked "Cancelled") and no longer occupies the time slot.
  - (Cancelled appointment moved out of Upcoming and appeared in the Cancelled tab marked "cancelled", "$150 • refunded".)

- [X] FT-07: Patient can view appointment history with visit notes
  - Action: Open the appointment history section in the patient's personal center.
  - Expected: Past appointments are listed with doctor name, date, and each completed consultation shows its visit notes.
  - (Completed tab lists past appointments with doctor name, date, and expandable "Visit Notes" containing the doctor's notes and follow-up instructions.)

- [X] FT-08: Patient receives follow-up instructions from the doctor after each session
  - Action: Open the follow-up section for a completed consultation.
  - Expected: Follow-up instructions written by the doctor for that session (e.g., medication reminders, activity tasks) are displayed.
  - (Visit Notes for the completed consultation display "Follow-up Instructions" from the doctor — medication (Acetaminophen 500mg), hydration, rest, activity tasks — and the My Health follow-up section shows the same plan tasks.)

- [X] FT-09: Patient can mark follow-up task completion status
  - Action: In the follow-up section of the personal center, click the completion checkbox/toggle for an unfinished follow-up task.
  - Expected: The task status changes to completed and the overall follow-up completion progress reflects the update.
  - (Marking "Get adequate rest (7-8 hours sleep)" complete changed its badge to "Completed" and progress updated from 71% (5/7) to 86% (6/7).)

- [X] FT-10: Patient can upload physical sign data (blood pressure, blood glucose)
  - Action: In the follow-up section, fill in blood pressure (e.g., "120/80") and blood glucose (e.g., "5.6 mmol/L") values and submit.
  - Expected: The submitted values are saved and displayed in the patient's follow-up sign data list with correct values and timestamps.
  - (BP "120/80" saved as "120/80 mmHg" and glucose "5.6 mmol/L" saved, both displayed with timestamps "11/8/2026, 6:54 AM"; counter rose to 8. Note: glucose displays with an appended "mg/dL" — see CT-03.)

- [X] FT-11: Doctor can view patient task completion progress in real time and adjust the follow-up plan
  - Action: In the doctor's patient follow-up view, open the patient's follow-up plan; then have the patient mark a task complete (or use default progress data) and, from the doctor side, edit the plan (e.g., add or modify a follow-up task) and save.
  - Expected: The doctor's view shows the patient's task completion progress and uploaded sign data; the saved plan changes appear in the patient's follow-up section.
  - (Doctor dashboard showed the patient-updated progress — "6/7 tasks, 86%", task "Get adequate rest" with "Completed: 11/7/2026" — and the newly uploaded BP/glucose values. Doctor added task "Walk 30 minutes every morning" via Modify Plan → Add Task; it appeared in the patient's follow-up section as Pending, progress recalculated to 75% (6/8).)

## Constraint

- [X] CS-01: Appointment is not confirmed without successful payment
  - Action: Start a booking and attempt to confirm with empty or invalid payment details (e.g., blank card number or failed payment).
  - Expected: The booking is not confirmed, no appointment is created, and an error message about payment is shown.
  - (Clicking "Pay $150" with a blank card showed error toast "Invalid card — Please enter a valid card number"; dialog remained on the payment step and no appointment was created.)

- [ ] CS-02: Already-booked time slot cannot be double-booked
  - Action: Attempt to book the same doctor for a time slot that is already booked (use a slot occupied by an existing appointment in default data).
  - Expected: The slot is shown as unavailable and the booking is rejected; the slot remains booked by the original appointment.
  - Bug Report:
    - Issue: Double-booking of an occupied time slot is allowed; no slot-availability check
    - Actual: After booking Dr. Sarah Mitchell for Mon, Nov 9, 2026 at 9:00 AM, reopening the booking dialog showed the 9:00 AM slot still selectable (not disabled/marked unavailable). Completing the flow again succeeded with toast "Appointment Booked! Your appointment with Dr. Sarah Mitchell is confirmed." and a second appointment for the exact same doctor/date/time ("Second attempt for the same slot") was created, leaving two paid appointments occupying the same slot.

- [ ] CS-03: Physical sign data cannot be submitted with missing or invalid values
  - Action: In the sign data upload form, leave a required field empty or enter non-numeric text (e.g., "abc") and submit.
  - Expected: The submission is rejected with a validation message, and no invalid entry is added to the sign data list.
  - Bug Report:
    - Issue: Missing input validation for non-numeric vital sign values
    - Actual: An empty value was correctly rejected with "Please fill in all required fields", but entering "abc" as the Blood Pressure value was accepted with success toast "Vital sign recorded successfully", and an invalid entry "Blood Pressure — abc mmHg — 11/8/2026, 6:54:22 AM" was added to the sign data list (counter increased from 5 to 6).

- [X] CS-04: A completed consultation appointment cannot be cancelled
  - Action: From appointment history, open a completed (past) appointment and check for a cancel option.
  - Expected: No cancel action is available for completed appointments; only upcoming appointments can be cancelled.
  - (Completed appointments show only "Visit Notes" toggle; no Cancel button. Cancel buttons appear only on Upcoming appointments.)

## Interaction

- [X] IX-01: Booking confirmation feedback is shown after successful payment
  - Action: Complete a booking with valid payment.
  - Expected: A success toast/message confirms the booking and payment (e.g., "Appointment booked successfully") and the appointment appears in upcoming appointments.
  - (Toast "Appointment Booked! Your appointment with Dr. Sarah Mitchell is confirmed." shown after payment; appointment appeared in Upcoming.)

- [X] IX-02: Cancellation requires confirmation before taking effect
  - Action: Click the cancel button on an upcoming appointment.
  - Expected: A confirmation dialog appears; the appointment is cancelled only after confirming, and feedback (e.g., "Appointment cancelled") is shown.
  - (Dialog "Cancel Appointment? … A full refund of $150 will be processed" with Keep/Yes-Cancel buttons; after confirming, toast "Appointment Cancelled — Your appointment has been cancelled and refund initiated." appeared.)

- [ ] IX-03: Task completion toggle updates progress display immediately
  - Action: Toggle a follow-up task's completion status on and off.
  - Expected: The task's visual state (checkbox/icon) and the follow-up completion progress (e.g., "2/5 tasks completed") update instantly without page errors.
  - Bug Report:
    - Issue: One-way completion toggle; no "off" control for completed tasks
    - Actual: Marking a pending task complete worked instantly (badge Pending→Completed, icon changed, progress 71% (5/7) → 86% (6/7), no page errors). However, once completed, the task shows only a static "Completed" badge with no un-check/toggle-off control (clicking the task icon and the badge produced no state change), so the completion status cannot be toggled back off.

- [X] IX-04: Doctor's progress view reflects patient updates without requiring re-login or manual refresh
  - Action: With the doctor's patient progress view open, have the patient mark a task complete or upload sign data.
  - Expected: The doctor's view updates the completion progress and sign data (immediately or on next view load) without the patient data being lost or stale.
  - (After patient-side task completion and BP/glucose uploads, opening the Doctor View reflected "Tasks Completed 6/7, Compliance 86%", the task's "Completed: 11/7/2026" date, and the new measurements "120/80 mmHg" and "5.6 mmol/L" with current timestamps — no re-login required.)

## Content

- [X] CT-01: Doctor search results match the queried specialty or symptom
  - Action: Review the result lists from FT-01 and FT-02 searches.
  - Expected: Every listed doctor's profile (name, specialty, title) is relevant to the searched specialty/symptom, with no unrelated doctors shown.
  - (Specialty search "Cardiologist" returned only Dr. Sarah Mitchell, Cardiologist; symptom search "Chest Pain" returned Dr. Sarah Mitchell, whose profile lists Chest Pain under "Conditions Treated". No unrelated doctors in either list.)

- [X] CT-02: Visit notes in appointment history match their consultations
  - Action: Open a past appointment from history and read its visit notes.
  - Expected: The visit notes contain coherent, medically relevant content for that consultation (doctor, date, and reason consistent with the appointment record).
  - (For the Dec 10, 2024 consultation with Dr. James Wilson recorded with symptoms "Persistent headache and mild fever for 3 days", the visit notes state "Patient presented with tension-type headache and low-grade fever… Vital signs were stable" — coherent and consistent with the appointment record.)

- [ ] CT-03: Follow-up instructions and sign data are relevant and accurately displayed
  - Action: Check the follow-up section for a completed session, including the doctor's instructions and uploaded sign data entries.
  - Expected: Instructions are relevant to that consultation's theme, and uploaded blood pressure/blood glucose values are displayed exactly as submitted with correct units (e.g., mmHg, mmol/L).
  - Bug Report:
    - Issue: Incorrect unit display for submitted blood glucose value
    - Actual: Instructions are relevant to their consultations (headache/fever → Acetaminophen, hydration, rest; rash → hydrocortisone cream, hypoallergenic products) and blood pressure is displayed correctly ("120/80 mmHg"). However, the blood glucose value submitted as "5.6 mmol/L" is displayed as "5.6 mmol/L mg/dL" — the app appends its default "mg/dL" unit to a value that already contains "mmol/L", so the entry is not displayed exactly as submitted and shows duplicated/contradictory units.
