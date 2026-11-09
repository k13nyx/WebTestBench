# Test Result

## Functionality

- [X] FT-01: Patient can search for doctors by specialty and view matching results
  - Action: Enter a specialty (e.g., "Cardiology") in the doctor search and submit.
  - Expected: A list of doctors whose specialty matches the entered term is displayed.

- [X] FT-02: Patient can search for doctors by symptoms and view matching results
  - Action: Enter a symptom (e.g., "headache") in the doctor search and submit.
  - Expected: A list of doctors who treat the entered symptom is displayed.

- [X] FT-03: Patient can open a doctor profile and see experience and consultation fee
  - Action: Click on a doctor from the search results.
  - Expected: The doctor's profile page shows the doctor's experience (years/background) and consultation fee.

- [X] FT-04: Patient can compare multiple doctors side-by-side
  - Action: Select two or more doctors from the search results and open the comparison view.
  - Expected: A comparison view shows the selected doctors' experience and consultation fees together for side-by-side review.

- [X] FT-05: Patient can book an appointment and pay the consultation fee in the booking flow
  - Action: Choose a doctor, select an available time slot, click "Book", and complete payment.
  - Expected: The appointment is created and the consultation fee payment is recorded as successful.

- [X] FT-06: Patient can cancel an existing appointment
  - Action: From appointment history, click "Cancel" on an upcoming appointment.
  - Expected: The appointment status changes to cancelled and no longer appears as upcoming.

- [X] FT-07: Patient can view appointment history with visit notes from the doctor
  - Action: Navigate to the appointment history section in the personal center.
  - Expected: Each past appointment entry includes visit notes written by the doctor.

- [X] FT-08: Patient can view follow-up instructions from the doctor after a session
  - Action: Open the follow-up section for a completed appointment.
  - Expected: Follow-up instructions provided by the doctor are visible to the patient.

- [X] FT-09: Patient can mark a follow-up task as completed
  - Action: In the follow-up section, click the "Mark complete" control on a follow-up task.
  - Expected: The task's status changes to completed and is reflected in the patient's follow-up list.

- [ ] FT-10: Patient can upload physical sign data (blood pressure and blood glucose)
  - Action: In the follow-up section, enter/submit blood pressure and blood glucose values for a task.
  - Expected: The sign data values are saved and shown alongside the related follow-up task.
  - Bug Report:
    - Issue: Missing task association for vital sign data
    - Actual: Vital signs (blood pressure 125/85 mmHg and blood glucose 110 mg/dL) were recorded successfully, but they appear in a separate "Vital Signs" tab as standalone entries and are NOT shown "alongside the related follow-up task". The form requires only ONE measurement type + ONE value at a time, with no link to any specific follow-up task. Sign data has no per-task association.

- [ ] FT-11: Doctor can view a patient's task completion progress in real time
  - Action: As a doctor, open the patient's follow-up view from the doctor side.
  - Expected: The doctor's view shows the patient's task completion status and uploaded sign data.
  - Bug Report:
    - Issue: Doctor view shows stale task completion data (not real-time)
    - Actual: After marking "Get adequate rest" as Completed on patient side (progress went from 71% (5/7) to 86% (6/7)), the Doctor Dashboard still showed "Tasks Completed: 5 / 7" and "Overall Compliance: 71%". The doctor's view did not reflect the patient's most recent action.

- [ ] FT-12: Doctor can adjust the patient's follow-up plan based on progress
  - Action: As a doctor, edit/add/remove a follow-up task or instruction for a patient and save.
  - Expected: The patient's follow-up section reflects the updated plan after the change.
  - Bug Report:
    - Issue: Doctor's plan changes do not persist on the patient side
    - Actual: After clicking "Modify Plan" and successfully adding a new task ("New follow-up: Monitor blood pressure daily") with confirmation "Task added to follow-up plan", the task appeared on the doctor dashboard within the session. However, after navigating to the patient's My Health page, the new task was NOT visible — only the original tasks were shown. The change did not persist across views.

## Constraint

- [X] CS-01: Booking cannot be finalized without a successful consultation payment
  - Action: Attempt to confirm a booking without completing payment (skip or fail the payment step).
  - Expected: The appointment is not created/confirmed and the user is required to complete payment before the booking is finalized.

- [ ] CS-02: Follow-up sign data submission requires both blood pressure and blood glucose values
  - Action: Submit the follow-up sign-data form with only blood pressure (or only blood glucose) filled in.
  - Expected: Submission is rejected and the patient is prompted to provide both blood pressure and blood glucose values.
  - Bug Report:
    - Issue: Form does not require both BP and BG together
    - Actual: The "Record Vital Signs" form uses a single "Measurement Type" dropdown (Blood Pressure, Blood Glucose, Heart Rate, Weight, Temperature) and a single "Value" field. A submission with only Blood Pressure (or only Blood Glucose) is accepted without any prompt to provide both — there is no constraint that requires both values to be entered together.

## Interaction

- [X] IX-01: Cancelling an appointment requires a confirmation step before the change takes effect
  - Action: Click "Cancel" on an upcoming appointment.
  - Expected: A confirmation dialog appears; the appointment is only cancelled after the user confirms.

- [ ] IX-02: Doctor's view of patient progress updates after the patient marks a task or uploads sign data
  - Action: As a patient, mark a task complete / upload new sign data; then refresh or revisit the doctor's patient view.
  - Expected: The doctor's view reflects the latest task status and most recent sign data without requiring a manual reload workaround.
  - Bug Report:
    - Issue: Doctor dashboard does not auto-update with latest patient progress
    - Actual: After patient marked a task complete (progress 71% → 86%) and recorded new vital signs (BP 125/85, BG 110), the Doctor Dashboard continued to show "Tasks Completed: 5 / 7", "Overall Compliance: 71%", and the original 5 "Recent Measurements". Real-time sync is not implemented; a manual reload would be required to see any updates.

## Content

- [X] CT-01: Doctor profile page displays both experience information and consultation fee
  - Action: Open any doctor's profile from the default doctor list.
  - Expected: The page shows experience details (e.g., years, background) and a clearly labeled consultation fee.

- [ ] CT-02: Follow-up section contains dedicated fields for blood pressure and blood glucose
  - Action: Open the patient's follow-up section in the personal center.
  - Expected: Two distinct input fields are present — one for blood pressure and one for blood glucose.
  - Bug Report:
    - Issue: Follow-up section lacks dedicated, distinct BP and BG input fields
    - Actual: The follow-up section has only ONE "Record Vital Signs" form with a single "Measurement Type" dropdown and a single "Value" field. There are NOT two distinct, dedicated input fields — one for blood pressure and one for blood glucose — as expected by the requirement.
