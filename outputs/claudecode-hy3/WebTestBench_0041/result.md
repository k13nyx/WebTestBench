All tests executed. Here is the complete result set.

# Test Result

## Functionality
- [X] FT-01: View all smart home devices in the dashboard
  - Action: Open the admin dashboard
  - Expected: A list/grid of all default smart home devices is displayed
- [X] FT-02: View devices grouped by room
  - Action: Select a room (e.g., "Living Room") from the room view/filter control
  - Expected: Only devices in the selected room are displayed
- [X] FT-03: View devices by device type
  - Action: Select a device type (e.g., "Light" or "Thermostat") from the type filter
  - Expected: Only devices of the selected type are displayed
- [X] FT-04: Filter to show only offline devices
  - Action: Apply the "Offline" status filter
  - Expected: Only devices with status "Offline" are displayed
- [X] FT-05: Filter to show only idle devices
  - Action: Apply the "Idle" status filter
  - Expected: Only devices with status "Idle" are displayed
- [ ] FT-06: Adjust brightness on a light device
  - Action: Open a light device and change its brightness value/slider
  - Expected: The brightness value is updated and persisted
  - Bug Report:
    - Issue: Value not persisted (lost on navigation/reload)
    - Actual: Brightness updated via slider (75% → 80% → 85%), but after navigating to /schedules and back to /devices, and after a full page reload, the value reverted to 75%. The change is held only in transient UI state and is not saved.
- [ ] FT-07: Adjust target temperature on a thermostat
  - Action: Open a thermostat and change its target temperature
  - Expected: The target temperature is updated and persisted
  - Bug Report:
    - Issue: Value not persisted (lost on navigation/reload)
    - Actual: Target temperature updated via slider (Smart Thermostat 70°F → 71°F), but after a full page reload it reverted to 70°F. The change is not persisted to any store/storage.
- [X] FT-08: Create a schedule for a light to change state
  - Action: Create a schedule for a light (e.g., turn on at 8:00 PM) and save
  - Expected: The schedule is created and listed under the device
- [X] FT-09: Create a schedule for a thermostat to change state
  - Action: Create a schedule for a thermostat (e.g., set 70°F at 9:00 PM) and save
  - Expected: The schedule is created and listed under the device
- [X] FT-10: View recent activity / last used time
  - Action: Open the recent activity section
  - Expected: Each device shows a "last used" timestamp or activity entry

## Constraint
- [ ] CS-01: Brightness is constrained to a valid range (0–100%)
  - Action: Attempt to set brightness to an invalid value (e.g., 150 or -10)
  - Expected: The value is rejected and a validation message is shown
  - Bug Report:
    - Issue: No input field / no validation message
    - Actual: Brightness is controlled only by a Radix slider with aria-valuemin=0 / aria-valuemax=100. There is no numeric input in which to type 150 or -10, the slider silently clamps at bounds, and no validation/error message is displayed anywhere.
- [ ] CS-02: Target temperature is constrained to a valid range
  - Action: Attempt to set temperature outside the allowed range
  - Expected: The value is rejected and a validation message is shown
  - Bug Report:
    - Issue: No input field / no validation message
    - Actual: The thermostat target is a slider with aria-valuemin=60 / aria-valuemax=85°F. There is no numeric input to enter an out-of-range value; the slider clamps silently and no validation/error message appears.
- [ ] CS-03: Schedule requires a valid time
  - Action: Attempt to save a schedule with an empty or invalid time
  - Expected: The schedule is not saved and a validation error is shown
  - Bug Report:
    - Issue: No validation error message shown
    - Actual: With Device, Action, and Day selected but the Time field left empty, clicking "Create Schedule" correctly prevents saving (dialog stays open, no new schedule added), but no validation/error message is displayed to the user.

## Interaction
- [ ] IX-01: Success confirmation appears after saving a change
  - Action: Save a brightness/temperature change or a new schedule
  - Expected: A success toast/confirmation is displayed
  - Bug Report:
    - Issue: No success toast/confirmation rendered
    - Actual: After creating 3 schedules and changing a brightness value, no success toast or confirmation appears. The sonner toaster component ([data-sonner-toaster]) is not mounted in the DOM, and the "Notifications" region list remains empty.
- [X] IX-02: Device list updates instantly when a filter is applied
  - Action: Apply any room, type, or status filter
  - Expected: The list refreshes to matching devices without a full page reload
  - (Verified: applying Room/Type/Status filters updated the "Showing X of 20" count and device list immediately while the URL stayed on /devices — an SPA re-render, not a full reload.)

## Content
- [X] CT-01: Device icons/images match device type
  - Action: Inspect the device list icons/images
  - Expected: Each device shows an icon/image consistent with its type (light, thermostat, etc.)
  - (Verified: icons are type-specific Lucide SVGs — lights use `lucide-lightbulb`, lamps `lucide-lamp`, thermostats `lucide-thermometer`, speakers `lucide-speaker`, cameras `lucide-camera`, locks `lucide-lock`, fan `lucide-fan`, sensor `lucide-eye`.)
- [X] CT-02: Recent activity entries are relevant and well-formed
  - Action: Open the recent activity section
  - Expected: Entries describe actual device usage (e.g., "Light turned on") with valid timestamps
  - (Verified on /activity: "Main Ceiling Light — Turned on — 5 minutes ago", "Smart Thermostat — Temperature adjusted to 70°F — 30 minutes ago", "Smart Lock — Locked remotely", "Kitchen Camera — Motion detected", etc.)

### Summary
- **Passed (12):** FT-01, FT-02, FT-03, FT-04, FT-05, FT-08, FT-09, FT-10, IX-02, CT-01, CT-02
- **Failed (6):** FT-06, FT-07 (no persistence of control changes), CS-01, CS-02 (no range validation UI/feedback), CS-03 (no validation error message), IX-01 (no success toast/confirmation)

**Notable findings:** Device control changes (brightness/temperature) update live but are **not persisted** and revert on navigation/reload, unlike schedules which persist across navigation. No constraint validation messages exist for brightness/temperature (slider-only, silently clamped), and no success toast is shown on save.