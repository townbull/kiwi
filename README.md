skymesh-kiwi
============

The core cloud integration service for skymesh, a cloud integration as a service platform.

[v0.5]
Features:
* connect google drive
* connect dropbox
* web interface
* command line interface


Cli Subcommands:

    list			   	list all supported cloud    
    connect			    connect a cloud											<cloud>
    disconnect		    disconnect a cloud										<cloud>
    file-list     		list all the files and folders in a cloud director		<cloud>:<dir>
    file-add 			add a file (*or a folder) in a cloud directory			<cloud>:<dir> <filename> <*type>
    file-delete			delete a file (*or a folder) in a cloud directory		<cloud>:<dir> <filename> <*type>
    file-copy			copy a file (*or a folder) from a cloud directory /		src <cloud>:<dir><filename> dest /
    					to another												<cloud>:<dir><filename>
    file-open 			open a file in a cloud directory using another /		<cloud>:<dir><filename> [opening <cloud>]
    					cloud function
