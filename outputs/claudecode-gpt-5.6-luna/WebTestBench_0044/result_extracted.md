# Test Result

## Functionality

- [X] TEST-ID: **FT-01: View the personal job application list**
  - Action: Open the application list using the default data already present.
  - Expected: Each listed application displays its company, role, date, status, and associated notes.

- [X] TEST-ID: **FT-02: Add a new job application**
  - Action: Select **Add Application**, enter a company, role, date, status, and brief notes, then select **Save**.
  - Expected: The new application appears in the personal list with all entered details unchanged.

- [X] TEST-ID: **FT-03: Edit an existing application**
  - Action: Select **Edit** on a default application, change its company, role, date, status, or notes, then save.
  - Expected: The list displays the updated values and no longer displays the replaced values.

- [X] TEST-ID: **FT-04: Delete an existing application**
  - Action: Select **Delete** for a default application and confirm the deletion if prompted.
  - Expected: The selected application is removed from the list and its details are no longer displayed.

- [X] TEST-ID: **FT-05: Assign supported application statuses**
  - Action: Set an application’s status to **Applied**, **Interviewed**, and **Offered**, saving after each change.
  - Expected: The selected status is displayed for the application after each save.

- [ ] TEST-ID: **FT-06: Save and display application notes**
  - Action: Edit a default application, enter a brief note, and save it.
  - Expected: The note is displayed only with the associated application and remains visible after revisiting or refreshing the list.
  - Bug Report:
    - Issue: Changes are not persisted after revisiting or refreshing the list.
    - Actual: The edited Stripe application initially displayed the updated company, role, date, and note, but navigating to the application URL again restored the original Stripe details and note.

## Constraint

- [ ] TEST-ID: **CS-01: Require essential application details**
  - Action: Open **Add Application**, leave **Company**, **Role**, or **Date** empty one at a time, and select **Save**.
  - Expected: The application is not saved while any required basic detail is empty, and the incomplete field is identified.
  - Bug Report:
    - Issue: Missing required fields are not visibly identified.
    - Actual: The Save button becomes disabled when Company, Role, or Date is empty, but no validation message, error text, or visible invalid-field indication identifies the incomplete field.

- [ ] TEST-ID: **CS-02: Accept only valid dates**
  - Action: Enter an invalid or incorrectly formatted value in the **Date** field and select **Save**.
  - Expected: The application is not saved, and the date field displays a validation message or equivalent error state.
  - Bug Report:
    - Issue: Invalid date input has no visible validation feedback.
    - Actual: Entering `not-a-date` into the date control was rejected by the browser and left the field blank; the application was not saved, but no validation message or visible error state was displayed.

- [ ] TEST-ID: **CS-03: Restrict status values to supported options**
  - Action: Open the **Status** control for an application.
  - Expected: The available status choices are limited to **Applied**, **Interviewed**, and **Offered**.
  - Bug Report:
    - Issue: Unsupported status option is available.
    - Actual: The Status control includes `Rejected` in addition to Applied, Interviewed, and Offered.

- [ ] TEST-ID: **CS-04: Prevent accidental deletion**
  - Action: Select **Delete** for a default application, then cancel or dismiss the confirmation prompt.
  - Expected: The application remains in the list unchanged.
  - Bug Report:
    - Issue: Delete action has no confirmation prompt.
    - Actual: Selecting Delete immediately removed the application without presenting a confirmation dialog or cancellation option.

## Interaction

- [X] TEST-ID: **IX-01: Open and close the application form**
  - Action: Select **Add Application**, then close or cancel the form without saving.
  - Expected: The form opens for data entry and closes without adding or modifying an application.

- [X] TEST-ID: **IX-02: Show saved changes in the list**
  - Action: Save a valid new application or edit an existing one.
  - Expected: The list updates immediately to show the saved company, role, date, status, and notes without requiring duplicate submission.

- [ ] TEST-ID: **IX-03: Provide clear validation feedback**
  - Action: Submit the application form with missing or invalid data.
  - Expected: The invalid fields are visibly indicated and the form remains available for correction.
  - Bug Report:
    - Issue: Invalid fields are not visibly indicated.
    - Actual: The form remained open and prevented saving when required data was missing or the date was invalid, but it did not visibly mark the invalid fields or provide corrective validation feedback.

## Content

- [X] TEST-ID: **CT-01: Keep application details associated correctly**
  - Action: Compare each default application’s company, role, date, status, and notes within the list.
  - Expected: Every displayed value belongs to the same application and no values are shown under the wrong entry.

- [ ] TEST-ID: **CT-02: Display status labels exactly**
  - Action: Review the status shown for each application.
  - Expected: Status text uses only the labels **Applied**, **Interviewed**, or **Offered**, with no misspellings or unrelated values.
  - Bug Report:
    - Issue: An unrelated status label is displayed.
    - Actual: The default Figma application displays the status `Rejected`, which is not one of the supported labels.
