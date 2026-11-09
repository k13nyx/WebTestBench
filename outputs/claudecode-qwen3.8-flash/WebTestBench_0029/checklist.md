# Test Checklist

## Functionality
- [ ] FT-01: User can add a new book with title, author, genre, and optional notes
  - Action: Open "Add Book" form, enter title, author, select a genre, type a note, submit.
  - Expected: The new book appears in the library list under "To Read" showing all entered details.

- [ ] FT-02: User can move a book from "To Read" to "Currently Reading"
  - Action: On a default "To Read" book, trigger the status change (e.g., select "Currently Reading").
  - Expected: Book disappears from "To Read" and appears in "Currently Reading"; a start date is captured.

- [ ] FT-03: Reading progress can be tracked by percentage
  - Action: Edit a "Currently Reading" book and set progress to a percentage value (e.g., 45%).
  - Expected: Progress reflects 45% on the book's card/row in the list.

- [ ] FT-04: Reading progress can be tracked by page count
  - Action: Edit a "Currently Reading" book and update progress via pages read (e.g., page 120).
  - Expected: Page count is saved and displayed for that book.

- [ ] FT-05: Marking a book "Completed" prompts for rating and review
  - Action: Move a "Currently Reading" book to "Completed".
  - Expected: The completion flow asks the user to give a rating and write a review before/while finalizing.

- [ ] FT-06: Finished book with rating and review appears in reading history
  - Action: Complete a book with a rating (e.g., 4 stars) and a review, then open the "Reading History" section.
  - Expected: The book is listed in history showing its rating, review text, and finish date.

- [ ] FT-07: User can edit an existing rating/review from reading history
  - Action: In Reading History, open the edit option for a completed book, change the rating and review text, save.
  - Expected: Updated rating and review are displayed for that book in history.

- [ ] FT-08: User can delete a rating/review from reading history
  - Action: In Reading History, use the delete option on a book's rating/review and confirm.
  - Expected: The rating/review is removed; the book remains in the library in a sensible state (e.g., completed without rating, or returns to "To Read").

- [ ] FT-09: Recommendations are shown based on most-read genres or highly rated books
  - Action: Open the "Recommendations" area after the library contains books with varying genres and at least one 5-star rating.
  - Expected: Recommended books are displayed and drawn from within the user's library, biased toward frequent genres / high-rated books.

- [ ] FT-10: Search finds books by title and author
  - Action: Type the exact title of a default book into the search field; then search by an author name.
  - Expected: Matching book(s) are shown; non-matching books are hidden.

- [ ] FT-11: Filters can be combined (genre + status + rating)
  - Action: Apply a genre filter, a status filter (e.g., "Currently Reading"), and a minimum rating filter simultaneously.
  - Expected: Only books matching ALL three criteria are displayed.

## Constraint
- [ ] CS-01: Required fields are enforced when adding a book
  - Action: Submit the "Add Book" form with empty title (and/or author).
  - Expected: Save is blocked and a validation message indicates the missing required field(s).

- [ ] CS-02: Progress values must stay within valid bounds
  - Action: Attempt to set progress above 100% or below 0% (or pages exceeding total pages / negative).
  - Expected: Input is rejected with an error, or clamped to valid range; invalid value is not stored.

- [ ] CS-03: Rating must be valid when completing a book
  - Action: Attempt to finish a book with no rating selected, or an out-of-range rating (e.g., 6 on a 5-star scale).
  - Expected: Completion is blocked until a valid in-range rating is provided.

- [ ] CS-04: Finish date cannot be earlier than start date
  - Action: Set a book's finish date to a date before its recorded start date.
  - Expected: The value is rejected with a validation message; the book's dates remain consistent.

## Interaction
- [ ] IX-01: Feedback is shown after key actions
  - Action: Add a book, move a book between lists, and save a review.
  - Expected: A visible confirmation (e.g., success toast or inline message) appears for each action.

- [ ] IX-02: Lists update immediately after a status change
  - Action: Move a default book from "To Read" to "Currently Reading" and observe the page.
  - Expected: The book appears in the new list and disappears from the old one without stale entries.

- [ ] IX-03: Empty state shown when search/filters match nothing
  - Action: Search for a nonsense string like "zzzqqq", or combine filters that no default book satisfies.
  - Expected: A clear "no results" message is shown instead of a blank page or broken list.

## Content
- [ ] CT-01: Default library data displays completely and correctly
  - Action: Open the reading management page without making changes; inspect several default books.
  - Expected: Each book shows relevant, complete details (title, author, genre, status), and progress/rating/review fields are either populated or gracefully absent — no placeholder text, broken labels, or contradictory data.