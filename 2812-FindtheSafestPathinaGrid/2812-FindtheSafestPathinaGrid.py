
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n:
                    new_safe = min(d, dist[nr][nc])
                    if new_safe > max_safeness[nr][nc]:
                        max_safeness[nr][nc] = new_safe
                        heapq.heappush(max_heap, (-new_safe, nr, nc))

        return -1  
[
