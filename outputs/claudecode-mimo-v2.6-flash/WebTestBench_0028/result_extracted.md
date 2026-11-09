# Test Result

## Functionality
- [X] FT-01: User can create a new account
  - Action: Open the sign-up page, enter a unique username and password, and submit the form.
  - Expected: The account is created and the user is taken to the login page (or logged in directly) with no error shown.
  - Note: App uses email as account identifier; submitted vaultuser01@example.com / Str0ngPass!2026 via "Create Vault". Toast "Account created successfully" shown and user was logged in directly to the vault dashboard with no errors.

- [X] FT-02: User can log in with valid credentials
  - Action: On the login page, enter the registered username and correct password, then click "Log In".
  - Expected: The user is authenticated and the document vault dashboard is displayed.
  - Note: "Unlock Vault" with correct email/password → toast "Welcome back!", vault dashboard displayed (folders + documents).

- [X] FT-03: User can upload a document
  - Action: While logged in, click the upload button, select a local file, and confirm the upload.
  - Expected: The file appears in the document list with its filename and is retrievable after a page refresh.
  - Note: Uploaded financial_summary.txt → listed immediately; after a full page reload the session persisted and the document (renamed "Insurance Policy 2026") was still retrievable inside the Taxes folder.

- [X] FT-04: User can create a folder and organize a document into it
  - Action: Create a folder named "Taxes", then move or upload an existing document into that folder.
  - Expected: The folder "Taxes" exists and the document is listed inside it.
  - Note: Created root folder "Taxes" (Folders (2) → (3)); moved the document via options → Move → Taxes → "Move Here". Root "Taxes" shows "1 document" and lists the document. (Note: the app seeds a second folder also named "Taxes" under Personal; disambiguation in the Move dialog is ambiguous, but the target folder verification passed.)

- [X] FT-05: User can tag a document
  - Action: Open a document's options and add the tag "important" to it.
  - Expected: The tag "important" is attached to the document and visible on its entry.
  - Note: Options → Edit Tags → selected "important" → Save Tags; badge "important" visible on the entry.

- [X] FT-06: User can rename a document
  - Action: Select a stored document, choose rename, enter "Insurance Policy 2026", and save.
  - Expected: The document is now displayed as "Insurance Policy 2026" in the list.
  - Note: Options → Rename → "Insurance Policy 2026" → Rename; list heading now shows exactly "Insurance Policy 2026".

- [X] FT-07: User can delete a document
  - Action: Select a stored document and use the delete action, confirming when prompted.
  - Expected: The document no longer appears in the list or in any folder/tag view.
  - Note: Deleted draft_note.txt via options → Delete → confirmed native prompt "Delete "draft_note.txt"? This cannot be undone." → list shows Documents (1); search for "draft" returns "No results found".

- [X] FT-08: User can search documents by name
  - Action: Type a known document's name (or a distinct part of it) into the search field.
  - Expected: Only documents whose filenames match the query are shown in the results.
  - Note: Query "Insurance" → "Search Results (1)": only "Insurance Policy 2026"; draft_note.txt excluded.

- [X] FT-09: User can search documents by tag
  - Action: Search using the tag "important" that was applied to a document.
  - Expected: The tagged document appears in the search results.
  - Note: Query "important" → "Search Results (1)": "Insurance Policy 2026" with its "important" badge.

## Constraint
- [X] CS-01: Account creation is blocked when required fields are empty
  - Action: Submit the sign-up form with an empty username or empty password.
  - Expected: No account is created and an inline error indicates the required field is missing.
  - Note: Clicking "Create Vault" on the empty form blocked submission (form still on page); all three inputs are `required` and show validation message "Please fill out this field." (native inline validation), focus moved to the empty field, no account created.

- [X] CS-02: Registration is blocked for an already-used username
  - Action: Attempt to sign up with a username that already exists.
  - Expected: The submission is rejected with a message stating the username is taken.
  - Note: Sign-up with existing vaultuser01@example.com → error toast "An account with this email already exists"; remained on sign-up form.

- [X] CS-03: Login is rejected with a wrong password
  - Action: Enter a valid username with an incorrect password and click "Log In".
  - Expected: The user is not authenticated; an error message is shown and the vault remains inaccessible.
  - Note: Correct email + wrong password → error toast "Invalid email or password"; stayed on the login page, vault not shown. Correct password afterwards logged in normally.

- [X] CS-04: Document deletion requires confirmation
  - Action: Click the delete action on a document but cancel at the confirmation prompt.
  - Expected: The document remains in the vault unchanged.
  - Note: Delete on draft_note.txt raised confirm dialog "Delete "draft_note.txt"? This cannot be undone."; cancelled → document still listed (Documents (2)) with name/size/tag unchanged.

- [X] CS-05: Vault content is inaccessible without an authenticated session
  - Action: Log out (or open the vault URL in a fresh browser session with no login).
  - Expected: The user is redirected to the login page and no document names, tags, or file content are visible.
  - Note: "Sign out" (and subsequent fresh page load while logged out) → login/sign-in view only; no document names, tags, or file content present in the DOM.

- [ ] CS-06: Folder creation is blocked with an empty name
  - Action: Attempt to create a folder while the folder name field is empty.
  - Expected: No folder is created and an error asks for a folder name.
  - Bug Report:
    - Issue: Missing Inline Validation Error Message
    - Actual: With an empty folder name, "Create Folder" is simply rendered `disabled` — clicking it (even via script) does nothing, no folder is created, and no error/notice asking for a folder name ever appears anywhere in the DOM (no role=alert, no toast, no inline message). The blocking works only via a silently disabled button, so the user gets no explanation of the missing required field.

## Interaction
- [X] IX-01: A success confirmation appears after uploading a document
  - Action: Complete a valid file upload and observe the interface.
  - Expected: A success message (toast/notice) such as "Upload complete" is displayed and the list refreshes to include the new file.
  - Note: After confirming upload, toast "1 document uploaded and encrypted" appeared and the document list updated to include the new file (Documents (1) → showed the uploaded file).

- [X] IX-02: Search results respond live to the query
  - Action: Type into the search field, then clear the query completely.
  - Expected: Results filter as the query changes, and clearing it restores the full document list.
  - Note: Typing "Insurance" immediately rendered "Search Results (1)"; intermediate "draft" rendered "No results found"; clearing the input restored the full "Documents (2)" list.

## Content
- [X] CT-01: Document entries display correct metadata
  - Action: After uploading a file, inspect its entry in the list.
  - Expected: The entry shows the exact original filename and a file-type indicator matching the uploaded file.
  - Note: Entry showed exact filename "financial_summary.txt" with "94 B • Nov 9, 2026". File-type indicator is type-aware: text/document files render a `lucide-file` glyph (+ encryption lock badge), while an uploaded .png rendered an actual image thumbnail (alt="vacation_photo.png") — indicator matches the file type in each case.

- [ ] CT-02: Applied tags and folder names are shown accurately on documents
  - Action: Review a document that has tag "important" inside folder "Taxes".
  - Expected: The document entry displays the tag "important" and indicates it belongs to folder "Taxes" with no typos or missing labels.
  - Bug Report:
    - Issue: Missing Folder Label on Document Entry
    - Actual: The document entry displays the tag "important" correctly, but the entry itself contains no folder indication — its full content is "Insurance Policy 2026 / 94 B • Nov 9, 2026 / important". Folder membership ("Taxes") appears only in the page breadcrumb navigation (Vault › Taxes), and global search results for the tagged document show no folder label at all, so the entry never indicates it belongs to folder "Taxes".
