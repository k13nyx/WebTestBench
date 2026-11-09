# Test Checklist

## Functionality
- [ ] FT-01: Add a new book with full details
  - Action: Click "Add Book", fill in Title, Author, Genre, and Notes, then save.
  - Expected: Book is created and appears in the library under the "To Read" list with the entered details.

- [ ] FT-02: Update reading progress with a page count
  - Action: Open a default book from "Currently Reading", enter a current page number (e.g., page 50 of 200) and save.
  - Expected: Reading progress is stored and displayed (e.g., 25% or "50 / 200 pages").

- [ ] FT-03: Mark start and finish dates on a book
  - Action: Set a start date on a "To Read" book, move it to "Currently Reading", then set a finish date.
  - Expected: Both dates are saved and displayed on the book's details.

- [ ] FT-04: Move a book between the three status lists
  - Action: Move a default book "To Read" → "Currently Reading" → "Completed" using the status controls.
  - Expected: The book appears under the correct list after each move and is removed from the previous list.

- [ ] FT-05: Give a rating when finishing a book
  - Action: Move a book to "Completed" and assign a rating (e.g., 4 out of 5 stars) in the completion flow.
  - Expected: The rating is saved and shown on the completed book.

- [ ] FT-06: Write a review when finishing a book
  - Action: In the completion flow, enter review text (e.g., "Great ending, highly recommend") and save.
  - Expected: The review is saved and visible on the book's entry.

- [ ] FT-07: Completed books appear in reading history
  - Action: Open the reading history section after completing a book with rating and review.
  - Expected: The finished book appears in the history with its finish date, rating, and review.

- [ ] FT-08: Edit an existing rating and review from history
  - Action: In reading history, edit a book's rating (e.g., 4 → 5 stars) and review text, then save.
  - Expected: The updated rating and review text replace the old values in history and on the book.

- [ ] FT-09: Delete a rating and review from history
  - Action: In reading history, delete a book's rating/review and confirm.
  - Expected: The rating and review are removed while the book remains in history.

- [ ] FT-10: View recommendations based on reading habits
  - Action: Open the recommendations section.
  - Expected: Recommendations are shown and drawn from books in the user's library matching most-read genres or highly-rated books.

- [ ] FT-11: Search the collection by text
  - Action: Type a default book's title (or author name) into the search input.
  - Expected: Only books matching the search text are displayed; clearing the search restores the full list.

- [ ] FT-12: Combine genre, status, and rating filters
  - Action: Apply filters together, e.g., Genre = a genre with default books, Status = "Completed", Rating = minimum 4 stars.
  - Expected: Only books matching all three selected filters are displayed.

## Constraint
- [ ] CS-01: Notes field is optional when adding a book
  - Action: Add a book with Title, Author, and Genre filled but Notes left empty.
  - Expected: The book saves successfully; no validation error is shown for empty Notes.

- [ ] CS-02: Required fields must be filled to add a book
  - Action: Attempt to save a new book with Title (or Author) left empty.
  - Expected: The book is not created and a validation message identifies the missing required field.

- [ ] CS-03: Reading progress stays within valid bounds
  - Action: Enter invalid progress values, e.g., 150% (or current page 250 of a 200-page book), and a negative value.
  - Expected: The invalid value is rejected or clamped (e.g., to 100% / 200 pages); progress never displays an impossible value.

- [ ] CS-04: Rating is limited to the valid rating scale
  - Action: Attempt to set a rating outside the allowed scale (e.g., 0 or 6 on a 1–5 star scale).
  - Expected: Only ratings within the defined scale can be selected and saved.

## Interaction
- [ ] IX-01: Moving a book between lists updates the page immediately
  - Action: Change a book's status from "Currently Reading" to "Completed".
  - Expected: The book instantly disappears from "Currently Reading" and appears under "Completed" without a page reload.

- [ ] IX-02: Progress display updates after entering progress
  - Action: Change a book's page count or percentage in the progress input.
  - Expected: The progress bar / percentage shown on the book's card updates immediately after saving.

## Content
- [ ] CT-01: Book entries display their stored details correctly
  - Action: Inspect several default books across the three lists.
  - Expected: Each entry shows a title, author, and genre that match the book's stored data, with no missing or mismatched fields.

- [ ] CT-02: Recommendations are relevant to the user's reading profile
  - Action: Review the recommendations list after checking the user's most-read genres and highest-rated books.
  - Expected: Every recommended book comes from the user's own library and matches a most-read genre or is similar to a highly-rated book; unrelated books are not recommended.