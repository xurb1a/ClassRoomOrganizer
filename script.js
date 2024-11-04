let studentRoster = [
    {
        "name": "Karina M",
        "age": 8,
        "height": 48,
        "favorite_subject": "Math",
        "favorite_animal": "Dog"
    },
    {
        "name": "Yori K",
        "age": 7,
        "height": 50,
        "favorite_subject": "Art",
        "favorite_animal": "Cat"
    },
    {
        "name": "Alex C",
        "age": 7,
        "height": 47,
        "favorite_subject": "Science",
        "favorite_animal": "Cow"
    },
    {
        "name": "Esmeralda R",
        "age": 8,
        "height": 52,
        "favorite_subject": "History",
        "favorite_animal": "Rabbit"
    },
    {
        "name": "Sandy P",
        "age": 7,
        "height": 49,
        "favorite_subject": "Recess",
        "favorite_animal": "Guinea Pig"
    },
    {
        "name": "Matthew Q",
        "age": 7,
        "height": 46,
        "favorite_subject": "Music",
        "favorite_animal": "Walrus"
    },
    {
        "name": "Trudy B",
        "age": 8,
        "height": 45,
        "favorite_subject": "Science",
        "favorite_animal": "Ladybug"
    },
    {
        "name": "Benny D",
        "age": 7,
        "height": 51,
        "favorite_subject": "Math",
        "favorite_animal": "Ant"
    },
    {
        "name": "Helena L",
        "age": 7,
        "height": 53,
        "favorite_subject": "Art",
        "favorite_animal": "Butterfly"
    },
    {
        "name": "Marisol R",
        "age": 8,
        "height": 50,
        "favorite_subject": "Math",
        "favorite_animal": "Lion"
    }
];

function displayStudents() {
    const studentList = document.getElementById('student-list');
    studentList.innerHTML = '';

    studentRoster.forEach(student => {
        const li = document.createElement('li');
        li.textContent = student.name;
        studentList.appendChild(li);
    });
}

function addStudent() {
    const name = document.getElementById('name').value;
    const age = document.getElementById('age').value;
    const height = document.getElementById('height').value;
    const favoriteSubject = document.getElementById('favorite-subject').value;
    const favoriteAnimal = document.getElementById('favorite-animal').value;

    const newStudent = {
        name,
        age: parseInt(age),
        height: parseInt(height),
        favorite_subject: favoriteSubject,
        favorite_animal: favoriteAnimal
    };

    studentRoster.push(newStudent);
    displayStudents();
    clearInputFields();
}

function removeStudent() {
    const nameToRemove = document.getElementById('remove-name').value;
    studentRoster = studentRoster.filter(student => student.name !== nameToRemove);
    displayStudents();
}

function sortNames() {
    const sortedNames = studentRoster.map(student => student.name).sort();
    const sortedNamesList = document.getElementById('sorted-names-list');
    sortedNamesList.innerHTML = '';

    sortedNames.forEach(name => {
        const li = document.createElement('li');
        li.textContent = name;
        sortedNamesList.appendChild(li);
    });
}

function clearInputFields() {
    document.getElementById('name').value = '';
    document.getElementById('age').value = '';
    document.getElementById('height').value = '';
    document.getElementById('favorite-subject').value = '';
    document.getElementById('favorite-animal').value = '';
    document.getElementById('remove-name').value = '';
}

displayStudents();
