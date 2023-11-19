#curl -X PUT -H "Authorization: Bearer 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" -H "Content-Type: application/json" -d '{"message":"Commit message","content":"lams file_content","branch":"master"}' https://api.github.com/repos/github2demo/repo1/contents/lamsfile1.txt
curl -L \
  -X PUT \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer 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" \
  -H "X-GitHub-Api-Version: 2022-11-28" \
  https://api.github.com/repos/github2demo/repo1/contents/lamsfile16.txt \
  -d '{"message":"my commit message.","committer":{"name":"m lam","email":"lam2020email@gmail.com"},"content":"bXkgbmV3IGZpbGUgY29udGVudHM="}'
