push:
	# rsync -e "ssh -i ~/Documents/jy.pem" -avH site root@47.52.104.107:/home/wwj/mylab/scratch3_adapter_docs
	# ssh -i ~/Documents/al_cn.pem root@118.31.62.99
	rsync -e "ssh -i ~/Documents/al_cn.pem" -avH site root@118.31.62.99:/home/wwj/mylab/scratch3_adapter_docs
push-cn:
	rsync  -avH site ubuntu@119.254.210.56:/home/ubuntu/mylab/scratch3_adapter_docs
cp-github:
	rm -rf /Users/wuwenjie/githubblog/others/scratch3-adapter-docs;
	cp -r /Users/wuwenjie/mylab/changxue/scratch3-adapter-docs/site /Users/wuwenjie/githubblog/others/scratch3-adapter-docs;

build:
	mkdocs build
