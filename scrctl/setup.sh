# setup from Windows scrctl command

getgd() {
    eval `$1`=`where sh`
}

dir=$(cd $(dirname $0); pwd)

echo $dir
getgd gitdir
echo $gitdir
echo ${gitdir:0:-14}
read sss





