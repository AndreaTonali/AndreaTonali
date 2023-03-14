## Personal dev Repo


### Useful Commands

Below a list of commands useful when working on Linux command line.

|command | description
|--- | ---
|`df -h` | hard drive
|`mkdir` | creates a directory
|`ln -s /home/folder1/` | creates an hyperlink
|`mkdir -p` | create intermediate directories as required.
|`pwd` | print wrok directory
|`rm -r` | remove directory
|`rm -rf` | force remove directory
|`unizip name_file.zip` | extract-all .zip
|`tar -zxvf name_file.gzip` | extract-all .gxip
|`diff -u file1 file2` | difference in between two files
|`zless file1.log.gz` | list of all entries in ziped file
|`less file1.log` | list of all entries in file
|`ps -l -A` | list of all your active process with info
|`ps ufx \| grep python` | identify the process wiht grep and part of the name of the process running (u=user oriented format, f=ascii art process hierarchy, x=lift the BSD-style (must have a tty))
|`ps aux \| grep python`
|`ps aux \| head 1; ps aux \| grep cron (or Python)` | identify the porcess running bring back only the first line
|`ps afx \| grep rstudio-server`
|`kill 'number of the process you want to kiil'` | PID  
|`kill -9 $(pgrep -f run_ABC.py)` | kill a spacific script
|`tail -f /path/thefile.log` | following the progress of your .log file
|`ps ufx \| grep name_of_the_ps \| awk '{print $2}' \| xargs kill -9` | dinamically kill a process
|`ps aux \| grep name_of_the_ps \| awk '{sum=sum+$6}; END {print sum/1024 " MB"}'` | memory usage in Megabyte
|`ps aux \| grep name_of_the_ps \| awk '{sum=sum+$6}; END {print sum " KB"}'` | memory usage in Byte
|`grep -irn "value"` | how to look recursivelly within a directory and sub-directory inside all the avaialble files.
| `cp -fR /source/. /dest/` | copy the content of one directory into another directory
| `cp -a /source/. /dest/` | The -a option is an improved recursive option, that preserve all file attributes, and also preserve symlinks. The . at end of the source path is a specific cp syntax that allow to copy all files and folders, included hidden ones.
| `history \| tail -n 20` | history of commands beening run the number states how many of them you want to see

---

### CHMOD (File permissions)

### https://en.wikipedia.org/wiki/Chmod

```				
         Permission                     rwx
___________________________________________

7        read, write and execute        rwx
-------------------------------------------
6        read and write                 rw-
-------------------------------------------
5        read and execute               r-x
-------------------------------------------
4        read only                      r--
-------------------------------------------
3        write and execute              -wx
-------------------------------------------
2        write only                     -w-
-------------------------------------------
1        enxecute only                  --x
-------------------------------------------
0        none                           ---
___________________________________________

```
|cmd| rwx 
|:---:|:---:
| `chmod 700` | rwx------
| `chmod 600` | rw-------
| `chmod 755` | rwxr-xr-x

---

### CRONTAB (Schedule Jobs)

|cmd| description 
|:---|:---:
|`crontab -e` | edit the crontba scheduler, like vim
|`crontab -l` | to visualize your scheduler
|`crontab -l > /some/shared/location/crontab.bak` | how to back up your crontab
|`cat -n crontab.bak` |

```
# Each task to run has to be defined through a single line
# indicating with different fields when the task will be run
# and what command to run for the task
#
# To define the time you can provide concrete values for
# minute (m), hour (h), day of month (dom), month (mon),
# and day of week (dow) or use '*' in these fields (for 'any').#
# Notice that tasks will be started based on the cron's system
# daemon's notion of time and timezones.
#	
# Output of the crontab jobs (including errors) is sent through
# email to the user the crontab file belongs to (unless redirected).
#
# For example, you can run a backup of all your user accounts
# at 5 a.m every week with:
# 0 5 * * 1 tar -zcf /var/backups/home.tgz /home/
#
# For more information see the manual pages of crontab(5) and cron(8)

# 0 - Sun      Sunday
# 1 - Mon      Monday
# 2 - Tue      Tuesday
# 3 - Wed      Wednesday
# 4 - Thu      Thursday
# 5 - Fri      Friday
# 6 - Sat      Saturday
# 7 - Sun      Sunday

# ┌────────── minute (0 - 59)
# │ ┌──────── hour (0 - 23)
# │ │ ┌────── day of month (1 - 31)
# │ │ │ ┌──── month (1 - 12)
# │ │ │ │ ┌── day of week (0 - 6 => Sunday - Saturday, or
# │ │ │ │ │                1 - 7 => Monday - Sunday)
# ↓ ↓ ↓ ↓ ↓
# * * * * * command to be executed
```
---
### SCREEN 
_(situation where you perform a long-running task on a remote machine, and suddenly your connection drops, the SSH session is terminated, and your work is lost.)_

Screen or GNU Screen is a terminal multiplexer. In other words, it means that you can start a screen session and then open any number of windows (virtual terminals) inside that session. Processes running in Screen will continue to run when their window is not visible even if you get disconnected.

|cmd| description 
|:---|:---:
| `screen` | activates a session
| `screen -ls` | list of active socket
| `screen -r 18980` | - r reattache + number of the socket 
| `screen -X -S 18980 quit` | quit the socket 
