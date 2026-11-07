class ValidationError(Exception):
    """
    Exception raised for errors when trying to validate a file
    """

def create_post(title:str, body:str) -> dict:
    if not title.strip():
        raise ValidationError("Title is required")
    if not body.strip() or len(body.strip()) < 15:
        raise ValidationError("Body is required or should be 15 characters long")
    return {"title":title, "body":body}


if __name__ == "__main__":

    title_text = "example title"
    body_text = "example "

    try:
        print(create_post(title_text, body_text))
    except ValidationError as e:
        print(f"Can not create {e}")


