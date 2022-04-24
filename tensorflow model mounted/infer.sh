image=$(ls ./images | shuf -n 1)
docker exec my_container python classify.py --input /images/$image
echo "Expected: ${image: 10: -4}"