from opensearchpy import OpenSearch
import json

def get_opensearch(the_host="localhost"):
    host = the_host
    port = 9200
    auth = ('admin', 'admin')
    client = OpenSearch(
        hosts=[{'host': host, 'port': port}],
        http_compress=True,  # enables gzip compression for request bodies
        http_auth=auth,
        # client_cert = client_cert_path,
        # client_key = client_key_path,
        use_ssl=True,
        verify_certs=False,
        ssl_assert_hostname=False,
        ssl_show_warn=False,
        # ca_certs=ca_certs_path
    )
    return client

def get_body(path: str):
    with open(path) as f:
        body = json.loads(f.read())
    return body

if __name__=='__main__':
    client = get_opensearch()
    print(f"BEFORE:\n{client.cat.indices(params={'v':'true'})}")
    json_path = '/home/elastic/search_engineering/week1/bbuy_products.json'
    body = get_body(json_path)
    index_name = 'bbuy_products'
    if not client.indices.exists(index_name):
        client.indices.create(index=index_name, body=body)
    # client.indices.put_settings(body={'refresh_interval':'30s'})
    print(f"AFTER:\n{client.cat.indices(params={'v':'true'})}")