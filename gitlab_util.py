import gitlab
import sys, os
import argparse

def gitlab_auth():
    token='yourlongesttoken'
    url='https://yourgitlabserver'
    gl = gitlab.Gitlab(url, private_token=token)
    gl.auth()
    return gl

def list_users():
    gl = gitlab_auth()
    projects = gl.projects.list(all=True)
    for project in projects:
        print 'Project ID: ' + str(project.id)
        print 'Link to project: ' + project.http_url_to_repo
        print 'Users:'
        try:
            users = project.users.list()
            for user in users:
                    print user.username
        except:
            pass

def list_members():
    gl = gitlab_auth()
    projects = gl.projects.list(all=True)
    for project in projects:
        print 'Project ID: ' + str(project.id)
        print 'Link to project: ' + project.http_url_to_repo
        print 'Members:'
        try:
	    members = project.members.list()
            for mem in members:
                print 'Username: ' + mem.username + ' Name: ' +  mem.name
        except:
            pass

def list_groups():
    gl = gitlab_auth()
    groups = gl.groups.list()
    for group in groups:
	print 'Group Name: ' + group.full_name
	print 'Link: ' + group.web_url
	print 'Members of group: '
        members = group.members.list()
        for mem in members:
	    print mem.name

def list_sourcetree():
    gl = gitlab_auth()
    projects = gl.projects.list(all=True)
    for project in projects:
        print 'Project ID: ' + str(project.id)
        print 'Link to project: ' + project.http_url_to_repo
        try:
	    items = project.repository_tree(all=True, recursive=True)
            for item in items:
                print os.path.join(project.web_url, item['path'])
        except:
            pass

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Gitlab API Scripts')
    parser.add_argument('option', help="To list all projects with users, members, groups, or sourcetree")
    args = parser.parse_args()
    if len(sys.argv) < 2:
       print "Usage: %s option <users, members, groups, or sourcetree>" \
              "or type %s -h for help" % (sys.argv[0], sys.argv[0])
       sys.exit(1)
    if sys.argv[1] == "users":
	print "All Users"
	list_users()
    elif sys.argv[1] == "members":
	print "All Members"
	list_members()
    elif sys.argv[1] == "groups":
        print "Groups"
	list_groups()
    elif sys.argv[1] == "sourcetree":
        print "Source Tree"
        list_sourcetree()
    else:
	print "Invalid option. Try python %s -h for help" % sys.argv[0]
