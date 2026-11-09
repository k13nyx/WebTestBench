# Test Checklist

## Functionality
- [ ] FT-01: Browse default pet listing from multiple shelters
  - Action: Open the homepage / pet listing page without applying any filters.
  - Expected: A list of adoptable pets is displayed, each showing the pet's name, photo, species, and the shelter it belongs to; pets from more than one shelter appear.

- [ ] FT-02: Search pets by keyword
  - Action: Type an existing pet's name (or species keyword) into the "Search" input and submit the search.
  - Expected: The list updates to show only pets matching the keyword, and the matched pet is visible.

- [ ] FT-03: Filter pets by species
  - Action: Select a single species option (e.g., "Dog") in the filter panel and apply it.
  - Expected: Only pets of the selected species are shown; all other species are excluded.

- [ ] FT-04: Filter pets by age range
  - Action: Apply an age range filter (e.g., "0–2 years") and inspect the results.
  - Expected: Every listed pet's age falls within the selected range; pets outside the range are excluded.

- [ ] FT-05: Filter pets by size
  - Action: Apply a size filter (e.g., "Small") and inspect the results.
  - Expected: Every listed pet matches the selected size; other sizes are excluded.

- [ ] FT-06: Filter by compatibility (good with kids / good with other pets)
  - Action: Apply the "Good with kids" filter, then the "Good with other pets" filter, and inspect results after each.
  - Expected: With each filter active, only pets marked as compatible with kids (or with other pets) are shown.

- [ ] FT-07: Sort pets by time listed
  - Action: On the filtered/unfiltered list, switch the sort option from "Relevance" to "Time listed" (newest first).
  - Expected: The list reorders so the most recently listed pets appear first; switching back to "Relevance" restores the relevance-based order.

- [ ] FT-08: Open a pet's detailed profile
  - Action: Click a pet card in the list to open its profile page.
  - Expected: The profile opens showing the pet's name, one or more photos, a text description, species/age/size details, and its shelter name.

- [ ] FT-09: Save a pet to favorites and view the favorites list
  - Action: On a pet's card or profile, click the "Save to favorites" (heart) button, then open the "Favorites" list.
  - Expected: The pet appears in the favorites list, and clicking it navigates back to that pet's profile.

- [ ] FT-10: Submit an adoption inquiry from a pet's page
  - Action: On a pet's profile, fill the adoption inquiry form (name, email, message) and click "Submit".
  - Expected: The inquiry is submitted successfully and the user sees a confirmation (see IX-01).

## Constraint
- [ ] CS-01: Combined filters return only pets matching ALL criteria
  - Action: Apply multiple filters at once (e.g., species "Cat" + size "Medium" + "Good with kids") and inspect the results.
  - Expected: Only pets satisfying every selected filter are shown; pets failing any one criterion are excluded.

- [ ] CS-02: Empty result set shows a clear "no matches" state
  - Action: Apply a filter combination that matches no pets (e.g., search a nonexistent name).
  - Expected: The list shows an explicit "No pets match your search" message (or equivalent) rather than a blank/broken page.

- [ ] CS-03: Adoption inquiry form cannot be submitted with empty required fields
  - Action: On a pet's page, leave required fields (name, email, message) empty and click "Submit".
  - Expected: Submission is blocked and validation messages identify the missing required fields; no inquiry is sent.

- [ ] CS-04: A pet cannot be added to favorites twice
  - Action: Click the "Save to favorites" button on the same pet two or more times.
  - Expected: The pet appears only once in the favorites list (no duplicate entries).

## Interaction
- [ ] IX-01: Adoption inquiry submission shows success feedback
  - Action: Submit a completed adoption inquiry form on a pet's page.
  - Expected: A visible success message or toast (e.g., "Your inquiry has been sent") appears and the form clears or confirms.

- [ ] IX-02: Favorite button reflects saved/unsaved state
  - Action: Click the favorite (heart) button on a pet, then click it again.
  - Expected: The button visibly toggles between saved (e.g., filled heart) and unsaved (e.g., outlined heart) states, and the favorites list updates accordingly.

- [ ] IX-03: Search/filter changes update the list and result count immediately
  - Action: Apply a species filter, then clear it.
  - Expected: The pet list and the displayed result count refresh to reflect the filtered and unfiltered states without errors.

## Content
- [ ] CT-01: Pet photos are relevant and load correctly
  - Action: Browse the pet list and several pet profile pages, checking each pet's image(s).
  - Expected: Every pet displays an actual photo of that animal (matching its listed species), with no broken image icons or unrelated placeholder images.

- [ ] CT-02: Pet descriptions are relevant to the pet
  - Action: Read the description text on 2–3 pet profile pages.
  - Expected: Each description refers to that specific pet (correct name/species, temperament, adoption-related info) and contains no lorem-ipsum or off-theme content.

- [ ] CT-03: Shelter attribution is present and consistent
  - Action: Compare the shelter name shown on a pet's list card with the shelter name on that pet's profile page.
  - Expected: Both display the same valid shelter name (a real shelter, not a placeholder), and listed pets collectively come from multiple distinct shelters.