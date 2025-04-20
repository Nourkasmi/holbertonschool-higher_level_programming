import os

def generate_invitations(template, attendees):
    # --- 1. Type checks ---
    if not isinstance(template, str):
        print(f"Error: template must be a string, got {type(template).__name__}")
        return
    if not isinstance(attendees, list) or not all(isinstance(a, dict) for a in attendees):
        print(f"Error: attendees must be a list of dictionaries, got {type(attendees).__name__}")
        return

    # --- 2. Empty-input checks ---
    if not template.strip():
        print("Template is empty, no output files generated.")
        return
    if len(attendees) == 0:
        print("No data provided, no output files generated.")
        return

    # --- 3. Process each attendee ---
    for idx, attendee in enumerate(attendees, start=1):
        # Safely fetch each field, substituting "N/A" if missing or None
        name            = attendee.get("name")            or "N/A"
        event_title     = attendee.get("event_title")    or "N/A"
        event_date      = attendee.get("event_date")     or "N/A"
        event_location  = attendee.get("event_location") or "N/A"

        # Fill in the template
        content = template
        content = content.replace("{name}",           str(name))
        content = content.replace("{event_title}",    str(event_title))
        content = content.replace("{event_date}",     str(event_date))
        content = content.replace("{event_location}", str(event_location))

        # Prepare output filename
        filename = f"output_{idx}.txt"

        # Warn if we're overwriting an existing file
        if os.path.exists(filename):
            print(f"Warning: '{filename}' already exists and will be overwritten.")

        # Write to disk
        try:
            with open(filename, "w", encoding="utf-8") as f:
                f.write(content)
        except Exception as e:
            print(f"Error writing '{filename}': {e}")
