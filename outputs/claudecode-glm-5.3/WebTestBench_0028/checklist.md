# Test Checklist

## Functionality
- [ ] FT-01: User can create a new account
  - Action: On the sign-up page, fill in a valid email and password, then click the "Sign Up" (or equivalent) button.
  - Expected: Account is created and the user is logged in and taken to the vault/dashboard, or shown a success message.

- [ ] FT-02: User can log in with valid credentials
  - Action: On the login page, enter the registered email and password, then click "Log In".
  - Expected: User is authenticated and redirected to their document vault.

- [ ] FT-03: User can log out
  - Action: While logged in, click the "Log Out" button.
  - Expected: User session ends and user is returned to the login page.

- [ ] FT-04: User can upload a document
  - Action: Click the "Upload" button, select a file (e.g., a PDF), and confirm the upload.
  - Expected: The uploaded document appears in the vault's document list with its original file name.

- [ ] FT-05: User can create a folder and move a document into it
  - Action: Create a new folder (e.g., "Finance"), then move a default document into it using the move option.
  - Expected: The document is listed inside the "Finance" folder and no longer appears at the vault root.

- [ ] FT-06: User can add a tag to a document
  - Action: Open a default document's options and add a tag (e.g., "insurance"), then save.
  - Expected: The tag is displayed on the document and the document is findable under that tag.

- [ ] FT-07: User can rename a document
  - Action: Select a default document, choose "Rename", enter a new name, and confirm.
  - Expected: The document list shows the new name; the old name no longer appears.

- [ ] FT-08: User can delete a document
  - Action: Select a default document and choose "Delete", then confirm.
  - Expected: The document is removed from the vault and no longer appears in any folder, tag list, or search result.

- [ ] FT-09: User can search documents by name
  - Action: Type the (partial) name of a default document into the search bar.
  - Expected: Search results show only documents whose names match the query.

- [ ] FT-10: User can search documents by tag
  - Action: Type an existing tag name (e.g., "insurance") into the search bar, or click the tag.
  - Expected: Search results show only documents carrying that tag.

## Constraint
- [ ] CS-01: Registration rejects an already-registered email
  - Action: Attempt to sign up using an email that already has an account.
  - Expected: Registration is blocked with an error message (e.g., "Email already in use"); no duplicate account is created.

- [ ] CS-02: Login fails with wrong credentials
  - Action: Attempt to log in with a valid email but an incorrect password.
  - Expected: Login is rejected with an error message (e.g., "Invalid email or password") and the vault is not accessible.

- [ ] CS-03: Vault is inaccessible without authentication
  - Action: While logged out, open the vault/documents URL directly in the browser.
  - Expected: User is not shown any documents and is redirected to the login page.

- [ ] CS-04: User cannot see another user's documents
  - Action: Log in as user A and note the visible documents; log out, create/log in as user B, and check the vault.
  - Expected: User B sees only their own (default) documents — none of user A's documents, folders, or tags are visible.

- [ ] CS-05: Upload cannot be completed without selecting a file
  - Action: Open the upload dialog and click "Upload"/"Confirm" without choosing any file.
  - Expected: Upload is blocked (button disabled or validation error shown); no empty document entry is created.

## Interaction
- [ ] IX-01: Success feedback after document upload
  - Action: Upload a valid document.
  - Expected: A success toast/notification (e.g., "Document uploaded") appears and the new document shows in the list without a full page reload error.

- [ ] IX-02: Confirmation dialog before deleting a document
  - Action: Click "Delete" on a default document.
  - Expected: A confirmation dialog appears (e.g., "Are you sure you want to delete this document?"); the document is only deleted after confirming, and remains if canceled.

- [ ] IX-03: Search results update dynamically
  - Action: Type characters into the search bar and observe the results list.
  - Expected: The results list updates to reflect the current query without requiring a page reload.

## Content
- [ ] CT-01: Document list displays accurate metadata
  - Action: Browse the vault and open a default document's details.
  - Expected: Each document shows a correct name, its assigned tags, and its folder location; no placeholder or broken entries are displayed.

- [ ] CT-02: Document content is only viewable through the authenticated app
  - Action: While logged in, open a default document and verify its content displays correctly; then log out and attempt to reopen the same document's URL/content.
  - Expected: Content renders fully when authenticated in the app, and cannot be viewed or downloaded after logout (indicating protected/encrypted access).