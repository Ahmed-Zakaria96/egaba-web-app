document.addEventListener('DOMContentLoaded', function() {

	tinymce.init({
		selector: '.editor',
		setup: function(editor) {
			editor.on('change', function() {
				tinymce.triggerSave();
			});
		},
		height: 300,
		menubar: false,
		plugins: [
			'advlist autolink lists link image charmap print preview anchor',
			'searchreplace visualblocks code fullscreen',
			'insertdatetime media table paste code help wordcount',
			'codesample'
		],
		toolbar: 'undo redo | formatselect | ' + ' codesample ' +
			'bold italic backcolor | alignleft aligncenter ' +
			'alignright alignjustify | bullist numlist outdent indent | ' +
			'removeformat',
		content_style: 'body { font-family:Helvetica,Arial,sans-serif; font-size:14px }'
	});

	// university select change faculty
	const university_select = document.getElementById("id_university");

	university_select.addEventListener('change', () => {
		try {
			const university_id = parseInt(university_select.value);
			if (university_id) {
				fetch(`/questions/university_faculty_options/${university_id}`)
					.then(response => response.json())
					.then(data => {
						const faculty_options = document.getElementById('id_faculty');
						let html_option = '<option value="">---------</option>';
						data.forEach(faculty => {
							html_option += `<option value="${faculty.id}">${faculty.name}</option>`
						})
						faculty_options.innerHTML = html_option;
					})
			}
		} catch (error) {
			console.log(error)
		}
	})

	// faculty select change departments
	const faculty_select = document.getElementById('id_faculty');

	faculty_select.addEventListener('change', () => {
		try {
			const faculty_id = parseInt(faculty_select.value);
			if (faculty_id) {
				fetch(`/questions/faculty_department_options/${faculty_id}`)
					.then(response => response.json())
					.then(data => {
						const department_options = document.getElementById('id_department');
						let html_option = '<option value="">---------</option>';
						data.forEach(department => {
							html_option += `<option value="${department.id}">${department.name}</option>`
						})
						department_options.innerHTML = html_option;
					})
			}
		} catch (error) {
			console.log(error);
		}
	})

	// subject_options
	const department_select = document.getElementById('id_department');

	department_select.addEventListener('change', () => {
		try {
			const department_id = parseInt(department_select.value);
			if (department_id) {
				fetch(`/questions/department_level_options/${department_id}`)
					.then(response => response.json())
					.then(data => {
						const level_options = document.getElementById('id_level');
						let html_option = '<option value="">---------</option>';
						data.forEach(level => {
							html_option += `<option value="${level.id}">${level.name}</option>`
						})
						level_options.innerHTML = html_option;
					})
			}
		} catch (error) {
			console.log(error);
		}
	})

	const level_select = document.getElementById('id_level');

	level_select.addEventListener('change', () => {
		try {
			const level_id = parseInt(level_select.value);
			if (level_id) {
				fetch(`/questions/level_subject_options/${level_id}`)
					.then(response => response.json())
					.then(data => {
						const subject_options = document.getElementById('id_subject');
						let html_option = '<option value="">---------</option>';
						data.forEach(subject => {
							html_option += `<option value="${subject.id}">${subject.name}</option>`
						})
						subject_options.innerHTML = html_option;
					})
			}
		} catch (error) {
			console.log(error);
		}
	})


})
