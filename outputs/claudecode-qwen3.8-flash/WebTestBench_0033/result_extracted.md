# Test Result

## Functionality
- [X] FT-01: Patient can search doctors by specialty
  - Action: On the doctor search page, enter/select a specialty (e.g., "Cardiology") and submit the search.
  - Expected: A results list is returned showing only doctors whose specialty matches the selected value.
  - Actual: Selecting "Cardiologist" narrowed "8 doctors found" → "1 doctors found" showing only Dr. Sarah Mitchell (Cardiologist). Result set exactly matches the selected specialty.

- [ ] FT-02: Patient can search doctors by symptom
  - Action: Enter a symptom keyword (e.g., "headache") in the symptom search field and submit.
  - Expected: Results list doctors who treat that symptom, and the matched symptom is visible on each result.
  - Bug Report:
    - Issue: Missing element in search results (matched symptom not rendered)
    - Actual: Selecting the "Headache" chip correctly returns 2 doctors who treat headaches (Dr. James Wilson, Dr. David Kim), but the matched symptom is NOT visible on any result. Full card text of both results is only "4.7 Dr. David Kim Neurologist 13 yrs 4.7 (198) $160 Mon Tue Fri View Profile Book Now" — no symptom tag anywhere on the card.

- [X] FT-03: Search results allow comparison of experience and fees
  - Action: Run any specialty/symptom search and inspect the result cards/rows.
  - Expected: Each result simultaneously displays the doctor's years of experience and consultation fee (with currency), so profiles can be compared side by side; opening a profile shows the same values in full detail.
  - Actual: Every card shows experience + fee (e.g., "15 yrs" + "$150", "13 yrs" + "$160"). Profile of Dr. Sarah Mitchell shows "15 years experience" and "$150 per consultation" — same values in full detail.

- [X] FT-04: Patient can book an appointment with a chosen doctor
  - Action: From a doctor profile, click "Book Appointment", pick an available date/time slot, complete the patient/consultation details, and submit.
  - Expected: Booking is accepted and a new appointment with doctor name, date, time, and status "Booked"/"Upcoming" is created.
  - Actual: Book Now → dialog (date "Mon, Nov 9", time "9:00 AM") → symptom description → payment → new record appeared in My Appointments: "Dr. Sarah Mitchell / Cardiologist / Upcoming / Nov 9, 2026 / 9:00 AM / $150 • paid" with the entered symptom text.

- [X] FT-05: Consultation payment is taken during the booking flow
  - Action: Proceed through booking to the payment step, enter valid payment details, and confirm.
  - Expected: A payment step is presented before confirmation, showing the exact consultation fee of that doctor, and payment is marked as completed for the appointment.
  - Actual: Step 3 of the wizard is "Payment Details" showing "Consultation Fee $150" and a "Pay $150" button; after entering a card number and paying, the appointment shows "$150 • paid".

- [X] FT-06: Patient can cancel an existing appointment
  - Action: Open the booked appointment and click "Cancel Appointment", then confirm.
  - Expected: The appointment status changes to "Cancelled" and the slot is released; no completed/past appointment is deletable.
  - Actual: Cancel on the booked appointment changed its badge to "Cancelled" with "$150 • refunded"; completed appointments offer only "Visit Notes" and no delete/cancel control exists for them. (Note: slot-release semantics are moot because the app never reserves slots — captured as a CS-01 failure.)

- [X] FT-07: Appointment history is visible to the patient
  - Action: Open the patient's personal center → "Appointment History".
  - Expected: A list of past appointments is shown with date, doctor, specialty, status, and payment status.
  - Actual: "My Appointments" lists all appointments in Upcoming/Completed/Cancelled tabs; each entry shows doctor name (Dr. James Wilson), specialty (General Physician), date (Dec 10, 2024), time, status ("completed"/"upcoming"/"cancelled"), and payment ("$80 • paid", "$180 • refunded").

- [X] FT-08: Visit notes are available per completed consultation
  - Action: In appointment history, open the detail of a consultation with status "Completed".
  - Expected: The doctor's visit notes for that session are displayed and are non-empty.
  - Actual: "Visit Notes" button on Dr. Wilson's completed appointment expands: "Patient presented with tension-type headache and low-grade fever. Physical examination showed no concerning findings. Vital signs were stable." — non-empty and consistent with the session's recorded symptoms.

- [X] FT-09: Follow-up instructions appear after each completed session
  - Action: Open the follow-up section for a completed appointment.
  - Expected: Doctor-issued follow-up instructions for that session are shown (e.g., medication/diet guidance), tied to that specific appointment.
  - Actual: Instructions appear with the appointment detail ("Follow-up Instructions: 1. Take prescribed medication (Acetaminophen 500mg)… 2. Stay well hydrated…") and in My Health as plans titled "Follow-up from Dr. James Wilson — Created: 12/10/2024" (matching that appointment's date/doctor) and "Follow-up from Dr. Emily Chen — Created: 11/28/2024".

- [ ] FT-10: Patient can mark follow-up task completion status
  - Action: In personal center → Follow-up, toggle a follow-up task item to "Done"/"Completed".
  - Expected: The task's status changes and persists after reload, with an overall completion count/percentage shown.
  - Bug Report:
    - Issue: Data not persisted (all app state is in-memory only; no localStorage/IndexedDB)
    - Actual: Toggle worked in-session: "Get adequate rest…" changed from "Pending" to "Completed: 11/8/2026" and the aggregate updated 71% (5/7) → 86% (6/7). However, after a page reload everything reset: back to "Pending", 71% (5/7); newly recorded vitals and appointments were also lost. Persistence requirement fails.

- [X] FT-11: Patient can upload physical sign values in the follow-up section
  - Action: In Follow-up, submit a blood pressure reading (e.g., 120/80) and a blood glucose value (e.g., 5.6), then save.
  - Expected: Records are stored with the entered values and a date/time stamp, and appear in the patient's measurement list.
  - Actual: "Blood Pressure / 120/80 mmHg" and "Blood Glucose / 5.6 mg/dL / 11/8/2026, 11:27:54 AM" appear at the top of Recent Measurements and the "Vital Signs Recorded" stat increments. (Also visible to the doctor in Vital Signs History.)

- [X] FT-12: Doctor can view patient progress and adjust the follow-up plan
  - Action: Log in as the doctor and open the assigned patient's follow-up dashboard; edit a follow-up task/instruction and save.
  - Expected: The doctor sees the patient's per-task completion status and uploaded vitals, and the saved plan change is immediately reflected in the patient's follow-up section.
  - Actual: Doctor View shows John Doe's plan with per-task statuses ("Get adequate rest … Completed: 11/8/2026"), aggregates (Tasks Completed 6/7, Compliance 86%), and the patient's uploaded vital "Blood Glucose 5.6 mg/dL, 11/8/2026". "Modify Plan" → Add New Task ("Walk 20 minutes daily after dinner") → saved and immediately present in the patient's Follow-up Tasks (total 7→8). Minor note: existing task text cannot be edited directly (only add/remove pending tasks), but plan adjustment round-trips correctly.

## Constraint
- [ ] CS-01: A time slot already booked cannot be booked again
  - Action: Attempt to book a slot that is already occupied for that doctor.
  - Expected: The slot is shown as unavailable/unselectable, and submitting is blocked with an "already booked" or equivalent error.
  - Bug Report:
    - Issue: Missing occupancy validation (double-booking accepted)
    - Actual: After booking Dr. Mitchell for Mon, Nov 9 at 9:00 AM, reopening her booking dialog shows "9:00 AM" as a fully enabled, selectable button (disabled=false, no "Booked" marker). A second booking for the same doctor/date/time was accepted without any error — My Appointments then showed two "Upcoming" records for "Nov 9, 2026 9:00 AM" with Dr. Sarah Mitchell (tab count went to "Upcoming 3").

- [ ] CS-02: Booking cannot be completed without required information or payment
  - Action: Submit the booking form with a required field left empty, then with the payment step skipped.
  - Expected: Booking is rejected in both cases and an inline error names the missing field / unpaid consultation; no appointment record is created.
  - Bug Report:
    - Issue: Missing inline validation messages (rejection is only implicit)
    - Actual: Submission is never *rejected with a message*: the wizard simply disables "Continue"/"Continue to Payment" while fields are empty, and clicking "Pay $150" with an empty card number silently does nothing (dialog text identical before/after click, no error, no toast). No appointment record is created in either case — but the required "inline error names the missing field / unpaid consultation" is absent everywhere.

- [ ] CS-03: Only future, non-cancelled appointments can be cancelled
  - Action: Attempt to cancel an appointment that is already Cancelled, and one whose date is in the past.
  - Expected: No cancel action is offered/accepted for either, and their statuses remain unchanged.
  - Bug Report:
    - Issue: Cancel action offered on a past-dated appointment
    - Actual: Cancelled appointments (Dr. Garcia) and completed appointments correctly show no Cancel/Delete control. However, the seeded appointment dated "Dec 15, 2024" — a past date relative to the app's own clock (its slot picker generates dates from the real current week, Nov 9–20, 2026) — is labeled "Upcoming" and offers an active "Cancel" button. A past appointment can therefore be cancelled.

- [ ] CS-04: Physical sign input is validated
  - Action: Enter non-numeric or out-of-range values (e.g., blood glucose "abc" or "-5") and save.
  - Expected: Save is rejected with a validation message identifying the invalid field, and no malformed record is stored.
  - Bug Report:
    - Issue: Missing input validation (malformed records stored)
    - Actual: Blood Pressure value "abc" was accepted and stored — "Blood Pressure | abc mmHg | 11/8/2026, 11:27:46 AM" appeared in Recent Measurements and "Vital Signs Recorded" incremented 5→6. Blood Glucose "-5" was likewise stored as "-5 mg/dL". No validation message was displayed in any case.

## Interaction
- [ ] IX-01: Feedback is shown after a successful booking
  - Action: Complete a booking with payment.
  - Expected: A visible confirmation (toast or confirmation screen) states the booking succeeded and shows the booked date/time; the UI reflects the new appointment without a manual reload.
  - Bug Report:
    - Issue: No success feedback after booking
    - Actual: After "Pay $150" → "Processing…", the dialog silently closes and the user is left on the doctor profile/search page. No toast was rendered (notifications region stayed empty; polled every 300 ms through completion and 400 ms after) and no confirmation screen stating the booking succeeded or the booked date/time appears. The new appointment is only discoverable by navigating to My Appointments (whose count did update, but there is no booking-time confirmation message).

- [X] IX-02: Cancellation requires confirmation and updates state everywhere
  - Action: Click "Cancel Appointment" on a booked appointment.
  - Expected: A confirmation dialog appears first; after confirming, the status badge in history updates to "Cancelled" and cancelling from the dialog (dismiss) leaves the appointment intact.
  - Actual: Clicking Cancel opens an alert dialog "Cancel Appointment? … A full refund of $150 will be processed" with "Keep Appointment"/"Yes, Cancel". Dismissing via "Keep Appointment" left the appointment intact (Upcoming still 3). Confirming updated everything without reload: Upcoming 3→2 and the Cancelled tab immediately showed the record badged "cancelled / $150 • refunded".

- [X] IX-03: Task progress syncs live between patient and doctor views
  - Action: Mark a follow-up task complete as the patient, then refresh/open the doctor's dashboard for that patient.
  - Expected: The doctor's view shows that task as completed and the aggregate progress bar/count increases accordingly.
  - Actual: After the patient marked "Get adequate rest (7-8 hours sleep)" Completed (11/8/2026), opening Doctor View showed that exact task badged "Completed: 11/8/2026", plan progress "1 pending / 75%", and overall counters Tasks Completed "6 / 7" / Overall Compliance "86%" (up from 5/7, 71%).

## Content
- [X] CT-01: Default doctor dataset is present and on-theme
  - Action: Load the search page with no filters applied.
  - Expected: Multiple pre-existing doctor profiles are listed, each with a telemedicine-relevant specialty, experience, consultation fee, and treated symptoms; no placeholder/lorem text or broken avatar images.
  - Actual: 8 seeded doctors (Cardiologist, General Physician, Dermatologist, Pediatrician, Psychiatrist, Orthopedic, Gynecologist, Neurologist), each card with experience ("15 yrs") and fee ("$150"); profiles list "Conditions Treated" (e.g., Chest Pain, Shortness of Breath, Fatigue, Dizziness). All 8 avatar <img> elements have naturalWidth > 0 (none broken); no "lorem ipsum" text anywhere on the page.

- [ ] CT-02: Default appointments carry coherent clinical content
  - Action: Inspect the seeded history, visit notes, follow-up instructions, and vitals of the default patient account.
  - Expected: Each entry is consistent and relevant to its appointment (notes/instructions match the doctor and specialty shown), with no empty required fields or contradictory dates/statuses.
  - Bug Report:
    - Issue: Contradictory dates/statuses in seeded data
    - Actual: Clinical content is mostly coherent (Wilson's headache notes ↔ Acetaminophen instructions ↔ his General Physician profile; Chen's rash notes ↔ hydrocortisone instructions; Garcia cancelled ↔ "$180 • refunded"; vitals with units/timestamps). But status/date logic contradicts itself: an appointment dated "Dec 15, 2024" is badged "Upcoming" with active Join/Cancel actions, although the app's own date generator uses the real current date (booking slots offered are Nov 9–20, 2026). Likewise, follow-up tasks due "12/17/2024" remain "Pending" while the system clock is Nov 2026 — past-dated appointments/tasks are never reclassified.
