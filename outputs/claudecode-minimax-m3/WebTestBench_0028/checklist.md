# Test Checklist

## Functionality
- [ ] FT-01: User can create a new account
  - Action: Navigate to registration page, enter a valid email and password, click "Sign Up" / "Register"
  - Expected: Account is created and the user is logged in or redirected to the login page

- [ ] FT-02: User can log in with valid credentials
  - Action: Enter the registered email and password on the login form, click "Log In"
  - Expected: User is authenticated and redirected to the vault dashboard

- [ ] FT-03: User can log out
  - Action: While logged in, click the "Log Out" button
  - Expected: User session ends and the user is returned to the login page

- [ ] FT-04: User can upload a document to the vault
  - Action: Click "Upload", select a file (e.g., PDF or image), confirm upload
  - Expected: The uploaded document appears in the vault's document list

- [ ] FT-05: User can create a new folder
  - Action: Click "New Folder" / "Create Folder", enter a folder name, confirm
  - Expected: New folder appears in the folder list with the entered name

- [ ] FT-06: User can organize documents into a folder
  - Action: Select an existing document, use "Move to" or drag it into an existing folder
  - Expected: Document is listed inside the selected folder and no longer appears in the root list

- [ ] FT-07: User can add tags to documents (tagged collections)
  - Action: Select a document, click "Add Tag", enter a tag name, save
  - Expected: Tag is associated with the document and visible on its detail/list view

- [ ] FT-08: User can rename a document
  - Action: Right-click a document (or click "Rename"), enter a new name, save
  - Expected: Document displays the new name throughout the vault list and search

- [ ] FT-09: User can delete a document
  - Action: Select a document, click "Delete", confirm the deletion in the confirmation dialog
  - Expected: Document is removed from the vault and no longer appears in lists, folders, or search

- [ ] FT-10: User can search documents by name
  - Action: Type a known full or partial document name into the search bar
  - Expected: Only documents whose names match the query are displayed in the results

- [ ] FT-11: User can search documents by tag
  - Action: Type a known tag name (or select an existing tag) in the search/filter
  - Expected: Only documents associated with the matching tag are displayed in the results

## Constraint
- [ ] CS-01: Login fails with invalid credentials
  - Action: Enter a registered email with an incorrect password, click "Log In"
  - Expected: Login is rejected and an error message such as "Invalid email or password" is shown

- [ ] CS-02: Registration is blocked when required fields are missing
  - Action: Leave the email or password field empty on the registration form, click "Register"
  - Expected: Submission is prevented and a validation error is displayed for the empty field(s)

- [ ] CS-03: Unauthenticated users cannot access vault content
  - Action: While logged out, attempt to navigate directly to a vault page (e.g., documents, folders, search)
  - Expected: Access is denied; user is redirected to the login page

- [ ] CS-04: Users cannot view or manage another user's documents
  - Action: Log in as User B (after User A has uploaded documents), search for or attempt to open User A's documents
  - Expected: User B sees no documents belonging to User A and cannot open or modify them

- [ ] CS-05: Registration enforces password strength
  - Action: Attempt to register with a weak password (e.g., "123" or "password")
  - Expected: Registration is rejected with a message requiring a stronger password

## Interaction
- [ ] IX-01: Successful login provides positive feedback
  - Action: Submit valid login credentials
  - Expected: A success indicator (e.g., redirect to dashboard, welcome message, or toast) is shown

- [ ] IX-02: Successful document upload shows confirmation
  - Action: Complete a document upload
  - Expected: A success message or confirmation (e.g., "Upload complete") appears, and the new document appears in the list

- [ ] IX-03: Search results update dynamically as the user types
  - Action: Type different keywords/tags into the search bar
  - Expected: The result list updates to reflect the current query without requiring a manual refresh

## Content
- [ ] CT-01: Uploaded document content is preserved intact
  - Action: Upload a file with known/unique content, then download or open it from the vault
  - Expected: The downloaded file matches the originally uploaded file in name, type, and content

- [ ] CT-02: Document names and tags are displayed correctly
  - Action: View the document list after uploading, renaming, or tagging documents
  - Expected: Each document displays its correct name and any applied tag(s) without truncation or mismatch