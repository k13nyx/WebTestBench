# Test Result

## Functionality

- [X] FT-01: Patient can search for doctors by specialty.
  - Action: Open the doctor search, enter a specialty available in the default data, and submit the search.
  - Expected: Doctors matching the selected specialty are displayed.

- [X] FT-02: Patient can search for doctors using symptoms.
  - Action: Enter a symptom supported by the default data and submit the search.
  - Expected: Doctors relevant to the entered symptom are displayed.

- [X] FT-03: Patient can compare doctor profiles.
  - Action: Select at least two doctors from the search results and choose **Compare**.
  - Expected: A comparison view displays the selected doctors’ experience and consultation fees side by side.

- [X] FT-04: Patient can book an available online appointment.
  - Action: Open a doctor profile, select an available future date and time, and proceed with booking.
  - Expected: The selected appointment is created and shown as an upcoming appointment.

- [X] FT-05: Patient can pay for a consultation during booking.
  - Action: During booking, enter valid payment details in the payment section and submit the payment.
  - Expected: Payment succeeds and the appointment is confirmed with a paid status.

- [X] FT-06: Patient can cancel an upcoming appointment online.
  - Action: Open an upcoming appointment and select **Cancel Appointment**, then confirm cancellation.
  - Expected: The appointment status changes to **Cancelled** and it is no longer listed as an active upcoming appointment.

- [X] FT-07: Patient can view appointment history and visit notes.
  - Action: Open **Appointment History** and select a completed appointment from the default data.
  - Expected: The record displays the appointment date, doctor, status, and associated visit notes.

- [X] FT-08: Patient can view doctor-provided follow-up instructions after a session.
  - Action: Open a completed appointment with follow-up information and select **Follow-up** or **View Instructions**.
  - Expected: The doctor’s follow-up instructions are displayed and associated with that appointment.

- [X] FT-09: Patient can update follow-up task completion status.
  - Action: Open the follow-up section in **Personal Center**, mark an assigned task as complete, and save the change.
  - Expected: The task displays the updated completion status after saving and reopening the follow-up section.

- [X] FT-10: Patient can upload physical sign data.
  - Action: In the follow-up section, enter valid blood pressure and blood glucose values, then submit the data.
  - Expected: The values are saved and displayed in the patient’s follow-up records with their corresponding measurements.

- [X] FT-11: Doctor can view a patient’s task completion progress.
  - Action: In the doctor view, open a patient’s follow-up plan after the patient changes a task status.
  - Expected: The doctor can see the patient’s updated task completion status and progress.

- [X] FT-12: Doctor can adjust a patient’s follow-up plan.
  - Action: Modify a patient’s follow-up task or instruction in the doctor view and save the plan.
  - Expected: The updated follow-up plan is saved and visible to the patient in the patient follow-up section.

## Constraint

- [X] CS-01: Search results do not include doctors unrelated to the selected specialty or symptom.
  - Action: Search using a specialty or symptom that does not match a displayed doctor’s profile.
  - Expected: The unrelated doctor is not included in the results.

- [ ] CS-02: Patient cannot book an unavailable appointment slot.
  - Action: Attempt to select a slot marked unavailable, already booked, or in the past.
  - Expected: The slot cannot be selected or booking cannot be completed.
  - Bug Report:
    - Issue: Unavailable-slot restriction could not be validated.
    - Actual: The appointment selector exposed all listed time slots as selectable and did not display an unavailable, already-booked, or past slot that could be tested.

- [X] CS-03: Appointment is not confirmed when required payment fails.
  - Action: Attempt to complete booking with invalid or declined payment details.
  - Expected: A payment failure message is shown and no confirmed paid appointment is created.

- [ ] CS-04: Invalid physical sign values cannot be submitted.
  - Action: Enter nonnumeric, incomplete, or otherwise invalid blood pressure or blood glucose values and submit.
  - Expected: Validation identifies the invalid fields and the data is not saved.
  - Bug Report:
    - Issue: Invalid physical sign values are accepted.
    - Actual: Submitting `abc` as a blood pressure value displayed “Vital sign recorded successfully” and saved the record as “Blood Pressure abc mmHg”.

- [X] CS-05: Cancelled appointments cannot remain in an active booked state.
  - Action: Cancel an eligible upcoming appointment and revisit the appointment list.
  - Expected: The appointment is marked **Cancelled** and cannot be treated as an active upcoming booking.

## Interaction

- [X] IX-01: Search controls update the doctor results after submission.
  - Action: Submit a specialty or symptom search, then change the search criteria and submit again.
  - Expected: The results refresh to reflect the latest criteria without retaining unrelated prior results.

- [ ] IX-02: Booking provides clear status feedback.
  - Action: Complete a valid appointment booking and payment.
  - Expected: The interface shows a booking-success confirmation containing the selected doctor, date, time, and payment status.
  - Bug Report:
    - Issue: Booking confirmation is incomplete.
    - Actual: The success notification stated “Appointment Booked! Your appointment with Dr. James Wilson is confirmed.” but did not include the selected date, time, or payment status in the confirmation.

- [ ] IX-03: Follow-up progress is reflected to the doctor in real time.
  - Action: Keep the patient follow-up view and doctor patient-progress view open, then change a task completion status in the patient view.
  - Expected: The doctor view reflects the changed status without requiring a manual page refresh.
  - Bug Report:
    - Issue: Real-time doctor progress update was not observed.
    - Actual: The doctor dashboard did not visibly update while the patient follow-up view was being changed; the updated progress was only observed after navigating/opening the doctor view.

- [ ] IX-04: Updated follow-up plans refresh for the patient.
  - Action: Save a follow-up plan change in the doctor view while the patient follow-up section is open.
  - Expected: The patient sees the updated task or instruction and its current status.
  - Bug Report:
    - Issue: Patient follow-up view does not demonstrate live plan refresh.
    - Actual: The newly added “Check blood pressure daily” task became visible only after navigating back to the patient follow-up page, not while the patient view remained open.

## Content

- [X] CT-01: Doctor profiles show complete comparison data.
  - Action: Open a doctor profile and the doctor comparison view.
  - Expected: Each displayed doctor has a relevant specialty, experience information, and consultation fee.

- [X] CT-02: Appointment history content is tied to the correct visit.
  - Action: Open multiple completed appointment records from the default data.
  - Expected: Each record shows the correct doctor, visit date, status, and visit notes for that specific appointment.

- [X] CT-03: Follow-up content clearly identifies tasks and physical sign measurements.
  - Action: Open a patient follow-up plan containing tasks and uploaded measurements.
  - Expected: Tasks show their completion status, and blood pressure and blood glucose values are labeled with the correct measurement names and associated dates.
