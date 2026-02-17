import json

# Define file paths
DATA_FILE = 'data.json'

def remove_duplicates():
    print(f"Loading {DATA_FILE}...")
    with open(DATA_FILE, 'r', encoding='utf-8') as f:
        data = json.load(f)

    original_count = len(data['repositories'])
    unique_repos = []
    seen_links = set()
    duplicates_found = 0

    # Iterate through repositories and keep only uniques
    for repo in data['repositories']:
        # Normalize link to lowercase and strip whitespace for comparison
        link = repo.get('link', '').strip().lower()
        
        if link in seen_links:
            print(f"Duplicate removed: {repo['name']} ({link})")
            duplicates_found += 1
        else:
            seen_links.add(link)
            unique_repos.append(repo)

    # Update the data object
    data['repositories'] = unique_repos

    # Save back to file
    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        # Use indent=4 to match the file's existing style
        json.dump(data, f, indent=4, ensure_ascii=False)
        # Add a trailing newline which is standard for git files
        f.write('\n') 

    print("-" * 30)
    print(f"Total repos before: {original_count}")
    print(f"Total repos after:  {len(unique_repos)}")
    print(f"Duplicates removed: {duplicates_found}")

if __name__ == "__main__":
    remove_duplicates()