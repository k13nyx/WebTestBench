# Test Checklist

## Functionality
- [ ] FT-01: New visitor can sign up and reach an authenticated session
  - Action: Open the site, click "Sign Up", submit a valid username, email and password
  - Expected: Account is created, user is logged in, and their own author dashboard/profile is reachable

- [ ] FT-02: Author can create a post written in Markdown and it renders
  - Action: Create a new post containing a heading, bullet list, inline code and a fenced code block, then save/publish
  - Expected: The post displays as rendered HTML (heading styled, list bulleted, code in monospace block), not raw Markdown syntax

- [ ] FT-03: Author can edit an existing post
  - Action: Open one of the author's own posts, click "Edit", change title and body text, save
  - Expected: The post detail page and profile listing show the updated title and body

- [ ] FT-04: Published post appears on the author's own profile page
  - Action: Publish a post, then open the author's profile page
  - Expected: The post is listed on the profile with title and preview, and links to the full post

- [ ] FT-05: A visitor can open and read any published post
  - Action: From the profile/post list, click a post title as a non-author visitor
  - Expected: The full post content opens on its own page and is readable without login prompts

- [ ] FT-06: Visitor can leave a comment under a post
  - Action: Open a post, type a comment in the comment field and submit
  - Expected: The comment is displayed beneath the post body, attributed to the commenter with a timestamp

- [ ] FT-07: Visitor can like a post and the count reflects it
  - Action: Click the "Like" button on a post, then reload the post page
  - Expected: The displayed like count increases by exactly 1 and persists after reload

- [ ] FT-08: Visitor can save a post to a personal list and find it again
  - Action: Click "Save"/bookmark on a post, then open the personal "Saved" list page
  - Expected: That post appears in the saved list and links back to the post

- [ ] FT-09: Author can attach custom tags when publishing
  - Action: Publish a post and enter/select custom tags such as "Technology", "Life", "Reading Notes"
  - Expected: The chosen custom tags are displayed on the post detail page and in the post's listing entry

- [ ] FT-10: System auto-generates intelligent tags from post content
  - Action: Publish a code-related article (Python snippets, frontend markup), then open its detail page
  - Expected: Intelligent tags (e.g. "Python", "Frontend Development") are generated automatically and shown distinctly from the author's custom tags, with no manual entry

- [ ] FT-11: Articles can be filtered by custom tag, intelligent tag, and both combined
  - Action: Apply the custom tag filter "Technology"; then apply intelligent tag "Python"; then apply both together
  - Expected: Each filter shows only matching articles; the combined filter shows only articles having BOTH "Technology" and "Python"

- [ ] FT-12: Frequently-used tag groups can be saved and re-applied
  - Action: With a combined tag filter active (e.g. "Technology + Python"), save it as a named tag group; clear filters, then click the saved group
  - Expected: The saved group appears in a tag-groups area and re-applies the exact same filter set with one click

- [ ] FT-13: Author backend shows per-tag statistics and a popularity report
  - Action: As the author, open the backend/analytics page and view stats per tag, then click "Generate tag popularity report"
  - Expected: Page views, like counts and comment counts are listed per tag, and a popularity report is produced ranking tags with those figures

## Constraint
- [ ] CS-01: Post cannot be published with missing required fields
  - Action: Submit the new-post form with an empty title, then with an empty body
  - Expected: Publishing is blocked and a validation error naming the missing field is shown; no partial post is created

- [ ] CS-02: Unpublished/draft posts are not visible to visitors
  - Action: Save a post as draft (or without publishing), then view the author's profile and post list as a logged-out visitor
  - Expected: The draft does not appear anywhere in visitor-facing lists and cannot be reached by URL

- [ ] CS-03: Only the post's author can edit or delete that post
  - Action: As a different logged-in visitor, open an author's post and look for edit/delete controls
  - Expected: No "Edit"/"Delete" controls are shown to the non-author, and the post remains unmodified

## Interaction
- [ ] IX-01: Post actions give immediate visual state and confirmation
  - Action: Click "Like" and "Save" on a post, and submit a comment and a published post
  - Expected: The Like/Save buttons switch to an active state, counts update in place without a manual reload, and a success message/toast confirms publish and comment submission

- [ ] IX-02: Tag filter controls respond to selection and can be cleared
  - Action: Click tag chips to select custom and intelligent tags, then clear/remove a selection
  - Expected: Selected tags show an active/highlighted state, the article list updates to the filtered set, and removing a tag restores the unfiltered results

## Content
- [ ] CT-01: Auto-generated intelligent tags are relevant to the article's content
  - Action: Open intelligent tags on the code-related post and on a non-technical post (e.g. a "Life" essay)
  - Expected: Tags match the subject matter actually present in each article; no unrelated or empty/garbled tag strings are shown

- [ ] CT-02: Default content supports the blogging and tagging features
  - Action: Load the home/profile page and the tag filter lists before creating any data
  - Expected: Pre-existing posts with titles, Markdown bodies, custom tags (Technology/Life/Reading Notes) and comments are present and all links/images resolve (no broken placeholders or lorem-ipsum leftover text)