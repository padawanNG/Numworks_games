function submitFile() {
  const fileInput = document.getElementById("fileInput");
  const file = fileInput.files[0];
  
  const token = "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";
  const url = "https://api.github.com/repos/padawanNG/Numworks_games/contents/submitted-files/" + file.name;
  
  const reader = new FileReader();
  reader.onload = function(event) {
    const content = event.target.result;
    
    const xhr = new XMLHttpRequest();
    xhr.open("PUT", url, true);
    xhr.setRequestHeader("Authorization", "token " + token);
    xhr.setRequestHeader("Content-Type", "application/json");
    
    xhr.onreadystatechange = function() {
      if (xhr.readyState === 4) {
        if (xhr.status === 200 || xhr.status === 201) {
          alert("Le fichier a été soumis avec succès !");
        } else {
          alert("Une erreur s'est produite lors de la soumission du fichier.");
        }
      }
    };
    
    const data = JSON.stringify({
      message: "Ajout de " + file.name,
      content: btoa(String.fromCharCode.apply(null, new Uint8Array(content)))
    });
    
    xhr.send(data);
  };
  
  reader.readAsArrayBuffer(file);
}    
    
    const data = JSON.stringify({
      message: "Ajout de " + file.name,
      content: encodedContent
    });
    
    xhr.send(data);
  };
  
  reader.readAsText(file);
}
