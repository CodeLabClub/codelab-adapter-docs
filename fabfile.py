# 所有包含eim的插件, 跟adapter通信
import os
import platform
# from fabric.context_managers import cd
import subprocess
import sys
import json
import pathlib
from pprint import pprint as print
from fabric import task
# https://www.dazhuanlan.com/2019/10/16/5da6201e822c1/
from invoke.util import cd

#  "scratch3_teachable_machine",


def run_cmd(cmd):
    subprocess.call(cmd, shell=True)

def build():
    cmd = "mkdocs build"
    run_cmd(cmd)

@task
def push3(c):
    '''
    v3
    '''
    generate_extensions(c)
    build()
    cmd = 'rsync -e "ssh -i ~/Documents/al_cn.pem" -avH site root@118.31.62.99:/home/wwj/mylab/scratch3_adapter_docsv2'
    run_cmd(cmd)





@task
def serve(c):
    cmd = "mkdocs serve"
    run_cmd(cmd)


def get_extensions_and_nodes(codelab_adapter_extensions):
    extensions_and_nodes = {}
    types = ["nodes", "extensions"]
    for t in types:
        t_dir = f"{t}_v3/"
        t_files = pathlib.Path(f'{codelab_adapter_extensions}/{t_dir}').glob("*.py")
        # 移除eim_moniter 和 trigger
        t_files = [{"value":e.name, "url":f'https://adapter.codelab.club/extensions_nodes_mirrors/{e.name}'} for e in t_files if ("extension_" in e.name or "node_" in e.name)]
        extensions_and_nodes[t] = t_files
    return extensions_and_nodes

@task
def generate_extensions(c):
    # https://adapter.codelab.club/extensions_nodes_mirrors/extensions_nodes.json
    codelab_adapter_extensions = "/Users/wuwenjie/mylab/codelabclub/github_repo/codelab_adapter_extensions"
    cmds = [
        f'cp {codelab_adapter_extensions}/nodes_v3/node_*.py  docs/extensions_nodes_mirrors;',
        f'cp {codelab_adapter_extensions}/extensions_v3/extension_*.py  docs/extensions_nodes_mirrors;'
    ]
    for cmd in cmds:
        subprocess.call(cmd, shell=True)
    # 获得插件名字 生成json
    extensions_and_nodes = get_extensions_and_nodes(codelab_adapter_extensions)
    print(extensions_and_nodes)
    with open("docs/extensions_nodes_mirrors/extensions_nodes.json", "w") as f:
        f.write(json.dumps(extensions_and_nodes))
    # create json file
    
@task
def edit_notify(c):
    cmd = "code docs/user_guide/notify.json"
    run_cmd(cmd)    

@task
def edit_version(c):
    cmd = "code docs/about/latest_version.json"
    run_cmd(cmd)  
# 生成json
