#!/usr/bin/python3
import requests
import csv

def fetch_and_print_posts():
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    
    # Print the HTTP status code
    print(f"Status Code: {response.status_code}")
    
    # If the request is successful, parse JSON and print post titles
    if response.status_code == 200:
        posts = response.json()
        for post in posts:
            print(post.get('title'))

def fetch_and_save_posts():
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    
    # If the request is successful, filter data and save to CSV
    if response.status_code == 200:
        posts = response.json()
        
        # Structure the data into a list of dictionaries with specific keys
        filtered_posts = []
        for post in posts:
            filtered_posts.append({
                'id': post.get('id'),
                'title': post.get('title'),
                'body': post.get('body')
            })
            
        # Write the filtered data into a CSV file named posts.csv
        with open('posts.csv', mode='w', encoding='utf-8', newline='') as file:
            fieldnames = ['id', 'title', 'body']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            
            writer.writeheader()
            writer.writerows(filtered_posts)
