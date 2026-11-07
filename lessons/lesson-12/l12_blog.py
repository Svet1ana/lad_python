import json
import logging
from pathlib import Path
from l12_validation import ValidationError
from l12_try_finallly import POSTS_FILE

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(name)s - %(message)s"

)

logger = logging.getLogger('blog')

def load_posts() -> list:
    if not Path(POSTS_FILE).exists():
        logger.info(f" file {POSTS_FILE} not find. return empty list")
        return []

    try:
        with POSTS_FILE.open(encoding='utf-8') as f:
            return json.load(f)
    except json.decoder.JSONDecodeError as err:
        logger.error(f" invalid json {POSTS_FILE} {err}")
        raise

def save_posts(posts: list) -> None:
    with POSTS_FILE.open(mode='w', encoding='utf-8') as f:
        json.dump(posts, f, ensure_ascii=False, indent=4)
    logger.info(f" saved {len(posts)} posts")

def add_post(title: str, body: str) -> dict:
    if not title or not body:
        raise ValidationError("title or body is required")

    posts = load_posts()

    post = {"title": title, "body": body }
    posts.append(post)
    save_posts(posts)
    return post

def lists_posts() -> None:
    posts = load_posts()
    if not posts:
        print("no posts")
        return
    for num, post in enumerate(posts, start=1):
        try:
            print(f" [{num}] {post['title']} : {post['body']}")
        except KeyError as err:
            logger.error(f" not valid structure data {err}")
            print(f" not valid structure file {err}")
            break

if __name__ == "__main__":
    logger.info("starting...")
    while True:
        print("""
        choose an option:
        add - > add a post
        list - > list all posts
        exit  - > exit the program
        """)

        action = input(">").lower().strip()
        if action == "add":
            title: str = input("title: ")
            body: str = input("body: ")
            try:
                add_post(title, body)
            except ValidationError as err:
                logger.warning(f" not valid {err}")
                print(f" Error!! not valid . Try aggain \n"
                      f"{err}")
                continue
            except json.decoder.JSONDecodeError:
                print(f" invalid json")
                continue
            else:
                print(f" successfully added {title} and {body}")
        elif action == "list":
            try:
                lists_posts()
            except json.decoder.JSONDecodeError:
                print(f" invalid json")
        elif action == "exit":
            logger.info("exiting...")
            print("exiting...")
            break
        else:
            print(f" invalid action {action}")