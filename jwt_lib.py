import jwt

SECRET = "secret"
DEFAULT_ALGORITHM = "HS256"


if __name__ == "__main__":
    payload = {
        "name": "someuser",
        "details": {
            "age": 12,
            "email": "someone@gmail.com"
        },
        "exp": "000000"
    }
    token = jwt.encode(payload, SECRET, algorithm=DEFAULT_ALGORITHM)
    print(token)

    unverified_details = jwt.decode(token, options={"verify_signature": False})
    print(unverified_details)

    try:
        decoded_payload = jwt.decode(token, SECRET, algorithms=[DEFAULT_ALGORITHM])
        print(decoded_payload)
    except jwt.ExpiredSignatureError as e:
        print("Oops! Signature expired")

