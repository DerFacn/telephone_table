const checkboxes = document.querySelectorAll('.checkbox')
const allEntries = document.querySelectorAll('.entry')

function changeDisplay() {
    let checkedCheckboxes = false

    checkboxes.forEach(checkbox => {
        if (checkbox.checked) {
            checkedCheckboxes = true
        }
    });

    if (!checkedCheckboxes) {
        allEntries.forEach(entry => {
            entry.classList.remove('hidden')
        })
        return
    }

    checkboxes.forEach(checkbox => {
        const currentCity = checkbox.getAttribute('data-filter')
        const currentState = checkbox.checked

        allEntries.forEach(entry => {
            if (entry.getAttribute('data-filter') === currentCity) {
                if (currentState) {
                    entry.classList.remove('hidden')
                } else {
                    entry.classList.add('hidden')
                }
            }
        })
    })
}

function search(input) {
    const value = input.value.toLowerCase()

    if (value.trim() === "") {
        allEntries.forEach(entry => {
            entry.classList.remove('bySearch-hidden')
        })
    }

    allEntries.forEach(entry => {
        if (entry.innerText.toLowerCase().includes(value)) {
            entry.classList.remove('bySearch-hidden')
        } else {
            entry.classList.add('bySearch-hidden')
        }
    });
}


document.addEventListener('DOMContentLoaded', (event) => {
    changeDisplay(checkboxes[0])
})