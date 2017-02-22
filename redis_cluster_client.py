from rediscluster import StrictRedisCluster
#startup_nodes = [{"host": "10.30.79.2", "port": "9000"},{"host": "10.30.79.2", "port": "9001"},{"host": "10.30.79.3", "port": "9000"},{"host": "10.60.79.3", "port": "9001"},{"host": "10.30.79.4", "port": "9000"},{"host": "10.30.79.4", "port": "9001"}]
startup_nodes = [{"host": "127.0.0.1", "port": "9000"}]
r = StrictRedisCluster(startup_nodes=startup_nodes, decode_responses=True)
count = 1
while (count < 1000):
   count = count + 1
   print 'insert key:', count
   r.set(count, 'w3F9z75HtSMSDqADJgqUaMCNa9SlCB+PGYRJvq9UnN22hl7dWZerKQsRAK0DD8QmI')

