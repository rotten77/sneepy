var selectedFolder = "";
var searchQuery = ""

function selectFolder(el) {
	selectedFolder = el.dataset.folder;

	elements = document.querySelectorAll("#sidebar ul li")
	for (var i = 0; i < elements.length; i++) {
		elements[i].classList.remove('active');
    }
	el.classList.add('active');

	showSnippets();
}

function setSearchQuery() {
	searchQuery = document.getElementById("query").value;

	showSnippets();
}

function clearSearchQuery() {
	searchQuery = "";
	searchQuery = document.getElementById("query").value = "";
	showSnippets();
}

function showSnippets() {
	addSnippetButton = document.getElementById("add-snippet");
	console.log(addSnippetButton);
	console.log(addSnippetButton.classList);
	if(selectedFolder=="") {
		addSnippetButton.classList.add('disabled');
		console.log("add");
	} else {
		addSnippetButton.classList.remove('disabled');
		console.log("remove");
	}
	let snippets = document.querySelectorAll(".snippet");

	for (var i = 0; i < snippets.length; i++) {
		let snippetFolder = snippets[i].dataset.folder
		let snipperTitle = snippets[i].dataset.title

		searchMatch = new RegExp(searchQuery, "gi");

		let folderMatch = false;
		let queryMatch = false;

		if(selectedFolder=="") {
			folderMatch = true;
		} else {
			if(snippetFolder==selectedFolder) folderMatch = true;
		}

		if(searchQuery=="") {
			queryMatch = true;
		} else {
			if(snipperTitle.match(searchMatch)) queryMatch = true;
		}

		snippets[i].style.display = (queryMatch && folderMatch ? "block" : "none");
		
    }
}

function copySnippet(wrapper) {
	let id = wrapper.dataset.snippetId;
	var element = document.getElementById('snippet' + id);

	pywebview.api.copySnippet(element.innerText)
	if(config_minimize) pywebview.api.minimizeWindow()

	wrapper.classList.add('copied');
	setTimeout(function () {
		wrapper.classList.remove('copied');
	}, 3000);
}

function addSnippet() {
	if(selectedFolder=="") {
		alert("No folder selected");
		return false;
	}
	let fileName = prompt("Enter file name");
	let response = ""
	if (fileName != null) {
		response = pywebview.api.addSnippet(selectedFolder, fileName);
	}
	if(response!="") {
		alert(response)
	}
}

function addFolder() {
	let folderName = prompt("Enter folder name");
	let response = ""
	if (folderName != null) {
		response = pywebview.api.addFolder(folderName);
	}
	if(response!="") {
		alert(response)
	}
}

function editSnippet(folder, fileName) {
	pywebview.api.editSnippet(folder, fileName);
	console.log(folder);
	console.log(fileName);
}

function manageFiles() {
	pywebview.api.manageFiles();
}

function reload() {
	document.getElementById('reload').classList.add('disabled');
	pywebview.api.reload();
}