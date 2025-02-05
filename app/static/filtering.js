// Get the table and the headers
const table = document.getElementById("table");
const headers = table.getElementsByTagName("th");

let isAscending = [true, true, true];  // Track sorting order for each column (true = ascending)

// Add click event listeners to each column header
for (let i = 0; i < headers.length; i++) {
  headers[i].addEventListener("click", function() {
    sortTable(i);
  });
}

function sortTable(columnIndex) {
  const rows = Array.from(table.tBodies[0].rows);  // Get all rows inside <tbody>
  const isAsc = isAscending[columnIndex];  // Get the current sorting order

  // Sort rows based on the column clicked
  rows.sort((rowA, rowB) => {
    const cellA = rowA.cells[columnIndex].textContent.trim();
    const cellB = rowB.cells[columnIndex].textContent.trim();

    // Compare the values based on the column type (numeric or string)
    if (isNaN(cellA) || isNaN(cellB)) {
      // Sort as string
      return isAsc ? cellA.localeCompare(cellB) : cellB.localeCompare(cellA);
    } else {
      // Sort as number
      return isAsc ? parseFloat(cellA) - parseFloat(cellB) : parseFloat(cellB) - parseFloat(cellA);
    }
  });

  // Reappend rows to the table body in sorted order
  rows.forEach(row => table.tBodies[0].appendChild(row));

  // Toggle the sorting order for the next click
  isAscending[columnIndex] = !isAsc;
}

sortTable(0)
