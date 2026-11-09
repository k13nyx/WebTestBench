# Test Result

## Functionality
- [X] FT-01: Search adoptable animals by keyword
  - Action: Type a search term (e.g., "dog" or a pet name) into the search box and submit.
  - Expected: The list updates to show only pets matching the search term.
- [X] FT-02: Filter by species
  - Action: Select a species filter (e.g., "Dog").
  - Expected: Only pets of the selected species appear in the list.
- [X] FT-03: Filter by age range
  - Action: Select an age range filter (e.g., "Puppy/Kitten (< 1 year)").
  - Expected: Only pets within that age range appear in the list.
- [X] FT-04: Filter by size
  - Action: Select a size filter (e.g., "Small").
  - Expected: Only pets of the selected size appear in the list.
- [X] FT-05: Filter by "good with kids"
  - Action: Enable the "Good with kids" filter.
  - Expected: Only pets flagged as good with kids appear in the list.
- [X] FT-06: Filter by "good with other pets"
  - Action: Enable the "Good with other pets" filter.
  - Expected: Only pets flagged as good with other pets appear in the list.
- [X] FT-07: Sort the result list
  - Action: Select "Relevance" and then "Time listed" in the sort control.
  - Expected: Each selection reorders the list accordingly, with "Time listed" showing newest entries first.
- [X] FT-08: Open a detailed pet profile
  - Action: Click a pet in the result list.
  - Expected: A detailed profile page opens showing the pet's photos and a written description.
- [X] FT-09: Save a pet to favorites
  - Action: Click the save/favorite control on a pet.
  - Expected: The pet is added to the favorites list.
- [X] FT-10: View the favorites list
  - Action: Navigate to the favorites page/list.
  - Expected: All previously saved pets are listed, each with its name and photo.
- [X] FT-11: Send an adoption inquiry
  - Action: On a pet's profile page, fill the adoption inquiry form with valid details and submit it.
  - Expected: The inquiry is submitted successfully for that pet.

## Constraint
- [X] CS-01: Inquiry form rejects empty required fields
  - Action: Leave one or more required fields (e.g., name, email, message) blank and click submit.
  - Expected: The form does not submit and an error is indicated on the blank required field(s).
- [X] CS-02: Multiple active filters combine correctly
  - Action: Apply species + age range + size + "Good with kids" simultaneously.
  - Expected: Every listed pet satisfies ALL active filters; no pet missing any selected criterion is shown.

## Interaction
- [X] IX-01: Result list responds immediately to filter/sort changes
  - Action: Change any filter or the sort option with a result list already displayed.
  - Expected: The list and the displayed result count update immediately without a page reload.
- [X] IX-02: Success confirmation after inquiry submission
  - Action: Submit a valid adoption inquiry form.
  - Expected: A clear success confirmation (e.g., "Inquiry sent" message) is displayed.
- [X] IX-03: Favorite control reflects saved state
  - Action: Click the save/favorite control on a pet, then revisit that pet.
  - Expected: The control visibly changes to a saved/filled state and stays saved.
- [X] IX-04: No-match state is displayed
  - Action: Apply filters that no pet satisfies (e.g., a rare filter combination).
  - Expected: An explicit "no results" message is shown instead of an empty/broken list.

## Content
- [X] CT-01: Pet photos are present and relevant
  - Action: Browse the result list and open several pet profiles.
  - Expected: Each pet shows at least one photo that clearly depicts that pet; no broken or placeholder images.
- [X] CT-02: Pet profile content is relevant and complete
  - Action: Open a pet's detailed profile.
  - Expected: The description includes relevant details for that pet — name, breed/type, age, size, shelter, and kid/other-pet compatibility.
- [X] CT-03: Shelter attribution and multi-shelter coverage
  - Action: Review pets in the list and their profiles.
  - Expected: Each pet displays the name of its originating shelter, and pets from more than one shelter are represented.
