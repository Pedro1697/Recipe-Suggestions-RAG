import csv

def read_csv_in_chunks(file_path, chunk_size=5):
    with open(file_path, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        chunk = []
        for i, row in enumerate(reader, 1):
            chunk.append(row)
            if i % chunk_size == 0:
                yield chunk
                chunk = []
        if chunk:
            yield chunk
