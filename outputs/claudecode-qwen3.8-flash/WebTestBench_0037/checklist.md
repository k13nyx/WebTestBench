# Test Checklist

## Functionality
- [ ] FT-01: Keyword search returns matching pets
  - Action: Enter a pet name/breed keyword from the default data (e.g., "Bella") into the search box and submit.
  - Expected: The results list shows only pets matching the keyword; unrelated pets are hidden.

- [ ] FT-02: Species filter narrows results correctly
  - Action: Select species filter "Dog", then switch to "Cat".
  - Expected: Only pets of the selected species appear in the results list.

- [ ] FT-03: Age range filter narrows results correctly
  - Action: Apply an age range filter (e.g., "Puppy/Young" or a min–max age) to the default pets.
  - Expected: Every listed pet's displayed age falls within the selected range.

- [ ] FT-04: Size filter narrows results correctly
  - Action: Apply size filter "Small" (and then "Large").
  - Expected: Only pets with the selected size attribute are shown.

- [ ] FT-05: "Good with kids / good with other pets" filters work
  - Action: Enable "Good with kids", then enable "Good with other pets".
  - Expected: Results contain only pets marked as good with kids (resp. other pets).

- [ ] FT-06: Sorting by relevance and by time listed
  - Action: Open the sort control, select "Time Listed", then select "Relevance".
  - Expected: Both options exist; "Time Listed" reorders the list by listing date (newest/oldest), and "Relevance" produces a distinct ordering.

- [ ] FT-07: Pet detail profile opens from the list
  - Action: Click any pet card in the results list.
  - Expected: A profile page/panel opens for that specific pet showing photo(s), a description, and the pet's name.

- [ ] FT-08: Favorites can be saved and viewed in a favorites list
  - Action: From a pet's profile, click "Save"/"Add to Favorites"; then open the Favorites list/page.
  - Expected: The pet appears in the favorites list; removing it takes it out of the list.

- [ ] FT-09: Adoption inquiry submits from the pet's page
  - Action: On a pet's profile, fill the inquiry form (name, email, message) with valid data and submit.
  - Expected: The form submits successfully and the inquiry is recorded/confirmed (no error).

## Constraint
- [ ] CS-01: Inquiry form blocks submission with empty required fields
  - Action: On the pet's inquiry form, leave required fields blank and click submit.
  - Expected: Submission is blocked and validation errors identify the missing required fields.

- [ ] CS-02: Inquiry form rejects invalid email format
  - Action: Enter an invalid email (e.g., "not-an-email") with other fields filled, then submit.
  - Expected: Submission is blocked with an email-format validation error.

- [ ] CS-03: No-match filter combination shows an empty state
  - Action: Apply conflicting filters so no default pet matches (e.g., species "Bird" or an impossible combination).
  - Expected: A clear "no pets found" message is shown; the page does not error or show a broken/blank list.

- [ ] CS-04: Pet cannot be favorited more than once
  - Action: Click "Add to Favorites" twice on the same pet's profile and view the Favorites list.
  - Expected: The pet appears exactly once in favorites; no duplicate entries.

## Interaction
- [ ] IX-01: Results list updates immediately when filters/search change
  - Action: With results showing, change a filter (e.g., toggle species) or edit the search text.
  - Expected: The matching-pets list refreshes to reflect the new criteria without a manual page reload.

- [ ] IX-02: Success feedback after inquiry submission
  - Action: Submit a valid adoption inquiry on a pet's page.
  - Expected: A visible success confirmation (toast/message, e.g., "Inquiry sent") appears after submission.

- [ ] IX-03: Favorite button reflects saved state visually
  - Action: Click the favorite control on a pet's profile, revisit the profile, and un-favorite it.
  - Expected: The control shows a distinct active/inactive state (e.g., filled vs. outline) and clicking it again removes the pet from favorites.

- [ ] IX-04: Multiple photos browsable on the pet profile
  - Action: Open the profile of a default pet that has more than one photo; click/switch through thumbnails or gallery arrows.
  - Expected: Each selection changes the main displayed photo.

## Content
- [ ] CT-01: Pet cards display complete key information
  - Action: Inspect cards in the default results list.
  - Expected: Each card shows the pet's photo, name, species, age, size, and shelter name — none missing or placeholder ("Lorem ipsum").

- [ ] CT-02: Profile photos and description are relevant to the pet
  - Action: Open 2–3 pet profiles of different species (e.g., a dog and a cat).
  - Expected: Photos depict an animal of that pet's species, and the description matches the pet shown in the list (name/species consistent).

- [ ] CT-03: Shelter attribution spans multiple shelters
  - Action: Browse the default listings and profiles.
  - Expected: Pets are drawn from multiple distinct shelters, and each profile/listing names a specific shelter (not a single generic source).