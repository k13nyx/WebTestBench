# Test Result

## Functionality
- [X] FT-01: Create a new account
  - Action: Open the sign-up screen and register with a new email and password, then submit.
  - Expected: Account is created and the user is taken into the vault (or to login) without error.

- [X] FT-02: Log in with valid credentials
  - Action: Enter a registered email and correct password on the login screen, then submit.
  - Expected: The user is authenticated and lands on the vault/document dashboard.

- [X] FT-03: Upload a personal document
  - Action: Use the "Upload" control to select and upload a document file from local storage.
  - Expected: The file is added to the user's vault and listed among stored documents.

- [X] FT-04: Organize a document into a folder
  - Action: Move or assign an existing document to a folder within the vault.
  - Expected: The document is grouped under the chosen folder and reflects that location.

- [X] FT-05: Tag a document into a collection
  - Action: Add one or more tags to an existing document.
  - Expected: The document becomes part of the tagged collection and the tag is associated with it.

- [X] FT-06: Rename a document
  - Action: Open the rename option for a stored document and enter a new name, then save.
  - Expected: The document now displays under the new name in the vault.

- [X] FT-07: Delete a document
  - Action: Select the delete option for a stored document and confirm.
  - Expected: The document is removed from the vault and no longer appears in any list.

- [X] FT-08: Search documents by name
  - Action: Enter a stored document's name (or part of it) into the search field.
  - Expected: Only matching documents by name are returned in the results.

- [X] FT-09: Search documents by tag
  - Action: Enter or select a tag in the search/filter control.
  - Expected: Only documents carrying that tag are returned in the results.

## Constraint
- [X] CS-01: Reject login with incorrect credentials
  - Action: Attempt to log in with a valid email but a wrong password.
  - Expected: Access is denied and an authentication error is shown; vault is not entered.

- [X] CS-02: Block access to the vault when not logged in
  - Action: Try to open the vault/document URL directly without an active session.
  - Expected: The user is redirected to the login screen and cannot view any documents.

- [X] CS-03: Isolate documents between accounts
  - Action: Log in with a second account and view the vault.
  - Expected: Documents belonging to the first account are not visible or accessible.

- [X] CS-04: Validate required account fields
  - Action: Submit the sign-up form with an empty email or empty password.
  - Expected: Registration is blocked and a validation message identifies the missing field.

- [X] CS-05: Prevent duplicate account registration
  - Action: Attempt to register using an email address that already exists.
  - Expected: Registration is rejected with a message that the account already exists.

## Interaction
- [X] IX-01: Confirm before deleting a document
  - Action: Trigger the delete action on a document.
  - Expected: A confirmation prompt appears; the document is only removed after confirmation.

- [X] IX-02: Show success feedback after upload
  - Action: Upload a document successfully.
  - Expected: A success notification (toast/message) confirms the upload completed.

- [X] IX-03: Show error feedback on failed login
  - Action: Submit the login form with invalid credentials.
  - Expected: A clear error message is displayed and the form remains on the login screen.

## Content
- [X] CT-01: Uploaded document retains its original filename
  - Action: Upload a file named, e.g., "tax-2024.pdf" and view the vault.
  - Expected: The document is listed with exactly its original filename, not a random or corrupted name.

- [ ] CT-02: Encryption status is visibly indicated to the user
  - Action: Inspect the vault or document view.
  - Expected: A clear indicator/label states that stored content is encrypted and private to the user.
  - Bug Report:
    - Issue: Missing persistent encryption/privacy indicator in the authenticated vault and document views.
    - Actual: A DOM text search of the logged-in vault/document view returns no "encrypt" content except the browser tab title ("SecureVault - Encrypted Document Storage"). The only encryption references appear on the pre-login landing screen ("🔒 All data is encrypted and stored locally in your browser") and in transient elements (the upload dialog note "All files will be encrypted before storage" and the success toast "1 document uploaded and encrypted"). Once inside the vault, there is no visible label/badge stating stored content is encrypted and private to the user.

- [X] CT-03: Document metadata displays correctly
  - Action: Open a stored document's details.
  - Expected: Its name, assigned folder, and tags are shown accurately and match what was set.
  - Note: The app has no separate details modal; metadata is shown inline in the document list. Verified for `tax-2024-renamed.pdf`: name = "tax-2024-renamed.pdf", folder = "Personal" (correctly nested), tag = "important" — all accurate and matching what was set via Rename/Move/Edit Tags.
