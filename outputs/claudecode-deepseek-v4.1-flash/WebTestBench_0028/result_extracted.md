# Test Result

## Functionality
- [X] FT-01: User can create a new account with valid details
  - Action: Open the sign-up page, enter a valid email and password in all required fields, click "Create Account".
  - Expected: Account is created and the user is taken into their private vault.

- [X] FT-02: User can log in with valid credentials
  - Action: On the login page, enter the registered email and correct password, click "Log In".
  - Expected: User is authenticated and lands on their document vault.

- [X] FT-03: User can upload a personal document
  - Action: Click "Upload", select a valid document from the desktop, confirm the upload.
  - Expected: The document appears in the vault listing with its file name.

- [X] FT-04: User can create a folder to organize documents
  - Action: Click "New Folder", enter a folder name, confirm.
  - Expected: The new folder appears in the folders list and is selectable.

- [X] FT-05: User can move a document into a folder
  - Action: Select an existing document, choose "Move to", pick a folder, confirm.
  - Expected: The document is listed inside the chosen folder and no longer in its previous location.

- [X] FT-06: User can organize a document into a tagged collection
  - Action: Open a document's context menu, choose "Add Tag", enter a tag name, confirm.
  - Expected: The tag is applied and displayed on the document; a tagged collection for it is available.

- [ ] FT-07: User can open and view a stored document
  - Action: Click on a stored document in the vault.
  - Expected: The document opens and its content is viewable by the owner.
  - Bug Report:
    - Issue: Unresponsive element / Missing feature (no in-app document viewer)
    - Actual: Clicking a stored document does nothing — the title ("vault-report-2026.txt"), the file icon, and the card container are all non-interactive (no `cursor:pointer`, no `role="button"`, no open/preview handler). The document's context menu offers only "Download", "Rename", "Edit Tags", "Move", "Delete" — there is no "View"/"Preview"/"Open" action anywhere in the DOM (body text contains none of those words). The file can only be retrieved via the Download action (which saved it externally); its content is never rendered/viewable inside the app.

- [X] FT-08: User can rename a document
  - Action: Select a document, choose "Rename", enter a new name, confirm.
  - Expected: The document is displayed under the new name everywhere it is listed.

- [X] FT-09: User can delete a document
  - Action: Select a document, choose "Delete", confirm the deletion.
  - Expected: The document is removed from the vault listing and no longer retrievable.

- [X] FT-10: User can search documents by name
  - Action: Type a known stored document's name into the search field and submit.
  - Expected: Only documents matching the name are shown in the results.

- [X] FT-11: User can search documents by tag
  - Action: Type a known existing tag into the search field and submit.
  - Expected: All documents carrying that tag are shown in the results.

## Constraint
- [X] CS-01: Account creation is blocked for an already-registered email
  - Action: On the sign-up page, submit with an email that already has an account.
  - Expected: Submission is rejected with a message that the email is already in use; no duplicate account is created.

- [X] CS-02: Login is blocked with incorrect credentials
  - Action: On the login page, enter a valid email with a wrong password and click "Log In".
  - Expected: Access is denied with an error message; the vault is not entered.

- [X] CS-03: Registration/login cannot be submitted with empty required fields
  - Action: Leave required fields blank and attempt to submit the form.
  - Expected: Submission is blocked with validation messages indicating the required fields.

- [ ] CS-04: Stored content is inaccessible without the owner's authentication
  - Action: Log out, then attempt to access a previously uploaded document's content directly.
  - Expected: The content is not viewable or readable; access requires re-authenticating as the owner.
  - Bug Report:
    - Issue: Insecure storage — content is stored unencrypted (readable without authentication)
    - Actual: After logging out, the uploaded document's content remains fully readable in `localStorage` without any authentication. Key `vault_data_<aliceUserId>` holds `"content":"data:text/plain;base64,U0VDVVJFVkFVTFQtUUEtTUFSS0VSLTQy..."`, which base64-decodes directly to the plaintext `"SECUREVAULT-QA-MARKER-42\nLine two of test document.\n"`. The app's own `/src/lib/crypto.ts` explicitly documents "Simulated encryption … we just base64 encode with a simple XOR", and its `encryptContent` is never called by `VaultContext` (content is stored as a raw FileReader data URL). The password hash is also unsalted SHA-256. Content is therefore trivially decodable by anyone with the browser profile — the owner's password is not required — contradicting the "strongly encrypted so only I can view" requirement.

- [X] CS-05: One user cannot view or manage another user's documents
  - Action: Log in as a second account and attempt to open, rename, or delete the first account's documents.
  - Expected: The other user's documents are not visible or manageable; the attempt is denied.

## Interaction
- [X] IX-01: Confirmation feedback is shown after a successful upload
  - Action: Upload a valid document and wait for completion.
  - Expected: A success notification/toast confirms the upload, and a progress/loading indicator disappears.

- [X] IX-02: Delete presents a confirmation dialog before removing
  - Action: Select a document and choose "Delete".
  - Expected: A confirmation dialog appears with confirm and cancel options; canceling leaves the document intact.

- [X] IX-03: Search shows an appropriate empty state when there are no matches
  - Action: Enter a search term that matches no document name or tag.
  - Expected: A clear "no results" message is displayed instead of an empty or unchanged list.

## Content
- [X] CT-01: Vault listings display relevant, accurate document metadata
  - Action: View the document list for a stored file.
  - Expected: The displayed name, tag/folder label, and file details correctly correspond to that document, with no unrelated or placeholder content.
