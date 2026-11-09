# Test Checklist

## Functionality
- [ ] FT-01: Add a new book to the personal library with title, author, genre, and notes.
  - Action: Click "Add Book", enter title "Dune", author "Frank Herbert", genre "Science Fiction", notes "Book club pick", and save.
  - Expected: The book is saved and appears in the library listing.

- [ ] FT-02: Edit the details of an existing book in the library.
  - Action: Open a default book from the library, change its author and notes, and save.
  - Expected: The book's entry reflects the updated author and notes; all other fields remain unchanged.

- [ ] FT-03: Delete a book from the library.
  - Action: Delete a default book from the library.
  - Expected: The book no longer appears in the library or in any status list.

- [ ] FT-04: Track reading progress using a percentage or a page count.
  - Action: Open a book in "Currently Reading", set progress to 50% and save; then update progress to page count 120 and save.
  - Expected: The book displays the saved progress value after each update (50%, then 120 pages).

- [ ] FT-05: Mark start and finish dates on a book.
  - Action: Open a book and set its start date to 2026-03-01 and its finish date to 2026-03-15.
  - Expected: Both dates are saved and displayed on the book's entry.

- [ ] FT-06: Move a book between "To Read", "Currently Reading", and "Completed".
  - Action: Move a book from "To Read" to "Currently Reading", then move it to "Completed".
  - Expected: After each move the book appears in the target list and is removed from the previous list.

- [ ] FT-07: Rate a finished book.
  - Action: On a book in "Completed", select a 4-star rating and save.
  - Expected: The 4-star rating is saved on the book.

- [ ] FT-08: Write and save a review for a finished book.
  - Action: On a book in "Completed", enter review text "Great world-building, slow middle." and save.
  - Expected: The review is saved on the book.

- [ ] FT-09: View the reading history of finished books.
  - Action: Open the reading history after completing a rated and reviewed book.
  - Expected: The completed book appears in the reading history, showing its rating and review.

- [ ] FT-10: Edit and delete ratings and reviews from the reading history.
  - Action: In reading history, edit a book's rating to 5 stars with new review text and save; then delete that rating and review.
  - Expected: The edited rating and review are displayed after saving; after deletion the rating and review no longer appear, while the book remains in history.

- [ ] FT-11: Search the library and apply combined genre, status, and rating filters.
  - Action: Type a keyword matching one default book's title or author; then apply a genre filter, a status filter, and a rating filter together.
  - Expected: Displayed books match the keyword and all applied filters simultaneously; clearing the filters restores the full library.

- [ ] FT-12: View book recommendations within the library.
  - Action: Open the recommendations section of the page.
  - Expected: A recommendations section displays suggested books drawn from the user's library.

## Constraint
- [ ] CS-01: Required book fields must be provided; notes are optional.
  - Action: Submit the add-book form with the title field empty (repeat with author or genre empty); then submit the form with only notes empty.
  - Expected: A missing required field shows a validation error and the book is not saved; a book with empty notes saves successfully.

- [ ] CS-02: Reading progress input is validated.
  - Action: Enter progress percentage 150 and -10, and a negative page count, on a book.
  - Expected: Each invalid value is rejected with an error message and not saved.

- [ ] CS-03: Finish date cannot be earlier than the start date.
  - Action: Set a book's start date to 2026-03-10, then set its finish date to 2026-03-01.
  - Expected: The earlier finish date is rejected with an error and the previously saved dates remain unchanged.

- [ ] CS-04: Only completed books can be rated and reviewed.
  - Action: Open a book in "To Read" or "Currently Reading" and attempt to set a rating or review on it.
  - Expected: Rating and review controls are unavailable or the submission is rejected for books not in "Completed".

## Interaction
- [ ] IX-01: Saving a book gives immediate confirmation and updates the view.
  - Action: Add a book (or save edits to an existing book) and observe the page without reloading.
  - Expected: A success confirmation (message/toast) appears and the library list reflects the change immediately.

- [ ] IX-02: Editing a rating/review opens prefilled with current values.
  - Action: Click edit on an existing rating and review in the reading history.
  - Expected: The edit form shows the current star rating and review text already filled in.

## Content
- [ ] CT-01: Book entries display all saved details accurately.
  - Action: Compare a book's saved title, author, genre, and notes with its entry in the library.
  - Expected: All details are displayed exactly as saved, with notes shown when present and no fields missing or altered.

- [ ] CT-02: Recommendations are relevant to the user's reading patterns.
  - Action: Check each recommended book's genre against the user's most-read genres and the genres of the user's highest-rated books.
  - Expected: Every recommended book falls within a most-read genre or the genre of a highly rated book; no unrelated books are suggested.