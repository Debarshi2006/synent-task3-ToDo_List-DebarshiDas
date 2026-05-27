import sqlite3
conn = sqlite3.connect("Todo.db")
cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS work(
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        time TEXT NOT NULL
    )
''')

def list_Work():
    cursor.execute("SELECT * FROM work")
    rows = cursor.fetchall()
    print("\n" + "="*70)
    if not rows:
        print("No Work found.")
    for row in rows:
        # Unpacking the tuple (id, name, time)
        id, name, time = row
        print(f"ID: {id} | Title: {name} | Duration: {time}")
    print("="*70)

        
def add_Work(name, time):
    cursor.execute("INSERT INTO work (name, time) VALUES(?,?)",(name, time))
    conn.commit()
    
def update_Work(work_id, name, time):
    cursor.execute("UPDATE work SET name = ? , time = ? WHERE id = ?", (name, time, work_id))
    conn.commit()
    
def delete_Work(work_id):
    cursor.execute("DELETE FROM work WHERE id = ?",(work_id,))
    conn.commit()

def main():
    while True:
        print("\n To Do list with DB")
        print("1. List of work.")
        print("2. Add work")
        print("3. Update work")
        print("4. Delete Work")
        print("5. Exit")
        choice = input("Enter Your choice:")
        match choice:
            case '1':
                list_Work()
            case '2':
                name = input("Enter the name of work: ")
                time = input("Time needed for the work: ")
                add_Work(name, time)
            case '3':
                work_id = input("Enter the ID to update: ")
                name = input("Enter the name of work: ")
                time = input("Time needed for the work: ")
                update_Work(work_id, name, time)
            case '4':
                work_id = input("Enter the ID to update: ")
                delete_Work(work_id)
            case '5':
                break
            case _:
                print("Invalid Choice!")
    conn.close()
if __name__ == "__main__":
    main()