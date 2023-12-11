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

	const answer_button = document.getElementById('toggle_answer');
	answer_button.addEventListener('click', ()=>{
		const form = document.getElementById('answer_form');
		if (form.classList.contains('d-none')){
			form.classList.remove('d-none')
		} else {
			form.classList.add('d-none')
		}
	})
})
