# Test Checklist

## Functionality
- [ ] FT-01: Visitor can create an account with a new email and password
  - Action: On the sign-up page, enter a valid unique email and password (e.g. `qa.newuser@example.com`), then submit the registration form.
  - Expected: Account is created, the user is authenticated, and the vault (dashboard/document list) is displayed.

- [ ] FT-02: Registered user can log in with valid credentials
  - Action: Log out, then enter the registered email and the correct password on the login form and submit.
  - Expected: Login succeeds and the user lands in the vault with their documents visible.

- [ ] FT-03: Default documents are listed in the vault after login
  - Action: Log in with an account that has pre-existing documents and observe the document list.
  - Expected: All pre-existing documents are listed with their names, and no document from another account appears.

- [ ] FT-04: User can upload a document to the vault
  - Action: Click the upload control, choose a file from the local filesystem, confirm the upload, and wait for completion.
  - Expected: The document appears in the document list with its original filename and is stored in the current location.

- [ ] FT-05: User can create a folder
  - Action: Click the "New Folder" / create-folder control, enter a folder name, and confirm.
  - Expected: The new folder appears in the folder list or sidebar with the given name.

- [ ] FT-06: User can organize a document into a folder
  - Action: Open the organize/move options for an existing document, select an existing folder, and save.
  - Expected: The document is listed under the selected folder and is no longer shown in the unfiled/root list.

- [ ] FT-07: User can tag a document with one or more tags
  - Action: Open the tag control for an existing document, add a tag name, and confirm.
  - Expected: The document displays the new tag and the tag appears in the tag/collection list.

- [ ] FT-08: User can rename a document
  - Action: Open the rename option for an existing document, enter a new name, and confirm.
  - Expected: The document displays the new name everywhere it appears (list, folder view, search results), and the old name is no longer shown.

- [ ] FT-09: User can delete a document
  - Action: Open the delete option for an existing document and confirm the deletion.
  - Expected: The document is removed from the document list, from its folder, and from search results for that document.

## Constraint
- [ ] CS-01: Registration rejects an email that is already registered
  - Action: Attempt to create an account using an email that already exists in the application.
  - Expected: Registration is blocked with a visible duplicate/already-registered error, and no second account is created.

- [ ] CS-02: Login rejects invalid credentials and invalidates the session
  - Action: Enter a valid registered email with an incorrect password and submit; then try to access the vault URL directly.
  - Expected: A visible invalid-credentials error is shown, no vault content is revealed, and direct access is redirected to the login page.

- [ ] CS-03: Vault is not accessible while logged out
  - Action: Log out, then attempt to open the vault, document, and folder pages/URLs directly in the browser.
  - Expected: All requests to view documents, folders, or search results are blocked and the user is redirected to the login page.

- [ ] CS-04: One user's documents are never visible to another user
  - Action: Log in as a second account and browse all folders, tags, and search results.
  - Expected: No documents, folders, or tags belonging to the first account are listed or openable.

- [ ] CS-05: Stored document content is not readable as plaintext outside the app
  - Action: Inspect the stored/uploaded file data and the network traffic for a document's contents.
  - Expected: The document bytes are encrypted (no readable filename or file body appears in storage or in network responses), and content is only recoverable after the owner's authenticated decryption.

- [ ] CS-06: Rename and delete cannot target a non-existent document
  - Action: Invoke the rename and delete operations for a document identifier that does not exist (e.g. after the document was already deleted).
  - Expected: The operation fails safely with a clear error, and no unrelated document is renamed or deleted.

## Interaction
- [ ] IX-01: Successful upload gives immediate visual confirmation
  - Action: Complete an upload and observe the screen immediately afterward.
  - Expected: A success toast/notification appears and the new document is shown in the list without a manual page reload.

- [ ] IX-02: Failed login gives immediate visual feedback
  - Action: Submit the login form with a wrong password.
  - Expected: An inline error message appears on the form, the invalid credentials are not accepted, and no vault content is shown.

- [ ] IX-03: Delete asks for confirmation and cancels cleanly
  - Action: Click delete on an existing document, then cancel the confirmation; then repeat and confirm.
  - Expected: Cancelling leaves the document intact and listed; confirming removes it from the list.

- [ ] IX-04: Search results update as the query is typed
  - Action: Type a partial document name and a tag name into the search field.
  - Expected: The result list narrows to matching documents as typing proceeds, and matches are shown for both name and tag queries.

## Content
- [ ] CT-01: Interface labels match the vault feature set
  - Action: Inspect the visible labels and headings across the sign-up, login, vault, folder, and search views.
  - Expected: Labels are accurate and relevant to a personal document vault (e.g. "Upload", "New Folder", "Tags", "Search", "Rename", "Delete") with no placeholder or lorem-ipsum text and no unrelated feature wording.

- [ ] CT-02: Document names and tags are displayed accurately
  - Action: Open the document list, a folder view, and the tag list, and compare each displayed name/tag with the original filename and tag applied.
  - Expected: Filenames and tag labels are shown exactly as stored, with no truncation that changes the visible name, no garbled characters, and no tags attached to the wrong document.