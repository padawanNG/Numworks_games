const express = require('express');
const fileUpload = require('express-fileupload');

const app = express();

// Activer l'upload de fichiers
app.use(fileUpload());

// Définir la route pour la soumission de fichiers
app.post('/submit-file', (req, res) => {
  // Vérifier si des fichiers ont été soumis
  if (!req.files || Object.keys(req.files).length === 0) {
    return res.status(400).send('Aucun fichier n\'a été soumis.');
  }

  // Récupérer le fichier soumis
  const submittedFile = req.files.submittedFile;

  // Enregistrer le fichier dans le dossier "submitted-files"
  submittedFile.mv('submitted-files/' + submittedFile.name, (err) => {
    if (err) {
      return res.status(500).send(err);
    }

    res.send('Le fichier a été soumis avec succès !');
  });
});

// Démarrer le serveur
app.listen(3000, () => {
  console.log('Le serveur est lancé sur le port 3000.');
});
