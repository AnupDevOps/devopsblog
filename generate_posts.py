import os
import frontmatter
import markdown
import json

posts_dir = '_posts'
posts = []

for filename in os.listdir(posts_dir):
    if filename.endswith('.md'):
        with open(os.path.join(posts_dir, filename), 'r', encoding='utf-8') as f:
            post = frontmatter.load(f)
            post_data = {
                'title': post['title'],
                'url': f"{filename.replace('.md', '.html')}"
            }
            posts.append(post_data)

            # Convert Markdown to HTML and save it
            html_content = markdown.markdown(post.content)
            html_filename = filename.replace('.md', '.html')
            with open(html_filename, 'w', encoding='utf-8') as html_file:
                html_file.write(f"<html><head><title>{post['title']}</title></head><body>{html_content}</body></html>")

with open('posts.json', 'w', encoding='utf-8') as f:
    json.dump(posts, f, ensure_ascii=False, indent=4)
