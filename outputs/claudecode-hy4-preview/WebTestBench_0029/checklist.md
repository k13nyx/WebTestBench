# Test Checklist

## Functionality
- [ ] FT-01: Add a new book with title, author, genre, and optional notes
  - Action: Open the "Add Book" form, enter a title, author, and genre, leave the notes field empty, and submit.
  - Expected: A new book entry appears in the library showing the entered title, author, and genre; no notes text is shown for it.
- [ ] FT-02: Track reading progress by percentage
  - Action: Open a default book, set its progress to 50% using the percentage control, and save.
  - Expected: The book's progress displays as 50% after saving.
- [ ] FT-03: Track reading progress by page count
  - Action: Open a default book that has a total page count, set a current page number lower than the total, and save.
  - Expected: Progress displays as "current / total pages" and the equivalent percentage is shown.
- [ ] FT-04: Mark start and finish dates
  - Action: On a default book, set a start date, then set a later finish date, and save.
  - Expected: Both the start date and finish date are displayed on the book's entry.
- [ ] FT-05: Move a book between "To Read", "Currently Reading", and "Completed"
  - Action: Take a default book in "To Read", change its status to "Currently Reading", then change it to "Completed".
  - Expected: The book appears in "Currently Reading" and is absent from "To Read"; then appears in "Completed" and is absent from "Currently Reading".
- [ ] FT-06: Rate and review a completed book
  - Action: Open a default book in the "Completed" list, select a star rating, enter review text, and submit.
  - Expected: The rating and review are saved and displayed on that book's entry.
- [ ] FT-07: Reading history lists completed books with their ratings, reviews, and dates
  - Action: Open the "Reading History" view.
  - Expected: Every book with "Completed" status appears in the list, each showing title, finish date, rating, and review.
- [ ] FT-08: Edit an existing rating and review from reading history
  - Action: In Reading History, change an existing book's rating (e.g., 4 → 5) and edit its review text, then save.
  - Expected: The updated rating and updated review text are displayed for that book.
- [ ] FT-09: Delete an existing rating/review from reading history
  - Action: In Reading History, delete the review for a book that has one, and confirm if prompted.
  - Expected: The review is no longer displayed for that book; the book remains in history.
- [ ] FT-10: Recommendations based on most-read genres or highly rated books
  - Action: Open the recommendations section of the library page.
  - Expected: At least one book is recommended; every recommended book comes from the user's own library and matches either a most-read genre or a highly rated book.
- [ ] FT-11: Combine keyword search with genre, status, and rating filters
  - Action: Enter a keyword in the search box, then apply a genre filter, a status filter, and a rating filter together.
  - Expected: Only books matching all four criteria are displayed.

## Constraint
- [ ] CS-01: Required fields block book creation
  - Action: Submit the "Add Book" form with the title field empty (repeat with author empty, then genre empty).
  - Expected: No book is created; a validation message is shown for the empty required field in each case.
- [ ] CS-02: Progress cannot exceed valid bounds
  - Action: Set progress to a percentage above 100 (and separately set a current page greater than the total pages), then save.
  - Expected: The invalid value is rejected with a validation message; saved progress never exceeds 100% or the total page count.
- [ ] CS-03: Rating and review are restricted to completed books
  - Action: Open a book in "To Read" or "Currently Reading" and attempt to submit a rating and review.
  - Expected: The rating/review control is unavailable or the submission is blocked with a message stating only completed books can be rated/reviewed.
- [ ] CS-04: Finish date cannot be earlier than start date
  - Action: On a book with a start date, set a finish date earlier than the start date and save.
  - Expected: The save is blocked with a validation message; the dates remain unchanged.

## Interaction
- [ ] IX-01: Success confirmation after adding a book
  - Action: Successfully add a new book using the "Add Book" form.
  - Expected: A success message/toast confirming the book was added is displayed.
- [ ] IX-02: Status change relocates the book card without a page reload
  - Action: Change a book's status to "Completed" from its current list.
  - Expected: The book card immediately disappears from the previous list and appears in the "Completed" list.
- [ ] IX-03: Clearing filters restores the full library
  - Action: Apply at least one filter, then click the "Clear"/"Reset" filters control.
  - Expected: All filter and search inputs return to their default state and the full library is displayed again.

## Content
- [ ] CT-01: Book entries display all stored details accurately
  - Action: View a default book entry in the library.
  - Expected: Title, author, genre, notes (if present), progress, and start/finish dates are displayed and match the book's stored data.
- [ ] CT-02: Ratings and reviews are rendered correctly in reading history
  - Action: In Reading History, inspect an entry that has a rating and a review.
  - Expected: The rating is shown as the correct number of filled rating units, the review text is shown in full, and the finish date is displayed.