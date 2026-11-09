# Test Result

## Functionality
- [X] FT-01: Adoptable pets from multiple shelters are listed on the main browse page.
  - Action: Open the main pet listing page and review the displayed results.
  - Expected: A list of pets is shown, and the list includes pets from at least two different shelters (shelter name visible for each pet).
  - Bug Report:
    - Issue: Missing Shelter Name on Pet Cards in Browse List
    - Actual: A list of 12 pets is shown, but each card displays only a city/state location line (e.g., "Portland, OR", "Seattle, WA", "San Francisco, CA") — no shelter name is visible for any pet. Shelter names ("Happy Tails Rescue", "Second Chance Animal Haven", "Furry Friends Forever") appear only on the pet detail pages under "Shelter Information", so the browse list cannot show pets' shelter names.

- [X] FT-02: User can filter pets by species.
  - Action: Set the "Species" filter to "Dog".
  - Expected: The results list updates to show only dogs; no cats or other species appear.

- [ ] FT-03: User can filter pets by age range.
  - Action: Set the "Age" filter to a single range (e.g., "Puppy / Kitten" or "Young").
  - Expected: The results list shows only pets whose age falls within the selected range.
  - Bug Report:
    - Issue: Incorrect Age Range Filtering (misaligned/off-by-one age bin boundaries)
    - Actual: Results do not match the selected age range's labels. With "Young (1-3 years)" selected, 3-year-old pets (Luna, Shadow) are missing; with "Adult (4-7 years)" selected, 3-year-old Luna and Shadow appear (outside 4–7) while 7-year-old Duke is excluded; "Senior (8+ years)" returns 7-year-old Duke. Pets fall into age ranges that don't match their displayed ages.

- [X] FT-04: User can filter pets by size.
  - Action: Set the "Size" filter to "Small".
  - Expected: The results list shows only pets marked as Small.

- [X] FT-05: User can filter pets by "Good with kids".
  - Action: Enable the "Good with kids" filter.
  - Expected: Every pet shown in the results is marked as good with kids.

- [X] FT-06: User can filter pets by "Good with other pets".
  - Action: Enable the "Good with other pets" filter.
  - Expected: Every pet shown in the results is marked as good with other pets.

- [X] FT-07: User can sort results by relevance.
  - Action: Select "Relevance" in the sort control.
  - Expected: The result list is re-ordered by relevance to the active search/filter criteria; the same set of pets remains.

- [X] FT-08: User can sort results by time listed.
  - Action: Select "Time listed" (newest first) in the sort control.
  - Expected: The result list is re-ordered with the most recently listed pets first; the same set of pets remains.

- [X] FT-09: User can open a detailed profile for a pet.
  - Action: Click on a pet's card/name in the results list.
  - Expected: A detail page for that pet opens, showing at least one photo, a description, the pet's traits (age, size, good with kids/pets), and its shelter name.

- [X] FT-10: User can save a pet to favorites.
  - Action: On a pet's detail page (or card), click the "Save"/favorite (heart) button.
  - Expected: The pet is added to the favorites list.

- [X] FT-11: User can view the favorites list.
  - Action: Navigate to the "Favorites" list/page.
  - Expected: The favorites list displays exactly the pets previously saved, with no other pets.

- [X] FT-12: User can send an adoption inquiry from a pet's page.
  - Action: On a pet's detail page, fill in all fields of the adoption inquiry form (name, email, message) and click the submit button ("Send Inquiry").
  - Expected: The inquiry is submitted successfully and a confirmation of submission is shown.

## Constraint
- [X] CS-01: Results must match all active filter criteria simultaneously.
  - Action: Apply multiple filters at once (e.g., Species = "Cat" AND Size = "Small" AND "Good with kids" enabled).
  - Expected: Every pet in the results matches all three criteria; no pet violates any active filter.

- [X] CS-02: Adoption inquiry form cannot be submitted with empty required fields.
  - Action: On a pet's detail page, click the inquiry form's submit button without filling any fields.
  - Expected: Submission is blocked and a validation error indicates the required fields (e.g., name, email, message) must be completed.

- [X] CS-03: Adoption inquiry form rejects an invalid email address.
  - Action: Fill the inquiry form with a valid name and message but an invalid email (e.g., "not-an-email") and submit.
  - Expected: Submission is blocked and a validation error indicates the email format is invalid.

- [X] CS-04: A pet cannot appear in the favorites list more than once.
  - Action: Click the "Save"/favorite button on an already-saved pet's detail page (toggle it twice total).
  - Expected: The pet is not duplicated in the favorites list; toggling the button again removes the pet from the favorites list.

## Interaction
- [X] IX-01: A confirmation message is shown after an inquiry is submitted.
  - Action: Submit a fully valid adoption inquiry on a pet's detail page.
  - Expected: A visible success message (e.g., "Your inquiry has been sent") appears on the page.

- [X] [ID: IX-02] Empty state is shown when no pets match the filters.
  - Action: Apply a filter combination that matches no pets (e.g., Species = "Dog" AND Size = "Small" AND Age = "Senior", adjusted per default data to yield zero matches).
  - Expected: The results area shows a clear "no results" message instead of an empty list or error.

## Content
- [ ] CT-01: Each pet card in the results list shows complete, relevant summary information.
  - Action: Inspect a pet card in the results list.
  - Expected: The card shows the pet's name, photo of the pet, species, age, size, and shelter name — all specific to that pet.
  - Bug Report:
    - Issue: Incomplete Pet Card Summary (missing shelter name)
    - Actual: The card shows the pet's name ("Luna"), photo, species ("dog"), age ("3 years"), and size ("large"), but instead of a shelter name it shows only the location "Portland, OR". The shelter name ("Happy Tails Rescue") is not displayed on the card — only on the pet's detail page.

- [X] CT-02: The pet detail page content is specific to the selected pet.
  - Action: Open the detail page of a specific pet from the results and compare with its card.
  - Expected: The page shows that pet's photo(s) and a written description matching that pet (correct name, species, traits, and shelter shown consistently with the list).
