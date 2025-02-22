import requests
import csv


def fetch_and_print_posts():
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    print("Status Code:", response.status_code)
    if response.status_code == 200:
        posts = response.json()
        for post in posts:
            print(post.get("title"))
    else:
        print("Failed to retrieve posts.")


def fetch_and_save_posts():
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    if response.status_code == 200:
        posts = response.json()
        # Structure the data: only include id, title, and body for each post.
        filtered_posts = [
            {"id": post["id"], "title": post["title"], "body": post["body"]}
            for post in posts
        ]
        # Write the data into a CSV file called posts.csv
        with open("posts.csv", "w", newline='', encoding="utf-8") as csvfile:
            fieldnames = ["id", "title", "body"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(filtered_posts)
        print("Data saved to posts.csv")
    else:
        print("Failed to retrieve posts.")
