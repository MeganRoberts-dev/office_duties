/* Array of motivational quotes */
var quotes = [
    "Believe in yourself and all that you are.",
    "The only way to achieve the impossible is to believe it is possible.",
    "Success is not the key to happiness. Happiness is the key to success.",
    "Don't watch the clock; do what it does. Keep going.",
    "You are never too old to set another goal or to dream a new dream.",
    "Start where you are. Use what you have. Do what you can."
  ];
  
  function changeTitle() {
    var titleElement = document.querySelector('h1');
    var randomIndex = Math.floor(Math.random() * quotes.length);
    titleElement.textContent = quotes[randomIndex];
}

// Change the title every 5 seconds
setInterval(changeTitle, 5000);
changeTitle();

// Todo List
var data = (localStorage.getItem('todoList')) ? JSON.parse(localStorage.getItem('todoList')) : {
    todo: [],
    completed: []
};

renderTodoList();

document.getElementById('add').addEventListener('click', function() {
    var value = document.getElementById('item').value;
    if (value) {
        addItem(value);
    }
});

document.getElementById('item').addEventListener('keydown', function(e) {
    if ((e.code === 'Enter' || e.code === 'NumpadEnter') && this.value) {
        addItem(this.value);
    }
});

function addItem(value) {
    addItemToDOM(value);
    document.getElementById('item').value = '';
    data.todo.push(value);
    dataObjectUpdated();
}

function renderTodoList() {
    if (!data.todo.length && !data.completed.length) return;

    for (var i = 0; i < data.todo.length; i++) {
        addItemToDOM(data.todo[i]);
    }

    for (var j = 0; j < data.completed.length; j++) {
        addItemToDOM(data.completed[j], true);
    }
}

function dataObjectUpdated() {
    localStorage.setItem('todoList', JSON.stringify(data));
}

function removeItem() {
    var item = this.parentNode.parentNode;
    var parent = item.parentNode;
    var id = parent.id;
    var value = item.innerText;

    if (id === 'todo') {
        data.todo.splice(data.todo.indexOf(value), 1);
    } else {
        data.completed.splice(data.completed.indexOf(value), 1);
    }

    dataObjectUpdated();
    parent.removeChild(item);
}

function completeItem() {
    var item = this.parentNode.parentNode;
    var parent = item.parentNode;
    var id = parent.id;
    var value = item.innerText;

    if (id === 'todo') {
        data.todo.splice(data.todo.indexOf(value), 1);
        data.completed.push(value);
    } else {
        data.completed.splice(data.completed.indexOf(value), 1);
        data.todo.push(value);
    }

    dataObjectUpdated();
    var target = (id === 'todo') ? document.getElementById('completed') : document.getElementById('todo');
    parent.removeChild(item);
    target.insertBefore(item, target.childNodes[0]);
}

function addItemToDOM(text, completed) {
    var list = (completed) ? document.getElementById('completed') : document.getElementById('todo');
    var item = document.createElement('li');
    item.innerText = text;

    var buttons = document.createElement('div');
    buttons.classList.add('buttons');

    var remove = document.createElement('button');
    remove.classList.add('remove');
    remove.innerHTML = 'Remove';
    remove.addEventListener('click', removeItem);

    var complete = document.createElement('button');
    complete.classList.add('complete');
    complete.innerHTML = 'Complete';
    complete.addEventListener('click', completeItem);

    buttons.appendChild(remove);
    buttons.appendChild(complete);
    item.appendChild(buttons);
    list.insertBefore(item, list.childNodes[0]);
}