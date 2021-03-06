let filterElement = document.getElementById("filter");
function update() {
    let filter = filterElement.value;

    for (let rowElement of document.querySelectorAll("table tr")) {
        let rowCells = [...rowElement.querySelectorAll("td")].map((cellElement) => cellElement.textContent);
        let match = filter === "" || rowCells.some(cell => cell.indexOf(filter) !== -1);
        rowElement.classList.toggle("filtered-out", !match);
    }
}
filterElement.addEventListener("change", (event) => { update(); });
filterElement.addEventListener("keydown", (event) => { update(); });
filterElement.addEventListener("keyup", (event) => { update(); });
filterElement.addEventListener("keypress", (event) => { update(); });