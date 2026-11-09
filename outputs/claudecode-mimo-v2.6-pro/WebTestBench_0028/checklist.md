# Test Checklist

## Functionality
- [ ] FT-01: New user can create an account with a valid email and password.
  - Action: Open the Sign Up page, fill "Email" and "Password" with valid values, click "Create Account".
  - Expected: Account is created, user is logged in and lands on the document vault ("My Documents") page.
- [ ] FT-02: Registered user can log in with valid credentials.
  - Action: Open the Log In page, enter valid "Email" and "Password", click "Log In".
  - Expected: User is authenticated and the vault page with document list is displayed.
- [ ] FT-03: User can upload a personal document.
  - Action: Click "Upload Document", select a local PDF file (e.g., `Passport.pdf`), confirm upload.
  - Expected: The file appears in the document list with its file name and an upload date.
- [ ] FT-04: User can create a folder and organize a document into it.
  - Action: Click "New Folder", name it "Personal", save; then drag (or use "Move to") a document into the "Personal" folder.
  - Expected: Folder "Personal" appears in the folder panel, and the moved document is listed only under that folder.
- [ ] FT-05: User can assign a tag to a document to build a tagged collection.
  - Action: Open a document's details, enter tag "identity" in the "Tags" field, save.
  - Expected: Tag "identity" is shown on the document, and the tag appears in the tag/filter list.
- [ ] FT-06: User can rename a document.
  - Action: Click the "Rename" action on an uploaded document, change the name to "ID_Scan.pdf", save.
  - Expected: The document list shows the new name "ID_Scan.pdf" for that document.
- [ ] FT-07: User can delete a document.
  - Action: Click the "Delete" action on a document and confirm the deletion.
  - Expected: The document is removed from the document list and no longer appears in search or folder views.
- [ ] FT-08: User can search documents by name.
  - Action: Type a partial file name of an existing document (e.g., "Pass") in the "Search" field and submit.
  - Expected: Only documents whose name matches the query are listed.
- [ ] FT-09: User can search documents by tag.
  - Action: Search for the tag applied to an existing document (e.g., "identity").
  - Expected: Only documents carrying that tag are listed.
- [ ] FT-10: User can open and view an uploaded document's content.
  - Action: Click an existing document in the list to open it.
  - Expected: The document's content is decrypted and displayed/downloadable to the logged-in owner.
- [ ] FT-11: User can log out of the vault.
  - Action: Click "Log Out" in the account menu.
  - Expected: The session ends and the Log In page is shown.

## Constraint
- [ ] CS-01: Sign-up form rejects duplicate email and empty required fields.
  - Action: Try "Create Account" with an already-registered email; then try with an empty "Email" or "Password".
  - Expected: An error message is shown and no account is created; the user remains on the Sign Up page.
- [ ] CS-02: Log-in rejects invalid credentials.
  - Action: Enter a registered email with a wrong password and click "Log In".
  - Expected: An error message (e.g., "Invalid email or password") is shown and the vault is not accessible.
- [ ] CS-03: Vault and document pages require authentication.
  - Action: While logged out, navigate directly to the vault page URL and to a document view URL.
  - Expected: Both requests redirect to the Log In page; no document data is shown.
- [ ] CS-04: A user cannot view or manage another user's documents.
  - Action: While logged in as user A, navigate directly to the URL of a document owned by another account.
  - Expected: Access is denied (error message or redirect); the document cannot be viewed, renamed, or deleted.
- [ ] CS-05: Upload rejects invalid or empty files.
  - Action: Click "Upload Document" and attempt to upload an unsupported file type (e.g., `.exe`) and an empty (0 KB) file.
  - Expected: Each attempt shows an error message and no new entry appears in the document list.

## Interaction
- [ ] IX-01: Deleting a document requires explicit confirmation.
  - Action: Click the "Delete" action on a document without confirming, then confirm in the dialog.
  - Expected: A confirmation dialog appears first; cancelling keeps the document, confirming removes it.
- [ ] IX-02: The interface confirms successful state changes and updates results.
  - Action: Upload a document, then run a search query.
  - Expected: A success toast (e.g., "Document uploaded") appears after the upload, and the results area refreshes to show only matching documents after the search.

## Content
- [ ] CT-01: Document entries show accurate, vault-relevant metadata.
  - Action: Inspect each entry in the document list of the default vault content.
  - Expected: Each entry displays its file name, applied tag labels (if any), and upload date — all matching the actual stored document.
- [ ] CT-02: All UI text is relevant to the secure document vault purpose.
  - Action: Review labels and messages on the Sign Up, Log In, vault, upload, and search screens.
  - Expected: Labels use vault-appropriate wording (e.g., "Upload Document", "My Documents", "Folders", "Tags", "Search documents"); empty states show helpful text such as "No documents found" with no unrelated or placeholder text.