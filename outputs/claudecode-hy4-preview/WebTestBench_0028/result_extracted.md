# Test Result

## Functionality

- [X] FT-01: User can create a new account and land in their vault
  - Action: Open the sign-up page, enter a unique email, a password of at least 8 characters, confirm the password, and submit.
  - Expected: Account is created, user is logged in automatically, and the vault dashboard (document list view) is displayed.

- [X] FT-02: User can log out and log back in with unchanged access to their documents
  - Action: From the logged-in vault, click "Log out", then log in again with the same email and password.
  - Expected: Login succeeds and the vault shows the same documents and folders as before logging out.

- [X] FT-03: User can upload a document into the vault
  - Action: Click the "Upload" button, select a file (e.g., a PDF or TXT) from disk, and confirm the upload.
  - Expected: The document appears in the vault document list with its original file name and is available to open/download.

- [X] FT-04: User can create a folder and move a document into it
  - Action: Click "New folder", name it (e.g., "Taxes"), confirm, then move an existing document into that folder.
  - Expected: The folder appears in the vault navigation and the moved document is listed inside it, not in the unorganized root list.

- [X] FT-05: User can add a tag to a document
  - Action: Open an existing document's options/details panel, add the tag "important", and save.
  - Expected: The tag "important" is displayed on the document and is usable for searching.

- [X] FT-06: User can rename a document
  - Action: Select the "Rename" action on an existing document, enter a new name (e.g., "Passport_2026"), and confirm.
  - Expected: The document is listed under the new name everywhere in the vault and its content remains openable.

- [X] FT-07: User can delete a document
  - Action: Select the "Delete" action on an existing document and confirm the deletion.
  - Expected: The document is removed from the vault list and is no longer findable by search.

- [X] FT-08: User can search documents by name
  - Action: Type an exact substring of an existing document's name into the search field and submit.
  - Expected: Only documents whose names contain that substring are shown; unrelated documents are hidden.

- [X] FT-09: User can search documents by tag
  - Action: Click the "important" tag (or type it in the search field) on a document that carries it.
  - Expected: Only documents carrying the "important" tag are shown; documents without the tag are hidden.

## Constraint

- [X] CS-01: Login is rejected with an incorrect password
  - Action: Log out, then attempt to log in with a registered email and a wrong password.
  - Expected: Login fails, an error message such as "Invalid email or password" is shown, and the vault is not accessible.

- [X] CS-02: Sign-up is rejected for an already-registered email
  - Action: Attempt to create a new account using an email that already exists.
  - Expected: Sign-up is blocked and an error message indicating the email is already in use is displayed.

- [X] CS-03: Vault content is inaccessible while logged out
  - Action: Log out, then navigate directly to the vault/documents page URL.
  - Expected: The vault does not render; the user is redirected to the login page.

- [X] CS-04: One user's documents are not visible or manageable by another user
  - Action: Log in as a second, different account, then browse the vault and search for a document name that belongs to the first account.
  - Expected: The second account's vault shows none of the first account's documents, folders, or tags; the search returns no results.

- [X] CS-05: Deleting a document requires confirmation and cancelling preserves the document
  - Action: Select "Delete" on an existing document, then choose "Cancel" in the confirmation prompt.
  - Expected: The confirmation closes, the document remains in the vault list, and it is still openable.

## Interaction

- [X] IX-01: A success notification appears after a document is uploaded
  - Action: Upload a document and observe the interface after the upload completes.
  - Expected: A success message/toast confirming the upload appears and then dismisses; no error state is shown.

- [X] IX-02: A clear message is shown when a search returns no matches
  - Action: Enter a random non-matching string (e.g., "zzzqqq123") into the search field and submit.
  - Expected: An empty-state message such as "No documents found" is displayed instead of a blank or broken list.

- [ ] IX-03: An empty vault shows guidance instead of a blank screen
  - Action: Log in to an account that has no documents and view the vault.
  - Expected: An empty-state message prompting the user to upload their first document is displayed, with a working "Upload" action.
  - Bug Report:
    - Issue: Missing empty-state guidance on the vault dashboard
    - Actual: After creating a brand-new second account (testuser2@example.com) with zero documents, the vault dashboard `main` region renders only the folders section — its entire text content is just `Folders (2) / Personal / 0 documents, 1 folder / Work / 0 documents`. No `Documents (0)` section, no empty-state heading, and no prompt to upload a first document is rendered anywhere on the page. The empty state (`Your vault is empty` — `Start by uploading documents or creating folders to organize your secure files.` with working `Upload Documents` / `Create Folder` buttons) only appears when navigating *into* an empty folder, not on the root vault view that a new user lands on.

## Content

- [X] CT-01: All branding and headings reflect the secure document-vault purpose
  - Action: Review the login, sign-up, and vault page titles/headings and any onboarding text.
  - Expected: Text consistently identifies the product as a secure/encrypted personal document vault; no unrelated or demo branding (e.g., "My Blog", "Store") is present.

- [X] CT-02: Icons and imagery match document-vault actions
  - Action: Inspect the icons next to the Upload, New folder, Tag, Rename, and Delete actions.
  - Expected: Each action uses a relevant icon (upload, folder, tag/label, pencil/edit, trash); no mismatched or placeholder icon is used for any action.

- [X] CT-03: Encryption/privacy status is communicated to the user
  - Action: View the vault dashboard and any document details view.
  - Expected: A lock icon or explicit text (e.g., "Encrypted" / "Only you can access this") is present; no claim contradicts the encrypted-only-you promise.
