task = []

def add_task(task_name, deadline, status):
    global tasks
    
    task = {
        "task_name": task_name,
        "deadline": deadline,
        "status": status
    }
    
    tasks.append(task)

def display_tasks():
    global tasks
    print("\nタスク情報:")
    for task in tasks:
        print(f"タスク名: {task['task_name']}")
        print(f"締め切り日: {task['deadline']}")
        print(f"ステータス: {task['status']}")
        print("----------------------")

task_name = input("タスク名を入力してください:")
deadline = input("締め切り日を入力してください (YYYY-MM-DD): ")
status = input("ステータスを入力してください (例: 未完了, 完了):")

add_task(task_name, deadline, status)

display_tasks()