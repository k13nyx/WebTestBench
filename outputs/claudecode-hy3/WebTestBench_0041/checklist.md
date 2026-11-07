# Test Checklist

## Functionality
- [ ] FT-01: View all smart home devices in the dashboard
  - Action: Open the admin dashboard
  - Expected: A list/grid of all default smart home devices is displayed
- [ ] FT-02: View devices grouped by room
  - Action: Select a room (e.g., "Living Room") from the room view/filter control
  - Expected: Only devices in the selected room are displayed
- [ ] FT-03: View devices by device type
  - Action: Select a device type (e.g., "Light" or "Thermostat") from the type filter
  - Expected: Only devices of the selected type are displayed
- [ ] FT-04: Filter to show only offline devices
  - Action: Apply the "Offline" status filter
  - Expected: Only devices with status "Offline" are displayed
- [ ] FT-05: Filter to show only idle devices
  - Action: Apply the "Idle" status filter
  - Expected: Only devices with status "Idle" are displayed
- [ ] FT-06: Adjust brightness on a light device
  - Action: Open a light device and change its brightness value/slider
  - Expected: The brightness value is updated and persisted
- [ ] FT-07: Adjust target temperature on a thermostat
  - Action: Open a thermostat and change its target temperature
  - Expected: The target temperature is updated and persisted
- [ ] FT-08: Create a schedule for a light to change state
  - Action: Create a schedule for a light (e.g., turn on at 8:00 PM) and save
  - Expected: The schedule is created and listed under the device
- [ ] FT-09: Create a schedule for a thermostat to change state
  - Action: Create a schedule for a thermostat (e.g., set 70°F at 9:00 PM) and save
  - Expected: The schedule is created and listed under the device
- [ ] FT-10: View recent activity / last used time
  - Action: Open the recent activity section
  - Expected: Each device shows a "last used" timestamp or activity entry

## Constraint
- [ ] CS-01: Brightness is constrained to a valid range (0–100%)
  - Action: Attempt to set brightness to an invalid value (e.g., 150 or -10)
  - Expected: The value is rejected and a validation message is shown
- [ ] CS-02: Target temperature is constrained to a valid range
  - Action: Attempt to set temperature outside the allowed range
  - Expected: The value is rejected and a validation message is shown
- [ ] CS-03: Schedule requires a valid time
  - Action: Attempt to save a schedule with an empty or invalid time
  - Expected: The schedule is not saved and a validation error is shown

## Interaction
- [ ] IX-01: Success confirmation appears after saving a change
  - Action: Save a brightness/temperature change or a new schedule
  - Expected: A success toast/confirmation is displayed
- [ ] IX-02: Device list updates instantly when a filter is applied
  - Action: Apply any room, type, or status filter
  - Expected: The list refreshes to matching devices without a full page reload

## Content
- [ ] CT-01: Device icons/images match device type
  - Action: Inspect the device list icons/images
  - Expected: Each device shows an icon/image consistent with its type (light, thermostat, etc.)
- [ ] CT-02: Recent activity entries are relevant and well-formed
  - Action: Open the recent activity section
  - Expected: Entries describe actual device usage (e.g., "Light turned on") with valid timestamps