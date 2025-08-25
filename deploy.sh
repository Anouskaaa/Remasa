echo "Git deploy for Remasa Repo"
git add .
echo "Commit message : "
read -r commitmsg
git commit -m $commitmsg
echo "Remote name : "
read Remote
git push $Remote main

