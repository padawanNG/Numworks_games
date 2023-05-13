function submitFile() {
  const fileInput = document.getElementById('fileInput');
  const file = fileInput.files[0];
  if (file && file.name.endsWith('.py')) {
    const formData = new FormData();
    formData.append('file', file);
    fetch('https://uploads.github.com/repos/PadawanNG/Numworks_games/git/blobs', {
      method: 'POST',
      headers: {
        'Authorization': 'token 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',
        'Content-Type': 'text/plain'
      },
      body: file
    })
    .then(response => response.json())
    .then(data => {
      const blobSha = data.sha;
      const path = 'submitted-files/' + file.name;
      fetch('https://api.github.com/repos/oadawanNG/Numworks_games/contents/' + path, {
        method: 'PUT',
        headers: {
          'Authorization': 'token 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',
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({
          message: 'Ajout d\'un fichier ' + file.name,
          content: blobSha,
          path: path,
          branch: 'main'
        })
      })
      .then(response => response.json())
      .then(data => console.log(data))
      .catch(error => console.error(error));
    })
    .catch(error => console.error(error));
  }
}

