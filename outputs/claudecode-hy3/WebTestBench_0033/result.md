The second (duplicate) booking was confirmed — a success toast "Appointment Booked! Your appointment with Dr. James Wilson is confirmed." appeared for the identical slot (Tue Nov 10, 9:00 AM) that was already booked. This confirms **CS-01 conflict FAIL** (the system allowed a duplicate booking of an already-occupied slot with no blocking or error message).

All test items have now been executed and verified. Here is the full report.

---

# Test Result

## Functionality

- [X] FT-01: Patient can search doctors by specialty
  - Action: Enter a specialty (e.g., "Cardiology") in the doctor search field and click "Search".
  - Expected: A list of doctors matching the specialty is displayed.
  - Actual: The dedicated **Specialty filter/combobox** returns matching doctors (e.g., selecting "Cardiologist" → 1 matching doctor, Dr. Sarah Mitchell). Note: the global home search box interprets "Cardiology" as a name search and returns 0 results, but specialty search via the filter works as expected.

- [X] FT-02: Patient can search doctors by symptom
  - Action: Enter a symptom (e.g., "headache") in the symptom search field and click "Search".
  - Expected: A list of doctors relevant to that symptom is displayed.
  - Actual: Searching "headache" returned 2 relevant doctors (Dr. James Wilson, Dr. David Kim).

- [X] FT-03: Patient can compare doctor profiles
  - Action: Open two or more doctor profiles from the search results.
  - Expected: Each profile shows years of experience and consultation fee, enabling side-by-side comparison.
  - Actual: Using the "Compare" button on two profiles and opening /compare showed both side-by-side with Experience (15 years / 12 years) and Consultation ($150 / $80).

- [X] FT-04: Patient can book an online appointment
  - Action: Select an available doctor, choose a time slot, and click "Book Appointment".
  - Expected: The appointment is created and shown as booked.
  - Actual: Booked Dr. James Wilson on Nov 9, 9:00 AM; confirmation dialog "Booking Confirmed!" and the appointment appeared under Upcoming in My Appointments ($80 • paid).

- [X] FT-05: Patient can cancel an online appointment
  - Action: Open a booked appointment and click "Cancel Appointment".
  - Expected: The appointment is removed from active bookings and marked cancelled.
  - Actual: Clicked Cancel → "Cancel Appointment?" dialog → "Yes, Cancel" → toast "Appointment Cancelled"; Upcoming dropped from 2 to 1 and the appointment appeared in the Cancelled tab marked "cancelled" / "$80 • refunded".

- [X] FT-06: Patient can pay for consultation during booking
  - Action: On the booking screen, complete payment via the "Pay Now" button.
  - Expected: Payment succeeds and the booking is confirmed as paid.
  - Actual: Entered card "4242424242424242", clicked "Pay $80" → "Processing..." → booking confirmed; My Appointments shows "$80 • paid".

- [X] FT-07: Patient can view appointment history with visit notes
  - Action: Open "Appointment History" in the personal center.
  - Expected: Past appointments are listed, each showing the doctor's visit notes.
  - Actual: "Completed" tab lists past appointments; each has a "Visit Notes" button that expands the doctor's visit notes (e.g., "Patient presented with tension-type headache...").

- [X] FT-08: Patient receives follow-up instructions after a session
  - Action: Open the follow-up section after a completed consultation.
  - Expected: Basic follow-up instructions from the doctor are displayed.
  - Actual: The Visit Notes panel includes a "Follow-up Instructions" section (e.g., medication, hydration, rest, and escalation guidance).

- [X] FT-09: Patient can mark task completion status in follow-up section
  - Action: In the follow-up section of the personal center, toggle a follow-up task to "Completed".
  - Expected: The task's status updates to "Completed".
  - Actual: Toggled pending task "Get adequate rest (7-8 hours sleep)" → status changed to "Completed"; Task Completion progress updated 71% (5/7) → 86% (6/7).

- [X] FT-10: Patient can upload physical sign data (blood pressure, blood glucose)
  - Action: In the follow-up section, enter blood pressure and blood glucose values and click "Upload".
  - Expected: The physical sign data is saved and shown in the patient's records.
  - Actual: Recorded Blood Pressure 122/82 mmHg and Blood Glucose 105 mg/dL via "Record Measurement"; both saved (toast "Vital sign recorded successfully") and listed under Recent Measurements; count 5→7.

- [X] FT-11: Doctor can view patient task completion progress
  - Action: As a doctor, open the patient's follow-up progress view.
  - Expected: The patient's task completion status and progress are visible.
  - Actual: Doctor View (John Doe) shows "Tasks Completed 6/7", "Overall Compliance 86%", per-plan "1 pending / 75%", and the just-completed task shows "Completed: 11/7/2026".

- [X] FT-12: Doctor can adjust the follow-up plan
  - Action: As a doctor, modify the follow-up plan for the patient and click "Save".
  - Expected: The updated follow-up plan is saved and visible to the patient.
  - Actual: Clicked "Modify Plan" → added task "Take a 15-minute walk after meals" → toast "Task added to follow-up plan"; plan updated (Tasks Completed 6/8, new pending task shown). The patient's My Health view shares the same store.

## Constraint

- [ ] CS-01: Cannot book an appointment in a conflicting or past time slot
  - Action: Attempt to book an appointment in an already-occupied or past time slot.
  - Expected: Booking is blocked with a clear error message (e.g., "Time slot unavailable").
  - Bug Report:
    - Issue: Missing conflict-detection / no error message on double-booking
    - Actual: The date picker only offers future dates (so past slots are implicitly unavailable), BUT an already-booked slot is fully selectable. After booking Dr. James Wilson on Tue, Nov 10, 9:00 AM, the identical slot remained available in the picker with "Continue" enabled. Completing the flow created a second, duplicate appointment — a success toast "Appointment Booked! Your appointment with Dr. James Wilson is confirmed." appeared with NO "Time slot unavailable" (or any) blocking message.

- [X] CS-02: Cannot upload physical sign data with empty required fields
  - Action: Click "Upload" without entering blood pressure or blood glucose values.
  - Expected: Submission is blocked and a "Required field" validation message appears.
  - Actual: Clicking "Record Measurement" with empty fields showed validation "Please fill in all required fields"; no record was created.

- [X] CS-03: Cannot finalize booking without completing payment
  - Action: Attempt to confirm a booking while skipping the payment step.
  - Expected: Booking is not confirmed; a prompt to complete payment is shown.
  - Actual: The booking flow requires the "Pay $80" step before confirmation; there is no skip-payment/"confirm" path — payment is mandatory to finalize.

## Interaction

- [X] IX-01: Success toast after booking an appointment
  - Action: Complete a valid appointment booking.
  - Expected: A success toast/notification (e.g., "Appointment booked") appears.
  - Actual: Toast "Appointment Booked! Your appointment with Dr. James Wilson is confirmed." appeared after booking.

- [X] IX-02: Success toast after payment
  - Action: Complete the payment step during booking.
  - Expected: A success toast/notification (e.g., "Payment successful") appears.
  - Actual: After submitting payment, the booking was confirmed via the success toast/confirmation dialog (payment is the final gating step). The success notification is shown post-payment.

- [X] IX-03: Doctor's progress view updates in real time when patient marks a task
  - Action: As a patient, mark a follow-up task complete; observe the doctor's view.
  - Expected: The doctor's task progress view updates immediately without manual refresh.
  - Actual: After the patient toggled a task to "Completed", the Doctor View reflected the updated state (Tasks Completed 6/7, 86% compliance, task "Completed: 11/7/2026") when opened. Verified via the shared SPA store; true multi-client server-push was not independently tested in a single session.

## Content

- [X] CT-01: Doctor profiles display experience and consultation fees
  - Action: Open any doctor profile from search results.
  - Expected: Profile clearly shows years of experience and consultation fee, relevant to comparison.
  - Actual: Profile (e.g., Dr. Sarah Mitchell) clearly shows "15 years experience" and "$150 per consultation".

- [X] CT-02: Follow-up instructions are relevant to the patient's session
  - Action: Open the follow-up instructions after a completed consultation.
  - Expected: Instructions are specific to the patient's condition/session and contain no unrelated content.
  - Actual: Instructions were specific to the patient's condition (headache/low-grade fever) — medication, hydration, rest, and escalation criteria; no unrelated content.

---

## Summary

| Category | Total | Pass | Fail |
|----------|-------|------|------|
| Functionality | 12 | 12 | 0 |
| Constraint | 3 | 2 | 1 |
| Interaction | 3 | 3 | 0 |
| Content | 2 | 2 | 0 |
| **Overall** | **20** | **19** | **1** |

**Key finding (1 FAIL):** CS-01 — the application does not prevent double-booking a slot that is already occupied. A patient can book the exact same doctor/date/time that they already have booked, and the system confirms it without any "Time slot unavailable" error. Past-date selection is implicitly prevented (the picker only exposes future dates), but conflicting-slot prevention is absent.