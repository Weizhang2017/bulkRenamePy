### Usage on Windows


#### Install Python3.7 and Git

1. Python3.7 can be downloaded [here](https://www.python.org/downloads/release/python-376/). It is recommanded to download [executable installer](https://www.python.org/ftp/python/3.7.6/python-3.7.6-amd64.exe)

2. Git is a version control tool and can be downloaded [here](https://git-scm.com/downloads)


#### Clone the repository

1.  Open the Windows Command Prompt by typing cmd in the search bar. 
	![cmd image](https://www.isunshare.com/images/article/windows-10/4-ways-to-open-command-prompt-in-windows-10/open-command-prompt-in-start-menu.png)

2.  Run the following commands:

* Change directory to your Desktop or any other directory you'd like to download the repository to
```
cd %userprofile%\Desktop
```

* Download the repository
```
git clone https://github.com/Weizhang2017/bulkRenamePy.git
```


#### Rename files

1. Change directory to the repository

	```
	cd bulkRenamePy
	```
2. Install the package
	```
	py setup.py install
	```

2. Check command usage
	```
	py bin/bulkRenamePy --help
	```	

	Response:
	```
	usage: bulkRenamePy [-h] --folderpath folderpath --namefile namefile
	rename files in bulk
	optional arguments:
	  -h, --help            show this help message and exit
	  --folderpath folderpath
	                        folder-path for names of the files to be renamed
	  --namefile namefile   a file mapping original filenames to new filenames
	```

3. Check the test folder

	```
	start test
	```	
	Double click to open name_file

	> The first column in the __name-file__ indicates the __original file names__ and the second column indicates the __file names to be renamed to__.


3. Rename the file in the test folder

	```
	py bin/bulkRenamePy --folderpath test\\ --namefile test\\name_file.csv
	```
	> The folder path and the name-file path can be either relative or absolute  


	Response:
	```
	filename not changed for name_file.csv, no new filename found in test\\name_file.csv
	filename changed for original.txt, new name: changed.txt
	filename changed for original2.txt, new name: changed2.txt
	```
	> If the file name is found in the name-file, it will be renamed according to the mapping. Otherwise, no change will be made.