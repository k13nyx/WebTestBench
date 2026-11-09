# Test Result

## Functionality

- [X] FT-01: Search returns adoptable pets from multiple shelters
  - Action: Enter a valid search term that matches default adoptable pets, then submit the search.
  - Expected: The results list displays matching adoptable pets and includes pets attributed to more than one shelter when matching data exists.

- [X] FT-02: Filters find pets by all supported criteria
  - Action: Apply the **Species**, **Age range**, **Size**, **Good with kids**, and **Good with other pets** filters using values represented in the default data.
  - Expected: The results list updates to show only pets satisfying every selected filter.

- [ ] FT-03: Matching pets appear in a clear results list
  - Action: Perform a search or apply at least one filter.
  - Expected: Each result clearly displays the pet’s name, species, age, size, shelter, and an option to view details.
  - Bug Report:
    - Issue: Missing shelter information on result cards
    - Actual: Result cards display the pet’s name, species, age, size, location, and a clickable card, but do not display the shelter name.

- [ ] FT-04: Results can be sorted by relevance or time listed
  - Action: Select **Relevance** from the **Sort by** control, then select **Time listed**.
  - Expected: The list order changes according to the selected sort option, and the selected option remains visible.
  - Bug Report:
    - Issue: Missing Time listed sort option
    - Actual: The sort control provides “Relevance,” “Newest First,” “Oldest First,” and “Name A-Z,” but no “Time listed” option.

- [X] FT-05: User can open a pet profile
  - Action: Select a pet from the search results.
  - Expected: A detail page opens for the selected pet and identifies the same pet shown in the results.

- [X] FT-06: User can save and access favorite pets
  - Action: Select **Save favorite** for a pet, then open the **Favorites** list.
  - Expected: The selected pet appears in the Favorites list once and can be opened from that list.

- [X] FT-07: User can send an adoption inquiry from a pet profile
  - Action: Open a pet profile, complete the inquiry fields such as **Name**, **Email**, and **Message**, then select **Send inquiry**.
  - Expected: The inquiry is submitted for the pet whose profile is open.

## Constraint

- [X] CS-01: Combined filters exclude pets that violate any selected criterion
  - Action: Select a species, age range, size, **Good with kids**, and **Good with other pets** filter combination.
  - Expected: No displayed pet falls outside any selected criterion.

- [ ] CS-02: Required inquiry fields prevent incomplete submission
  - Action: Leave each required field in the adoption inquiry form empty and select **Send inquiry**.
  - Expected: The form is not submitted, and each missing required field is identified for correction.
  - Bug Report:
    - Issue: Required-field feedback is incomplete
    - Actual: Submission is prevented and the browser focuses the first empty field, but the form does not visibly identify all missing required fields at the same time.

- [X] CS-03: Invalid email input prevents inquiry submission
  - Action: Enter an invalid email format in the **Email** field, complete the other required fields, and select **Send inquiry**.
  - Expected: The inquiry is not submitted, and the Email field displays a validation message.

- [X] CS-04: No-match searches do not display unrelated pets
  - Action: Enter a search term or filter combination that matches no default pets.
  - Expected: The results area displays a clear no-results state and does not show pets that fail the search criteria.

- [X] CS-05: Clearing filters restores the available results
  - Action: Apply multiple filters, then select **Clear filters** or remove every active filter.
  - Expected: All filter controls return to their unselected state and the available unfiltered pet results are restored.

## Interaction

- [X] IX-01: Search and filter changes update the results state
  - Action: Apply a filter, remove it, and apply a different filter.
  - Expected: The results list refreshes after each change, and the active filter controls visibly reflect the current selections.

- [X] IX-02: Favorite state toggles correctly
  - Action: Select **Save favorite** for a pet, then select the same control again.
  - Expected: The control changes to the saved state after the first selection and returns to the unsaved state after the second selection.

- [X] IX-03: Successful inquiry submission provides confirmation
  - Action: Submit an adoption inquiry with valid values.
  - Expected: A visible confirmation states that the adoption inquiry was sent successfully.

- [X] IX-04: Pet profile photo controls work
  - Action: On a pet profile with multiple photos, select each available thumbnail or next/previous photo control.
  - Expected: The main displayed photo changes to the selected pet photo without leaving the profile.

## Content

- [ ] CT-01: Pet results contain relevant and consistent information
  - Action: Compare a pet card with its corresponding detail profile.
  - Expected: The pet name, species, age, size, shelter, and compatibility information are relevant to the same animal and do not conflict.
  - Bug Report:
    - Issue: Shelter name missing from pet result cards
    - Actual: The pet card and detail profile match for the pet’s name, species, age, and size, but the card shows only the shelter location and does not identify the associated shelter by name.

- [X] CT-02: Pet profiles contain usable photos and descriptions
  - Action: Open several pet profiles from the results list.
  - Expected: Each profile displays at least one relevant pet photo and a readable description specific to that pet.

- [X] CT-03: Favorites identify the correct saved pets
  - Action: Save multiple different pets and open the **Favorites** list.
  - Expected: Each saved entry shows the correct pet name and photo or identifying details, with no unrelated entries or duplicate entries.

- [X] CT-04: Inquiry form identifies the selected pet
  - Action: Open an inquiry form from a pet profile.
  - Expected: The form clearly identifies the pet and, when provided, the associated shelter so the inquiry context is unambiguous.