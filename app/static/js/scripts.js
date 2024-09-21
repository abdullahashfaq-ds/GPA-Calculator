document.addEventListener('DOMContentLoaded', function () {
    const addCourseBtn = document.getElementById('add-course-btn');
    const coursesTable = document.querySelector('#courses-table tbody');

    if (addCourseBtn && coursesTable) {
        addCourseBtn.addEventListener('click', function () {
            const newRow = document.createElement('tr');

            newRow.innerHTML = `
                <td><input type="text" name="course_title" placeholder="Enter course title" required></td>
                <td><input type="text" name="credit_hours" placeholder="Enter credit hours" required></td>
                <td><input type="text" name="obtained_marks" placeholder="Enter obtained marks" required></td>
                <td><button type="button" class="remove-course-btn">Remove</button></td>
            `;

            coursesTable.appendChild(newRow);

            newRow.querySelector('.remove-course-btn').addEventListener('click', function () {
                newRow.remove();
            });
        });

        document.querySelectorAll('.remove-course-btn').forEach(button => {
            button.addEventListener('click', function () {
                button.closest('tr').remove();
            });
        });
    }
});
