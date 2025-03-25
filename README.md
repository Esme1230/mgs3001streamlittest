# Initialize Git repository
git init

# Add remote repository
git remote add origin https://github.com/JunyanZhu/mgs3001streamlittest.git

# Create and checkout main branch
git checkout -b main

# Add all files to staging
git add .

# Commit changes
git commit -m "Initial commit of loan qualifier app"

# Push to GitHub
git push -u origin main
