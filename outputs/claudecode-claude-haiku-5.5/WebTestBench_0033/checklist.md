# Test Checklist

## Functionality
- [ ] FT-01: Patient can find doctors by specialty and symptom
  - Action: On the search page, select a specialty (e.g., "Cardiology") and enter the symptom "chest pain", then click "Search".
  - Expected: Results show only doctors matching the specialty and listing the symptom. Each result shows name, specialty, years of experience, and consultation fee.
- [ ] FT-02: Patient can compare doctor profiles side by side
  - Action: Tick "Compare" on two doctors in the results, then click "Compare Selected".
  - Expected: A comparison view opens with both doctors' specialty, years of experience, and consultation fee in aligned columns, matching their individual profiles.
- [ ] FT-03: Patient can book a consultation and pay during booking
  - Action: Open an available doctor's profile, click "Book Appointment", select an open date and time slot, click "Pay & Confirm", and complete payment with the test payment method provided for this environment.
  - Expected: Payment succeeds and the appointment appears in "My Appointments" with status "Upcoming", showing the doctor, date, time, and "Paid".
- [ ] FT-04: Patient can cancel an upcoming appointment
  - Action: In "My Appointments", open an "Upcoming" appointment, click "Cancel Appointment", and confirm.
  - Expected: The appointment status changes to "Cancelled" and the time slot becomes bookable again on the doctor's schedule.
- [ ] FT-05: Patient can view appointment history with visit notes and follow-up instructions
  - Action: Open "Appointment History" and click a completed appointment.
  - Expected: The list shows past appointments with date, doctor, and status. The detail view shows the visit notes and the doctor's follow-up instructions.
- [ ] FT-06: Patient can mark follow-up tasks as completed
  - Action: Go to Personal Center > Follow-up, tick the checkbox of task "Take prescribed medication", then reload the page.
  - Expected: The task remains marked as completed after reload, and the progress indicator (e.g., "1/3 completed") reflects the change.
- [ ] FT-07: Patient can upload blood pressure and blood glucose readings
  - Action: In Personal Center > Follow-up, click "Add Sign Data", choose "Blood Pressure", enter systolic 120 and diastolic 80, click "Save". Repeat with "Blood Glucose", value 5.6.
  - Expected: Both entries are saved and listed in the sign data history with date/time and values "120/80 mmHg" and "5.6 mmol/L".
- [ ] FT-08: Doctor can view patient task progress and sign data in real time
  - Action: Log in as the doctor and open the follow-up dashboard for a patient. In a separate session, log in as that patient and tick a task and upload a blood glucose reading. Watch the doctor dashboard without manually refreshing.
  - Expected: Within 10 seconds, the doctor dashboard shows the updated task status, the new glucose reading, and the updated completion progress.
- [ ] FT-09: Doctor can adjust a patient's follow-up plan
  - Action: As the doctor, open the patient's follow-up plan, change "Measure blood glucose" frequency from "Daily" to "Twice daily", and click "Save Plan". Then log in as the patient and open Personal Center > Follow-up.
  - Expected: The plan saves, and the patient sees the task with frequency "Twice daily".

## Constraint
- [ ] CS-01: Patient cannot book a time slot that is already taken
  - Action: On a doctor's booking calendar, find a slot labeled "Booked" or "Unavailable" and attempt to click it.
  - Expected: The slot cannot be selected, and "Pay & Confirm" is not reachable for that slot.
- [ ] CS-02: Booking is not created when payment fails
  - Action: Book an available slot and, at payment, use the declined test payment method provided for this environment. Click "Pay & Confirm".
  - Expected: An error "Payment failed" is shown, the slot is not held, and no new appointment appears in "My Appointments".
- [ ] CS-03: Completed appointments cannot be cancelled
  - Action: In "Appointment History", open a "Completed" appointment.
  - Expected: No "Cancel Appointment" button is shown or it is disabled.
- [ ] CS-04: Invalid sign data is rejected
  - Action: In "Add Sign Data" for "Blood Pressure", leave the diastolic field blank and enter "abc" in systolic, then click "Save".
  - Expected: Saving is blocked, field-level errors "Enter a valid number" appear for both fields, and no entry is added to the history.
- [ ] CS-05: Patient cannot edit the follow-up plan
  - Action: As the patient, open Personal Center > Follow-up and look for any control to edit frequency, add, or remove plan items.
  - Expected: No plan-editing controls exist. The patient can only tick task checkboxes and add sign data.

## Interaction
- [ ] IX-01: Booking shows a confirmation message after successful payment
  - Action: Complete a successful booking as in FT-03.
  - Expected: A confirmation message "Appointment confirmed" appears on screen before the page redirects to "My Appointments".
- [ ] IX-02: Cancel action asks for confirmation and can be undone
  - Action: Click "Cancel Appointment" on an upcoming appointment, then click "Keep Appointment" in the dialog.
  - Expected: The dialog closes, the appointment status remains "Upcoming", and no change is saved.
- [ ] IX-03: Task completion updates instantly on the page
  - Action: In Personal Center > Follow-up, tick a task checkbox without reloading the page.
  - Expected: The task text is immediately struck through and the progress indicator updates at once.

## Content
- [ ] CT-01: Doctor profiles display complete experience and fee information
  - Action: Open the profile of three different doctors from search results.
  - Expected: Each profile shows a non-empty years-of-experience value and a consultation fee with a currency symbol. No field is blank or shows "undefined" or "null".
- [ ] CT-02: Visit notes and follow-up instructions match their appointment
  - Action: Open a completed appointment in "Appointment History".
  - Expected: The doctor name, appointment date, and visit notes/instructions correspond to that appointment and no other.
- [ ] CT-03: Sign data units and task lists are consistent between patient and doctor views
  - Action: Compare the follow-up task list and sign data history for one patient in the patient view (Personal Center > Follow-up) and the doctor view for the same patient.
  - Expected: Both views show the same tasks and statuses. Blood pressure is labeled "mmHg" and blood glucose is labeled "mmol/L" in both.