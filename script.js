// Récupérer le formulaire HTML
const form = document.getElementById('upload-form');

// Attacher un écouteur d'événements pour intercepter la soumission du formulaire
form.addEventListener('submit', async (event) => {
  event.preventDefault(); // Empêcher le comportement de soumission par défaut

  // Récupérer le fichier sélectionné par l'utilisateur
  const file = event.target.fileInput.files[0];

  // Configuration de la requête POST pour télécharger le fichier
  const owner = 'padawanNG';
  const repo = 'Numworks_games';
  const path = `submitted-files/${file.name}`;
  const message = 'Ajout d\'un nouveau fichier';
  const content = await readFileAsync(file);
  const token = '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';

  // Télécharger le fichier sur GitHub en utilisant Octokit
  const octokit = new Octokit({ auth: token });
  try {
    const response = await octokit.request('PUT /repos/{owner}/{repo}/contents/{path}', {
      owner,
      repo,
      path,
      message,
      content
    });
    console.log('Le fichier a été téléchargé avec succès sur GitHub !');
  } catch (error) {
    console.error(error);
    alert('Une erreur est survenue lors de l\'envoi du fichier.');
  }
});

// Fonction utilitaire pour lire le contenu du fichier en tant que texte
function readFileAsync(file) {
  return new Promise((resolve, reject) => {
    const reader = new FileReader();
    reader.onload = () => resolve(reader.result);
    reader.onerror = reject;
    reader.readAsText(file);
  });
}
