# Test Checklist

## Functionality
- [ ] FT-01: Patient can search for doctors by specialty and view matching results
  - Action: Enter a specialty (e.g., "Cardiology") in the doctor search and submit.
  - Expected: A list of doctors whose specialty matches the entered term is displayed.

- [ ] FT-02: Patient can search for doctors by symptoms and view matching results
  - Action: Enter a symptom (e.g., "headache") in the doctor search and submit.
  - Expected: A list of doctors who treat the entered symptom is displayed.

- [ ] FT-03: Patient can open a doctor profile and see experience and consultation fee
  - Action: Click on a doctor from the search results.
  - Expected: The doctor's profile page shows the doctor's experience (years/background) and consultation fee.

- [ ] FT-04: Patient can compare multiple doctors side-by-side
  - Action: Select two or more doctors from the search results and open the comparison view.
  - Expected: A comparison view shows the selected doctors' experience and consultation fees together for side-by-side review.

- [ ] FT-05: Patient can book an appointment and pay the consultation fee in the booking flow
  - Action: Choose a doctor, select an available time slot, click "Book", and complete payment.
  - Expected: The appointment is created and the consultation fee payment is recorded as successful.

- [ ] FT-06: Patient can cancel an existing appointment
  - Action: From appointment history, click "Cancel" on an upcoming appointment.
  - Expected: The appointment status changes to cancelled and no longer appears as upcoming.

- [ ] FT-07: Patient can view appointment history with visit notes from the doctor
  - Action: Navigate to the appointment history section in the personal center.
  - Expected: Each past appointment entry includes visit notes written by the doctor.

- [ ] FT-08: Patient can view follow-up instructions from the doctor after a session
  - Action: Open the follow-up section for a completed appointment.
  - Expected: Follow-up instructions provided by the doctor are visible to the patient.

- [ ] FT-09: Patient can mark a follow-up task as completed
  - Action: In the follow-up section, click the "Mark complete" control on a follow-up task.
  - Expected: The task's status changes to completed and is reflected in the patient's follow-up list.

- [ ] FT-10: Patient can upload physical sign data (blood pressure and blood glucose)
  - Action: In the follow-up section, enter/submit blood pressure and blood glucose values for a task.
  - Expected: The sign data values are saved and shown alongside the related follow-up task.

- [ ] FT-11: Doctor can view a patient's task completion progress in real time
  - Action: As a doctor, open the patient's follow-up view from the doctor side.
  - Expected: The doctor's view shows the patient's task completion status and uploaded sign data.

- [ ] FT-12: Doctor can adjust the patient's follow-up plan based on progress
  - Action: As a doctor, edit/add/remove a follow-up task or instruction for a patient and save.
  - Expected: The patient's follow-up section reflects the updated plan after the change.

## Constraint
- [ ] CS-01: Booking cannot be finalized without a successful consultation payment
  - Action: Attempt to confirm a booking without completing payment (skip or fail the payment step).
  - Expected: The appointment is not created/confirmed and the user is required to complete payment before the booking is finalized.

- [ ] CS-02: Follow-up sign data submission requires both blood pressure and blood glucose values
  - Action: Submit the follow-up sign-data form with only blood pressure (or only blood glucose) filled in.
  - Expected: Submission is rejected and the patient is prompted to provide both blood pressure and blood glucose values.

## Interaction
- [ ] IX-01: Cancelling an appointment requires a confirmation step before the change takes effect
  - Action: Click "Cancel" on an upcoming appointment.
  - Expected: A confirmation dialog appears; the appointment is only cancelled after the user confirms.

- [ ] IX-02: Doctor's view of patient progress updates after the patient marks a task or uploads sign data
  - Action: As a patient, mark a task complete / upload new sign data; then refresh or revisit the doctor's patient view.
  - Expected: The doctor's view reflects the latest task status and most recent sign data without requiring a manual reload workaround.

## Content
- [ ] CT-01: Doctor profile page displays both experience information and consultation fee
  - Action: Open any doctor's profile from the default doctor list.
  - Expected: The page shows experience details (e.g., years, background) and a clearly labeled consultation fee.

- [ ] CT-02: Follow-up section contains dedicated fields for blood pressure and blood glucose
  - Action: Open the patient's follow-up section in the personal center.
  - Expected: Two distinct input fields are present — one for blood pressure and one for blood glucose.