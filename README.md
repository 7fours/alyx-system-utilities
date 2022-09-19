# alyx-system-utilities
Quality of life improvements for linux and windows systems. In essence, just a cli wrapper for a multitude of applications
Written and maintained by alyxx

### Alyx's "shell" (ash)

Parser for asu/shell extension
**WIP**
              
- Starts ash and begins parsing user input for scripting. 
- apm and other extensions can be called independently;
```        
ex. [apm -I '{package_name}']
```
- or as a single command itself;
```
ex. [ash -apm -I '{package_name}']
```
- and can set default commands unless otherwise specified;
```
ex. [ash --default_function 'apm']
    [ash -I '{package_name}']
```
- as well as changing between explicit status' vs implied/toggled;
if we set bools to be explicitly stated such as this;
```
ex. [ash --explicit_bools 'True']
    [ash -apm -I '{package_name} --no-confirm]
    Installs package without need for user confirmation but requires the flag with every operation.
    Otherwise will return to default verbose output.
```
- Meanwhile if we change bools to implied;
```
        ex. [ash --explicit_bools 'False']
            [ash -apm -I '{package_name}' --no-confirm]
        apm would install the package with no output and then remember this flag for the next operation as well until altered. 
```        



### Alyx's Package Manager (apm)
```
        Alyx's Package Manager/apm     
        
    !! might/should work with winget? !!

Usage: [-I] [-R] [-U] [-P] [-d]
       [--manager] [--sandbox] [--autoremove] [--debug]
       
ex. [apm -I firefox] Would install the firefox from our repository
ex. [apm -I firefox --manager snap] Would install the snap version of firefox

Options:
-I, --install        Installs specified package
-R, --remove         Removes specified package
-U, --update         Updates packages in background then upgrades available packages
-P, --purge          Remove package as well as all dependencies/unused related packages
-d, --details        Gives information on the specified package as well as the dependencies
Long commands only:

--no-confirm         Don't require confirmation for further permissions
--manager            If a specific package manager needs to be used, use this flag
--autoremove         Autoremove unused/unneeded packages from system
Dev tools:

--sandbox            sandbox and test package without installing to system [WIP]
--debug
```

```
To-Do list:
        --add all package managers
        --finish adding all options and main functions
        --find a way to push and pull from repos from within script?
        --add manager.conf file
        --make downloader function
        --use google drive as repo location?
        --add winget
        --add pacstall
        --finish help/man page
        --make... entire shell?
        --parser implementation
        --file structure creation
        --script formatting and assignment
        

```
