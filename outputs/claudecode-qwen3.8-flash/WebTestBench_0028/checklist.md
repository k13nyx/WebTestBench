# Test Checklist

## Functionality
- [ ] FT-01: User can create a new account
  - Action: Open the app, click "Sign Up" / "Create Account", enter a unique email/username and a password, submit.
  - Expected: Account is created and the user lands inside their own empty/new vault (document list visible).

- [ ] FT-02: User can log in with valid credentials
  - Action: From the "Log In" screen, enter the default/existing account's email and password and submit.
  - Expected: User is taken to the vault view showing their documents and folders.

- [ ] FT-03: User can upload a document
  - Action: Click "Upload" (or the upload/drag-drop zone), select a test file (e.g., `report.pdf`) from the default files provided.
  - Expected: The uploaded document appears in the document list with its correct file name.

- [ ] FT-04: Logged-in user can view a stored document's content
  - Action: Click/open a pre-existing (default) document in the vault.
  - Expected: The document's content/preview renders correctly and is readable (not corrupted or blank).

- [ ] FT-05: User can create a folder and move a document into it
  - Action: Click "New Folder", name it "Taxes"; then use "Move to" (or drag-drop) to move a default document into it.
  - Expected: Folder "Taxes" appears in the folder list; the moved document shows inside "Taxes" and no longer in the root/all-documents view.

- [ ] FT-06: User can tag a document and browse the tagged collection
  - Action: Add a tag (e.g., "contracts") to a default document via its tag control, then click that tag in the tag list/sidebar.
  - Expected: Only documents carrying the tag "contracts" are displayed in the tagged collection view.

- [ ] FT-07: User can rename a document
  - Action: Open a document's "Rename" control, change the name from its default to `New Name`, confirm.
  - Expected: The document appears as `New Name` in the list; opening it still shows the original (unchanged) content.

- [ ] FT-08: User can delete a document
  - Action: Click "Delete" on a default document and confirm the deletion.
  - Expected: The document is removed from the list and no longer appears in folders, tags, or search results.

- [ ] FT-09: Search by document name returns matching documents
  - Action: Type an exact/partial name of a default document (e.g., "report") into the search field and submit.
  - Expected: Results list shows that document and excludes documents whose names do not contain the term.

- [ ] FT-10: Search by tag returns matching documents
  - Action: Search for an existing default tag name (e.g., "contracts") in the search field.
  - Expected: All documents carrying that tag are returned in the results.

## Constraint
- [ ] CS-01: Vault is inaccessible without logging in
  - Action: Log out (or open a new browser session), then directly navigate to the vault/documents URL.
  - Expected: The user is redirected to the login screen; no documents, folders, or tags are displayed.

- [ ] CS-02: Incorrect credentials are rejected
  - Action: On the "Log In" form, enter a valid username with a wrong password and submit.
  - Expected: An error message (e.g., "Invalid credentials") is shown and the vault is not displayed.

- [ ] CS-03: Sign-up with missing required fields is blocked
  - Action: On the "Sign Up" form, leave the password (and/or email) blank and submit.
  - Expected: Submission is rejected with a validation message identifying the required field; no account is created.

- [ ] CS-04: Duplicate account registration is rejected
  - Action: Attempt "Sign Up" again using the email/username of an existing account.
  - Expected: An error (e.g., "Account already exists") is shown and the user is not signed into a new account.

- [ ] CS-05: One user cannot view or manage another user's files
  - Action: Sign up as a second account, log in, and inspect the document list, folders, tags, and search results for any of the first account's documents.
  - Expected: None of the first account's documents, folder names, or tags are visible or accessible by direct link to the second account.

## Interaction
- [ ] IX-01: Password entry is masked
  - Action: Type into the password field on the "Sign Up" and "Log In" forms.
  - Expected: Characters display as masked dots/asterisks (with an optional reveal toggle), never as plain text.

- [ ] IX-02: Success feedback after upload
  - Action: Upload a document (per FT-03).
  - Expected: A visible confirmation (toast/banner, e.g., "Upload successful") appears and then dismisses without a page reload wiping the state.

- [ ] IX-03: Delete requires confirmation; cancel is safe
  - Action: Click "Delete" on a document, then choose "Cancel" in the confirmation dialog.
  - Expected: A confirmation dialog naming the document appears; canceling leaves the document in the vault.

- [ ] IX-04: Search results and empty state respond to input
  - Action: Type a search term that matches no default document or tag (e.g., "zzzq9").
  - Expected: The results area updates and shows a clear "no matches" message (not a blank screen or stale results).

## Content
- [ ] CT-01: Default vault content is present and legible
  - Action: Log in to the default account and inspect the initial document list, folders, and tags.
  - Expected: Pre-seeded documents, folder names, and tag names are displayed with meaningful, non-placeholder text (no "lorem ipsum", no broken/untitled entries).

- [ ] CT-02: Security/encryption messaging aligns with the vault theme
  - Action: Review the vault UI (document rows, account/settings area, login screen) for security indicators such as lock icons or "encrypted" labels.
  - Expected: Encryption/security content is shown where promised (e.g., lock or "Encrypted" badge on documents) and all copy is relevant to a secure document vault; no unrelated or contradictory content.