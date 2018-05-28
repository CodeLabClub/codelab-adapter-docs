push:
	rsync -e "ssh -i ~/Documents/jy.pem" -avH site root@47.52.104.107:/home/wwj/mylab/scratch3_adapter_docs
cp-github:
	rm -rf /Users/wuwenjie/githubblog/others/scratch3-adapter-docs;
	cp -r /Users/wuwenjie/mylab/changxue/scratch3-adapter-docs/site /Users/wuwenjie/githubblog/others/scratch3-adapter-docs;

