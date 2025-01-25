# This is youtube_manager which is use sqlite3 as a Database 

import sqlite3
from tabulate import tabulate

conn = sqlite3.connect('youtube_video.db')

cursor = conn.cursor()

cursor.execute(''' 
    CREATE TABLE IF NOT EXISTS videos(
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               name TEXT NOT NULL,
               time TEXT NOT NULL
               )
''')

def list_videos():
    cursor.execute("SELECT * FROM videos")
    rows = cursor.fetchall()
    if rows:
        headers = ["ID", "Name", "Time"]
        print(tabulate(rows, headers, tablefmt="pretty"))
    else:
        print("No videos found.")

def add_video(name, time):
    cursor.execute("INSERT INTO videos (name, time) VALUES (?, ?)", (name, time))
    conn.commit()

def update_video(video_id, new_name, new_time):
    cursor.execute("UPDATE videos SET name=?, time=? WHERE id=?", (new_name, new_time, video_id))
    conn.commit()

def delete_video(video_id):
    cursor.execute("DELETE FROM videos WHERE id=?", (video_id,))
    conn.commit()

def main():
    while True:
        print("\nYoutube manager app with DB")
        print("1. List videos")
        print("2. Add video")
        print("3. Update video")
        print("4. Delete video")
        print("5. Exit app")

        choice = input("Enter your choice: ")

        if choice == '1':
            list_videos()
        elif choice == '2':
            name = input("Enter the video name: ")
            time = input("Enter the video time: ")
            add_video(name, time)
        elif choice == '3':
            video_id = input("Enter the Video ID: ")
            name = input("Enter the video name: ")
            time = input("Enter the video time: ")
            update_video(video_id, name, time)
        elif choice == '4':
            video_id = input("Enter the Video ID: ")
            delete_video(video_id)
        elif choice == '5':
            break
        else:
            print("Invalid choice!")

    conn.close()     

if __name__ == '__main__':
    main()
