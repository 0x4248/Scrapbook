#
# ~/.bashrc
#

# If not running interactively, don't do anything
[[ $- != *i* ]] && return


echo -e " _   _ _______  ___   _ ____  "
echo -e "| \ | | ____\ \/ | | | / ___| "
echo -e "|  \| |  _|  \  /| | | \___ \ "
echo -e "| |\  | |___ /  \| |_| |___) |"
echo -e "|_| \_|_____/_/\_\\___/|____/ "
echo ""
echo "Welcome to nexus intranet"
uptime -p
uname -a

alias ls='ls --color=auto'
alias ll='ls -alF'
alias la='ls -A'
alias l='ls -CF'
alias h='cd ~'
alias e='exit'
alias q='exit'
alias grep='grep --color=auto'

PS1='\[\033[01;32m\]\u@\h\[\033[00m\]:\[\033[01;34m\]\w\[\033[00m\]\$ '

export PATH="$PATH:/home/blix/.local/bin"
