All 22 checklist items have been executed. Here is the complete result:

# Test Result

## Functionality
- [X] FT-01: New student can register an account
  - Action: Open the sign-up page, enter a name/email/password, and click "Sign Up" / "Create Account".
  - Expected: Account is created, user is logged in, and a profile setup is accessible.
- [X] FT-02: User can set up profile with subjects, current level, and preferred study times
  - Action: In profile settings, add a subject (e.g., "Calculus"), select a level (e.g., "Undergraduate"), and set preferred study times (e.g., "Evenings 6–9 PM"); save.
  - Expected: Saved profile displays the subject, level, and preferred study times.
- [X] FT-03: User can create a new study group
  - Action: Click "Create Group", enter a topic name (e.g., "Calculus Group"), and submit.
  - Expected: The group is created and shown with the creator as a member.
- [X] FT-04: User can join an existing study group
  - Action: Browse/search the group list for a topic like "Biology" and click "Join Group".
  - Expected: User becomes a group member and the group appears in "My Groups".
- [X] FT-05: Group members can add notes/outlines/reading summaries into labeled sections
  - Action: In a group's shared space, create/select a labeled section (e.g., "Notes") and add a post with a title and text.
  - Expected: The item appears under that labeled section and is visible to group members.
- [X] FT-06: Group members can post questions and answers in the discussion area
  - Action: In the group's discussion area, post a question; then (as another member or same member) post a reply/answer.
  - Expected: Question and answer both appear in the running discussion thread in order.
- [ ] FT-07: Member can schedule a study session with time selector showing who is available
  - Action: In a group, click "Schedule Session", choose a date/time via the time selector, and save.
  - Expected: Session is listed with date/time and shows which members have marked themselves available for that time.
  - Bug Report:
    - Issue: Missing availability display / Incomplete feature
    - Actual: Session is created and listed with date/time ("Midterm Review Session, 17:00 - 19:00, Sunday, November 15, 2026"), but nowhere is it shown *which* members are available/attending — only aggregate counts ("1 attending / 0 maybe"). The scheduler dialog contains only Title/Description/Date/Start Time/End Time fields with no member-availability list at all.
- [ ] FT-08: Member can RSVP to a scheduled session
  - Action: Open an upcoming session and click "RSVP" / "Attending".
  - Expected: The member's name appears in the attendees list and the attendee count updates.
  - Bug Report:
    - Issue: Missing attendees list
    - Actual: Clicking "Attending" updates the count (0→1, verified via "Can't make it"→0 then "Attending"→1), but no attendees list with member names/avatars is ever rendered. Session card DOM contains zero name/avatar elements (`img[alt]` count = 0); only "1 attending / 0 maybe" counts are shown.
- [X] FT-09: User can mark their profile as a mentor
  - Action: In profile settings, toggle/enable "Available as Mentor" and save.
  - Expected: The profile displays a mentor designation/badge.
- [ ] FT-10: Group can invite a mentor to join
  - Action: In a group, open the mentor list, pick a mentor profile, and click "Invite".
  - Expected: The mentor is invited/joined and appears in the group member list with a distinct mentor role.
  - Bug Report:
    - Issue: Invitation never results in membership
    - Actual: "Invite Mentor" dialog lists Dr. Emily Wong with an "Invite" button; clicking it shows toast "Invitation sent! The mentor will see your request.", but the member count stays at 3 and the Members tab still shows only Marcus Johnson, Alex Chen, and Sarah Martinez — the invited mentor never appears in the group member list with a mentor role.
- [ ] FT-11: Mentor can highlight recommended resources
  - Action: As a mentor in a group, add a resource post marked "Recommended Resource".
  - Expected: The resource appears visibly flagged/highlighted as a recommended resource in the group space.
  - Bug Report:
    - Issue: No visible flag/label on recommended resources
    - Actual: As mentor (Alex in Calculus Champions), clicking the star icon only toggles the tiny star icon color (`text-accent`); no "Recommended Resource" label, badge, or highlighted section appears anywhere on the resource card. No toast or other confirmation either.
- [ ] FT-12: Mentor can pin an important post
  - Action: As a mentor, select a post in the group space and click "Pin".
  - Expected: The post appears at the top of the group space marked as pinned.
  - Bug Report:
    - Issue: Pin action has no visible effect on placement or labeling
    - Actual: Clicking the pin icon on "Week 3 Lecture Summary" toggles the pin icon color (`text-primary`), but the post remains in its original position (2nd of 3) — it does not move to the top — and no "Pinned" label/marker appears on the card.

## Constraint
- [X] CS-01: Registration cannot be completed with missing/invalid required fields
  - Action: Submit the sign-up form with an empty email or password (or invalid email format).
  - Expected: Submission is blocked and a validation error message is shown.
- [X] CS-02: User cannot access a group's shared space or discussion without being a member
  - Action: As a non-member, attempt to open a group's shared space/discussion content directly.
  - Expected: Access is denied or content is hidden; only a "Join" option is available.
- [ ] CS-03: Duplicate account email is rejected
  - Action: Sign up again with an email already registered.
  - Expected: Registration is blocked with an error stating the email/account already exists.
  - Bug Report:
    - Issue: Duplicate account creation allowed
    - Actual: Signed up again with the already-registered email `alex@study.edu` (new name "Dup Test"); no error was shown — the form was accepted, a second account was created, and the app logged in and redirected to /profile.
- [X] CS-04: Only mentors can pin posts or mark recommended resources
  - Action: As a regular (non-mentor) member, look for "Pin" or "Recommended Resource" controls on a post.
  - Expected: Those controls are not available to non-mentors (pinning attempt is prevented).
- [ ] CS-05: Profile requires subjects, level, and preferred study times before saving
  - Action: Attempt to save the profile with one of the required fields (subject, level, or study time) empty.
  - Expected: Save is blocked and the missing field is indicated.
  - Bug Report:
    - Issue: Missing required-field validation on profile save
    - Actual: Deselected the only subject ("Mathematics") leaving Subjects empty, then clicked "Save Changes" — the save succeeded with toast "Profile updated – Your changes have been saved." and no error/missing-field indication appeared.

## Interaction
- [X] IX-01: Successful actions show immediate visual feedback
  - Action: Join a group, RSVP to a session, or create a post.
  - Expected: A success toast/confirmation message or visible state change (e.g., button becomes "Joined"/"Attending") appears immediately.
- [ ] IX-02: Time selector updates availability display dynamically
  - Action: In the session scheduler, change the selected date/time slot.
  - Expected: The list of members marked available updates to match the newly selected time.
  - Bug Report:
    - Issue: Feature absent — no availability display in scheduler
    - Actual: The "Schedule a Study Session" dialog contains only Title/Description/Date/Start/End time inputs. Changing the date from 2026-11-15 to 2026-11-16 produced no update because no list of available members exists in the scheduler at all.
- [ ] IX-03: RSVP toggle reflects current state
  - Action: Click "RSVP" on a session, then click it again to cancel.
  - Expected: First click adds the user to attendees; second click removes them and the count updates both times.
  - Bug Report:
    - Issue: RSVP toggle does not cancel on second click
    - Actual: Observed sequence: initial "1 attending" (button active/green) → "Can't make it" → "0 attending" (button inactive) → "Attending" → "1 attending" (active) → clicking "Attending" a second time → count stays "1 attending" (still active). The second click on the same RSVP button does not remove the attendee; only switching to a different status button removes them.

## Content
- [X] CT-01: Group topics are relevant to study subjects
  - Action: Browse the group list/default groups.
  - Expected: Groups are themed around academic subjects (e.g., calculus, biology, literature), not unrelated content.
- [X] CT-02: Mentor profiles are visually distinct from student profiles
  - Action: View a mentor's profile in a member list or group roster.
  - Expected: The mentor shows a distinct label/role (e.g., "Mentor" badge) differentiating them from regular students.
- [ ] CT-03: Pinned and recommended content stays accessible in the group space
  - Action: Open a group with existing pinned posts and recommended resources.
  - Expected: Pinned posts appear prominently (top of the space) and recommended resources are clearly marked/labeled.
  - Bug Report:
    - Issue: Pinned/recommended states are not clearly marked or prioritized
    - Actual: In Calculus Champions, the pinned/recommended card ("Integration Techniques Cheat Sheet") has identical card styling to all other notes (`rounded-lg border bg-card ... relative`), sits in natural list order (pinning "Week 3 Lecture Summary" did not reorder anything), and there are no "Pinned" or "Recommended" text labels/badges anywhere — the only signal is a subtle color tint on the tiny pin/star icons.