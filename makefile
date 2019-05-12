push:
	rsync -e "ssh -i ~/Documents/al_cn.pem" -avH site root@118.31.62.99:/home/wwj/mylab/scratch3_adapter_docs

build:
	mkdocs build
