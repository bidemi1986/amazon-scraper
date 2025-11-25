from bs4 import BeautifulSoup

input_path = "Amazon.com_ Customer reviews_ Playstation 5 Disc Version PS5 Console - Additional Controller, 4K-TV Gaming, 16GB GDDR6 RAM, 8K Output, WiFi 6. Ultra-High Speed 825GB SSD - U Deal (Renewed).html"
output_path = "cleaned_reviews.html"

with open(input_path, "r", encoding="utf-8") as f:
    html = f.read()

soup = BeautifulSoup(html, "html.parser")

# Remove unwanted tags
for tag in soup(["script", "style", "meta", "link", "noscript", "iframe", "svg"]):
    tag.decompose()

# Keep only the body or main content
body = soup.find("body")
if body:
    cleaned_html = str(body)
else:
    cleaned_html = str(soup)

# Remove unwanted tags
for tag in soup(["script", "style", "meta", "link", "noscript", "iframe", "svg"]):
    tag.decompose()

# Keep only the body or main content
body = soup.find("body")
if body:
    cleaned_html = str(body)
else:
    cleaned_html = str(soup)

# Now extract review blocks from cleaned HTML
soup_clean = BeautifulSoup(cleaned_html, "html.parser")

# Check before cleaning
original_soup = BeautifulSoup(html, "html.parser")
original_reviews = original_soup.find_all(attrs={"data-hook": "review"})
print(f"Found {len(original_reviews)} reviews in original HTML")

# Try from cleaned
cleaned_reviews = soup_clean.find_all(attrs={"data-hook": "review"})
print(f"Found {len(cleaned_reviews)} reviews in cleaned HTML")

review_blocks = soup_clean.find_all(attrs={"data-hook": "review"})

# If no reviews found, try alternative selectors
if not review_blocks:
    review_blocks = soup_clean.find_all("div", class_="a-section review")

# Debugging: print some divs
print("Sample divs:")
for div in soup_clean.find_all("div", limit=10):
    print(div.get("data-hook"), div.get("class"))

print("Searching for 'review' in text:")
if "review" in soup_clean.get_text().lower():
    print("Found 'review' in text")
else:
    print("No 'review' in text")

print("Divs with 'review' in class:")
for div in soup_clean.find_all("div", class_=lambda c: c and "review" in " ".join(c)):
    print(div.get("class"))

# Try finding review list
review_list = soup_clean.find("div", id="cm_cr-review_list")
if review_list:
    print("Found review list div")
    inner_divs = review_list.find_all("div", limit=10)
    print("Inner divs in review list:")
    for d in inner_divs:
        print(d.get("class"), d.get("data-hook"))
    if not review_blocks:  # Only if not already found
        review_blocks = review_list.find_all("div", class_="a-section review")
        print(f"Found {len(review_blocks)} reviews in list")
else:
    print("No review list found")

# Create a minimal HTML file with just the reviews
with open(output_path, "w", encoding="utf-8") as out:
    out.write("<html><body>\n")
    for review in review_blocks:
        out.write(str(review) + "\n")
    out.write("</body></html>")

print(f"Extracted {len(review_blocks)} reviews to {output_path}")
print(f"Cleaned HTML length: {len(cleaned_html)}")
