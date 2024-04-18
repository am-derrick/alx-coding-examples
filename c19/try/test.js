class Task {
	description;
	completed;
	constructor(description) {
		this.description = description;
		this.completed = false;
	}

	completeTask() {
		this.completed = true;
	}
}

let tasks = [];

function addTask(description) {
	const newTask = new Task(description);
	tasks.push(newTask);
}

function markTask(index) {
	tasks[index].completeTask();
}

function displayTasks() {
	tasks.forEach((task, index) => {
		console.log(`${index}: ${task.description} - ${task.completed ? 'Completed' : 'Incomplete'}`);
	})
}


addTask("Please complete javascript basics tasks");
addTask("Don't forget DSA");
addTask("We'll also work with Python.");

displayTasks();

markTask(0);

displayTasks();
