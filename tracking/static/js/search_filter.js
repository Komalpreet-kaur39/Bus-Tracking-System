// document.addEventListener('DOMContentLoaded', function () {
//     const searchInput = document.getElementById('searchInput');
//     const table = document.querySelector('.searchable-table');
//     if (!searchInput || !table) return;

//     const rows = table.getElementsByTagName('tr');

//     searchInput.addEventListener('keyup', function () {
//         const filter = searchInput.value.toLowerCase();

//         for (let i = 1; i < rows.length; i++) {
//             const cells = rows[i].getElementsByTagName('td');
//             let matchFound = false;

//             for (let j = 0; j < cells.length; j++) {
//                 if (cells[j]) {
//                     const text = cells[j].textContent.toLowerCase();
//                     if (text.includes(filter)) {
//                         matchFound = true;
//                         break;
//                     }
//                 }
//             }

//             rows[i].style.display = matchFound ? "" : "none";
//         }
//     });
// });


// document.addEventListener('DOMContentLoaded', function () {
//     const searchInput = document.getElementById('searchInput');
//     const table = document.querySelector('.searchable-table');
//     if (!searchInput || !table) return;

//     const rows = table.getElementsByTagName('tr');

//     searchInput.addEventListener('keyup', function () {
//         const filter = searchInput.value.toLowerCase();

//         for (let i = 1; i < rows.length; i++) {
//             const cells = rows[i].getElementsByTagName('td');
//             let matchFound = false;

//             for (let j = 0; j < cells.length; j++) {
//                 const cell = cells[j];
//                 if (cell) {
//                     const text = cell.textContent.toLowerCase();

//                     // Split route name into possible stops (assumes stops are part of the name or joined)
//                     const possibleStops = text.split(',').map(stop => stop.trim());

//                     if (text.includes(filter)) {
//                         matchFound = true;
//                         break;
//                     }

//                     // Check if the filter matches any possible stop in the cell
//                     for (let stop of possibleStops) {
//                         if (stop.startsWith(filter)) {
//                             matchFound = true;
//                             break;
//                         }
//                     }

//                     if (matchFound) break;
//                 }
//             }

//             rows[i].style.display = matchFound ? "" : "none";
//         }
//     });
// });

document.addEventListener('DOMContentLoaded', function () {
    const searchInput = document.getElementById('searchInput');
    const table = document.querySelector('.searchable-table');
    
    if (!searchInput || !table) return;

    const rows = table.getElementsByTagName('tr');

    searchInput.addEventListener('keyup', function () {
        const filter = searchInput.value.toLowerCase();  // Get the filter input and make it lowercase

        // Loop through all rows (skip the header row)
        for (let i = 1; i < rows.length; i++) {  
            const cells = rows[i].getElementsByTagName('td');  // Get all cells of the row
            let matchFound = false;  // Flag to check if any match is found

            // Loop through each cell in the row
            for (let j = 0; j < cells.length; j++) {
                const cell = cells[j];
                if (cell) {
                    const text = cell.textContent.toLowerCase();  // Get the text content of the cell
                    
                    // Check if the search term exists in the cell text
                    if (text.includes(filter)) {
                        matchFound = true;  // Set matchFound to true if a match is found
                        break;  // No need to check other cells in this row
                    }
                }
            }

            // Display the row if a match was found, otherwise hide it
            rows[i].style.display = matchFound ? "" : "none";
        }
    });
});
