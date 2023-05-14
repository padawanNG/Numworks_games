function submitFile() {
  const fileInput = document.getElementById('fileInput');
  const file = fileInput.files[0];
  const formData = new FormData();
  formData.append('file', file);

  axios.post('https://file.io/?expires=1d', formData)
    .then(response => {
      const downloadLink = response.data.link;
      window.location.href = 'confirmation.html?link=' + encodeURIComponent(downloadLink);
    })
    .catch(error => {
      console.error(error);
    });
}

