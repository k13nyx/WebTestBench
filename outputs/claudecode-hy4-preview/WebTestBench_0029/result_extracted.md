# Test Result

## Functionality

- [X] FT-01: Add a new book with title, author, genre, and optional notes
  - Action: Open the "Add Book" form, enter a title, author, and genre, leave the notes field empty, and submit.
  - Expected: A new book entry appears in the library showing the entered title, author, and genre; no notes text is shown for it.

- [ ] FT-02: Track reading progress by percentage
  - Action: Open a default book, set its progress to 50% using the percentage control, and save.
  - Expected: The book's progress displays as 50% after saving.
  - Bug Report:
    - Issue: Missing Feature / Unreachable Control
    - Actual: No percentage control exists anywhere in the reachable UI. The "Add Book" and "Edit Book" dialogs contain only Total Pages and Current Page numeric inputs; the card renders the string "150 / 300 pages" with no percentage figure. A `ProgressModal` component (with a Slider and a `progress` + "%" readout) exists in the source (`/src/components/ProgressModal.tsx`) but is dead code — its `onUpdateProgress` prop is destructured in `BookCard` and never invoked, so the modal can never be opened.

- [ ] FT-03: Track reading progress by page count
  - Action: Open a default book that has a total page count, set a current page number lower than the total, and save.
  - Expected: Progress displays as "current / total pages" and the equivalent percentage is shown.
  - Bug Report:
    - Issue: Incomplete Rendering
    - Actual: Setting The Hobbit's current page to 150 of 300 saved correctly and the card rendered "Progress  150 / 300 pages", but no equivalent percentage is displayed. A page-wide text search returned no "%" character anywhere in the rendered library.

- [ ] FT-04: Mark start and finish dates
  - Action: On a default book, set a start date, then set a later finish date, and save.
  - Expected: Both the start date and finish date are displayed on the book's entry.
  - Bug Report:
    - Issue: Missing Feature / No Date Controls
    - Actual: Neither the "Add Book" dialog nor the "Edit Book" dialog contains any start-date or finish-date input. The complete label set is: Title, Author, Genre, Status, Total Pages, Current Page, Cover URL (optional), Notes (optional). Dates can only be auto-stamped by the "Start Reading" / "Mark as Completed" actions (e.g. The Hobbit received "Started: 11/7/2026, Finished: 11/7/2026"), so a user cannot manually mark them.

- [X] FT-05: Move a book between "To Read", "Currently Reading", and "Completed"
  - Action: Take a default book in "To Read", change its status to "Currently Reading", then change it to "Completed".
  - Expected: The book appears in "Currently Reading" and is absent from "To Read"; then appears in "Completed" and is absent from "Currently Reading".

- [ ] FT-06: Rate and review a completed book
  - Action: Open a default book in the "Completed" list, select a star rating, enter review text, and submit.
  - Expected: The rating and review are saved and displayed on that book's entry.
  - Bug Report:
    - Issue: Incomplete Rendering
    - Actual: Submission is saved — the toast "Review Saved / Your rating and review have been saved." appeared, and the star rating updates on the card. However, the review text is never rendered on the book's entry. `BookCard.tsx` only uses `book.review` as a boolean condition to show a `FileText` icon; it never outputs the text. Verified: after saving the review "QA review text: A timeless classic that still resonates today.", the card text remained "To Kill a Mockingbird | Harper Lee | Completed | Classic Fiction" with no review content.

- [ ] FT-07: Reading history lists completed books with their ratings, reviews, and dates
  - Action: Open the "Reading History" view.
  - Expected: Every book with "Completed" status appears in the list, each showing title, finish date, rating, and review.
  - Bug Report:
    - Issue: Missing Feature (View Does Not Exist)
    - Actual: There is no Reading History view. `App.tsx` defines only two routes: `path="/"` (Index) and `path="*"` (NotFound). The rendered page has zero `<a>` links, no navigation element beyond the "Add Book" button, no "History" text anywhere in the DOM, and navigating to `http://localhost:6029/history` returns a 404 ("Oops! Page not found"). Only the All / Reading / To Read / Completed tabs exist.

- [ ] FT-08: Edit an existing rating and review from reading history
  - Action: In Reading History, change an existing book's rating (e.g., 4 → 5) and edit its review text, then save.
  - Expected: The updated rating and updated review text are displayed for that book.
  - Bug Report:
    - Issue: Missing Feature (View Does Not Exist)
    - Actual: No Reading History view exists (see FT-07). Editing is only possible via a book card's "Edit Review" menu item, which does update the rating, but the review text is still not displayed on the entry afterwards.

- [ ] FT-09: Delete an existing rating/review from reading history
  - Action: In Reading History, delete the review for a book that has one, and confirm if prompted.
  - Expected: The review is no longer displayed for that book; the book remains in history.
  - Bug Report:
    - Issue: Missing Feature (View Does Not Exist)
    - Actual: No Reading History view exists, and no delete control for a rating/review is present anywhere in the UI. The only per-book actions are "Edit Details", "Start Reading"/"Mark as Completed"/"Edit Review", and "Remove from Library" (which deletes the whole book, not just the review).

- [ ] FT-10: Recommendations based on most-read genres or highly rated books
  - Action: Open the recommendations section of the library page.
  - Expected: At least one book is recommended; every recommended book comes from the user's own library and matches either a most-read genre or a highly rated book.
  - Bug Report:
    - Issue: Incorrect Recommendation Logic
    - Actual: Recommendations are "The Midnight Library" (Contemporary Fiction) and "The Name of the Wind" (Fantasy). Both come from the user's own library, but neither matches the criteria. Per `useBooks.ts`, the algorithm counts genres only across *highly rated completed* books: Classic Fiction (2), Science Fiction (1), Self-Help (1), Non-Fiction (1) — so top genres = Classic Fiction, Science Fiction, Self-Help. Neither recommended book's genre is in that set, and both are unrated "To Read" books. They appear only because of the fallback branch `if (recommended.length < 3) { push other to-read books }`, which surfaces unrelated unread books.

- [X] FT-11: Combine keyword search with genre, status, and rating filters
  - Action: Enter a keyword in the search box, then apply a genre filter, a status filter, and a rating filter together.
  - Expected: Only books matching all four criteria are displayed.

## Constraint

- [X] CS-01: Required fields block book creation
  - Action: Submit the "Add Book" form with the title field empty (repeat with author empty, then genre empty).
  - Expected: No book is created; a validation message is shown for the empty required field in each case.
  - Note: Empty title and empty author were each rejected with the native validation message "Please fill out this field." and the book count stayed at 10. The genre case could not be reproduced: genre is a closed dropdown whose 10 options are all real genres with no blank/placeholder option, so it can never be submitted empty — the constraint holds structurally rather than via a validation message.

- [X] CS-02: Progress cannot exceed valid bounds
  - Action: Set progress to a percentage above 100 (and separately set a current page greater than the total pages), then save.
  - Expected: The invalid value is rejected with a validation message; saved progress never exceeds 100% or the total page count.
  - Note: The page-count case is enforced: the Current Page input carries `max="300"`, and entering 999 blocked submission with "Value must be less than or equal to 300.", the dialog stayed open, and the card remained "150 / 300 pages". The percentage case is not applicable — no percentage input exists to over-fill (see FT-02), so progress can never exceed 100% or the total.

- [X] CS-03: Rating and review are restricted to completed books
  - Action: Open a book in "To Read" or "Currently Reading" and attempt to submit a rating and review.
  - Expected: The rating/review control is unavailable or the submission is blocked with a message stating only completed books can be rated/reviewed.
  - Note: Satisfied via the "control is unavailable" branch. A "To Read" book's menu offers only Edit Details / Start Reading / Remove from Library; a "Currently Reading" book offers only Edit Details / Mark as Completed / Remove from Library. The Edit Review / Add Review item appears only on "Completed" books.

- [ ] CS-04: Finish date cannot be earlier than start date
  - Action: On a book with a start date, set a finish date earlier than the start date and save.
  - Expected: The save is blocked with a validation message; the dates remain unchanged.
  - Bug Report:
    - Issue: Missing Feature / Validation Cannot Be Exercised
    - Actual: There are no start-date or finish-date inputs in either the Add or Edit forms (see FT-04), so no finish date can be entered at all and the validation rule cannot be triggered. Dates are only auto-assigned by status-change actions.

## Interaction

- [X] IX-01: Success confirmation after adding a book
  - Action: Successfully add a new book using the "Add Book" form.
  - Expected: A success message/toast confirming the book was added is displayed.

- [X] IX-02: Status change relocates the book card without a page reload
  - Action: Change a book's status to "Completed" from its current list.
  - Expected: The book card immediately disappears from the previous list and appears in the "Completed" list.

- [X] IX-03: Clearing filters restores the full library
  - Action: Apply at least one filter, then click the "Clear"/"Reset" filters control.
  - Expected: All filter and search inputs return to their default state and the full library is displayed again.

## Content

- [ ] CT-01: Book entries display all stored details accurately
  - Action: View a default book entry in the library.
  - Expected: Title, author, genre, notes (if present), progress, and start/finish dates are displayed and match the book's stored data.
  - Bug Report:
    - Issue: Missing Field in Display
    - Actual: Title, author, genre, progress ("150 / 300 pages") and start/finish dates all render and match the stored values. However, notes are never rendered: "The Great Gatsby" has `notes: 'A masterpiece of American literature exploring the jazz age.'` in the seed data (`/src/data/books.ts`), yet its card only shows "The Great Gatsby | F. Scott Fitzgerald | Completed | Classic Fiction | Started: 1/15/2024 | Finished: 1/28/2024". The string "notes" does not appear anywhere in `BookCard.tsx`.

- [ ] CT-02: Ratings and reviews are rendered correctly in reading history
  - Action: In Reading History, inspect an entry that has a rating and a review.
  - Expected: The rating is shown as the correct number of filled rating units, the review text is shown in full, and the finish date is displayed.
  - Bug Report:
    - Issue: Missing Feature (View Does Not Exist)
    - Actual: No Reading History view exists (see FT-07), so this entry cannot be inspected. For reference, on the library card the rating is rendered correctly as filled units — e.g. Project Hail Mary (rating 4) shows 4 of 5 stars with `fill-gold text-gold` and the 5th with `fill-transparent text-gold-muted` — and the finish date is displayed, but the review text is not rendered in full or at all.
