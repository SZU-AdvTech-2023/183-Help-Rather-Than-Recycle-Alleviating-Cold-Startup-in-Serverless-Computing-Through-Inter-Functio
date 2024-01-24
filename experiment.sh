sudo apt-get update
# 安装docker
curl -fsSL https://get.docker.com | bash -s docker --mirror Aliyun
sudo docker pull apache/couchdb:latest
sudo docker run -itd -p 5984:5984 -e COUCHDB_USER=openwhisk -e COUCHDB_PASSWORD=openwhisk --name couchdb couchdb
# 安装pip
sudo apt install python3-pip -y
pip3 uninstall zipp
pip3 install gevent docker-compose asyncio couchdb numpy flask psutil
sudo apt install python3-virtualenv -y
# 构建基础镜像
cd container
docker build --no-cache -t pagurus_base .
docker build --no-cache -t pagurus_base_repack .
cd ..
# 构建预热模板容器镜像
cd prewarm
docker build --no-cache -t pagurus_prewarm_base .
cd ..
# 为每个函数构建镜像
python3 inter_controller/inter_controller.py build_images
# 构建虚拟环境
bash intra_controller/init_virtualenv.bash
