push:
	rsync -e "ssh -i ~/Documents/jy.pem" -avH site root@47.52.104.107:/home/wwj/mylab/scratch3_adapter_docs
