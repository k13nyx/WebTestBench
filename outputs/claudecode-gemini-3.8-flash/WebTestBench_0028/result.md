# Test Result

## Functionality
- [X] FT-01: User Account Registration
  - Action: Navigate to the registration page, enter a valid email address and password, and click the "Sign Up" button.
  - Expected: Account is successfully created, and the user is redirected to the vault dashboard.
- [X] FT-02: User Account Login
  - Action: Navigate to the login page, enter registered account credentials, and click the "Log In" button.
  - Expected: User is authenticated and granted access to their private document vault.
- [X] FT-03: Upload Document
  - Action: Click the "Upload" button, select a valid local document file from the file picker, and confirm the upload.
  - Expected: The selected document appears in the user's document list.
- [X] FT-04: Create Folder for Organization
  - Action: Click the "New Folder" button, input "Financial Records" in the folder name field, and click "Create".
  - Expected: The "Financial Records" folder is created and displayed in the vault hierarchy.
- [X] FT-05: Move Document into a Folder
  - Action: Select an existing document and choose the "Move to Folder" option, selecting "Financial Records".
  - Expected: The document is moved and displays inside the "Financial Records" folder.
- [X] FT-06: Assign Tags to Document
  - Action: Select a document, open its tag management menu, input the tag "Taxes-2024", and press Enter/Save.
  - Expected: The "Taxes-2024" tag badge is attached and visible on the document item.
- [X] FT-07: Rename Document
  - Action: Click the "Rename" action on an existing document, enter "Passport_Copy_Updated.pdf", and click "Save".
  - Expected: The document list updates immediately to display the new name "Passport_Copy_Updated.pdf".
- [X] FT-08: Delete Document
  - Action: Click the "Delete" button on a document and confirm deletion in the prompt.
  - Expected: The document is permanently removed from the vault list.
- [ ] FT-09: View/Open Encrypted Document
  - Action: Click on an uploaded document row or the "View" button.
  - Expected: The document decrypts successfully and opens in the previewer or downloads in readable format.
  - Bug Report:
    - Issue: Unresponsive Element / Missing Feature
    - Actual: Clicking on an uploaded document row does not trigger any action, and there is no "View" button available on the document card or in its action menu.
- [X] FT-10: Search Documents by Name
  - Action: Type an existing file name into the search bar.
  - Expected: The document list dynamically filters to display only files matching the entered name.
- [X] FT-11: Filter Documents by Tag
  - Action: Click on a specific tag filter (e.g., "Taxes-2024") or search by tag name.
  - Expected: Only documents associated with the selected tag are displayed in the results list.

## Constraint
- [X] CS-01: Prevent Registration with Missing Fields
  - Action: Leave the password field empty on the registration form and click "Sign Up".
  - Expected: Submission is prevented and a validation error message indicates the password field is required.
- [ ] CS-02: Prevent Blank Document or Folder Renaming
  - Action: Trigger the rename option on a document, clear all text so the field is empty, and attempt to save.
  - Expected: System rejects the rename action and displays an error stating the name cannot be empty.
  - Bug Report:
    - Issue: Missing Validation Error Message
    - Actual: Clearing all text in the rename dialog disables the Rename button and silently ignores submission without displaying any validation error message indicating the name cannot be empty.
- [X] CS-03: Restrict Unauthenticated Access to Vault Files
  - Action: Copy a direct URL to a vault document or folder, log out of the account, and attempt to visit the URL in the browser.
  - Expected: Access is blocked and the user is redirected to the login page without exposing document data.

## Interaction
- [X] IX-01: Document Deletion Confirmation Prompt
  - Action: Click the "Delete" icon on an existing document or folder.
  - Expected: A confirmation modal dialog appears warning that the action is irreversible before proceeding.
- [ ] IX-02: Upload Progress and Completion Feedback
  - Action: Drag and drop a document into the vault upload dropzone.
  - Expected: A visual upload indicator appears showing progress, followed by a green success toast message once complete.
  - Bug Report:
    - Issue: Missing Upload Progress and Status Feedback
    - Actual: Dropping a document into the dropzone only stages the file in the modal list without triggering upload or showing an upload progress indicator, and completing upload displays a neutral toast without green success styling.

## Content
- [X] CT-01: Encryption Security Status Indicators
  - Action: View the document list and file details panel.
  - Expected: A security icon or status label (e.g., "Encrypted" badge or lock icon) is prominently displayed alongside stored documents.
- [ ] CT-02: Document Metadata Display
  - Action: Inspect the file row or information panel for an uploaded document.
  - Expected: File name, file size, upload date, and associated folder/tags are accurately displayed without truncated or missing data.
  - Bug Report:
    - Issue: Incomplete Metadata Display
    - Actual: The document card displays file name, file size, upload date, and tags, but completely omits the associated folder name.