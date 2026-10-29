
import pandas as pd


def parse_users(users):
    """Validate user records and return a cleaned DataFrame."""
    if not isinstance(users, list):
        raise ValueError("Users must be provided as a list")

    records = []

    for user in users:
        if not isinstance(user, dict):
            raise ValueError("Each user must be a dictionary")

        if "id" not in user or not user.get("name") or not user.get("email"):
            raise ValueError("Each user must have an id, name, and email")

        address = user.get("address") or {}
        city = address.get("city") if isinstance(address, dict) else None

        records.append({
            "id": user["id"],
            "name": user["name"],
            "email": user["email"],
            "city": city
        })

    columns = ["id", "name", "email", "city"]
    df = pd.DataFrame(records, columns=columns)

    if not df.empty:
        df["name"] = df["name"].astype(str).str.strip()
        df["email"] = df["email"].astype(str).str.strip()
        df["city"] = df["city"].fillna("").astype(str).str.strip()

    return df
