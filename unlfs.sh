#!/bin/bash

# This script converts Git LFS tracked files back to regular Git files
# It finds all LFS pointers and replaces them with the actual content

# Find all Git LFS pointer files
git lfs ls-files -l | while read -r oid type size path; do
    # Get the actual file content from LFS
    git lfs cat-file --include-lfs-size "$oid" > "$path"
    # Add the file back to Git (not as LFS)
    git add "$path"
done

echo "Conversion complete. Now commit the changes with: git commit -m 'Convert LFS files to regular Git files'"
