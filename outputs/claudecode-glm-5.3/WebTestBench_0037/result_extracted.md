# Test Result

## Functionality

- [ ] FT-01: Browse default pet listing from multiple shelters
  - Action: Open the homepage / pet listing page without applying any filters.
  - Expected: A list of adoptable pets is displayed, each showing the pet's name, photo, species, and the shelter it belongs to; pets from more than one shelter appear.
  - Bug Report:
    - Issue: Missing shelter attribution on pet listing cards
    - Actual: The listing page (`/pets`) shows 12 pets, each card displaying name, photo, species badge, breed, size, age, and only a city/state location (e.g., "Portland, OR" with a pin icon). No card shows the shelter's name. Shelter names (e.g., "Happy Tails Rescue" for Luna, Portland) appear only on the pet profile pages. Pets from more than one shelter are represented (3 distinct shelters verified via profiles: Happy Tails Rescue, Second Chance Animal Haven, Furry Friends Forever), but the card itself does not identify which shelter a pet belongs to.

- [X] FT-02: Search pets by keyword
  - Action: Type an existing pet's name (or species keyword) into the "Search" input and submit the search.
  - Expected: The list updates to show only pets matching the keyword, and the matched pet is visible.

- [X] FT-03: Filter pets by species
  - Action: Select a single species option (e.g., "Dog") in the filter panel and apply it.
  - Expected: Only pets of the selected species are shown; all other species are excluded.

- [ ] FT-04: Filter pets by age range
  - Action: Apply an age range filter (e.g., "0–2 years") and inspect the results.
  - Expected: Every listed pet's age falls within the selected range; pets outside the range are excluded.
  - Bug Report:
    - Issue: Age filter buckets misaligned with displayed pet ages
    - Actual: With "Young (1-3 years)" applied, the results (Oliver 2y, Max 1y, Biscuit 1y, Sunny 2y, Cinnamon 2y) are in range, but Luna and Shadow — displayed as "3 years" on their cards and "3 years old" on their profiles, i.e., within the labeled 1–3 range — are excluded. With "Adult (4-7 years)" applied, the results include Luna and Shadow (displayed age 3, outside 4–7) and exclude Duke (displayed "7 years"), who instead appears as the sole result under "Senior (8+ years)" despite being displayed as 7 years old. A pet displayed as "3 years old" is bucketed into "Adult (4-7 years)" and excluded from "Young (1-3 years)", and a pet displayed as "7 years old" is bucketed into "Senior (8+ years)" and excluded from "Adult (4-7 years)".

- [X] FT-05: Filter pets by size
  - Action: Apply a size filter (e.g., "Small") and inspect the results.
  - Expected: Every listed pet matches the selected size; other sizes are excluded.
  - (Verified: "Small" returned exactly Biscuit, Mochi, Sunny, Bella — the 4 small pets; result count updated to 4.)

- [X] FT-06: Filter by compatibility (good with kids / good with other pets)
  - Action: Apply the "Good with kids" filter, then the "Good with other pets" filter, and inspect results after each.
  - Expected: With each filter active, only pets marked as compatible with kids (or with other pets) are shown.
  - (Verified: "Good with kids" → 11 pets, excluding Whiskers whose profile shows an ✗ for "Good with kids"; "Good with other pets" → 10 pets, excluding Max and Sunny — Max's profile shows an ✗ for "Good with other pets". Filter results match the pets' actual compatibility marks.)

- [X] FT-07: Sort pets by time listed
  - Action: On the filtered/unfiltered list, switch the sort option from "Relevance" to "Time listed" (newest first).
  - Expected: The list reorders so the most recently listed pets appear first; switching back to "Relevance" restores the relevance-based order.
  - (Verified: "Newest First" reordered the 12 pets, e.g., Mochi first and the two oldest-listed pets — Whiskers and Shadow, "Listed about 2 years ago" — last; switching back to "Relevance" restored the original order pet-1 through pet-12.)

- [X] FT-08: Open a pet's detailed profile
  - Action: Click a pet card in the list to open its profile page.
  - Expected: The profile opens showing the pet's name, one or more photos, a text description, species/age/size details, and its shelter name.
  - (Verified on Luna's profile: name heading, main photo + 2 photo thumbnails, "About Luna" description, Age "3 years old" / Size "large" / species "dog", and shelter "Happy Tails Rescue".)

- [X] FT-09: Save a pet to favorites and view the favorites list
  - Action: On a pet's card or profile, click the "Save to favorites" (heart) button, then open the "Favorites" list.
  - Expected: The pet appears in the favorites list, and clicking it navigates back to that pet's profile.

- [X] FT-10: Submit an adoption inquiry from a pet's page
  - Action: On a pet's profile, fill the adoption inquiry form (name, email, message) and click "Submit".
  - Expected: The inquiry is submitted successfully and the user sees a confirmation (see IX-01).

## Constraint

- [X] CS-01: Combined filters return only pets matching ALL criteria
  - Action: Apply multiple filters at once (e.g., species "Cat" + size "Medium" + "Good with kids") and inspect the results.
  - Expected: Only pets satisfying every selected filter are shown; pets failing any one criterion are excluded.
  - (Verified: Cats → 4; + Medium → 3 (Oliver, Whiskers, Shadow); + Good with kids → 2 (Oliver, Shadow) — Whiskers correctly excluded for failing the kids criterion.)

- [X] CS-02: Empty result set shows a clear "no matches" state
  - Action: Apply a filter combination that matches no pets (e.g., search a nonexistent name).
  - Expected: The list shows an explicit "No pets match your search" message (or equivalent) rather than a blank/broken page.
  - (Verified: searching "Xyzzyq nonexistent pet" → count "0" and an explicit "No pets found — Try adjusting your search or filters to find more pets." panel with a "Clear all filters" button.)

- [X] CS-03: Adoption inquiry form cannot be submitted with empty required fields
  - Action: On a pet's page, leave required fields (name, email, message) empty and click "Submit".
  - Expected: Submission is blocked and validation messages identify the missing required fields; no inquiry is sent.
  - (Verified: with name/email/message empty, clicking "Send Inquiry" blocked submission, focus moved to the first invalid field, and each required input reported "Please fill out this field." via validation; no success toast or inquiry was sent.)

- [X] CS-04: A pet cannot be added to favorites twice
  - Action: Click the "Save to favorites" button on the same pet two or more times.
  - Expected: The pet appears only once in the favorites list (no duplicate entries).
  - (Verified: clicked the heart on Luna 3 times; the Favorites page displayed exactly one Luna entry — "1 pet saved to your favorites".)

## Interaction

- [X] IX-01: Adoption inquiry submission shows success feedback
  - Action: Submit a completed adoption inquiry form on a pet's page.
  - Expected: A visible success message or toast (e.g., "Your inquiry has been sent") appears and the form clears or confirms.
  - (Verified: toast "Inquiry Sent! Happy Tails Rescue will contact you soon about Luna." appeared, and the form was replaced by an "Inquiry Submitted!" confirmation panel.)

- [X] IX-02: Favorite button reflects saved/unsaved state
  - Action: Click the favorite (heart) button on a pet, then click it again.
  - Expected: The button visibly toggles between saved (e.g., filled heart) and unsaved (e.g., outlined heart) states, and the favorites list updates accordingly.
  - (Verified: saved state renders the heart with class `fill-accent text-accent` (filled/colored) and nav badge "1"; unsaved state renders `text-muted-foreground` (outlined/muted) and the badge disappears; favorites list updated on every toggle.)

- [X] IX-03: Search/filter changes update the list and result count immediately
  - Action: Apply a species filter, then clear it.
  - Expected: The pet list and the displayed result count refresh to reflect the filtered and unfiltered states without errors.
  - (Verified: applying "Dogs" instantly showed 5 results with count "5"; clearing it instantly restored all 12 with count "12"; search and other filters behaved the same with no errors.)

## Content

- [X] CT-01: Pet photos are relevant and load correctly
  - Action: Browse the pet list and several pet profile pages, checking each pet's image(s).
  - Expected: Every pet displays an actual photo of that animal (matching its listed species), with no broken image icons or unrelated placeholder images.
  - (Verified: all 12 listing images and all profile photos on 4 profile pages (Luna, Oliver, Whiskers, Max — each with a main photo + 2 thumbnails) loaded successfully — `naturalWidth > 0`, no broken images; each pet has a distinct Unsplash photo matching its species, e.g., dog photos for Luna/Max/Duke, cat photos for Oliver/Whiskers, rabbit photos for Biscuit/Cinnamon, bird photo for Sunny.)

- [X] CT-02: Pet descriptions are relevant to the pet
  - Action: Read the description text on 2–3 pet profile pages.
  - Expected: Each description refers to that specific pet (correct name/species, temperament, adoption-related info) and contains no lorem-ipsum or off-theme content.
  - (Verified on 4 profiles: Luna — "the sweetest girl… loves belly rubs, playing fetch… fully trained"; Oliver — "charming orange tabby… loves to chirp at birds… gets along great with other cats"; Whiskers — "beautiful Siamese mix with striking blue eyes… prefers a quiet home without young children but loves the company of other calm cats"; Max — "smart and energetic Border Collie… would do best as the only pet". All match each pet's name, species, and compatibility traits; no lorem-ipsum.)

- [ ] CT-03: Shelter attribution is present and consistent
  - Action: Compare the shelter name shown on a pet's list card with the shelter name on that pet's profile page.
  - Expected: Both display the same valid shelter name (a real shelter, not a placeholder), and listed pets collectively come from multiple distinct shelters.
  - Bug Report:
    - Issue: Shelter name missing on list cards — card/profile attribution inconsistent
    - Actual: The list card for Luna shows only the location "Portland, OR"; her profile shows the shelter name "Happy Tails Rescue" (Portland, OR). Likewise Oliver's card shows "Seattle, WA" while his profile shows "Second Chance Animal Haven". No listing card displays a shelter name at all, so the card and profile do not display the same shelter name. (The shelters themselves are valid and distinct — profiles confirm 3 shelters: Happy Tails Rescue, Second Chance Animal Haven, Furry Friends Forever — but only the location, not the shelter name, appears on cards.)
