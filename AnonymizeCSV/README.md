# DE-ashirvad
Steps tp execute:

docker build -t anonymize-csv .
docker run --rm -v $(pwd)/data:/app/data anonymize-csv python generate_csv.py

docker run --rm -v $(pwd)/data:/app/data anonymize-csv python anonymize_csv.py

docker run --rm -v $(pwd)/data:/app/data anonymize-csv python anonymize_large_csv.py
