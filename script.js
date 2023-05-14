import requests

def submitFile():
    file = document.getElementById("fileInput").files[0]
    filename = file.name
    with open(filename, 'rb') as data:
        response = requests.put(
            'https://upload.github.com/repos/padawanNG/Numworks_games/contents/submitted-files/{}'.format(filename),
            headers={'Authorization': 'token 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'},
            data=data
        )
    if response.status_code == 201:
        print('Le fichier a été soumis avec succès !')
    else:
        print('Erreur lors de la soumission du fichier.')
