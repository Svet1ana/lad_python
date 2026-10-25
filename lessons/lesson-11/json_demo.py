import json


# post = {
#     "title": "My first post",
#     "author": "Agent",
#     "tags": ["Python", "JSON", "Files"],
#     "published": True,
#     "views": 120,
# }
#
# with open( "post.json", "w", encoding="utf-8") as f:
#     json.dump(post, f, ensure_ascii=False,  indent=2)
    
# with open( "post.json", "r", encoding="utf-8") as f:
#     loaded = json.load(f)

text = """
{
  "title": "My first post",
  "author": "Agent",
  "tags": [
    "Python",
    "JSON",
    "Files"
  ],
  "published": true,
  "views": 120
}
"""
json_str = json.loads(text)

print(f"Title: {json_str['title']} ")
print(f"Tags: {json_str['tags']} ")
print(f"published: {json_str['published']} ")

