# Test Result

## Functionality
- [X] FT-01: User can add a new book with title, author, genre, and optional notes
  - Action: Open "Add Book" form, enter title, author, select a genre, type a note, submit.
  - Expected: The new book appears in the library list under "To Read" showing all entered details.
  - Verified: "The Silent Forest / Ava Chen / To Read / Fantasy" card appeared; note persisted (visible in the book's edit form); toast "Book Added" shown; To Read count 3→4.

- [X] FT-02: User can move a book from "To Read" to "Currently Reading"
  - Action: On a default "To Read" book, trigger the status change (e.g., select "Currently Reading").
  - Expected: Book disappears from "To Read" and appears in "Currently Reading"; a start date is captured.
  - Verified: "The Hobbit" moved via its "Start Reading" button; card now shows "Reading … Started: 11/8/2026"; tab counts updated To Read (3→1 after two starts), Reading (2→4).

- [ ] FT-03: Reading progress can be tracked by percentage
  - Action: Edit a "Currently Reading" book and set progress to a percentage value (e.g., 45%).
  - Expected: Progress reflects 45% on the book's card/row in the list.
  - Bug Report:
    - Issue: Missing Feature — no percentage-based progress input or display.
    - Actual: The Edit Book dialog only offers numeric "Total Pages"/"Current Page" fields; book cards show only "412 / 688 pages" text + an unlabeled progress bar. No percentage value can be entered, and no "%" text is rendered anywhere on the page. Secondary defect found while testing progress editing: the "Edit Book" dialog does not pre-load the book's own data — opening Edit for "Dune" (fresh session) showed an empty/default form (title/author blank, Genre "Classic Fiction", Status "To Read", 300/0 pages), and opening Edit for "1984" later showed the previously typed values of another book ("Dune", 688/120, Currently Reading), forcing manual re-entry of all fields.

- [X] FT-04: Reading progress can be tracked by page count
  - Action: Edit a "Currently Reading" book and update progress via pages read (e.g., page 120).
  - Expected: Page count is saved and displayed for that book.
  - Verified: Dune updated to current page 120 of 688; card displays "Progress | 120 / 688 pages" with "Reading" status (values had to be fully re-entered because the dialog doesn't pre-fill, see FT-03 note; save itself worked with toast "Book Updated").

- [X] FT-05: Marking a book "Completed" prompts for rating and review
  - Action: Move a "Currently Reading" book to "Completed".
  - Expected: The completion flow asks the user to give a rating and write a review before/while finalizing.
  - Verified: "Mark as Completed" on 1984 opened a "Rate & Review" dialog ("1984 by George Orwell — Your Rating (5 stars) / Review (optional)") that must be completed before finalizing; Save disabled until a rating is picked.

- [ ] FT-06: Finished book with rating and review appears in reading history
  - Action: Complete a book with a rating (e.g., 4 stars) and a review, then open the "Reading History" section.
  - Expected: The book is listed in history showing its rating, review text, and finish date.
  - Bug Report:
    - Issue: Missing Content — review text not displayed; no dedicated "Reading History" section.
    - Actual: In the Completed list (the only history-like view), "1984" shows rating (4/5 gold stars) and "Finished: 11/8/2026", but the saved review text is not rendered anywhere in the list ("A chilling masterpiece…" was absent from page text; the document icon beside the stars is decorative and clicking it reveals nothing). The app has no section explicitly named "Reading History" (only a tab "Completed (n)" and a subtitle mentioning history).

- [X] FT-07: User can edit an existing rating/review from reading history
  - Action: In Reading History, open the edit option for a completed book, change the rating and review text, save.
  - Expected: Updated rating and review are displayed for that book in history.
  - Verified: Completed-card menu offers "Edit Review" (dialog correctly pre-fills current rating 4★ and review text); changed to 5 stars and new text → card now renders 5/5 filled stars, and reopening Edit Review shows the updated rating and text; toast "Review Saved".

- [ ] FT-08: User can delete a rating/review from reading history
  - Action: In Reading History, use the delete option on a book's rating/review and confirm.
  - Expected: The rating/review is removed; the book remains in the library in a sensible state (e.g., completed without rating, or returns to "To Read").
  - Bug Report:
    - Issue: Missing Feature — no delete/clear control for rating or review.
    - Actual: The completed-book menu only offers "Edit Details / Edit Review / Remove from Library" (last removes the whole book). Inside Edit Review, clearing the review textarea and saving did NOT remove the review — reopening still showed "A masterpiece — even more chilling on re-read."; clicking the filled 5th star does not deselect the rating (still 5 filled). There is no path to remove a rating/review while keeping the book.

- [X] FT-09: Recommendations are shown based on most-read genres or highly rated books
  - Action: Open the "Recommendations" area after the library contains books with varying genres and at least one 5-star rating.
  - Expected: Recommended books are displayed and drawn from within the user's library, biased toward frequent genres / high-rated books.
  - Verified: "Recommended for You" section renders books from the library only (initial: The Midnight Library, The Hobbit, The Name of the Wind; after statuses changed and a 5★ Dystopian rating was added, it dynamically narrowed to the remaining unread book, The Name of the Wind — a Fantasy title matching the most-active genre). No external/placeholder entries shown.

- [X] FT-10: Search finds books by title and author
  - Action: Type the exact title of a default book into the search field; then search by an author name.
  - Expected: Matching book(s) are shown; non-matching books are hidden.
  - Verified: "Dune" → only Dune visible; "George Orwell" → only 1984 visible; all other books hidden.

- [X] FT-11: Filters can be combined (genre + status + rating)
  - Action: Apply a genre filter, a status filter (e.g., "Currently Reading"), and a minimum rating filter simultaneously.
  - Expected: Only books matching ALL three criteria are displayed.
  - Verified: Genre "Science Fiction" + Status "Completed" + Rating "4+ Stars" applied together → only "Project Hail Mary" (SciFi, Completed, 4★) displayed; Dune (Reading), 1984 (Dystopian), Gatsby (Classic Fiction) all correctly excluded.

## Constraint
- [X] CS-01: Required fields are enforced when adding a book
  - Action: Submit the "Add Book" form with empty title (and/or author).
  - Expected: Save is blocked and a validation message indicates the missing required field(s).
  - Verified: Title and author inputs carry `required`; clicking "Add Book" kept the dialog open (no book created) and the browser validation message "Please fill out this field." fired on the empty Title field.

- [X] CS-02: Progress values must stay within valid bounds
  - Action: Attempt to set progress above 100% or below 0% (or pages exceeding total pages / negative).
  - Expected: Input is rejected with an error, or clamped to valid range; invalid value is not stored.
  - Verified: "Current Page" input is bounded by 0..Total Pages. Entering 500 (total=300) → save blocked, native error "Value must be less than or equal to 300."; entering -10 → "Value must be greater than or equal to 0."; invalid values were never stored (dialog remained open, book unchanged).

- [X] CS-03: Rating must be valid when completing a book
  - Action: Attempt to finish a book with no rating selected, or an out-of-range rating (e.g., 6 on a 5-star scale).
  - Expected: Completion is blocked until a valid in-range rating is provided.
  - Verified: In the "Rate & Review" completion dialog, "Save Review" is disabled until a star rating is chosen (click on it failed with element-not-enabled); the rating control is a 5-star picker, making an out-of-range value like 6 unenterable. Saving became possible only after selecting a star.

- [ ] CS-04: Finish date cannot be earlier than start date
  - Action: Set a book's finish date to a date before its recorded start date.
  - Expected: The value is rejected with a validation message; the book's dates remain consistent.
  - Bug Report:
    - Issue: Missing Feature — no date editing exists at all, so the constraint cannot be exercised or enforced.
    - Actual: Neither the "Edit Book" dialog (only Title/Author/Genre/Status/Total Pages/Current Page/Cover URL/Notes) nor the "Rate & Review" completion dialog contains any date input; "Started:"/"Finished:" dates on cards are static auto-set text (no input[type=date] anywhere). Attempting to set a finish date earlier than the start date is impossible — no validation message exists because no such control exists.

## Interaction
- [X] IX-01: Feedback is shown after key actions
  - Action: Add a book, move a book between lists, and save a review.
  - Expected: A visible confirmation (e.g., success toast or inline message) appears for each action.
  - Verified: toast "Book Added — 'The Silent Forest' has been added to your library."; "Started Reading — You've started reading 'The Midnight Library'."; "Book Updated"; "Review Saved — Your rating and review have been saved."

- [X] IX-02: Lists update immediately after a status change
  - Action: Move a default book from "To Read" to "Currently Reading" and observe the page.
  - Expected: The book appears in the new list and disappears from the old one without stale entries.
  - Verified: After "Start Reading", tab counts updated live (To Read 3→1, Reading 2→4 matching exactly the two started books); The Hobbit card in the Reading list shows its new "Reading" badge + Started date, with no stale copy/old badge.

- [X] IX-03: Empty state shown when search/filters match nothing
  - Action: Search for a nonsense string like "zzzqqq", or combine filters that no default book satisfies.
  - Expected: A clear "no results" message is shown instead of a blank page or broken list.
  - Verified: With "zzzqqq" (on top of active filters) the list shows "No books found | Try adjusting your filters" — no blank/broken rendering.

## Content
- [X] CT-01: Default library data displays completely and correctly
  - Action: Open the reading management page without making changes; inspect several default books.
  - Expected: Each book shows relevant, complete details (title, author, genre, status), and progress/rating/review fields are either populated or gracefully absent — no placeholder text, broken labels, or contradictory data.
  - Verified: All 10 default books show title, author, status badge (Completed/Reading/To Read) and genre; Reading books show "x / y pages" + progress bar; Completed books show filled-star ratings and Started/Finished dates; To Read books gracefully show a "Start Reading" action instead. Stats consistent (10 books = 5+2+3; Avg 4.6 matches five completed ratings 5,5,4,5,4). Body text scan found zero occurrences of "undefined", "NaN", "[object" or lorem-placeholder text.
