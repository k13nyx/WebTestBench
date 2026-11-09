# Test Checklist

## Functionality
- [ ] FT-01: Search pets by keyword
  - Action: Enter a search term (e.g., a pet name like "Buddy") in the search box and submit.
  - Expected: The results list shows only pets whose name/description matches the term; non-matching pets are hidden.
- [ ] FT-02: Filter by species
  - Action: Select a species filter (e.g., "Dog") in the filter panel.
  - Expected: Only pets of that species remain listed; pets of other species disappear.
- [ ] FT-03: Filter by age range and size
  - Action: Apply an age range filter (e.g., Puppy/Young) and a size filter (e.g., Small) together.
  - Expected: Only pets matching both criteria are listed; combined filters narrow results cumulatively.
- [ ] FT-04: Filter by compatibility (good with kids / other pets)
  - Action: Toggle "Good with kids" and/or "Good with other pets" filters.
  - Expected: Only pets marked as compatible with the selected options are shown.
- [ ] FT-05: Sort results by relevance and by time listed
  - Action: Open the sort control, select "Relevance", then select "Time listed" (newest first).
  - Expected: Result order changes accordingly; with "Time listed", the most recently added pet appears first.
- [ ] FT-06: Open a detailed pet profile
  - Action: Click a pet card in the results list.
  - Expected: A detail page opens for that pet showing its name, photos, and a written description.
- [ ] FT-07: View multiple photos on the profile
  - Action: On a pet's detail page with more than one photo, navigate through the photo gallery (e.g., thumbnails or next arrow).
  - Expected: Different photos of the pet are displayed as the gallery is navigated.
- [ ] FT-08: Save a pet to favorites
  - Action: On a pet card or its detail page, click the favorite/save button (e.g., heart icon).
  - Expected: The pet is marked as saved (icon state changes) and appears in the favorites list.
- [ ] FT-09: View and manage the favorites list
  - Action: Open the favorites page/list containing previously saved pets, then remove one pet from it.
  - Expected: The list shows the saved pets with correct names; after removal, that pet disappears from the list.
- [ ] FT-10: Submit an adoption inquiry form
  - Action: On a pet's detail page, fill in the inquiry form fields (e.g., name, email, message) with valid values and click the submit button (e.g., "Send Inquiry").
  - Expected: The inquiry is accepted and a confirmation is shown (e.g., success message "Your inquiry has been sent").

## Constraint
- [ ] CS-01: Submit inquiry with empty required fields
  - Action: Click the inquiry submit button leaving required fields (e.g., name, email) blank.
  - Expected: Submission is blocked and a validation error message is displayed next to the empty fields; no success message appears.
- [ ] CS-02: Invalid email rejected in inquiry form
  - Action: Enter an invalid email (e.g., "not-an-email") in the inquiry form and submit.
  - Expected: An email format error is shown and the form is not submitted.
- [ ] CS-03: Filters combine without conflicts
  - Action: Apply filters that match no pets (e.g., species "Cat" + size "Large" + age "Puppy" if none exist).
  - Expected: An empty-state message (e.g., "No pets match your filters") is shown instead of unrelated pets or an error.
- [ ] CS-04: Clearing filters restores full list
  - Action: After applying filters that narrow results, click "Clear filters" / "Reset".
  - Expected: All default pets are listed again and sort selection remains functional.

## Interaction
- [ ] IX-01: Filter or search updates results immediately
  - Action: Change a filter (or type in the search box) and observe the results area.
  - Expected: The pet list updates to reflect the new criteria without requiring a full page reload or error.
- [ ] IX-02: Favorites toggle gives visible feedback
  - Action: Click the favorite button on a pet, then click it again.
  - Expected: The icon/state toggles visibly (e.g., filled ↔ unfilled heart) and the pet is added, then removed, from favorites.
- [ ] IX-03: Inquiry submission shows success feedback
  - Action: Submit a valid inquiry form.
  - Expected: A visible success indication (toast/message such as "Inquiry sent") appears; the form does not silently fail.
- [ ] IX-04: Pet cards are clickable with hover affordance
  - Action: Hover over a pet card in the results list, then click it.
  - Expected: The card shows a hover indication (e.g., highlight/cursor pointer) and clicking opens that pet's profile.

## Content
- [ ] CT-01: Pet photos are relevant and load correctly
  - Action: Browse the results list and open several pet detail pages.
  - Expected: Every card and profile displays a pet photo relevant to that animal (species matches the pet), with no broken-image placeholders.
- [ ] CT-02: Profile details are complete and consistent
  - Action: Open a pet's detail page and compare its info with its card in the list.
  - Expected: The profile shows the pet's name, species, age, size, shelter source, kid/other-pet compatibility, and a non-empty description consistent with the card data.