let consoleContent = document.getElementById("console-content");
let consoleCommand = document.getElementById("console-command");

consoleContent.addEventListener("focus", function (e) {
    consoleContent.blur();
    consoleCommand.focus();
});


let historyIndex = 0;

consoleCommand.addEventListener("keydown", function (e) {
        if (e.keyCode === 38) {
            historyIndex--;
            switchCommand();
        } else if (e.keyCode === 40) {
            historyIndex++;
            switchCommand();
        }
    }
)

function switchCommand() {
    let arr = sessionStorage.getItem("console_history").split('\n');
    let commandIndex = arr.length - 2 + historyIndex;
    if (commandIndex < 0) {
        historyIndex++;
    } else if (commandIndex === arr.length - 1) {
        consoleCommand.value = "";
    } else if (commandIndex > arr.length - 1) {
        historyIndex--;
    } else {
        let command = arr[commandIndex];
        consoleCommand.value = command;
    }
}


consoleCommand.addEventListener("keypress", function (e) {
    if (e.key === "Enter") {
        historyIndex = 0;
        let command = consoleCommand.value.trim();
        if (command.length === 0) {
            return;
        }
        if (sessionStorage.getItem("console_history")) {
            let consoleHistory = sessionStorage.getItem("console_history");
            sessionStorage.setItem("console_history", consoleHistory + command + "\n");
        } else {
            sessionStorage.setItem("console_history", command + "\n");
        }
        consoleContent.value = consoleContent.value + command + "\n";
        consoleContent.scrollTop = consoleContent.scrollHeight;
        consoleCommand.value = "";
        var arr = location.href.split("/");
        if (arr[arr.length - 1] == "simple")
            location.href = "/command?view=simple&value=" + command;
        else if (arr[arr.length - 1] == "detailed")
            location.href = "/command?view=detailed&value=" + command;
    }
});

window.addEventListener("load", function (e) {
    consoleCommand.focus();
    let consoleHistory = sessionStorage.getItem("console_history");
    if (consoleHistory != null) {
        consoleContent.value = consoleHistory;
        consoleContent.scrollTop = consoleContent.scrollHeight;
    }
});