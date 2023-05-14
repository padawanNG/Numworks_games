function submitFile() {
  var fileInput = $('#fileInput');
  var file = fileInput.prop('files')[0];
  var formData = new FormData();
  formData.append('file', file);

  $.ajax({
    url: 'upload.php',
    type: 'POST',
    data: formData,
    contentType: false,
    processData: false,
    success: function(response) {
      console.log('Fichier envoyé avec succès !');
    },
    error: function(error) {
      console.error('Erreur lors de l\'envoi du fichier : ' + error.statusText);
    }
  });
}
