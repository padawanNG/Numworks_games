const fileInput = document.getElementById('fileInput');
const submitButton = document.getElementById('submitButton');

submitButton.addEventListener('click', () => {
  const file = fileInput.files[0];
  if (file && file.name.endsWith('.py')) {
    const formData = new FormData();
    formData.append('file', file);
    fetch('/submitted-files', {
      method: 'POST',
      body: formData
    })
