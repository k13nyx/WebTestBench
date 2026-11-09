# Test Result

## Functionality

- [ ] **FT-01: Edit an existing book’s library details**
  - **Action:** Select a pre-existing book, choose **“Edit”**, update **Title**, **Author**, **Genre**, and optional **Notes**, then select **“Save”**.
  - **Expected:** The updated title, author, genre, and notes are displayed on the book record after saving.
  - **Bug Report:**
    - **Issue:** Incomplete display of saved book details
    - **Actual:** The updated title, author, and genre were displayed after saving, but the saved Notes value was not displayed on the book record.

- [X] **FT-02: Record reading progress**
  - **Action:** Open an existing book and enter valid progress using the available **percentage** field or **page count** field, then select **“Save”**.
  - **Expected:** The saved progress value is displayed on the book record and remains after reopening it.

- [ ] **FT-03: Record reading dates**
  - **Action:** Set a valid **Start Date** on an existing book and save it; set a valid **Finish Date** when the book is completed.
  - **Expected:** Both dates are displayed on the book record with the correct labels and values.
  - **Bug Report:**
    - **Issue:** Missing date controls
    - **Actual:** The Edit Book dialog did not contain Start Date or Finish Date fields, so dates could not be set or updated.

- [X] **FT-04: Move a book between reading-status lists**
  - **Action:** Change an existing book’s status using the status control to **“To Read”**, **“Currently Reading”**, or **“Completed”**.
  - **Expected:** The book appears in the selected status list and is removed from its previous status list.

- [ ] **FT-05: Complete a book with a rating and review**
  - **Action:** Move an existing book to **“Completed”**, enter a valid rating using the displayed rating scale, write a review, and select **“Save”**.
  - **Expected:** The rating and review are saved and the completed book appears in **“Reading History”**.
  - **Bug Report:**
    - **Issue:** Missing Reading History section
    - **Actual:** The book was marked Completed and the rating/review save confirmation appeared, but no Reading History section or history entry was present.

- [ ] **FT-06: Edit a rating and review from reading history**
  - **Action:** Open an existing completed book in **“Reading History”**, select **“Edit”**, change its rating and review, and select **“Save”**.
  - **Expected:** Reading History displays the updated rating and review.
  - **Bug Report:**
    - **Issue:** Reading History unavailable
    - **Actual:** No Reading History section or history entries were available to open and edit.

- [ ] **FT-07: Delete a rating and review from reading history**
  - **Action:** Open an existing history entry, select **“Delete”** for its rating/review, confirm the deletion, and return to Reading History.
  - **Expected:** The deleted rating and review no longer appear for that history entry.
  - **Bug Report:**
    - **Issue:** Reading History and delete controls unavailable
    - **Actual:** No Reading History section, history entries, or rating/review delete controls were present.

- [X] **FT-08: View personalized book recommendations**
  - **Action:** Open the **“Recommendations”** section after reviewing the existing library’s genres and ratings.
  - **Expected:** Recommendation results contain books from the user’s library and reflect either frequently read genres or highly rated books.

- [X] **FT-09: Search and combine collection filters**
  - **Action:** Search for an existing book by title or author, then apply a **Genre**, **Status**, and **Rating** filter together.
  - **Expected:** The collection displays only books matching the search term and all selected filters.

## Constraint

- [ ] **CS-01: Enforce required book details**
  - **Action:** Edit an existing book, clear **Title**, **Author**, or **Genre** one at a time, and select **“Save”**; leave **Notes** empty in a separate attempt.
  - **Expected:** Saving is blocked with a validation message for each missing required field; an empty Notes field does not block saving.
  - **Bug Report:**
    - **Issue:** Missing visible validation message
    - **Actual:** Clearing the Title left the edit dialog open after Save, but no visible validation message identifying the missing required field was displayed. Author and Genre validation could not be confirmed.

- [ ] **CS-02: Reject invalid reading-progress values**
  - **Action:** Enter an invalid percentage below 0 or above 100, or an invalid page count below 0, and select **“Save”**.
  - **Expected:** The invalid value is rejected with a validation message and the previous valid progress remains unchanged.
  - **Bug Report:**
    - **Issue:** Missing progress validation message
    - **Actual:** A negative page value remained in the form without a visible validation message. The previous saved progress remained displayed after closing the dialog, but the required validation feedback was absent.

- [ ] **CS-03: Enforce valid date order**
  - **Action:** Enter a **Finish Date** earlier than the **Start Date** and select **“Save”**.
  - **Expected:** Saving is blocked and a validation message identifies the invalid date order.
  - **Bug Report:**
    - **Issue:** Missing date fields and date-order validation
    - **Actual:** The Edit Book dialog contained no Start Date or Finish Date controls, so invalid date ordering could not be entered or validated.

- [X] **CS-04: Keep each book in one status list**
  - **Action:** Move an existing book from one status to another and inspect all three lists.
  - **Expected:** The book appears in exactly one of **“To Read”**, **“Currently Reading”**, or **“Completed”**, never in multiple lists simultaneously.

- [X] **CS-05: Restrict ratings and reviews to completed books**
  - **Action:** Open a book in **“To Read”** or **“Currently Reading”** and inspect its rating/review controls.
  - **Expected:** The app prevents saving a rating or review until the book is marked **“Completed”**, or clearly disables those controls.

## Interaction

- [X] **IX-01: Confirm successful saves**
  - **Action:** Save a valid book edit, progress update, date update, or review update using the **“Save”** button.
  - **Expected:** A visible success confirmation appears and the updated information is shown without requiring a page refresh.

- [X] **IX-02: Update the interface after a status change**
  - **Action:** Change a book’s status using the status selector or status action.
  - **Expected:** The book’s displayed status, list location, and any visible list count update immediately.

- [X] **IX-03: Update and clear search/filter results**
  - **Action:** Enter a search term, apply multiple filters, then select **“Clear Filters”** or clear the search field.
  - **Expected:** Results update after each change, and clearing the controls restores the full default collection.

## Content

- [ ] **CT-01: Display complete book information**
  - **Action:** Inspect multiple existing book records in the library.
  - **Expected:** Each record displays its **Title**, **Author**, **Genre**, current status, and progress; **Notes**, dates, rating, and review appear when they exist.
  - **Bug Report:**
    - **Issue:** Progress not displayed for all book records
    - **Actual:** To Read records displayed title, author, status, and genre but did not display progress information. Saved notes were also not displayed on the book record.

- [ ] **CT-02: Display accurate reading-history entries**
  - **Action:** Open **“Reading History”** and inspect completed books.
  - **Expected:** Each entry identifies the correct book and displays its completion information, finish date when recorded, rating, and review when present.
  - **Bug Report:**
    - **Issue:** Reading History section missing
    - **Actual:** No Reading History section or completed-book history entries were present.

- [X] **CT-03: Keep recommendation content relevant**
  - **Action:** Compare the books shown in **“Recommendations”** with the library’s frequently occurring genres and highly rated books.
  - **Expected:** Each recommendation is a library book and has a visible relevance to at least one frequently read genre or highly rated title.