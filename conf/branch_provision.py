import subprocess

branch_labels = [	'v2','v3','v4','v5','v6','v7','v8',
									'v9','v10','v11','v12','v13','v14',
									'v15','v16','v17','v18','v19'
								]



for ele in branch_labels:
	git_command = 'git checkout -b {}'.format(ele)
	p = subprocess.Popen(git_command, shell=True, stdout=subprocess.PIPE)
p.wait()