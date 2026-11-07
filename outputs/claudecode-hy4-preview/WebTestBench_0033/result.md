I've completed all checklist items. Here is the full results report.

# Test Result

## Functionality

- [X] FT-01: Search doctors by specialty
  - Action: On the doctor search page, select a specialty from the "Specialty" filter (e.g., the first listed option) and apply the search.
  - Expected: Only doctors whose specialty matches the selected filter are listed (count > 0), and each result's displayed specialty matches the filter.
  - Observed: Selecting "General Physician" reduced the list to "1 doctors found" — Dr. James Wilson, General Physician.

- [X] FT-02: Search doctors by symptom
  - Action: Enter or select a symptom (e.g., the first symptom option available) in the symptom search/filter and run the search.
  - Expected: Result list contains only doctors associated with that symptom; each result relates to the searched symptom; no unrelated doctors appear.
  - Observed: "Fever" returned 2 doctors (Dr. James Wilson, Dr. Lisa Patel). Both profiles list "Fever" under "Conditions Treated"; Dr. Sarah Mitchell (whose conditions are Chest Pain/Shortness of Breath/Fatigue/Dizziness) was correctly excluded.

- [X] FT-03: Doctor profile shows experience and consultation fee
  - Action: Open a doctor's profile from the search results.
  - Expected: Profile displays labeled "Years of Experience" (numeric) and "Consultation Fee" (amount with currency) values.
  - Observed: /doctor/dr-001 shows "15 years experience", "4.9 (328 reviews)", "$150 per consultation", plus a booking panel "Consultation Fee — $150". /doctor/dr-002 shows "12 years experience" and "$80 per consultation".

- [X] FT-04: Compare doctor profiles by experience and fee
  - Action: Select two doctors from the results (e.g., via "Compare" on each card) and open the comparison view.
  - Expected: Both doctors appear side by side, each showing years of experience and consultation fee, with values matching their individual profiles.
  - Observed: /compare shows Dr. James Wilson (Experience 12 years, Consultation $80) and Dr. Sarah Mitchell (Experience 15 years, Consultation $150) side by side, matching their profiles.

- [X] FT-05: Book an appointment and pay the consultation fee during booking
  - Action: From a doctor's profile, pick an available future date/time slot, proceed to booking, complete the payment step, and confirm.
  - Expected: Payment is accepted and a new appointment appears as "Confirmed"/"Booked" with that doctor, date and time; charged amount equals the doctor's displayed consultation fee.
  - Observed: Booked Dr. James Wilson, Nov 9, 2026 at 9:00 AM, paid $80 (equal to his $80 fee). Toast "Appointment Booked!" and dialog "Booking Confirmed! ... November 9, 2026 at 9:00 AM."; My Appointments → Upcoming lists it as "upcoming" with "$80 • paid".

- [X] FT-06: Cancel a booked appointment
  - Action: Open the upcoming appointment created in FT-05 (or any existing upcoming appointment) and choose "Cancel".
  - Expected: Appointment status changes to "Cancelled" and it no longer appears as an active upcoming booking.
  - Observed: Confirmation dialog "Cancel Appointment?" → "Yes, Cancel" produced toast "Appointment Cancelled — Your appointment has been cancelled and refund initiated."; Upcoming count dropped 3 → 2; the Cancelled tab shows it as "cancelled" with "$80 • refunded".

- [X] FT-07: Appointment history displays visit notes
  - Action: In the personal center, open "Appointment History" (or Past appointments) and open a completed appointment's details.
  - Expected: Past appointments are listed in date order; each completed appointment detail shows non-empty visit notes recorded by the doctor.
  - Observed: Completed tab lists Dec 10, 2024 (Dr. James Wilson) then Nov 28, 2024 (Dr. Emily Chen) in descending date order; both have a "Visit Notes" section with non-empty clinical text.

- [X] FT-08: Follow-up instructions shown after a session
  - Action: Open the details of a completed appointment from the history.
  - Expected: Doctor's follow-up instructions for that session are displayed (care/medication guidance), attributed to that session's doctor and distinct from the visit notes.
  - Observed: Under "Visit Notes" there is a separate "Follow-up Instructions" heading with numbered care/medication guidance (e.g., Acetaminophen 500mg dosing, hydration, rest) for the Dr. James Wilson session — content distinct from the notes paragraph.

- [ ] FT-09: Mark a follow-up task as completed
  - Action: In personal center → Follow-up section, open the follow-up plan of a completed session, mark one incomplete task as completed, and save.
  - Expected: That task's status becomes "Completed" and stays "Completed" after refreshing the page.
  - Bug Report:
    - Issue: State not persisted — task completion is lost on page refresh
    - Actual: Clicking the complete action on "Get adequate rest (7-8 hours sleep)" changed it to "Completed" (Completed: 11/7/2026) and the dashboard went from 71% (5/7) to 86% (6/7). After refreshing the page (/my-health reloaded), the same task reverted to "Pending" and the completion rate returned to 71% (5/7). The app keeps all state in memory only (no localStorage/sessionStorage keys present), so the completed mark does not survive a refresh.

- [X] FT-10: Upload physical sign data in the follow-up section
  - Action: In the same Follow-up section, enter a blood pressure value (e.g., 120/80) and a blood glucose value (e.g., 95), then submit.
  - Expected: Both entries are saved and appear in the physical sign records list with the entered values and the submission date.
  - Observed: "Blood Pressure / 120/80 mmHg — 11/8/2026" and "Blood Glucose / 95 mg/dL — 11/8/2026" both appear at the top of Recent Measurements, with toast "Vital sign recorded successfully".

- [X] FT-11: Doctor views patient progress in real time and adjusts the follow-up plan
  - Action: Open the doctor-side view of that same patient's follow-up record; check the task marked in FT-09 and the signs uploaded in FT-10 appear without re-entry; then edit the follow-up plan (add or modify a task) and save.
  - Expected: Doctor view shows the patient's current completion status and uploaded signs exactly as submitted; after saving, the patient's Follow-up section shows the updated task list.
  - Observed: Doctor Dashboard shows the FT-09 task as "Completed: 11/7/2026" and both new readings ("120/80 mmHg" and "95 mg/dL", 11/8/2026) with identical values/timestamps — no re-entry needed. "Modify Plan" → "Add New Task" added "Record body temperature each morning" (Daily, Due 11/20/2026) with toast "Task added to follow-up plan"; returning to My Health → Follow-up Tasks shows that new task under the Dr. James Wilson plan.

## Constraint

- [ ] CS-01: An already occupied time slot cannot be booked
  - Action: Attempt to book a date/time slot that is already booked or shown as unavailable for a doctor.
  - Expected: The slot cannot be booked — it is disabled or the booking is rejected with a message; no duplicate appointment is created.
  - Bug Report:
    - Issue: Double-booking allowed — occupied slot neither disabled nor rejected
    - Actual: Dr. James Wilson, Nov 9, 2026 at 9:00 AM was already booked and paid. Reopening the booking modal for the same doctor and date showed 9:00 AM as a normal, enabled button (not greyed out or marked unavailable). Selecting it, entering symptoms, and paying $80 succeeded: toast "Appointment Booked!" and dialog "Booking Confirmed! ... November 9, 2026 at 9:00 AM." My Appointments → Upcoming then listed two identical appointments for Dr. James Wilson on Nov 9, 2026 at 9:00 AM, both "upcoming" / "$80 • paid".

- [X] CS-02: Booking is not confirmed without successful payment
  - Action: Start a booking and use a payment that fails or is declined (or abandon the payment step), then check the appointment list.
  - Expected: No confirmed appointment exists for that slot; it remains unpaid/pending or is absent from appointments.
  - Observed: Clicking "Pay $80" with an empty card number was rejected with toast "Invalid card — Please enter a valid card number"; the Payment Details dialog stayed open and no appointment was created (the Upcoming list contained only the pre-existing appointment plus the one later paid for).

- [X] CS-03: A completed or already cancelled appointment cannot be cancelled again
  - Action: Open a past/completed appointment, then an already-cancelled appointment, from the history.
  - Expected: No active "Cancel" action is available for either (hidden or disabled); their statuses remain "Completed" and "Cancelled".
  - Observed: Completed tab entries (Dr. James Wilson Dec 10, 2024; Dr. Emily Chen Nov 28, 2024) show only a "Visit Notes" button — no Cancel action — and status "completed". Cancelled tab entries (Dr. Robert Garcia; the cancelled Dr. James Wilson booking) show no action buttons at all and status "cancelled".

- [ ] CS-04: Invalid physical sign values are rejected
  - Action: In the Follow-up physical sign form, submit a non-numeric value (e.g., "abc") or a negative/empty value and try to save.
  - Expected: Save is blocked with a visible validation message and no invalid entry is added to the records list.
  - Bug Report:
    - Issue: Missing numeric/range validation on vital-sign values
    - Actual: Submitting "abc" as Blood Pressure was accepted — toast "Vital sign recorded successfully" and a new record "Blood Pressure / abc mmHg — 11/8/2026, 2:18:33 AM" was added. Submitting "-5" as Blood Glucose was also accepted, adding "Blood Glucose / -5 mg/dL — 11/8/2026, 2:18:53 AM". Both invalid entries also appeared in the Doctor Dashboard's "Patient Vital Signs History". Only the empty-value case was blocked, with the message "Please fill in all required fields".

## Interaction

- [X] IX-01: Doctor list updates dynamically when filters change
  - Action: With the doctor list displayed, change the specialty or symptom filter, then clear it.
  - Expected: List refreshes to the matching doctors without a full page reload (no blank or broken state); clearing filters restores the full default doctor list.
  - Observed: Specialty "General Physician" → "1 doctors found"; symptom "Fever" → "2 doctors found"; "Clear all filters" → "8 doctors found" and the dropdown returned to "All Specialties". A `window` marker set before filtering was still present afterwards, confirming no full page reload; no blank/broken state at any point.

- [X] IX-02: Confirmation feedback for booking, payment and cancellation
  - Action: Complete a booking with payment, then cancel an appointment.
  - Expected: A success/confirmation message (toast or banner) appears after booking and payment confirming the appointment, and another after cancellation confirming it was cancelled.
  - Observed: After payment: toast "Appointment Booked! — Your appointment with Dr. James Wilson is confirmed." plus the modal "Booking Confirmed! ... November 9, 2026 at 9:00 AM." After cancellation: toast "Appointment Cancelled — Your appointment has been cancelled and refund initiated."

## Content

- [X] CT-01: Doctor cards and profiles contain relevant, complete medical content
  - Action: Review the doctor cards in search results and one doctor profile page.
  - Expected: Each card shows doctor name, specialty and a photo/avatar that loads correctly and depicts a person/doctor (no broken image or unrelated placeholder imagery).
  - Observed: All 8 cards show name, specialty, rating, experience and fee; all 8 avatars loaded successfully (naturalWidth/Height 300×300) from Unsplash face-cropped portrait URLs (e.g., photo-1559839734-2b71ea197ec2, photo-1612349317150-e413f6a5b16d), alt text matching each doctor's name. No broken images.

- [X] CT-02: Visit notes and follow-up instructions belong to the correct appointment
  - Action: Open the details of two different completed appointments from history.
  - Expected: Each shows notes and follow-up instructions specific to that appointment and its doctor (content differs across different sessions); no "lorem ipsum" or unrelated placeholder text.
  - Observed: Dr. James Wilson (Dec 10, 2024, headache/fever) → "Patient presented with tension-type headache and low-grade fever..." with instructions about Acetaminophen 500mg, hydration and rest. Dr. Emily Chen (Nov 28, 2024, skin rash) → "Diagnosed with contact dermatitis, likely caused by new laundry detergent..." with instructions about hydrocortisone cream and hypoallergenic products. Content is distinct, clinically coherent, and free of placeholder text.

- [X] CT-03: Physical sign records are labeled with correct units and dates
  - Action: Review the physical sign records list in the Follow-up section after FT-10.
  - Expected: Entries are labeled "Blood Pressure" (mmHg) and "Blood Glucose" (mg/dL or mmol/L) with correct units, and each entry shows the date it was recorded.
  - Observed: New entries read "Blood Pressure — 120/80 mmHg — 11/8/2026, 2:19:09 AM" and "Blood Glucose — 95 mg/dL — 11/8/2026, 2:19:22 AM"; historical entries follow the same pattern (118/78 mmHg, 102 mg/dL, 72 bpm). The form input label also switches to "Value (mmHg)" / "Value (mg/dL)" per type.