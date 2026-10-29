
from api_client import fetch_users
from data_parser import parse_users


def main():
    try:
        users = fetch_users()
        df = parse_users(users)

        df.to_csv("users.csv", index=False)

        print(f"Successfully processed {len(df)} users.")
        print(df.head())
        print("Saved results to users.csv")

    except Exception as error:
        print(f"Error processing API data: {error}")


if __name__ == "__main__":
    main()
