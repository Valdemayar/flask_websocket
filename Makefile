upload-container:
	aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 303029436715.dkr.ecr.us-east-1.amazonaws.com
	docker build -t rtmp_server .
	docker tag rtmp_server:latest 303029436715.dkr.ecr.us-east-1.amazonaws.com/rtmp_server:latest
	docker push 303029436715.dkr.ecr.us-east-1.amazonaws.com/rtmp_server:latest

docker-local:
	docker-compose build
	docker-compose up


push-lightsail:
	docker build -t rtmp_server .
	aws lightsail push-container-image --region us-east-1 --service-name rtmp-server  --label rtmp-server-4 --image rtmp_server:latest