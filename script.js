function submitFile() {
  // Récupérer le fichier déposé par l'utilisateur
  const file = document.getElementById('fileInput').files[0];

  // Créer un objet FormData contenant le fichier
  const formData = new FormData();
  formData.append('file', file);

  // Configurer la requête pour créer un nouveau commit avec le fichier
  const repoName = 'Numworks_games';
  const username = 'padawanNG';
  const accessToken = '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';
  const commitMessage = 'Ajout d\'un nouveau fichier';
  const branchName = 'main';
  const filePath = 'submitted-files/' + file.name;

  const url = `https://api.github.com/repos/${username}/${repoName}/contents/${filePath}`;
  const options = {
    method: 'PUT',
    headers: {
      'Authorization': `Bearer ${accessToken}`,
      'Content-Type': 'application/json; charset=utf-8'
    },
    body: JSON.stringify({
      message: commitMessage,
      content: btoa(file),
      branch: branchName,
      path: filePath
    })
  };

  // Envoyer la requête pour créer le nouveau commit
  fetch(url, options)
    .then(response => {
      if (response.ok) {
        alert('Le fichier a été ajouté avec succès!');
      } else {
        alert('Une erreur est survenue lors de l\'ajout du fichier.');
      }
    })
    .catch(error => {
      console.error(error);
      alert('Une erreur est survenue lors de l\'ajout du fichier.');
    });
}
