# Test Checklist

## Functionality
- [ ] FT-01: Add a new book to the personal library
  - Action: Click "Add Book", fill in Title, Author, Genre, and optional Notes fields, then click "Save".
  - Expected: The book is saved and appears in the library list with all entered details.
- [ ] FT-02: Track reading progress using page count or percentage
  - Action: Select an existing book in "Currently Reading", enter an updated page count or percentage, and click "Update Progress".
  - Expected: The book card displays the updated reading progress value and visual progress bar.
- [ ] FT-03: Record reading start and finish dates
  - Action: Select an existing book, set valid Start Date and Finish Date values, and click "Save Dates".
  - Expected: Start and finish dates are recorded and displayed in the book's details.
- [ ] FT-04: Move books between reading status lists
  - Action: Change an existing book's status between "To Read", "Currently Reading", and "Completed" via the status dropdown.
  - Expected: The book is moved to the selected status tab/list and removed from the previous list.
- [ ] FT-05: Submit rating and review upon completing a book
  - Action: Move an existing book to "Completed", select a star rating, enter review text into the review field, and click "Submit Review".
  - Expected: The rating and review are saved and displayed alongside the completed book.
- [ ] FT-06: View completed books in Reading History
  - Action: Navigate to the "Reading History" section.
  - Expected: All completed books appear listed with their completion dates, star ratings, and written reviews.
- [ ] FT-07: Edit an existing rating and review in Reading History
  - Action: In "Reading History", click "Edit" on a reviewed book, update the star rating and review text, then click "Save".
  - Expected: The updated rating and review text are displayed in Reading History.
- [ ] FT-08: Delete a rating and review in Reading History
  - Action: In "Reading History", click "Delete" on a book review and confirm the action.
  - Expected: The rating and review are permanently removed from the book entry in Reading History.
- [ ] FT-09: Filter and search library collection by combined criteria
  - Action: Enter a keyword in the search bar, select a Genre, a Status, and a minimum Rating filter.
  - Expected: Library displays only books that simultaneously match the keyword, selected genre, status, and rating threshold.
- [ ] FT-10: Generate library recommendations based on reading activity
  - Action: Navigate to the "Recommendations" section.
  - Expected: Displays recommended books from within the library matching the user's most-read genres or highest-rated books.

## Constraint
- [ ] CS-01: Prevent adding a book without mandatory fields
  - Action: Click "Add Book", leave Title and Author fields empty, and click "Save".
  - Expected: Form submission is blocked and validation error messages appear under the empty required fields.
- [ ] CS-02: Prevent progress values exceeding maximum limit or negative values
  - Action: Enter a page count greater than total pages (or percentage > 100%) or a negative number into the progress field and click "Update Progress".
  - Expected: Input is rejected with an error message stating the progress value must be between 0 and the maximum book limit.
- [ ] CS-03: Prevent finish date earlier than start date
  - Action: Set a Finish Date that is chronologically earlier than the Start Date and click "Save Dates".
  - Expected: Submission is blocked and an error message indicates the finish date cannot precede the start date.

## Interaction
- [ ] IX-01: Prompt rating and review modal when marking book as Completed
  - Action: Change an existing book's status from "Currently Reading" to "Completed".
  - Expected: A rating and review modal automatically opens over the screen.
- [ ] IX-02: Display confirmation dialog before deleting rating and review
  - Action: In "Reading History", click the "Delete" button on an existing rating/review.
  - Expected: A confirmation modal appears asking for confirmation with "Cancel" and "Confirm Delete" options.
- [ ] IX-03: Reset active filters to default state
  - Action: Apply search keywords and filter dropdowns, then click "Clear Filters".
  - Expected: All filter dropdowns and search inputs reset to their default blank states, and the full library view is restored.

## Content
- [ ] CT-01: Verify book card details in the library
  - Action: View any existing book card in the library.
  - Expected: Card displays Title, Author, Genre tag, current reading progress, and optional Notes text.
- [ ] CT-02: Verify recommendation reason label
  - Action: View items displayed in the "Recommendations" section.
  - Expected: Each recommended book card displays a descriptive basis tag (e.g., "Based on your top genre: Sci-Fi" or "Because you highly rated [Book Title]").