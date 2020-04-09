push2:
	rsync -e "ssh -i ~/Documents/al_cn.pem" -avH site root@118.31.62.99:/home/wwj/mylab/scratch3_adapter_docsv2

push-cn:
	rsync  -avH site ubuntu@119.254.210.56:/home/ubuntu/mylab/scratch3_adapter_docs
cp-github:
	rm -rf /Users/wuwenjie/githubblog/others/scratch3-adapter-docs;
	cp -r /Users/wuwenjie/mylab/changxue/scratch3-adapter-docs/site /Users/wuwenjie/githubblog/others/scratch3-adapter-docs;

build:
	mkdocs build
serve:
	mkdocs serve

generate-extensions:
	cp /Users/wuwenjie/mylab/codelabclub/github_repo/codelab_adapter_extensions/nodes_v3/*.py  docs/extensions_nodes_mirrors;
	cp /Users/wuwenjie/mylab/codelabclub/github_repo/codelab_adapter_extensions/extensions_v3/*.py  docs/extensions_nodes_mirrors;
