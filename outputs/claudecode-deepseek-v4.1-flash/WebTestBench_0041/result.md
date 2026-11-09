# Test Result

## Functionality

- [ ] FT-01: View all smart home devices grouped by room
  - Action: Open the dashboard and select the "By Room" grouping view.
  - Expected: Devices are listed under their assigned room headings (e.g., Living Room, Bedroom), each device showing its name and current state.
  - Bug Report:
    - Issue: Missing Feature / Non-existent Control
    - Actual: No "By Room" grouping view or toggle exists anywhere in the app. The Dashboard shows only room summary cards (device counts), the Rooms page shows room cards, and `/devices` offers a Room filter but renders a flat grid with no room headings. Devices are only shown under a heading when opening one room at a time (e.g., `/rooms?room=living-room`), never grouped by all room headings.

- [ ] FT-02: View all smart home devices grouped by device type
  - Action: Switch the grouping view to "By Device Type".
  - Expected: Devices are grouped under type headings (e.g., Lights, Thermostats, Sensors), each device showing its name and current state.
  - Bug Report:
    - Issue: Missing Feature / Non-existent Control
    - Actual: No "By Device Type" grouping view or toggle exists. The Devices page provides Type filter buttons (All Types, Lights, Thermostats, Locks, Cameras, Speakers, Sensors) that filter to a flat, un-sectioned grid; no type headings group the results.

- [X] FT-03: Adjust a light's brightness setting
  - Action: On a light device, change the brightness control and confirm the change.
  - Expected: The light's brightness updates to the selected value and the device detail reflects the new brightness.

- [X] FT-04: Adjust a thermostat's target temperature
  - Action: On a thermostat device, change the target temperature and confirm the change.
  - Expected: The thermostat's target temperature updates to the selected value and the device detail reflects the new target.

- [X] FT-05: Create a schedule for a light
  - Action: Open "Create Schedule", select a light, set a time and desired state (on/off), then save.
  - Expected: The schedule is saved and listed with the selected light, time, and action.

- [X] FT-06: Create a schedule for a thermostat
  - Action: Open "Create Schedule", select a thermostat, set a time and target temperature, then save.
  - Expected: The schedule is saved and listed with the selected thermostat, time, and target temperature.

- [X] FT-07: View recent activity / last-used time of devices
  - Action: Open the recent activity section of the dashboard.
  - Expected: A list of devices shows their last-used/state-change time, with the most recent activity visible.

- [X] FT-08: Filter devices by "Offline" status
  - Action: Apply the status filter and select "Offline".
  - Expected: Only devices currently marked offline are displayed.

- [X] FT-09: Filter devices by "Idle" status
  - Action: Apply the status filter and select "Idle".
  - Expected: Only devices currently marked idle are displayed.

## Constraint

- [X] CS-01: Brightness input is bounded to a valid range
  - Action: Attempt to set brightness below 0% or above 100%.
  - Expected: The value is rejected or clamped to 0–100; no out-of-range brightness is applied or saved.

- [X] CS-02: Target temperature input is bounded to a valid range
  - Action: Attempt to set a target temperature outside the allowed range (e.g., below the minimum or above the maximum).
  - Expected: The value is rejected or clamped to the allowed range; no out-of-range temperature is applied or saved.

- [ ] CS-03: Schedule cannot be saved with missing required fields
  - Action: Open "Create Schedule" and attempt to save without selecting a device, time, or action.
  - Expected: Save is blocked, an inline validation message identifies the missing field(s), and no schedule is created.
  - Bug Report:
    - Issue: Missing Validation Feedback
    - Actual: Clicking "Create Schedule" with all fields empty silently does nothing — the dialog stays open and no schedule is created (count remains 4), but no inline message, error text, highlight, or `aria-invalid` attribute identifies the missing Device/Action/Time fields. The user receives no feedback explaining why saving failed.

- [X] CS-04: Status filter results contain only matching devices
  - Action: Apply the "Offline" filter, then the "Idle" filter.
  - Expected: The list never contains a device whose status does not match the active filter.

- [ ] CS-05: Devices that are offline cannot be controlled or scheduled into an active change
  - Action: Attempt to change brightness/temperature or create an active schedule on a device marked offline.
  - Expected: The control/schedule is blocked with a clear message that the device is offline.
  - Bug Report:
    - Issue: Offline Restriction Bypassed
    - Actual: The offline device "Garage Light" (status badge "offline") is selectable in the schedule Device dropdown and a schedule ("Turn on", 07:00, Mon) was successfully saved for it — Active Schedules increased from 4 to 5 — with no warning or "device is offline" message. Only on-card power switches for offline devices are disabled; the schedule path is not blocked.

## Interaction

- [ ] IX-01: Confirmation feedback after a settings change
  - Action: Adjust brightness on a light and confirm the change.
  - Expected: A success notification (e.g., toast/message) confirms the setting was applied.
  - Bug Report:
    - Issue: Missing Success Notification
    - Actual: Changing brightness (0% → 100% via the slider) updated the label immediately, but no toast or message appeared. The "Notifications (F8)" region remained empty and no `[data-sonner-toast]`, `role="status"`, or `role="alert"` element was created.

- [X] IX-02: Newly created schedule appears without page reload
  - Action: Create and save a schedule.
  - Expected: The schedule list updates immediately to include the new entry.

- [X] IX-03: Device list updates dynamically when a status filter is applied or cleared
  - Action: Apply a status filter, then clear/reset it.
  - Expected: The device list refreshes to show only matching devices when filtered, and all devices when cleared.

- [ ] IX-04: Device cards provide visible hover/selection feedback
  - Action: Hover over and click a device card.
  - Expected: The card shows a visible hover state and a distinct selected/expanded state on click.
  - Bug Report:
    - Issue: Missing Selected/Expanded State
    - Actual: Hover feedback works (border color changed to `rgba(33,213,237,0.3)` and a shadow appeared), but clicking the "Floor Lamp" card produced no change — no class change, no `aria-selected`, no expansion, and no additional detail content. Only the hover style remains while the pointer is over the card.

## Content

- [X] CT-01: Device icons/images match their device type
  - Action: Inspect device cards and list entries across all device types.
  - Expected: Every icon/image is relevant to its device type (e.g., a bulb icon for lights, a thermostat icon for thermostats); no mismatched or placeholder imagery.

- [X] CT-02: Status labels and last-used data are relevant and coherent
  - Action: Review the displayed status labels and recent-activity timestamps across devices.
  - Expected: Labels reflect the smart-home domain (e.g., Online, Offline, Idle, Active) and each device's last-used time is present and consistent with its activity entry.