from functools import lru_cache

@lru_cache(maxsize=3)
def multip(c):
    return c * 1
  

if __name__=="__main__":
    print(multip(5))
    print(multip(2))
    print(multip(1))
    print(multip(1))
    print(multip(10))
    print(multip.cache_info())