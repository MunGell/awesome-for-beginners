#!/usr/bin/env python3
"""
Validates data.json for awesome-for-beginners:
- Valid UTF-8 and JSON syntax
- Top-level schema (technologies, repositories, sponsors)
- Required fields and types for each repository
- Direct, valid URLs (HTTP/HTTPS)
- No duplicate repository names or links
- No trailing whitespace on lines
- Single repository addition check when comparing against git base ref
"""

import json
import os
import re
import subprocess
import sys
from urllib.parse import urlparse

DATAFILE = "data.json"
REQUIRED_REPO_FIELDS = ["name", "link", "label", "technologies", "description"]


def error(msg):
    print(f"❌ ERROR: {msg}", file=sys.stderr)


def warning(msg):
    print(f"⚠️  WARNING: {msg}")


def check_trailing_whitespace(filepath):
    errors = []
    with open(filepath, "r", encoding="utf-8", errors="replace") as f:
        for idx, line in enumerate(f, start=1):
            line_no_newline = line.rstrip("\r\n")
            if re.search(r"[ \t]+$", line_no_newline):
                errors.append(f"Line {idx} has trailing whitespace.")
    return errors


def validate_entry(repo, index):
    errors = []
    for field in REQUIRED_REPO_FIELDS:
        if field not in repo:
            errors.append(f"Entry #{index} is missing required field: '{field}'")

    if "name" in repo and (not isinstance(repo["name"], str) or not repo["name"].strip()):
        errors.append(f"Entry #{index}: 'name' must be a non-empty string.")

    if "link" in repo:
        link = repo["link"]
        if not isinstance(link, str) or not link.strip():
            errors.append(f"Entry #{index}: 'link' must be a non-empty string.")
        else:
            parsed = urlparse(link)
            if parsed.scheme not in ("http", "https") or not parsed.netloc:
                errors.append(f"Entry #{index} ({repo.get('name', '')}): invalid URL '{link}'")

    if "label" in repo and (not isinstance(repo["label"], str) or not repo["label"].strip()):
        errors.append(f"Entry #{index} ({repo.get('name', '')}): 'label' must be a non-empty string.")

    if "technologies" in repo:
        techs = repo["technologies"]
        if not isinstance(techs, list) or len(techs) == 0:
            errors.append(f"Entry #{index} ({repo.get('name', '')}): 'technologies' must be a non-empty array.")
        else:
            for t in techs:
                if not isinstance(t, str) or not t.strip():
                    errors.append(f"Entry #{index} ({repo.get('name', '')}): technology '{t}' must be a non-empty string.")

    if "description" in repo and (not isinstance(repo["description"], str) or not repo["description"].strip()):
        errors.append(f"Entry #{index} ({repo.get('name', '')}): 'description' must be a non-empty string.")

    return errors


def validate_data_json(filepath=DATAFILE):
    all_errors = []

    # 1. Trailing whitespace
    ws_errors = check_trailing_whitespace(filepath)
    if ws_errors:
        all_errors.extend(ws_errors[:10])
        if len(ws_errors) > 10:
            all_errors.append(f"... and {len(ws_errors) - 10} more trailing whitespace errors.")

    # 2. JSON parsing
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            data = json.load(f)
    except json.JSONDecodeError as e:
        all_errors.append(f"JSON syntax error: {e}")
        return all_errors
    except Exception as e:
        all_errors.append(f"Could not read {filepath}: {e}")
        return all_errors

    # 3. Top-level structure
    if not isinstance(data, dict):
        all_errors.append("Root element must be a JSON object.")
        return all_errors

    for key in ("technologies", "repositories", "sponsors"):
        if key not in data:
            all_errors.append(f"Missing root key '{key}'.")

    if "repositories" not in data or not isinstance(data["repositories"], list):
        all_errors.append("'repositories' must be an array.")
        return all_errors

    # 4. Entry validation & duplicate checks
    seen_names = {}
    seen_links = {}

    for idx, repo in enumerate(data["repositories"], start=1):
        if not isinstance(repo, dict):
            all_errors.append(f"Entry #{idx} must be a JSON object.")
            continue

        entry_errors = validate_entry(repo, idx)
        all_errors.extend(entry_errors)

        name = repo.get("name", "").strip().lower()
        link = repo.get("link", "").strip().lower().rstrip("/")

        if name:
            if name in seen_names:
                all_errors.append(
                    f"Duplicate repository name '{repo.get('name')}' in entry #{idx} (previously seen in entry #{seen_names[name]})."
                )
            else:
                seen_names[name] = idx

        if link:
            if link in seen_links:
                all_errors.append(
                    f"Duplicate repository link '{repo.get('link')}' in entry #{idx} (previously seen in entry #{seen_links[link]})."
                )
            else:
                seen_links[link] = idx

    return all_errors


def check_single_addition(base_ref="origin/main"):
    """
    Checks if git diff adds more than 1 repository entry compared to base branch.
    Enforces CONTRIBUTING.md rule: 'Submit one pull request per repository suggestion'.
    """
    try:
        cmd = ["git", "show", f"{base_ref}:{DATAFILE}"]
        result = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", check=False)
        if result.returncode != 0:
            return None  # Cannot compare against base, skip check

        base_data = json.loads(result.stdout)
        with open(DATAFILE, "r", encoding="utf-8") as f:
            current_data = json.load(f)

        base_count = len(base_data.get("repositories", []))
        current_count = len(current_data.get("repositories", []))
        diff_count = current_count - base_count

        if diff_count > 1:
            return (
                f"PR adds {diff_count} repositories. Guidelines require submitting only one repository per pull request."
            )
    except Exception:
        pass
    return None


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    filepath = args[0] if args else DATAFILE
    print(f"Validating {filepath}...")

    errors = validate_data_json(filepath)

    if "--check-single-addition" in sys.argv:
        base_ref = "origin/main"
        for arg in sys.argv:
            if arg.startswith("--base="):
                base_ref = arg.split("=", 1)[1]
        single_err = check_single_addition(base_ref)
        if single_err:
            errors.append(single_err)

    if errors:
        print(f"\nValidation failed with {len(errors)} error(s):")
        for err in errors:
            error(err)
        sys.exit(1)

    print(f"✅ {filepath} is valid and meets all contribution guidelines!")


if __name__ == "__main__":
    main()
