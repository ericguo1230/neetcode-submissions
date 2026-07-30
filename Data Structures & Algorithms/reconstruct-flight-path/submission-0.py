class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        #Adj list (Create this using a hashmap (Source to targets))
        adj = defaultdict(list)
        for source, dest in tickets:
            adj[source].append(dest)
        
        for source in adj:
            heapq.heapify(adj[source])

        #Perform DFS greedily picking most visited and lexigraphically smallest node incase of tie-break
        output = []
        def dfs(start):
            while adj[start]:
                nxt = heapq.heappop(adj[start])
                dfs(nxt)
            output.append(start)
        #output result

        dfs("JFK")
        return output[::-1]