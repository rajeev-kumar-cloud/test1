from git import Repo
import os
import sys
import logging

class CreateBranchAndTag:
    
    def __init__(self, branch_name, tag_name):
        
        '''
        Args:
            branch_name(str): branch_name
            tag_name(str): tag_name
        '''
        
        self.branch_name=branch_name
        self.tag_name=tag_name
        
    def create_branch(self):
        
        '''
        
        Create a new branch and switch to it.
        Return: matched_branch
        
        '''
        
        repo = Repo(path_to_be_specified) # Need to specify the repo path
        branches = str(repo.git.branch()).splitlines()
        if self.branch_name in branches:
            repo.git.checkout(self.branch_name)
        else:
            repo.git.checkout('-b', self.branch_name)
        matched_branch = [branch.name for branch in \
        str(repo.git.branch()).splitlines() if branch.name == self.branch_name]
        
        if len(matched_branch)>0:
            return matched_branch[0]
        else:
            raise ValueError("Branch was not Created.")
    
    def create_tag(self):
        
        '''
        Create a new lightweight tag before pushing the code.
        Return: matched_tag
        '''
        
        repo = Repo(path_to_be_specified) # Need to specify the repo path
        if self.tag_name not in repo.tags:
            repo.create_tag(self.tag_name)
        matched_tag = [tag for tag in repo.tags if tag == self.tag_name]
        if len(matched_tag)>0:
            return matched_tag[0]
        else:
            raise ValueError("Tag was not created.")
    
    def git_status(self):
        repo = Repo('.')
        if '' not in repo.git.status():
            raise Exception("branch is not updated.")
        else:
            logging.INFO(repo.git.status())
    
    def git_add(self, *args):
        self.files = *args
        repo = Repo('.')
        if len(self.files)<1:
            raise Exception("No files to commit.")
        else:
            for file in self.files:
                repo.git.add(file)
            logging.INFO("Files are added successfully.")
    
    def git_commit(self):
        repo = Repo('.')
        message = "xyz"
        repo.git.commit(m=message)
    
    def git_push(self):
        repo = Repo('path/to/git/repo')
        origin = repo.remote('origin')
        origin.push()
            

# Based on the input.py sys.argv input index can be changed while integrating.
branch_tag = CreateBranchAndTag(sys.argv[1], sys.argv[2])
# Returned the branch
branch = branch_tag.create_branch()
# Returned the created tag
tag = branch_tag.create_tag

print(branch, tag)
