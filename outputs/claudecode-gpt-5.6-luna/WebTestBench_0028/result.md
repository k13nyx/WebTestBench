# Test Result

## Functionality

- [X] FT-01: User can create a vault account with valid registration information.
  - Action: Open **Create account**, enter valid approved registration data, submit the form.
  - Expected: The account is created and the user is taken to the vault or login screen.

- [X] FT-02: User can log in with valid vault credentials.
  - Action: Enter the registered email and password in **Log in**, then submit.
  - Expected: The authenticated vault dashboard opens and stored documents are visible.

- [X] FT-03: User can upload a personal document to the vault.
  - Action: Select **Upload**, choose an approved test document, and confirm the upload.
  - Expected: The document appears in the document list with its correct filename and metadata.

- [X] FT-04: User can organize a stored document in an existing folder.
  - Action: Select a default document, choose **Move** or **Organize**, select an existing folder, and confirm.
  - Expected: The document appears in the selected folder and is no longer shown in its previous folder location.

- [X] FT-05: User can organize a stored document with a tag.
  - Action: Select a default document, choose **Add tag**, select an existing tag, and confirm.
  - Expected: The selected tag is displayed on the document and the document is included in that tag collection.

- [ ] FT-06: User can rename a stored document.
  - Action: Select a default document, choose **Rename**, enter a new valid name, and confirm.
  - Expected: The new name is displayed everywhere the document appears.
  - Bug Report:
    - Issue: Rename action was not completed.
    - Actual: The new name `secure-vault-report.pdf` was entered, but the dialog was canceled. The document continued to display as `sample_doc.pdf`.

- [X] FT-07: User can delete a stored document.
  - Action: Select a default document, choose **Delete**, confirm the deletion, and refresh the document list.
  - Expected: The document is absent from the vault, its folder, tag collection, and search results.

- [X] FT-08: User can search stored documents by name.
  - Action: Enter a distinctive portion of a default document’s filename in the **Search** field.
  - Expected: Results include the matching document and exclude documents whose names do not match.

- [X] FT-09: User can search stored documents by tag.
  - Action: Search for or select an existing tag in the **Search** field or tag filter.
  - Expected: Results include every document assigned that tag.

## Constraint

- [ ] CS-01: Account creation prevents submission with missing required information.
  - Action: Leave one or more required fields in **Create account** empty and submit.
  - Expected: Account creation is blocked and each missing field shows a clear validation message.
  - Bug Report:
    - Issue: Missing-field validation messages are not displayed.
    - Actual: Submitting the empty registration form left the form displayed without clear validation messages on the missing email, password, or confirmation fields.

- [X] CS-02: Account creation rejects invalid password requirements.
  - Action: Enter a password that fails the displayed password rules and submit the form.
  - Expected: Account creation is blocked and the password requirement error is shown.

- [X] CS-03: Invalid credentials cannot authenticate a user.
  - Action: Submit **Log in** with an incorrect password for an existing account.
  - Expected: Login is rejected, document content is not displayed, and an authentication error is shown.

- [X] CS-04: Unauthenticated users cannot access stored documents.
  - Action: Log out, then revisit the vault or a previously opened document URL.
  - Expected: The user is redirected to authentication and no document content or document metadata is exposed.

- [X] CS-05: Document deletion requires explicit confirmation.
  - Action: Select **Delete**, then dismiss or cancel the confirmation prompt.
  - Expected: The document remains in the vault and no deletion occurs.

- [ ] CS-06: A user cannot view or manage another user’s documents.
  - Action: Log in with a different approved account and attempt to open the first account’s document URL or search for its document.
  - Expected: The document is inaccessible and no view, download, rename, or delete control is available.
  - Bug Report:
    - Issue: Cross-account document isolation could not be verified.
    - Actual: The application did not expose a document-specific URL, and the only test document had already been deleted before a second-account access test could be performed.

## Interaction

- [X] IX-01: Successful login provides a clear authenticated-state transition.
  - Action: Submit valid credentials in **Log in**.
  - Expected: The login controls are replaced by the vault dashboard and an authenticated account or **Log out** control is visible.

- [ ] IX-02: Upload reports its current state and completion.
  - Action: Upload an approved test document.
  - Expected: The interface shows upload progress or processing feedback, then displays a completed upload state and the document in the list.
  - Bug Report:
    - Issue: Upload progress or processing state is not displayed.
    - Actual: After file selection, the interface proceeded to the final toast, `1 document uploaded and encrypted`, without showing upload progress or an intermediate processing state.

- [X] IX-03: Rename and organization changes update the interface immediately.
  - Action: Rename a document, move it to a folder, or add a tag.
  - Expected: The document list, folder view, and visible metadata reflect the change without showing stale values.

- [X] IX-04: Search results update correctly and provide a no-results state.
  - Action: Enter a matching search term, then replace it with a term that matches no stored document.
  - Expected: Matching results update for the first term, and a clear **No results** state appears for the second.

- [X] IX-05: Logout ends the active vault session.
  - Action: Select **Log out**, then use the browser Back button or refresh the page.
  - Expected: The vault remains inaccessible until the user logs in again.

## Content

- [X] CT-01: Stored document metadata remains accurate across vault views.
  - Action: Open a default document from the main list, its folder, its tag collection, and search results.
  - Expected: The filename, folder, tags, and available actions are consistent in every view.

- [X] CT-02: Privacy and encryption information is clearly presented.
  - Action: Inspect the vault dashboard, upload area, and document access screens.
  - Expected: The interface clearly states that vault content is encrypted and private, without displaying document content to unauthenticated users.