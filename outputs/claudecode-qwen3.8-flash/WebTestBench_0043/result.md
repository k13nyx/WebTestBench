All checklist items executed. Compiling final results.

# Test Result

## Functionality
- [X] FT-01: New visitor can sign up and reach an authenticated session
  - Action: Open the site, click "Sign Up", submit a valid username, email and password
  - Expected: Account is created, user is logged in, and their own author dashboard/profile is reachable
  - Verified: "QA Tester" / qa.tester@example.com created → toast "Welcome to Inkwell!", authenticated nav (Home/Saved/Write), profile page with Published/Drafts/Analytics dashboard tabs reachable.

- [X] FT-02: Author can create a post written in Markdown and it renders
  - Action: Create a new post containing a heading, bullet list, inline code and a fenced code block, then save/publish
  - Expected: The post displays as rendered HTML (heading styled, list bulleted, code in monospace block), not raw Markdown syntax
  - Verified on detail page: `h1/h2/h3` elements rendered, `list > listitem` bullets, inline `code` in monospace, fenced blocks as `pre > code` (ui-monospace font, newlines preserved).

- [ ] FT-03: Author can edit an existing post
  - Action: Open one of the author's own posts, click "Edit", change title and body text, save
  - Expected: The post detail page and profile listing show the updated title and body
  - Bug Report:
    - Issue: Stale content preview after edit
    - Actual: The detail page shows the updated title ("Updated: Python Basics Guide") and edited body, and the profile listing shows the updated title — but the listing entry's body preview still renders the OLD content snapshot ("# Python for Frontend Developers … ## Benefits - Fast prototyping - Great for da…"); the excerpt saved at publish time is never refreshed when the body is edited.

- [X] FT-04: Published post appears on the author's own profile page
  - Action: Publish a post, then open the author's profile page
  - Expected: The post is listed on the profile with title and preview, and links to the full post
  - Verified: "Published (1)" tab listed the post with title, preview text, tags, and a working link to /post/post-1794110293621.

- [X] FT-05: A visitor can open and read any published post
  - Action: From the profile/post list, click a post title as a non-author visitor
  - Expected: The full post content opens on its own page and is readable without login prompts
  - Verified logged out: /post/post-1 and /post/<my-post> render full article content with no login gate or login prompt overlay on the body (only the comment box offers Sign In/Sign Up).

- [X] FT-06: Visitor can leave a comment under a post
  - Action: Open a post, type a comment in the comment field and submit
  - Expected: The comment is displayed beneath the post body, attributed to the commenter with a timestamp
  - Verified: On post-1, "Excellent piece on naming conventions!" displayed under the body as "QA Tester · 2026-11-08"; comment count 2→3→4 and persisted across reload.

- [X] FT-07: Visitor can like a post and the count reflects it
  - Action: Click the "Like" button on a post, then reload the post page
  - Expected: The displayed like count increases by exactly 1 and persists after reload
  - Verified: post-1 like count 2 → 3 in place; after reload still 3 (storage `likes: [user-1, user-3, QA-Tester]`); home listing also shows 3.

- [X] FT-08: Visitor can save a post to a personal list and find it again
  - Action: Click "Save"/bookmark on a post, then open the personal "Saved" list page
  - Expected: That post appears in the saved list and links back to the post
  - Verified: Bookmarking post-1 turned the icon button to an active accent state; /saved (via nav link) showed "Saved Posts — 1 post saved for later" with the post card linking back to /post/post-1.

- [X] FT-09: Author can attach custom tags when publishing
  - Action: Publish a post and enter/select custom tags such as "Technology", "Life", "Reading Notes"
  - Expected: The chosen custom tags are displayed on the post detail page and in the post's listing entry
  - Verified: "Technology" and "Reading Notes" entered via the Add-a-tag field appear as chips on the detail page, on the home listing card, and on the profile entry.

- [ ] FT-10: System auto-generates intelligent tags from post content
  - Action: Publish a code-related article (Python snippets, frontend markup), then open its detail page
  - Expected: Intelligent tags (e.g. "Python", "Frontend Development") are generated automatically and shown distinctly from the author's custom tags, with no manual entry
  - Bug Report:
    - Issue: Auto-generated intelligent tags not displayed per article
    - Actual: Detection works in the editor (auto-detected "Python", "JavaScript", "Frontend Development" live) and the values persist in storage (`autoTags:["Python","JavaScript","TypeScript","React","Frontend Development"]`), but after publishing, the post detail page shows ONLY the custom tags "Technology" / "Reading Notes". No intelligent-tag chips appear on the detail page or listings (confirmed after reload; same for post-1 whose stored `autoTags` of JavaScript/Code Examples are never rendered — its 3 chips are all from its custom `tags` array).

- [ ] FT-11: Articles can be filtered by custom tag, intelligent tag, and both combined
  - Action: Apply the custom tag filter "Technology"; then apply intelligent tag "Python"; then apply both together
  - Expected: Each filter shows only matching articles; the combined filter shows only articles having BOTH "Technology" and "Python"
  - Bug Report:
    - Issue: Contradictory incorrect empty-state text in filter results
    - Actual: Filter membership itself was correct (Technology → my post + post-3 which really carries "Technology"; Python → my post only; combined → only my post, "(showing posts matching all selected tags)" AND-logic). However, whenever the result set is exactly 1 item, the section renders heading "Filtered Stories (1)" while the results area simultaneously displays "No posts match the selected tags." — an incorrect message shown even though a matching article is displayed. The dedicated filter section itself shows zero cards in that case.

- [X] FT-12: Frequently-used tag groups can be saved and re-applied
  - Action: With a combined tag filter active (e.g. "Technology + Python"), save it as a named tag group; clear filters, then click the saved group
  - Expected: The saved group appears in a tag-groups area and re-applies the exact same filter set with one click
  - Verified: "Save Filter" dialog (name + tag preview) → group "Tech + Python (2 tags)" appears in "Saved Filters" (stored as customTags:[Technology], intelligentTags:[Python]); after Clear, one click re-applied Active: Technology + Python with the identical filtered result set.

- [ ] FT-13: Author backend shows per-tag statistics and a popularity report
  - Action: As the author, open the backend/analytics page and view stats per tag, then click "Generate tag popularity report"
  - Expected: Page views, like counts and comment counts are listed per tag, and a popularity report is produced ranking tags with those figures
  - Bug Report:
    - Issue: Inaccurate/untracked statistics and missing "Generate" control
    - Actual: The Analytics tab auto-renders a ranked "Tag Popularity Report" (no "Generate tag popularity report" button exists anywhere on the page — hasGenerate=false). The figures are wrong: my post was viewed many times (including by logged-out visitors) yet its `views` stayed 0 ("Total Views 0"); as Marcus (author of post-1, storage views=142, likes=3) the dashboard reports Total Views 18 and Total Likes 24, which match neither the stored counts nor session activity. Per-tag rows repeat the same inconsistent figures.

## Constraint
- [X] CS-01: Post cannot be published with missing required fields
  - Action: Submit the new-post form with an empty title, then with an empty body
  - Expected: Publishing is blocked and a validation error naming the missing field is shown; no partial post is created
  - Verified: Empty title → toast "Title required / Please add a title for your post."; empty body → "Content required / Please write some content for your post."; stayed on /write, no post entry created in storage.

- [ ] CS-02: Unpublished/draft posts are not visible to visitors
  - Action: Save a post as draft (or without publishing), then view the author's profile and post list as a logged-out visitor
  - Expected: The draft does not appear anywhere in visitor-facing lists and cannot be reached by URL
  - Bug Report:
    - Issue: Draft leak via direct URL
    - Actual: The draft ("Secret Unpublished Draft", `published:false`) correctly does NOT appear on the home feed or the logged-out public profile. However, a logged-out visitor navigating directly to /post/post-1794110552216 gets the full draft rendered (title and body "…DraftBodyXYZ" visible in the page) — the post detail route does not filter unpublished posts.

- [X] CS-03: Only the post's author can edit or delete that post
  - Action: As a different logged-in visitor, open an author's post and look for edit/delete controls
  - Expected: No "Edit"/"Delete" controls are shown to the non-author, and the post remains unmodified
  - Verified: As logged-in QA Tester on Marcus's post-1, zero `/edit/` links and no delete control existed (controls present on own posts: edit link + delete icon). Post body/title unchanged after the visitor session.

## Interaction
- [ ] IX-01: Post actions give immediate visual state and confirmation
  - Action: Click "Like" and "Save" on a post, and submit a comment and a published post
  - Expected: The Like/Save buttons switch to an active state, counts update in place without a manual reload, and a success message/toast confirms publish and comment submission
  - Bug Report:
    - Issue: Missing success toast on comment submission
    - Actual: Counts update in place (like 2→3; Comments (2)→(3) without reload), the Save button switches to an active accent state (`bg-accent/10 text-accent`), and publish/edit/draft toasts appear ("Post published!", "Post updated!", "Draft saved!"). But submitting a comment produces NO confirmation toast — the notification region stays empty (checked at 120 ms and 400 ms after "Post Comment" click) even though the comment is added silently.

- [X] IX-02: Tag filter controls respond to selection and can be cleared
  - Action: Click tag chips to select custom and intelligent tags, then clear/remove a selection
  - Expected: Selected tags show an active/highlighted state, the article list updates to the filtered set, and removing a tag restores the unfiltered results
  - Verified: Selected chips get an [active] state and an "Active:" pill with remove icon; list switches to "Filtered Stories (N)"; removing the active pill or clicking "Clear" restores the full unfiltered "Latest Stories".

## Content
- [ ] CT-01: Auto-generated intelligent tags are relevant to the article's content
  - Action: Open intelligent tags on the code-related post and on a non-technical post (e.g. a "Life" essay)
  - Expected: Tags match the subject matter actually present in each article; no unrelated or empty/garbled tag strings are shown
  - Bug Report:
    - Issue: Per-article intelligent tags not available to verify in UI (FT-10 display defect)
    - Actual: The required action cannot be completed: no post detail page or listing renders intelligent tags per article (verified on the code post and on the seeded posts). The only article-attributable evidence is in app storage (post-2 "Design/Creativity" essay → autoTags Design, Opinion; post-3 AI essay → Machine Learning, Opinion, Productivity; Python post → Python, JavaScript, TypeScript, React, Frontend Development). These are largely relevant, with one weak extraction ("TypeScript" for a post that never mentions TypeScript), but nothing can be "opened" on the post itself through the UI.

- [X] CT-02: Default content supports the blogging and tagging features
  - Action: Load the home/profile page and the tag filter lists before creating any data
  - Expected: Pre-existing posts with titles, Markdown bodies, custom tags (Technology/Life/Reading Notes) and comments are present and all links/images resolve (no broken placeholders or lorem-ipsum leftover text)
  - Verified pre-data: 3 seeded posts with titles, Markdown-rendered bodies (headings/blockquote/code), custom tags on listings (Programming, Best Practices, Design, Creativity, AI, Future, Software Development, Technology, Process), 2 attributed timestamped comments on post-1; filter dialog shows populated Custom/Intelligent tag lists (incl. "Technology"); all 4 images resolve (naturalWidth>0), all links valid hrefs, no lorem-ipsum. The tag names present differ from the illustrative set (only "Technology" of Technology/Life/Reading Notes exists in seed data, matching the user instruction's "e.g." wording), but all required content types are present.

## Additional Findings (outside checklist)
- Hard-loading the protected page /saved while logged in redirects to /login, and /login then renders BLANK (empty body) despite `blog_current_user` being present; the Saved page works only via in-app navigation.
- Console error: React `validateDOMNesting` warning on the home page (invalid DOM nesting in post cards).
- The like button has no accessible name (`aria-label` absent; announced only by its count).