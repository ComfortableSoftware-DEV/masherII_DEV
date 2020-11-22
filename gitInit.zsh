#!/usr/bin/env zsh

git init
git add .gitignore
git add

echo "Go to github."
echo "Log in to your account."
echo "Click the new repository button in the top-right. You’ll have an option there to initialize the repository with a README file, but I don’t."
echo "Click the “Create repository” button."
echo "Now, follow the second set of instructions, “Push an existing repository…”"
echo "$ git remote add origin git@github.com:username/new_repo"
echo "$ git push -u origin master"
echo "Actually, the first line of the instructions will say"
echo "$ git remote add origin https://github.com/username/new_repo"
