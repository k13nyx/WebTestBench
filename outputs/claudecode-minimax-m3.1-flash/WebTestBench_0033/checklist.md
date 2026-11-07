# Test Checklist

## Functionality
- [ ] FT-01: Search doctors by specialty
  - Action: On the doctor search page, open the Specialty filter, choose an existing specialty from the dropdown (e.g. "Cardiology"), and trigger the search.
  - Expected: The result list shows only doctors whose profile specialty matches the selected specialty, each card showing the doctor's name and specialty.

- [ ] FT-02: Search doctors by symptoms
  - Action: Enter a symptom term (e.g. "headache" or "chest pain") in the symptom search field and submit the search.
  - Expected: The result list shows doctors matching the entered symptom, with the matched symptom indicated on each result card or in the doctor profile.

- [ ] FT-03: View and compare doctor profiles
  - Action: Open two different doctors' profile pages from the search results (e.g. via "Compare" / "Add to compare" or by visiting each profile).
  - Expected: Each profile shows the doctor's name, specialty, years of experience, and consultation fee, so the two doctors' experience and fees can be compared side by side.

- [ ] FT-04: Book an appointment online
  - Action: On a doctor profile, click "Book Appointment", select an available date and time slot, confirm the booking, and submit.
  - Expected: The appointment is created and confirmed; a confirmation with the doctor name, date, and time appears, and the appointment appears in the patient's appointment list.

- [ ] FT-05: Pay for the consultation during booking
  - Action: During the appointment booking flow, select a payment method, enter valid payment details, and complete the payment step before the booking is finalized.
  - Expected: The payment is processed successfully, a payment confirmation/receipt (amount and doctor) is shown, and the appointment is only registered as confirmed when payment succeeds.

- [ ] FT-06: Cancel a booked appointment
  - Action: Open the patient's appointments list, locate the confirmed appointment to cancel, and click "Cancel" then confirm the cancellation.
  - Expected: The appointment's status changes to "Cancelled" and it no longer appears as an upcoming active appointment.

- [ ] FT-07: View appointment history with visit notes
  - Action: Open the patient's appointment history page and open a past/completed appointment record.
  - Expected: The record shows the appointment date, doctor, visit notes written by the doctor, and any follow-up instructions issued for that session.

- [ ] FT-08: Doctor issues follow-up instructions after a session
  - Action: Log in as the doctor, open a completed consultation, and enter follow-up instructions (e.g. tasks for the patient), then save.
  - Expected: The follow-up instructions are saved and become visible to the patient in their personal center follow-up section for that appointment.

- [ ] FT-09: Patient marks a follow-up task as completed
  - Action: In the personal center's follow-up section, find a follow-up task assigned by the doctor and mark its completion status as completed.
  - Expected: The task's status changes to completed and the updated completion state is retained on the follow-up list.

- [ ] FT-10: Patient uploads physical sign data (blood pressure / blood glucose)
  - Action: In the personal center's follow-up section, use the add/upload entry for physical signs, enter a blood pressure value and/or a blood glucose value, and save.
  - Expected: The new reading is recorded and listed in the patient's physical sign records with its type, value, and recorded date.

- [ ] FT-11: Doctor views patient task completion progress and adjusts the follow-up plan
  - Action: Log in as the doctor, open the patient whose follow-up tasks are assigned, review the patient's task completion progress and uploaded readings, then modify the follow-up plan (tasks/instructions) and save.
  - Expected: The doctor sees the patient's current task completion progress and physical sign data, and the adjusted follow-up plan is saved and reflected for the patient.

## Constraint
- [ ] CS-01: Booking requires a selected date and available time slot
  - Action: On the booking form, attempt to confirm the booking without choosing a date/slot, then repeat after choosing an already-taken slot.
  - Expected: The first attempt is blocked with a clear validation message and no appointment is created; the second attempt is rejected because the slot is unavailable.

- [ ] CS-02: An appointment cannot be confirmed without a successful payment
  - Action: In the booking flow, attempt to confirm the appointment without completing payment, then repeat with invalid payment details.
  - Expected: The booking is not confirmed and no appointment is recorded as confirmed; a clear error/payment-required message is shown.

- [ ] CS-03: A doctor cannot be double-booked for the same time slot
  - Action: Book a specific doctor/date/slot, then attempt to book the same doctor, date, and slot from another session.
  - Expected: The second booking is rejected as the slot is unavailable/already booked, and only one appointment exists for that slot.

- [ ] CS-04: Invalid physical sign values are rejected
  - Action: In the physical sign entry, attempt to save a blood pressure entry with a non-numeric or malformed value and a blood glucose entry with a negative or non-numeric value.
  - Expected: The entries are not saved, an inline validation error is shown next to the offending field, and no invalid record appears in the patient's physical sign history.

## Interaction
- [ ] IX-01: Booking success is confirmed to the patient
  - Action: Complete a successful booking (including payment) and observe the page response.
  - Expected: A success confirmation (e.g. success banner/toast and on-screen confirmation panel) is displayed and the interface transitions to the confirmed appointment state.

- [ ] IX-02: Doctor progress view reflects patient task status updates
  - Action: While logged in as the doctor on the patient's follow-up progress view, have the patient mark a follow-up task completed, then observe the doctor view without manually reloading the page.
  - Expected: The doctor's view updates to show the new completion status/progress (automatically or after the view's own refresh control) without showing stale "not completed" data.

- [ ] IX-03: Cancelling an appointment requires an explicit confirmation step
  - Action: Click "Cancel" on a confirmed appointment.
  - Expected: A confirmation dialog/notice appears with options to confirm or dismiss; dismissing leaves the appointment active, while confirming cancels it.

## Content
- [ ] CT-01: Doctor profile content is correct and complete
  - Action: Open a doctor profile and compare the displayed specialty, years of experience, and consultation fee against the same doctor's details shown in the search results.
  - Expected: Specialty, experience (years), and consultation fee are all present, non-empty, and consistent across the search result and the profile page.

- [ ] CT-02: Visit notes and follow-up instructions are readable and tied to the correct appointment
  - Action: Open an appointment in the patient's history and compare the visit notes and follow-up instructions with the text entered by the doctor for that same session.
  - Expected: The visit notes and follow-up instructions displayed match the doctor's entered text and are shown under the correct appointment/date.

- [ ] CT-03: Physical sign entries display the recorded type, value, and date
  - Action: Open the physical sign records list in the personal center after uploading a blood pressure and a blood glucose reading.
  - Expected: Each entry shows the correct measurement type (blood pressure / blood glucose), the entered numeric value, and the recorded date, with no missing or mislabeled values.