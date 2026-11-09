# Test Result

## Functionality
- [X] FT-01: Add a new book to the personal library with title, author, genre, and notes.
  - Action: Click "Add Book", enter title "Dune", author "Frank Herbert", genre "Science Fiction", notes "Book club pick", and save.
  - Expected: The book is saved and appears in the library listing.

- [ ] FT-02: Edit the details of an existing book in the library.
  - Action: Open a default book from the library, change its author and notes, and save.
  - Expected: The book's entry reflects the updated author and notes; all other fields remain unchanged.
  - Bug Report:
    - Issue: Incorrect Form Submission (Stale Form State) — the Edit Details dialog is prefilled with values from a previously used form instead of the target book's data, and saving overwrites every field of the target book.
    - Actual: Opening "The Great Gatsby" for edit showed the form pre-filled with "Dune" / "QA Edited Author" / "QA edited notes"; after save the entry read "Dune — QA Edited Author — To Read — Science Fiction" and Gatsby's original title, genre, dates, and rating were destroyed instead of remaining unchanged.

- [X] FT-03: Delete a book from the library.
  - Action: Delete a default book from the library.
  - Expected: The book no longer appears in the library or in any status list.

- [ ] FT-04: Track reading progress using a percentage or a page count.
  - Action: Open a book in "Currently Reading", set progress to 50% and save; then update progress to page count 120 and save.
  - Expected: The book displays the saved progress value after each update (50%, then 120 pages).
  - Bug Report:
    - Issue: Missing Feature / Incorrect Display — no percentage-based progress input exists (form offers only "Total Pages" and "Current Page"), and progress is rendered only as "X / Y pages".
    - Actual: "50%" could not be entered anywhere; entering 50 into "Current Page" displayed "Progress 50 / 300 pages" (not "50%"), and entering 120 displayed "Progress 120 / 300 pages" (not "120 pages"). Additionally, saving via the edit dialog corrupted the book via the stale-form bug ("1984" became "CS01 NotesEmpty — QA Author").

- [ ] FT-05: Mark start and finish dates on a book.
  - Action: Open a book and set its start date to 2026-03-01 and its finish date to 2026-03-15.
  - Expected: Both dates are saved and displayed on the book's entry.
  - Bug Report:
    - Issue: Missing Feature — no start/finish date input controls exist anywhere (Add/Edit dialogs contain only Title, Author, Genre, Status, Total Pages, Current Page, Cover URL, Notes).
    - Actual: Dates are auto-assigned only ("Started: <date>" appears when a book starts reading, completion date set automatically to today); 2026-03-01 and 2026-03-15 cannot be entered, so neither date could be set or displayed as specified.

- [X] FT-06: Move a book between "To Read", "Currently Reading", and "Completed".
  - Action: Move a book from "To Read" to "Currently Reading", then move it to "Completed".
  - Expected: After each move the book appears in the target list and is removed from the previous list.

- [X] FT-07: Rate a finished book.
  - Action: On a book in "Completed", select a 4-star rating and save.
  - Expected: The 4-star rating is saved on the book.

- [X] FT-08: Write and save a review for a finished book.
  - Action: On a book in "Completed", enter review text "Great world-building, slow middle." and save.
  - Expected: The review is saved on the book.

- [ ] FT-09: View the reading history of finished books.
  - Action: Open the reading history after completing a rated and reviewed book.
  - Expected: The completed book appears in the reading history, showing its rating and review.
  - Bug Report:
    - Issue: Missing Feature — no reading history section/view exists on the page.
    - Actual: The page contains only the library/status tabs and the recommendations section; there is no reading history element to open, so the completed, rated, and reviewed book cannot appear in it with its rating and review.

- [ ] FT-10: Edit and delete ratings and reviews from the reading history.
  - Action: In reading history, edit a book's rating to 5 stars with new review text and save; then delete that rating and review.
  - Expected: The edited rating and review are displayed after saving; after deletion the rating and review no longer appear, while the book remains in history.
  - Bug Report:
    - Issue: Missing Feature — no reading history exists to edit from, and no delete-rating/review control exists anywhere in the UI.
    - Actual: There is no reading history section, and the Rate & Review / Edit Review dialog offers only star selection, review textarea, and Save — no delete option — so ratings/reviews can never be deleted and the history-based edit/delete flow cannot be executed at all.

- [ ] FT-11: Search the library and apply combined genre, status, and rating filters.
  - Action: Type a keyword matching one default book's title or author; then apply a genre filter, a status filter, and a rating filter together.
  - Expected: Displayed books match the keyword and all applied filters simultaneously; clearing the filters restores the full library.
  - Bug Report:
    - Issue: Incorrect Filter Logic — the rating filter "N+ Stars" matches exactly N stars instead of ≥ N stars.
    - Actual: With keyword + genre + status + "4+ Stars" applied, the 5-star book "To Kill a Mockingbird" was wrongly excluded (results showed "No books found"); "3+ Stars" returned no results despite existing 4-star books. Clearing the filters restored all 10 books (that part worked).

- [X] FT-12: View book recommendations within the library.
  - Action: Open the recommendations section of the page.
  - Expected: A recommendations section displays suggested books drawn from the user's library.

## Constraint
- [X] CS-01: Required book fields must be provided; notes are optional.
  - Action: Submit the add-book form with the title field empty (repeat with author or genre empty); then submit the form with only notes empty.
  - Expected: A missing required field shows a validation error and the book is not saved; a book with empty notes saves successfully.

- [ ] CS-02: Reading progress input is validated.
  - Action: Enter progress percentage 150 and -10, and a negative page count, on a book.
  - Expected: Each invalid value is rejected with an error message and not saved.
  - Bug Report:
    - Issue: Missing Validation / Missing Feature — there is no percentage progress input to enter 150 or -10 into, and the out-of-range progress value 150 was accepted and saved without any error.
    - Actual: Entering 150 into the only progress field ("Current Page") saved without complaint ("Progress 150 / 300 pages" plus "Book Updated" toast). The negative page count -10 was blocked ("Value must be greater than or equal to 0.") and Total Pages -5 was blocked ("Value must be greater than or equal to 1."), both unsaved — but the percentage values 150% and -10% cannot even be entered because no percentage field exists.

- [ ] CS-03: Finish date cannot be earlier than the start date.
  - Action: Set a book's start date to 2026-03-10, then set its finish date to 2026-03-01.
  - Expected: The earlier finish date is rejected with an error and the previously saved dates remain unchanged.
  - Bug Report:
    - Issue: Missing Feature — no start/finish date inputs exist, so the date-order constraint cannot be exercised.
    - Actual: The Add/Edit dialogs contain no date fields (only Title, Author, Genre, Status, Total Pages, Current Page, Cover URL, Notes) and dates are auto-assigned on status changes; 2026-03-10 and 2026-03-01 cannot be set at all, so no rejection or preserved-dates behavior can be observed.

- [X] CS-04: Only completed books can be rated and reviewed.
  - Action: Open a book in "To Read" or "Currently Reading" and attempt to set a rating or review on it.
  - Expected: Rating and review controls are unavailable or the submission is rejected for books not in "Completed".

## Interaction
- [X] IX-01: Saving a book gives immediate confirmation and updates the view.
  - Action: Add a book (or save edits to an existing book) and observe the page without reloading.
  - Expected: A success confirmation (message/toast) appears and the library list reflects the change immediately.

- [ ] IX-02: Editing a rating/review opens prefilled with current values.
  - Action: Click edit on an existing rating and review in the reading history.
  - Expected: The edit form shows the current star rating and review text already filled in.
  - Bug Report:
    - Issue: Missing Feature — no reading history section exists, so there is no edit action for a rating/review in the reading history to click.
    - Actual: The specified interaction cannot be performed at all (for reference, the book-card "Edit Review" dialog does open prefilled with the current 4 stars and review text, but the required history-based edit entry point does not exist).

## Content
- [ ] CT-01: Book entries display all saved details accurately.
  - Action: Compare a book's saved title, author, genre, and notes with its entry in the library.
  - Expected: All details are displayed exactly as saved, with notes shown when present and no fields missing or altered.
  - Bug Report:
    - Issue: Missing Data Display — saved notes are never rendered on book entries.
    - Actual: Notes saved on a book (e.g., "Book club pick" on Dune) never appear on its entry — cards show only title, author, status, genre, progress, and dates. Additionally, the stale-edit-form bug can alter displayed fields on save (e.g., "The Great Gatsby" entry became "Dune / QA Edited Author" after an edit).

- [X] CT-02: Recommendations are relevant to the user's reading patterns.
  - Action: Check each recommended book's genre against the user's most-read genres and the genres of the user's highest-rated books.
  - Expected: Every recommended book falls within a most-read genre or the genre of a highly rated book; no unrelated books are suggested.