from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory task storage (temporary; resets on app restart)
tasks = []

# GET /tasks — Retrieve all tasks
@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify(tasks), 200

# POST /tasks — Create a new task
@app.route('/tasks', methods=['POST'])
def create_task():
    data = request.get_json()
    title = data.get('title')

    # Validate input title
    if not title or not title.strip():
        return jsonify({'error': 'Task title is required'}), 400

    task = {
        'id': len(tasks) + 1,
        'title': title.strip(),
        'completed': False
    }
    tasks.append(task)
    return jsonify(task), 201

# DELETE /tasks/<task_id> — Delete a task by its ID
@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    global tasks
    tasks = [task for task in tasks if task['id'] != task_id]
    return jsonify({'message': f'Task {task_id} deleted'}), 200

# PUT /tasks/<task_id> — Mark a task as completed
@app.route('/tasks/<int:task_id>', methods=['PUT'])
def complete_task(task_id):
    for task in tasks:
        if task['id'] == task_id:
            task['completed'] = True
            return jsonify(task), 200
    return jsonify({'error': 'Task not found'}), 404

# PATCH /tasks/<task_id> — Update a task's title
@app.route('/tasks/<int:task_id>', methods=['PATCH'])
def update_task_title(task_id):
    data = request.get_json()
    new_title = data.get('title')

    # Validate new title
    if not new_title or not new_title.strip():
        return jsonify({'error': 'Task title cannot be empty'}), 400

    for task in tasks:
        if task['id'] == task_id:
            task['title'] = new_title.strip()
            return jsonify(task), 200

    return jsonify({'error': 'Task not found'}), 404

# Run the Flask development server
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')