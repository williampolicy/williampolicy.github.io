import re
import datetime
from pathlib import Path

# 1. Open the markdown file
with open("blog_temp.md", 'r') as file:
    blog_content = file.read()

# 2. Analyze the file to extract information
title_search = re.search(r"# (.*)", blog_content)
title = title_search.group(1) if title_search else "Untitled"

date_search = re.search(r"(\d{4}-\d{2}-\d{2})", blog_content)
date = date_search.group(0) if date_search else datetime.date.today().isoformat()

category_search = re.search(r"(?<=\[).+?(?=\])", blog_content)
category = category_search.group(0) if category_search else "uncategorized"

# 3. Add the information to the top of the blog post
yaml_front_matter = f"""---
layout: post
title:  "{title}"
date:   {date}
categories: [{category}]
---
"""
blog_content = yaml_front_matter + blog_content

# 4. Save the file with the new filename format
new_filename = f"{date}-{title.replace(' ', '_')}.md"
with open(new_filename, 'w') as file:
    file.write(blog_content)

print(f"Blog post successfully saved as {new_filename}")
