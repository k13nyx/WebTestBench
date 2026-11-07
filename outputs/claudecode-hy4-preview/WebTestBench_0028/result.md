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

---

## Evidence Log

| ID | Observed evidence |
|----|-------------------|
| FT-01 | Toast `Account created successfully`; vault header shows `testuser1@example.com`, `Folders (2)` section rendered. |
| FT-02 | Toast `Welcome back!`; vault shows `Folders (3)` (Personal, Work, Taxes) and `Documents (1)` = `Tax_Return_2024.txt` with tag `important` — identical to pre-logout state. |
| FT-03 | Upload dialog accepted 3 files; toast `3 documents uploaded and encrypted`; `Documents (3)` listed `Passport_2025.txt`, `Tax_Return_2024.txt`, `Random_Notes.txt` with original names/sizes; per-document menu exposes `Download`. |
| FT-04 | Toast `Folder "Taxes" created`; after Move → `Taxes`, root list dropped to `Documents (2)` (Passport_2025.txt no longer at root) and the `Taxes` card reports `1 document`; folder appears in the sidebar navigation once opened. |
| FT-05 | `Edit Tags` → selected `important` → `Save Tags`; tag chip `important` renders on the `Tax_Return_2024.txt` card. |
| FT-06 | Toast `Document renamed`; card heading changed to `Passport_2026.txt`, metadata preserved (`26 B`). |
| FT-07 | Native confirm `Delete "Passport_2026.txt"? This cannot be undone.` accepted; list went to `Documents (1)`; search for `Passport_2026` then returned `No results found`. |
| FT-08 | Search `Tax_Return` → `Search Results (1)`, only `Tax_Return_2024.txt`. |
| FT-09 | Search `important` → `Search Results (1)`, only the tagged `Tax_Return_2024.txt`. |
| CS-01 | Toast `Invalid email or password`; remained on login screen, no vault content rendered. |
| CS-02 | Toast `An account with this email already exists`; no session created. |
| CS-03 | Logged out; `/vault` is not a route (404 page), and the vault route `/` renders the login form — no vault content. |
| CS-04 | Account `testuser2@example.com`: 0 documents, no tags; searches for `Tax_Return_2024` and `important` both returned `No results found`. |
| CS-05 | Confirmation dismissed; `Tax_Return_2024.txt` still present with `important` tag and `Download` action available. |
| IX-01 | Toast `3 documents uploaded and encrypted` shown, then auto-hidden (verified via `waitFor hidden`). |
| IX-02 | Empty state: `No results found` / `No documents match "zzzqqq123". Try a different search term or check your spelling.` |
| IX-03 | See bug report — no empty-state text in `main` on the root vault view. |
| CT-01 | Title `SecureVault - Encrypted Document Storage`; headings `SecureVault` / `Your documents, encrypted and protected`; CTAs `Unlock Vault`, `Create Vault`; footer `🔒 All data is encrypted and stored locally in your browser`. No demo branding. |
| CT-02 | `lucide-upload` (Upload), `lucide-folder-plus` (New Folder), `lucide-tag` (Edit Tags), `lucide-pencil` (Rename), `lucide-trash2` (Delete), plus `lucide-download` and `lucide-log-out`. |
| CT-03 | Each document card renders a `lucide-lock w-3 h-3` badge; upload dialog states `All files will be encrypted before storage`; login screen states `🔒 All data is encrypted and stored locally in your browser`. No contradictory claims. (Caveat: the dashboard communicates encryption via icon only — no accompanying "Encrypted" / "Only you can access this" text on the document list or card.) |

## Additional Observations (outside the checklist)

- **Ambiguous "Move Document" destination list.** The dialog flattens folders with no parent context, so two folders named "Taxes" (the seeded `Personal › Taxes` and a user-created root `Taxes`) appear as identical entries. My first move landed the document in the seeded nested folder; neither folder card reflected the move, so the misplacement was hard to notice. Showing a parent path (e.g. `Personal / Taxes`) would remove the ambiguity. FT-04 itself passed once the correct destination was selected.
- **New vaults are pre-seeded with folders.** A freshly created account already contains `Personal` (with a nested `Taxes` subfolder) and `Work`. Worth confirming that's intentional — it is what creates the duplicate-name situation above.
- **Harness note.** Uploads were driven by constructing `File` objects in the page context via `DataTransfer`, because writing fixture files to disk was blocked by workspace permissions. The app's own upload handler processed them normally, so FT-03 and IX-01 reflect real behaviour.

**Result: 20 of 21 passed; 1 defect (IX-03).**