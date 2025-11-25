import pickle

# Read the TSV file
cookies = []
with open('amazon_cookies.json', 'r') as f:
    for line in f:
        parts = line.strip().split('\t')
        if len(parts) >= 4:  # name, value, domain, path
            cookie = {
                'name': parts[0],
                'value': parts[1],
                'domain': parts[2],
                'path': parts[3],
            }
            if len(parts) > 4 and parts[4]:
                cookie['expires'] = parts[4]
            if len(parts) > 6 and parts[6] == '✓':
                cookie['httpOnly'] = True
            if len(parts) > 7 and parts[7] == '✓':
                cookie['secure'] = True
            cookies.append(cookie)

# Save as pickle
with open('amazon_cookies.pkl', 'wb') as f:
    pickle.dump(cookies, f)

print(f"Saved {len(cookies)} cookies to amazon_cookies.pkl")