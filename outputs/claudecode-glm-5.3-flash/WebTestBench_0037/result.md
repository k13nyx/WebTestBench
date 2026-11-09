All test items have been executed. Whiskers' detail page confirmed a real bug: it displays both compatibility chips ("Good with kids", "Good with other pets") despite Whiskers failing the kids filter, having no Kid-friendly card badge, and her own description stating she "prefers a quiet home without young children."

# Test Result

## Functionality

- [X] FT-01: Search pets by keyword
  - Action: Enter a search term (e.g., a pet name like "Buddy") in the search box and submit.
  - Expected: The results list shows only pets whose name/description matches the term; non-matching pets are hidden.
  - (Verified: searching "Max" returned only Max — "1 adorable pets available for adoption"; searching breed term "Bulldog" returned only Bella; clearing restored all 12 pets.)

- [X] FT-02: Filter by species
  - Action: Select a species filter (e.g., "Dog") in the filter panel.
  - Expected: Only pets of that species remain listed; pets of other species disappear.
  - (Verified: "Dogs" → Luna, Max, Duke, Bella, Charlie (5 dogs); "Cats" → Oliver, Whiskers, Mochi, Shadow (4 cats).)

- [X] FT-03: Filter by age range and size
  - Action: Apply an age range filter (e.g., Puppy/Young) and a size filter (e.g., Small) together.
  - Expected: Only pets matching both criteria are listed; combined filters narrow results cumulatively.
  - (Verified: "Young (1-3 years)" + "Small" → only Biscuit (rabbit, small, 1 yr) and Sunny (bird, small, 2 yrs).)

- [X] FT-04: Filter by compatibility (good with kids / other pets)
  - Action: Toggle "Good with kids" and/or "Good with other pets" filters.
  - Expected: Only pets marked as compatible with the selected options are shown.
  - (Verified: "Good with kids" → 11 pets, correctly excluding Whiskers who has no Kid-friendly card badge; adding "Good with other pets" → 9 pets; other-pets alone → 10 pets. Filter results consistently match the pets' card badges. Note: Sunny's *detail page* claims "Good with other pets" while the filter data excludes her — that display inconsistency is reported under CT-02.)

- [X] FT-05: Sort results by relevance and by time listed
  - Action: Open the sort control, select "Relevance", then select "Time listed" (newest first).
  - Expected: Result order changes accordingly; with "Time listed", the most recently added pet appears first.
  - (Verified: sort dropdown offers "Relevance", "Newest First", "Name A-Z". Relevance order: Luna, Oliver, Max, Whiskers…; "Newest First" reordered to Mochi, Cinnamon, Duke, Max… with oldest (Whiskers, Shadow) last; "Name A-Z" sorted alphabetically; switching back to Relevance restored the original order.)

- [X] FT-06: Open a detailed pet profile
  - Action: Click a pet card in the results list.
  - Expected: A detail page opens for that pet showing its name, photos, and a written description.
  - (Verified: clicking Luna's card opened /pets/pet-1 with name "Luna", photo gallery, and "About Luna" description.)

- [X] FT-07: View multiple photos on the profile
  - Action: On a pet's detail page with more than one photo, navigate through the photo gallery (e.g., thumbnails or next arrow).
  - Expected: Different photos of the pet are displayed as the gallery is navigated.
  - (Verified: Luna's profile has a main photo + 2 thumbnails; clicking "Thumbnail 2" switched the main image from "Luna - Photo 1" (photo-1552053831…) to "Luna - Photo 2" (photo-1587300003388…).)

- [X] FT-08: Save a pet to favorites
  - Action: On a pet card or its detail page, click the favorite/save button (e.g., heart icon).
  - Expected: The pet is marked as saved (icon state changes) and appears in the favorites list.
  - (Verified: heart icon gains `fill-accent text-accent` styling when saved; navbar Favorites badge showed "2"; favorites page listed Luna and Max.)

- [X] FT-09: View and manage the favorites list
  - Action: Open the favorites page/list containing previously saved pets, then remove one pet from it.
  - Expected: The list shows the saved pets with correct names; after removal, that pet disappears from the list.
  - (Verified: /favorites showed "2 pets saved to your favorites" — Luna, Max; after clicking Max's heart, list showed "1 pet saved" with only Luna.)

- [X] FT-10: Submit an adoption inquiry form
  - Action: On a pet's detail page, fill in the inquiry form fields (e.g., name, email, message) with valid values and click the submit button (e.g., "Send Inquiry").
  - Expected: The inquiry is accepted and a confirmation is shown (e.g., success message "Your inquiry has been sent").
  - (Verified: on Luna's page filled name/email/phone/message and clicked "Send Inquiry" — page showed "Inquiry Submitted! Happy Tails Rescue has received your inquiry about Luna…" plus toast "Inquiry Sent! Happy Tails Rescue will contact you soon about Luna.")

## Constraint

- [X] CS-01: Submit inquiry with empty required fields
  - Action: Click the inquiry submit button leaving required fields (e.g., name, email) blank.
  - Expected: Submission is blocked and a validation error message is displayed next to the empty fields; no success message appears.
  - (Verified: name/email/message are `required` HTML fields; empty submit was blocked (URL unchanged, no success message) and per-field native validation messages fired, e.g. "Please fill out this field.")

- [X] CS-02: Invalid email rejected in inquiry form
  - Action: Enter an invalid email (e.g., "not-an-email") in the inquiry form and submit.
  - Expected: An email format error is shown and the form is not submitted.
  - (Verified: with email "not-an-email" the field is invalid ("Please include an '@' in the email address…"); submission blocked, no success message.)

- [X] CS-03: Filters combine without conflicts
  - Action: Apply filters that match no pets (e.g., species "Cat" + size "Large" + age "Puppy" if none exist).
  - Expected: An empty-state message (e.g., "No pets match your filters") is shown instead of unrelated pets or an error.
  - (Verified: Cats + Large + Baby → "0 adorable pets available for adoption" and empty state "No pets found — Try adjusting your search or filters to find more pets." with a Clear all filters button; no errors.)

- [X] CS-04: Clearing filters restores full list
  - Action: After applying filters that narrow results, click "Clear filters" / "Reset".
  - Expected: All default pets are listed again and sort selection remains functional.
  - (Verified: "Clear all filters" restored all 12 pets; sort dropdown still worked afterward — Relevance, Newest First, and Name A-Z each reordered the full list.)

## Interaction

- [X] IX-01: Filter or search updates results immediately
  - Action: Change a filter (or type in the search box) and observe the results area.
  - Expected: The pet list updates to reflect the new criteria without requiring a full page reload or error.
  - (Verified: every search keystroke-submit and checkbox toggle updated the list and result count in-place on /pets with no page reload (URL unchanged) and no errors.)

- [X] IX-02: Favorites toggle gives visible feedback
  - Action: Click the favorite button on a pet, then click it again.
  - Expected: The icon/state toggles visibly (e.g., filled ↔ unfilled heart) and the pet is added, then removed, from favorites.
  - (Verified: on Oliver's card, heart class toggled `text-muted-foreground` → `fill-accent text-accent` on first click and back on second click; navbar badge count changed accordingly.)

- [X] IX-03: Inquiry submission shows success feedback
  - Action: Submit a valid inquiry form.
  - Expected: A visible success indication (toast/message such as "Inquiry sent") appears; the form does not silently fail.
  - (Verified: valid submission produced both an inline "Inquiry Submitted!" confirmation section and a toast "Inquiry Sent! Happy Tails Rescue will contact you soon about Luna.")

- [X] IX-04: Pet cards are clickable with hover affordance
  - Action: Hover over a pet card in the results list, then click it.
  - Expected: The card shows a hover indication (e.g., highlight/cursor pointer) and clicking opens that pet's profile.
  - (Verified: card cursor is `pointer` and hovering triggers visible feedback — pet photo scales up (transform matrix 1.1) and the name color changes; clicking opened the correct profile page.)

## Content

- [X] CT-01: Pet photos are relevant and load correctly
  - Action: Browse the results list and open several pet detail pages.
  - Expected: Every card and profile displays a pet photo relevant to that animal (species matches the pet), with no broken-image placeholders.
  - (Verified: all 12 card images have `naturalWidth > 0` (loaded), each pet has a distinct photo with matching alt text; detail pages for Luna, Sunny, and Whiskers all show 3 fully-loaded photos (main + 2 thumbnails) with no broken-image placeholders.)

- [ ] CT-02: Profile details are complete and consistent
  - Action: Open a pet's detail page and compare its info with its card in the list.
  - Expected: The profile shows the pet's name, species, age, size, shelter source, kid/other-pet compatibility, and a non-empty description consistent with the card data.
  - Bug Report:
    - Issue: Incorrect data display — profile compatibility information contradicts the pet's actual data
    - Actual: The detail page's "Compatibility" section renders "Good with kids" AND "Good with other pets" for every pet regardless of its actual data. Verified with Whiskers (/pets/pet-4): her card shows no "Kid-friendly" badge, the "Good with kids" filter correctly excludes her (11 of 12 pets match), and her own description says "She prefers a quiet home without young children" — yet her profile displays the "Good with kids" compatibility chip. The same contradiction appears on Sunny (/pets/pet-8), whose profile claims "Good with other pets" while the compatibility filter excludes her and her description says she "needs a home without cats or other predatory pets." All other fields (name, species, age, size, gender, shelter name/location/contact, non-empty description) are complete and consistent with the cards.