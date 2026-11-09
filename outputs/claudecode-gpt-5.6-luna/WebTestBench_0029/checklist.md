# Test Checklist

## Functionality

- [ ] **FT-01: Edit an existing book’s library details**
  - **Action:** Select a pre-existing book, choose **“Edit”**, update **Title**, **Author**, **Genre**, and optional **Notes**, then select **“Save”**.
  - **Expected:** The updated title, author, genre, and notes are displayed on the book record after saving.

- [ ] **FT-02: Record reading progress**
  - **Action:** Open an existing book and enter valid progress using the available **percentage** field or **page count** field, then select **“Save”**.
  - **Expected:** The saved progress value is displayed on the book record and remains after reopening it.

- [ ] **FT-03: Record reading dates**
  - **Action:** Set a valid **Start Date** on an existing book and save it; set a valid **Finish Date** when the book is completed.
  - **Expected:** Both dates are displayed on the book record with the correct labels and values.

- [ ] **FT-04: Move a book between reading-status lists**
  - **Action:** Change an existing book’s status using the status control to **“To Read”**, **“Currently Reading”**, or **“Completed”**.
  - **Expected:** The book appears in the selected status list and is removed from its previous status list.

- [ ] **FT-05: Complete a book with a rating and review**
  - **Action:** Move an existing book to **“Completed”**, enter a valid rating using the displayed rating scale, write a review, and select **“Save”**.
  - **Expected:** The rating and review are saved and the completed book appears in **“Reading History”**.

- [ ] **FT-06: Edit a rating and review from reading history**
  - **Action:** Open an existing completed book in **“Reading History”**, select **“Edit”**, change its rating and review, and select **“Save”**.
  - **Expected:** Reading History displays the updated rating and review.

- [ ] **FT-07: Delete a rating and review from reading history**
  - **Action:** Open an existing history entry, select **“Delete”** for its rating/review, confirm the deletion, and return to Reading History.
  - **Expected:** The deleted rating and review no longer appear for that history entry.

- [ ] **FT-08: View personalized book recommendations**
  - **Action:** Open the **“Recommendations”** section after reviewing the existing library’s genres and ratings.
  - **Expected:** Recommendation results contain books from the user’s library and reflect either frequently read genres or highly rated books.

- [ ] **FT-09: Search and combine collection filters**
  - **Action:** Search for an existing book by title or author, then apply a **Genre**, **Status**, and **Rating** filter together.
  - **Expected:** The collection displays only books matching the search term and all selected filters.

## Constraint

- [ ] **CS-01: Enforce required book details**
  - **Action:** Edit an existing book, clear **Title**, **Author**, or **Genre** one at a time, and select **“Save”**; leave **Notes** empty in a separate attempt.
  - **Expected:** Saving is blocked with a validation message for each missing required field; an empty Notes field does not block saving.

- [ ] **CS-02: Reject invalid reading-progress values**
  - **Action:** Enter an invalid percentage below 0 or above 100, or an invalid page count below 0, and select **“Save”**.
  - **Expected:** The invalid value is rejected with a validation message and the previous valid progress remains unchanged.

- [ ] **CS-03: Enforce valid date order**
  - **Action:** Enter a **Finish Date** earlier than the **Start Date** and select **“Save”**.
  - **Expected:** Saving is blocked and a validation message identifies the invalid date order.

- [ ] **CS-04: Keep each book in one status list**
  - **Action:** Move an existing book from one status to another and inspect all three lists.
  - **Expected:** The book appears in exactly one of **“To Read”**, **“Currently Reading”**, or **“Completed”**, never in multiple lists simultaneously.

- [ ] **CS-05: Restrict ratings and reviews to completed books**
  - **Action:** Open a book in **“To Read”** or **“Currently Reading”** and inspect its rating/review controls.
  - **Expected:** The app prevents saving a rating or review until the book is marked **“Completed”**, or clearly disables those controls.

## Interaction

- [ ] **IX-01: Confirm successful saves**
  - **Action:** Save a valid book edit, progress update, date update, or review update using the **“Save”** button.
  - **Expected:** A visible success confirmation appears and the updated information is shown without requiring a page refresh.

- [ ] **IX-02: Update the interface after a status change**
  - **Action:** Change a book’s status using the status selector or status action.
  - **Expected:** The book’s displayed status, list location, and any visible list count update immediately.

- [ ] **IX-03: Update and clear search/filter results**
  - **Action:** Enter a search term, apply multiple filters, then select **“Clear Filters”** or clear the search field.
  - **Expected:** Results update after each change, and clearing the controls restores the full default collection.

## Content

- [ ] **CT-01: Display complete book information**
  - **Action:** Inspect multiple existing book records in the library.
  - **Expected:** Each record displays its **Title**, **Author**, **Genre**, current status, and progress; **Notes**, dates, rating, and review appear when they exist.

- [ ] **CT-02: Display accurate reading-history entries**
  - **Action:** Open **“Reading History”** and inspect completed books.
  - **Expected:** Each entry identifies the correct book and displays its completion information, finish date when recorded, rating, and review when present.

- [ ] **CT-03: Keep recommendation content relevant**
  - **Action:** Compare the books shown in **“Recommendations”** with the library’s frequently occurring genres and highly rated books.
  - **Expected:** Each recommendation is a library book and has a visible relevance to at least one frequently read genre or highly rated title.