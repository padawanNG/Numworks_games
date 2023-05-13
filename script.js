// Récupération du fichier soumis par l'utilisateur
const fileInput = document.getElementById('fileInput');
const file = fileInput.files[0];

// Création du contenu du fichier
const content = "Contenu du fichier à envoyer sur GitHub";

// Configuration de l'objet qui contiendra les données à envoyer
const data = {
  message: 'Ajout d\'un nouveau fichier',
  content: btoa(content),
  branch: 'main'
};

// Envoi de la requête POST à l'API GitHub
fetch('https://api.github.com/repos/padawanNG/Numworks_games/contents/submitted-files/file.py', {
  method: 'PUT',
  headers: {
    Authorization: 'token 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',
    Accept: 'application/vnd.github.v3+json',
    'Content-Type': 'application/json'
  },
  body: JSON.stringify(data)
})
  .then(response => response.json())
  .then(data => console.log(data))
  .catch(error => console.error(error));
