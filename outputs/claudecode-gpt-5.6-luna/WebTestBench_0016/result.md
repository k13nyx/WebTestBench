# Test Result

## Functionality

- [ ] FT-01: Author can publish articles for travel stories, detailed recipes, and self-improvement guides.
  - Action: Open the author editor and publish an available draft for each supported content type.
  - Expected: Each article is published successfully and appears in the public blog.
  - Bug Report:
    - Issue: Author editor unavailable
    - Actual: Navigating to `/admin` displays a 404 “Oops! Page not found” page, so no drafts could be opened or published.

- [X] FT-02: Published articles can be organized using categories, tags, and series.
  - Action: Open a published article and inspect its displayed category, tags, and series assignment.
  - Expected: The assigned category, tags, and series are shown and link to the corresponding content listings.

- [X] FT-03: Visitors can browse articles by topic/category.
  - Action: Select a category such as “Travel,” “Recipes,” or “Self-Improvement.”
  - Expected: The page lists only articles assigned to the selected category.

- [X] FT-04: Visitors can browse articles by series.
  - Action: Select a displayed series name.
  - Expected: The page lists the articles belonging to that series in the correct order.

- [ ] FT-05: Visitors can browse articles by publication date.
  - Action: Select a displayed publication date or date-based browse option.
  - Expected: The page lists articles matching the selected date.
  - Bug Report:
    - Issue: No date-based browse control
    - Actual: The archive shows publication dates as text, but the dates are not selectable links or controls, and no other date-based browse option is available.

- [X] FT-06: Visitors can search articles by keywords or phrases.
  - Action: Enter a keyword and then an exact multi-word phrase in the search field, and submit each search.
  - Expected: Each results page lists articles whose searchable content matches the submitted term or phrase.

- [ ] FT-07: The home page highlights featured and most recent posts.
  - Action: Open the home page and inspect the “Featured” and “Most Recent” sections.
  - Expected: Featured articles appear in the featured section, and the most recently published articles appear in descending date order.
  - Bug Report:
    - Issue: Required home sections are missing or incorrectly labeled
    - Actual: The home page displays the top articles and a “Recent Stories” section, but it does not contain sections labeled “Featured” and “Most Recent.” The expected section structure is not present.

- [ ] FT-08: Visitors can browse the archive by month and year.
  - Action: Open the archive and select an available month/year entry.
  - Expected: The archive displays the articles published during the selected month and year.
  - Bug Report:
    - Issue: Month/year archive entries are not selectable
    - Actual: The archive groups articles under “2024,” “March,” “February,” and “January,” but the month/year headings are static text with no selectable controls or filtered archive view.

- [X] FT-09: Each post preview links to its full article.
  - Action: Select the title, image, or “Read More” link on a post preview.
  - Expected: The corresponding full article page opens.

- [X] FT-10: Each article page displays related-post suggestions.
  - Action: Open a full article and inspect its related-post section.
  - Expected: Related article suggestions are displayed and each suggestion opens the corresponding article.

- [X] FT-11: Visitors can submit comments on an article.
  - Action: Enter valid commenter details and comment text in the article’s comment form, then select “Post Comment” or the equivalent submit control.
  - Expected: The comment is accepted and appears in the article’s comments section.

- [X] FT-12: Visitors can add a simple reaction or “like” to an article.
  - Action: Select the article’s like/reaction control.
  - Expected: The reaction is recorded and the displayed reaction count or active state updates.

## Constraint

- [X] CS-01: Article metadata remains consistent with its assigned category, tags, and series.
  - Action: Open an article from its category, tag, and series listings.
  - Expected: The same article appears in all listings corresponding to its displayed assignments, without unrelated articles being included.

- [ ] CS-02: Empty or unmatched searches do not display unrelated articles.
  - Action: Submit the search form with no text, then submit a phrase that does not match any article.
  - Expected: Empty search is rejected or prompts for a query, and an unmatched query shows a clear “no results” state with no unrelated posts.
  - Bug Report:
    - Issue: Empty search is not rejected or prompted
    - Actual: Submitting an empty search returns the default listing of all 8 articles instead of rejecting the search or prompting for a query. An unmatched query does correctly display “0 articles found” and “No articles found matching your criteria.”

- [X] CS-03: A visitor cannot submit a blank comment.
  - Action: Leave the comment text empty and select the comment submission control.
  - Expected: Submission is blocked and a validation message identifies the required comment field.

## Interaction

- [ ] IX-01: Category, series, date, archive, and search selections update the displayed results.
  - Action: Apply each available browse or search control from a listing page.
  - Expected: The page visibly changes to the selected result set and identifies the active filter or query.
  - Bug Report:
    - Issue: Date and month/year archive filtering unavailable
    - Actual: Category, series, tag, and search selections update their result sets, but publication dates and month/year archive headings are not selectable controls, so those result sets cannot be applied.

- [X] IX-02: The like control provides immediate feedback after activation.
  - Action: Select the like/reaction control on an article.
  - Expected: The control visibly changes state and the updated reaction count remains displayed after the page finishes loading.

- [X] IX-03: Comment submission provides clear completion feedback.
  - Action: Submit a valid comment.
  - Expected: The new comment is visibly displayed or a clear confirmation indicates that it was posted successfully.

## Content

- [X] CT-01: Published content is relevant to the blog’s stated themes.
  - Action: Review the default published articles and their previews.
  - Expected: Articles contain travel stories, detailed recipes, or self-improvement guides; unrelated content is not presented as blog content.

- [X] CT-02: Post previews contain accurate identifying information.
  - Action: Review previews on the home page, browse pages, search results, and archive pages.
  - Expected: Each preview shows the correct article title, short summary, and publication date matching its full article.

- [X] CT-03: Article pages display complete article content and metadata.
  - Action: Open representative travel, recipe, and self-improvement articles.
  - Expected: Each page displays the full article text, title, publication date, and its applicable category, tags, and series.