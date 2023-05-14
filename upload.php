<?php
$file = $_FILES['file'];
$fileName = $file['name'];
$fileTmpName = $file['tmp_name'];

$githubUsername = 'padawanNG';
$githubToken = 'votre_token_github';

$repoName = 'Numworks_games';
$branchName = 'main';
$filePath = 'submitted-files/' . $fileName;

$fileContent = file_get_contents($fileTmpName);

$ch = curl_init();
curl_setopt($ch, CURLOPT_URL, "https://api.github.com/repos/{$githubUsername}/{$repoName}/contents/{$filePath}");
curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
curl_setopt($ch, CURLOPT_POST, 1);
curl_setopt($ch, CURLOPT_POSTFIELDS, json_encode(array(
    'message' => "Ajout de {$fileName}",
    'content' => base64_encode($fileContent),
    'branch' => $branchName
)));
curl_setopt($ch, CURLOPT_HTTPHEADER, array(
    "Authorization: token {$githubToken}",
    "User-Agent: {$githubUsername}"
));
$response = curl_exec($ch);
curl_close($ch);
?>
