document.addEventListener('DOMContentLoaded', function () {
    const addCourseBtn = document.getElementById('add-course-btn');
    const coursesTable = document.querySelector('#courses-table tbody');
    let courseIndex = 1;

    if (addCourseBtn && coursesTable) {
        addCourseBtn.addEventListener('click', function () {
            const newRow = document.createElement('tr');

            newRow.innerHTML = `
                <td><input type="text" name="course_title" placeholder="Course title" required class="w-full bg-[#F4D35E] text-[#083D77] placeholder-[#083D77] p-2 rounded"></td>
                <td><input type="text" name="credit_hours" placeholder="Credit hours" required class="w-full bg-[#F4D35E] text-[#083D77] placeholder-[#083D77] p-2 rounded"></td>
                <td><input type="text" name="obtained_marks" placeholder="Obtained marks" required class="w-full bg-[#F4D35E] text-[#083D77] placeholder-[#083D77] p-2 rounded"></td>
                <td><button type="button" class="remove-course-btn text-red-500 hover:text-red-700">Remove</button></td>
                
            `;

            coursesTable.appendChild(newRow);
            courseIndex++;

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
